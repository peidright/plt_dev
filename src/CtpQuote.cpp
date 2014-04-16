#include "CtpQuote.h"
#include "msgqueue.h"
#include "config.h"
#include <string>
#include <assert.h>
using namespace std;
boost::thread_group t_group;

 CtpQuote::CtpQuote(string username,string password, string quote_addr)
{
	/*
	this->api = CThostFtdcMdApi::CreateFtdcMdApi(localdir.c_str());
	md->RegisterSpi((CThostFtdcMdSpi*)q);
	md->RegisterFront("tcp://ctpmn1-front1.citicsf.com:51213");
	md->Init();
	*/
}


void quote_test(CtpQuoteSpi *ctpquotespi)
{
	cerr<<"quote_test"<<std::endl;
	cerr<<ctpquotespi->test<<std::endl;
	CThostFtdcReqUserLoginField f;
	memset(&f, 0, sizeof(f));
	strcpy(f.BrokerID, "1017");
	strcpy(f.UserID, "00000071");
	strcpy(f.Password, "123456");
	ctpquotespi->api->ReqUserLogin(&f, 1);
}


/*
void CtpQuoteApi::Init()
{
	assert(0);
}
int CtpQuoteApi::Join()
{
	assert(0);
	return 0;
}

void CtpQuoteApi::RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo)
{
}
void CtpQuoteApi::RegisterFront(char *pszFrontAddress)
{
}
void CtpQuoteApi::RegisterNameServer(char *pszNsAddress)
{
	assert(0);
}
void CtpQuoteApi::RegisterSpi(CThostFtdcMdSpi *pSpi)
{
	assert(0);
}


void CtpQuoteApi::Release()
{
	assert(0);
}
int CtpQuoteApi::ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID)
{
	assert(0);
	return 0;
}
int CtpQuoteApi::ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID)
{
	assert(0);
	return 0;
}
int CtpQuoteApi::SubscribeMarketData(char *ppInstrumentID[], int nCount)
{
	assert(0);
	return 0;
}

int CtpQuoteApi::UnSubscribeMarketData(char *ppInstrumentID[], int nCount)
{
	assert(0);
	return 0;
}
 CtpQuoteApi::~CtpQuoteApi()
{
}
 */

void CtpQuoteSpi::OnFrontConnected()
{
#if 0
	printf("spi on connected\n");
	this->test="dddd";
	t_group.add_thread(new boost::thread(quote_test,this));
	return;
	CThostFtdcReqUserLoginField f;
	memset(&f, 0, sizeof(f));
	strcpy(f.BrokerID, "1017");
	strcpy(f.UserID, "00000071");
	strcpy(f.Password, "123456");
	this->api->ReqUserLogin(&f, 1);
#else
	msg_t *msg=new(msg_t);
	msg->len=sizeof(QOnFrontConnected_t);
	msg->data=new(QOnFrontConnected_t);
	msg->type=QOnFrontConnected;
    	this->ctpquoter->post_msg(msg);
	LOG_INFO<<"Quote Connect"<<std::endl;
#endif

}
int CtpQuoteSpi::ReqUserLogin(TThostFtdcBrokerIDType	vAppId,
	        TThostFtdcUserIDType	vUserId,	TThostFtdcPasswordType	vPasswd)
{
	int ret;
#if 0
	CThostFtdcReqUserLoginField f;
	memset(&f, 0, sizeof(f));
	strcpy(f.BrokerID, "1017");
	strcpy(f.UserID, "00000071");
	strcpy(f.Password, "123456");
	this->api->ReqUserLogin(&f, 1);
#else
	CThostFtdcReqUserLoginField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, vAppId); //strcpy(appId, vAppId); 
	strcpy(req.UserID, vUserId);  //strcpy(userId, vUserId); 
	strcpy(req.Password, vPasswd);
	this->login_status=LOGIN;
	ret = this->api->ReqUserLogin(&req, 1);	
	if (ret) {
		LOG_INFO<<"login fail"<<ret<<std::endl;
		this->login_status=FAIL;
	}
	cerr<<"ReqUserLogin send request"<<std::endl;
#endif
	return ret;
}

void CtpQuoteSpi::OnFrontDisconnected(int nReason)
{
	msg_t *msg=new(msg_t);
	QOnFrontDisconnected_t *data=new( QOnFrontDisconnected_t );
	data->nReason=nReason;
	msg->data=data;
	msg->type=QOnFrontDisconnected;
	this->ctpquoter->post_msg(msg);
	LOG_INFO<<"Quote Disconnect"<<std::endl;
}

void CtpQuoteSpi::OnHeartBeatWarning(int nTimeLapse)
{
	msg_t *msg=new(msg_t);
	QOnHeartBeatWarning_t *data=new( QOnHeartBeatWarning_t );
	data->nTimeLapse=nTimeLapse;
	msg->data=data;
	msg->type=QOnHeartBeatWarning;
	this->ctpquoter->post_msg(msg);
	LOG_INFO<<"Quote OnHeartBeatWarning"<<std::endl;

}

void CtpQuoteSpi::OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

	if ( !this->IsErrorRspInfo(pRspInfo) ) {  
		msg_t *msg=new(msg_t);
		QOnRspError_t *data=new( QOnRspError_t );
		data->bIsLast=bIsLast;
		data->nRequestID=nRequestID;
		data->pRspInfo=NULL;

		if(pRspInfo) {
			data->pRspInfo=new(CThostFtdcRspInfoField);
			memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
		}
		/*todo*/
		msg->type=QOnRspError;
		this->ctpquoter->post_msg(msg);
	}
	LOG_INFO<<"Quote OnRspError"<<std::endl;
}
void CtpQuoteSpi::OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

	if ( !this->IsErrorRspInfo(pRspInfo) && pSpecificInstrument ) {  
		msg_t *msg=new(msg_t);
		QOnRspSubMarketData_t *data=new(QOnRspSubMarketData_t);
		data->pRspInfo=NULL;
		memcpy(&data->pSpecificInstrument,pSpecificInstrument,sizeof(CThostFtdcSpecificInstrumentField));
		if(pRspInfo) {
			data->pRspInfo=new(CThostFtdcRspInfoField);
			memcpy(data->pRspInfo, pRspInfo,sizeof(CThostFtdcRspInfoField));
		}
		msg->len=sizeof(QOnRspSubMarketData_t);
		msg->data=(void*)data;
		msg->type=QOnRspSubMarketData;
		this->ctpquoter->post_msg(msg);
	} else {
		/*todo err process
		 * */
	}

	LOG_INFO<<"Quote OnRspSubMarketData"<<std::endl;
}
void CtpQuoteSpi::OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	/*todo bugfix*/

	if ( !this->IsErrorRspInfo(pRspInfo) && pSpecificInstrument ) {  
		msg_t *msg=new(msg_t);
		QOnRspUnSubMarketData_t *data=new(QOnRspUnSubMarketData_t);
		data->bIsLast=bIsLast;
		data->nRequestID=nRequestID;

		memcpy(&data->pSpecificInstrument,pSpecificInstrument,sizeof(CThostFtdcSpecificInstrumentField));
		data->pRspInfo=NULL;
		if(pRspInfo) {
			data->pRspInfo=new (CThostFtdcRspInfoField);
			memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
		}
		msg->len=sizeof(QOnRspUnSubMarketData_t);
		msg->data=(void*)data;
		msg->type=QOnRspUnSubMarketData;
		this->ctpquoter->post_msg(msg);
	}

	LOG_INFO<<"Quote OnRspUnSubMarketData"<<std::endl;
}

void CtpQuoteSpi::OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	/*bug fix*/

	if ( !this->IsErrorRspInfo(pRspInfo) && pRspUserLogin ) {  
		msg_t *msg=new(msg_t);
		QOnRspUserLogin_t *data=new(QOnRspUserLogin_t);
		data->bIsLast=bIsLast;
		data->nRequestID=nRequestID;
		data->pRspInfo=NULL;
		if(pRspInfo) {
			data->pRspInfo=new(CThostFtdcRspInfoField);
			memcpy(&data->pRspInfo,pRspInfo,sizeof(pRspInfo));
		}
		memcpy(&data->pRspUserLogin,pRspUserLogin,sizeof(pRspUserLogin));
		msg->len=sizeof(QOnRspUserLogin_t);
		msg->data=(void*)data;
		msg->type=QOnRspUserLogin;
		this->ctpquoter->post_msg(msg);
	}
	LOG_INFO<<"Quote OnRspUserLogin"<<std::endl;
}

void CtpQuoteSpi::OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	LOG_INFO<<"Quote OnRspUserLogout"<<std::endl;
}

void dump_depthmarketdata(CThostFtdcDepthMarketDataField *dmd)
{
	//
	cout<<"业务日期         ActionDay :     "<<dmd->ActionDay<<endl;
	cout<<"交易所代码       ExchangeID:     "<<dmd->ExchangeID<<endl;
	cout<<"更新时间         UpdateTime:     "<<dmd->UpdateTime<<endl;
	cout<<"最后修改毫秒 UpdateMillisec:     "<<dmd->UpdateMillisec<<endl;
	cout<<"合约ID         InstrumentID:     "<<dmd->InstrumentID<<endl;
	cout<<"交易日           TradingDay:     "<<dmd->TradingDay<<endl;
	cout<<"今收盘           ClosePrice:     "<<dmd->ClosePrice<<endl;
	cout<<"昨收盘        PreClosePrice:     "<<dmd->PreClosePrice<<endl;
	cout<<"今开盘            OpenPrice:     "<<dmd->OpenPrice<<endl;
	cout<<"最高价         HighestPrice:     "<<dmd->HighestPrice<<endl;
	cout<<"最低价          LowestPrice:     "<<dmd->LowestPrice<<endl;
	cout<<"本次结算价  SettlementPrice:     "<<dmd->SettlementPrice<<endl;
	cout<<"上次结算价  PreSettlementPrice:  "<<dmd->PreSettlementPrice<<endl;
	cout<<"涨停板价    UpperLimitPrice:     "<<dmd->UpperLimitPrice<<endl;
	cout<<"跌停板价    LowerLimitPrice:     "<<dmd->LowerLimitPrice<<endl;
	cout<<"昨虚实度           PreDelta:     "<<dmd->PreDelta<<endl;
	cout<<"今虚实度          CurrDelta:     "<<dmd->CurrDelta<<endl;
	cout<<"数量                 Volume:     "<<dmd->Volume<<endl;
	cout<<"成交金额           Turnover:     "<<dmd->Turnover<<endl;
	cout<<"持仓量         OpenInterest:     "<<dmd->OpenInterest<<endl;
	cout<<"买1               BidPrice1:     "<<dmd->BidPrice1<<endl;
	cout<<"最新价            LastPrice:     "<<dmd->LastPrice<<endl;
	cout<<"买2               BidPrice2:     "<<dmd->BidPrice2<<endl;
	cout<<"买3               BidPrice3:     "<<dmd->BidPrice3<<endl;
	cout<<"买4               BidPrice4:     "<<dmd->BidPrice4<<endl;
	cout<<"买5               BidPrice5:     "<<dmd->BidPrice5<<endl;
	cout<<"卖1               AskPrice1:     "<<dmd->AskPrice1<<endl;
	cout<<"卖2               AskPrice2:     "<<dmd->AskPrice2<<endl;
	cout<<"卖3               AskPrice3:     "<<dmd->AskPrice3<<endl;
	cout<<"卖4               AskPrice4:     "<<dmd->AskPrice4<<endl;
	cout<<"卖5               AskPrice5:     "<<dmd->AskPrice5<<endl;
	cout<<"均价           AveragePrice:     "<<dmd->AveragePrice<<endl;
}

void CtpQuoteSpi::OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData)
{
	string contract;
/*
QOnRtnDepthMarketData,
typedef struct {
	CThostFtdcDepthMarketDataField pDepthMarketData;
}QOnRtnDepthMarketData_t;
*/
	//cout<<"Depth market Data post msg"<<endl;
	dump_depthmarketdata(pDepthMarketData);
	msg_t *msg=new(msg_t);
	QOnRtnDepthMarketData_t  *data=new(QOnRtnDepthMarketData_t);

	memcpy(&data->pDepthMarketData,pDepthMarketData,sizeof(CThostFtdcDepthMarketDataField));
	msg->len=sizeof(QOnRtnDepthMarketData_t);
	msg->data=(void*)data;
	msg->type=QOnRtnDepthMarketData;
	contract=pDepthMarketData->InstrumentID;
	this->ctpquoter->post_msg(msg,contract);
	LOG_INFO<<"Quote OnRtnDepthMarketData name: "<<pDepthMarketData->InstrumentID <<std::endl;
}

bool CtpQuoteSpi::IsErrorRspInfo(CThostFtdcRspInfoField *pRspInfo)
{
	// 如果ErrorID != 0, 说明收到了错误的响应
	bool ret = ((pRspInfo) && (pRspInfo->ErrorID != 0));
  if (ret){
    LOG_DEBUG<<"ERR MSG: "<<pRspInfo->ErrorMsg<<endl;
  }
	return ret;
}
