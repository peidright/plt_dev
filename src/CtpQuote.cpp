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
	this->api = CThostFtdcMdApi::CreateFtdcMdApi("./qlog");
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
}
int CtpQuoteApi::Join()
{
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
}
void CtpQuoteApi::RegisterSpi(CThostFtdcMdSpi *pSpi)
{
}


void CtpQuoteApi::Release()
{
}
int CtpQuoteApi::ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID)
{
	return 0;
}
int CtpQuoteApi::ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID)
{
	return 0;
}
int CtpQuoteApi::SubscribeMarketData(char *ppInstrumentID[], int nCount)
{
	return 0;
}

int CtpQuoteApi::UnSubscribeMarketData(char *ppInstrumentID[], int nCount)
{
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

	printf("OnFront Connect DEBUG\n");
    	this->ctpquoter->post_msg(msg);
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
		this->login_status=FAIL;
	}
	cerr<<"ReqUserLogin send request"<<std::endl;
#endif
	return ret;
}

void CtpQuoteSpi::OnFrontDisconnected(int nReason)
{
}
void CtpQuoteSpi::OnHeartBeatWarning(int nTimeLapse)
{
}
void CtpQuoteSpi::OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}
void CtpQuoteSpi::OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	cerr<<"sub md begin--------"<<std::endl;
	cout<<pSpecificInstrument->InstrumentID<<std::endl;
	cout<<pRspInfo->ErrorID<<pRspInfo->ErrorMsg<<std::endl;
	msg_t *msg=new(msg_t);
	QOnRspSubMarketData_t *data=new(QOnRspSubMarketData_t);
	msg->len=sizeof(QOnRspSubMarketData_t);
	msg->data=(void*)data;
	msg->type=QOnRspSubMarketData;
    	this->ctpquoter->post_msg(msg);
	cerr<<"sub md end----------"<<std::endl;
}
void CtpQuoteSpi::OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	cout<<pSpecificInstrument->InstrumentID<<std::endl;
	cout<<pRspInfo->ErrorID<<pRspInfo->ErrorMsg<<std::endl;
	msg_t *msg=new(msg_t);
	QOnRspUnSubMarketData_t *data=new(QOnRspUnSubMarketData_t);
	msg->len=sizeof(QOnRspUnSubMarketData_t);
	msg->data=(void*)data;
	msg->type=QOnRspUnSubMarketData;
    this->ctpquoter->post_msg(msg);
}

void CtpQuoteSpi::OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	/**/
	printf("on rsp login\n");
	cout<<pRspInfo->ErrorID<<pRspInfo->ErrorMsg<<std::endl;
	msg_t *msg=new(msg_t);
	QOnRspUserLogin_t *data=new(QOnRspUserLogin_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;
	memcpy(&data->pRspInfo,pRspInfo,sizeof(pRspInfo));
	memcpy(&data->pRspUserLogin,pRspUserLogin,sizeof(pRspUserLogin));
	msg->len=sizeof(QOnRspUserLogin_t);
	msg->data=(void*)data;
	msg->type=QOnRspUserLogin;
	this->ctpquoter->post_msg(msg);
	printf("OnRspUserLogin post msg");
}

void CtpQuoteSpi::OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

void dump_depthmarketdata(CThostFtdcDepthMarketDataField *dmd)
{
	//
	cout<<"ҵ������         ActionDay :     "<<dmd->ActionDay<<endl;
	cout<<"����������       ExchangeID:     "<<dmd->ExchangeID<<endl;
	cout<<"����ʱ��         UpdateTime:     "<<dmd->UpdateTime<<endl;
	cout<<"����޸ĺ��� UpdateMillisec:     "<<dmd->UpdateMillisec<<endl;
	cout<<"��ԼID         InstrumentID:     "<<dmd->InstrumentID<<endl;
	cout<<"������           TradingDay:     "<<dmd->TradingDay<<endl;
	cout<<"������           ClosePrice:     "<<dmd->ClosePrice<<endl;
	cout<<"������        PreClosePrice:     "<<dmd->PreClosePrice<<endl;
	cout<<"����            OpenPrice:     "<<dmd->OpenPrice<<endl;
	cout<<"��߼�         HighestPrice:     "<<dmd->HighestPrice<<endl;
	cout<<"��ͼ�          LowestPrice:     "<<dmd->LowestPrice<<endl;
	cout<<"���ν����  SettlementPrice:     "<<dmd->SettlementPrice<<endl;
	cout<<"�ϴν����  PreSettlementPrice:  "<<dmd->PreSettlementPrice<<endl;
	cout<<"��ͣ���    UpperLimitPrice:     "<<dmd->UpperLimitPrice<<endl;
	cout<<"��ͣ���    LowerLimitPrice:     "<<dmd->LowerLimitPrice<<endl;
	cout<<"����ʵ��           PreDelta:     "<<dmd->PreDelta<<endl;
	cout<<"����ʵ��          CurrDelta:     "<<dmd->CurrDelta<<endl;
	cout<<"����                 Volume:     "<<dmd->Volume<<endl;
	cout<<"�ɽ����           Turnover:     "<<dmd->Turnover<<endl;
	cout<<"�ֲ���         OpenInterest:     "<<dmd->OpenInterest<<endl;
	cout<<"��1               BidPrice1:     "<<dmd->BidPrice1<<endl;
	cout<<"���¼�            LastPrice:     "<<dmd->LastPrice<<endl;
	/*
	cout<<"��2               BidPrice2:     "<<dmd->BidPrice2<<endl;
	cout<<"��3               BidPrice3:     "<<dmd->BidPrice3<<endl;
	cout<<"��4               BidPrice4:     "<<dmd->BidPrice4<<endl;
	cout<<"��5               BidPrice5:     "<<dmd->BidPrice5<<endl;
	*/
	cout<<"��1               AskPrice1:     "<<dmd->AskPrice1<<endl;
	/*
	cout<<"��2               AskPrice1:     "<<dmd->AskPrice2<<endl;
	cout<<"��3               AskPrice1:     "<<dmd->AskPrice3<<endl;
	cout<<"��4               AskPrice1:     "<<dmd->AskPrice4<<endl;
	cout<<"��5               AskPrice1:     "<<dmd->AskPrice5<<endl;
	*/
	cout<<"����           AveragePrice:     "<<dmd->AveragePrice<<endl;
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

}

