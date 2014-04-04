#include <iostream>
#include <vector>
//#include <sys/sem.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "CtpTrade.h"
#include "ThostFtdcTraderApi.h"
//#include "CtpTraderSpi.h"
#include "CtpTrade.h"
//#include "CtpQuoteSpi.h"
#include "CtpQuote.h"
#include "CSem.h"
#include "config.h"

char MapDirection(char src, bool toOrig=true){
  if(toOrig){
    if('b'==src||'B'==src){src='0';}else if('s'==src||'S'==src){src='1';}
  }else{
    if('0'==src){src='B';}else if('1'==src){src='S';}
  }
  return src;
}
char MapOffset(char src, bool toOrig=true){
  if(toOrig){
    if('o'==src||'O'==src){src='0';}
    else if('c'==src||'C'==src){src='1';}
    else if('j'==src||'J'==src){src='3';}
  }else{
    if('0'==src){src='O';}
    else if('1'==src){src='C';}
    else if('3'==src){src='J';}
  }
  return src;
}
/*
CtpTrader::CtpTrader(CThostFtdcTraderApi* api)
{
}*/

/*
CtpTrader::~CtpTrader(void)
{
}*/


using namespace std;
extern TThostFtdcBrokerIDType appId;		// Ӧ�õ�Ԫ
extern TThostFtdcUserIDType userId;		// Ͷ���ߴ���


extern int requestId; 
extern CSem sem;

// �Ự����
extern int	 frontId;	//ǰ�ñ��
extern int	 sessionId;	//�Ự���
extern char orderRef[13];

vector<CThostFtdcOrderField*> orderList;
vector<CThostFtdcTradeField*> tradeList;

//char MapDirection(char src, bool toOrig);
//char MapOffset(char src, bool toOrig);
    


void CtpTradeSpi::OnFrontConnected()
{
	/*
	sem.sem_v();
	this->ReqUserLogin((char*)this->trader->brokerid.c_str(),
		(char*)this->trader->username.c_str(),
		(char*)this->trader->password.c_str()
		);
	*/
	msg_t *msg=new(msg_t);
	msg->len=sizeof(TOnFrontConnected_t);
	msg->data=new(TOnFrontConnected_t);
	msg->type=TOnFrontConnected;
	LOG_DEBUG<<"TOnFront Connect DEBUG"<<std::endl;
    	this->ctptrader->post_msg(msg);
}

void CtpTradeSpi::ReqUserLogin(TThostFtdcBrokerIDType	vAppId,
	        TThostFtdcUserIDType	vUserId,	TThostFtdcPasswordType	vPasswd)
{
	int ret;
 	/* 
	CThostFtdcReqUserLoginField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, vAppId); strcpy(appId, vAppId); 
	strcpy(req.UserID, vUserId);  strcpy(userId, vUserId); 
	strcpy(req.Password, vPasswd);
	this->login_status=LOGIN;
	int ret = this->api->ReqUserLogin(&req, ++this->requestId);
    	
	if (ret) {
		this->login_status=FAIL;
	}
	cerr<<" ���� | ���͵�¼..."<<((ret == 0) ? "�ɹ�" :"ʧ��") << endl;
	*/
	
	CThostFtdcReqUserLoginField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, vAppId); //strcpy(appId, vAppId); 
	strcpy(req.UserID, vUserId);  //strcpy(userId, vUserId); 
	strcpy(req.Password, vPasswd);
	this->login_status=LOGIN;
	ret = this->api->ReqUserLogin(&req, ++this->requestId);	
	if (ret) {
		this->login_status=FAIL;
	}
	LOG_DEBUG<<"Trade ReqUserLogin send request"<<std::endl;

}

void CtpTradeSpi::OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,
		CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	/*
	if ( !IsErrorRspInfo(pRspInfo) && pRspUserLogin ) {  
		this->frontId = pRspUserLogin->FrontID;
		this->sessionId = pRspUserLogin->SessionID;
		this->nextOrderRef = atoi(pRspUserLogin->MaxOrderRef);
		this->login_status=SUCESS;

		frontId = pRspUserLogin->FrontID;
		sessionId = pRspUserLogin->SessionID;
		nextOrderRef = atoi(pRspUserLogin->MaxOrderRef);
		sprintf(orderRef, "%d", ++nextOrderRef);
    cerr<<" ��Ӧ | ��¼�ɹ�...��ǰ������:"
      <<pRspUserLogin->TradingDay<<endl;     
    }else  {
		this->login_status=FAIL;
	}
	if(pRspInfo->ErrorID==0&&this->confirm==0) {
		CThostFtdcSettlementInfoConfirmField f;
		memset(&f, 0, sizeof(f));
		cout<<"send req settlement confirm"<<endl;
			//this->ReqSettlementInfoConfirm(&f, ++this->requestId);
		this->ReqSettlementInfoConfirm();
		this->confirm=1;
	}
	  if(bIsLast) sem.sem_v();
	*/
	/*
	if(pRspInfo)
		LOG_DEBUG<<pRspInfo->ErrorID<<pRspInfo->ErrorMsg<<std::endl;
	*/
	if ( !IsErrorRspInfo(pRspInfo) && pRspUserLogin ) {  

	msg_t *msg=new(msg_t);
	TOnRspUserLogin_t *data=new(TOnRspUserLogin_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;
	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(pRspInfo));
	}
	memcpy(&data->pRspUserLogin,pRspUserLogin,sizeof(pRspUserLogin));
	msg->len=sizeof(TOnRspUserLogin_t);
	msg->data=(void*)data;
	msg->type=TOnRspUserLogin;
	this->ctptrader->post_msg(msg);
	LOG_DEBUG<<"spi OnRspUserLogin post msg"<<std::endl;
	} else {
		LOG_DEBUG<<"err OnRspUserLogin "<<std::endl;
	}

}


void CtpTradeSpi::ReqSettlementInfoConfirm(const char * brokerid, const char *userid)

{
	CThostFtdcSettlementInfoConfirmField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->ctptrader->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->ctptrader->trader->username.c_str());
	int ret = this->api->ReqSettlementInfoConfirm(&req, ++this->requestId);
	assert(ret==0);
}


void CtpTradeSpi::OnRspSettlementInfoConfirm(
        CThostFtdcSettlementInfoConfirmField  *pSettlementInfoConfirm, 
        CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{	
	/*
	if( !IsErrorRspInfo(pRspInfo) && pSettlementInfoConfirm){
    cerr<<" ��Ӧ | ���㵥..."<<pSettlementInfoConfirm->InvestorID
      <<"...<"<<pSettlementInfoConfirm->ConfirmDate
      <<" "<<pSettlementInfoConfirm->ConfirmTime<<">...ȷ��"<<endl;
	 this->confirm=1;
    }else {
	   cerr<<"fail settlement confirm"<<endl;
	}
  	if(bIsLast) sem.sem_v();
	*/
	if( !IsErrorRspInfo(pRspInfo) && pSettlementInfoConfirm){

	msg_t *msg=new(msg_t);
	TOnRspSettlementInfoConfirm_t *data=new(TOnRspSettlementInfoConfirm_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;

	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(pRspInfo));
	} else {
		LOG_DEBUG<<"spi OnRspSettlement NULL pRspInfo"<<std::endl;
	}
	memcpy(&data->pSettlementInfoConfirm,pSettlementInfoConfirm,sizeof(*pSettlementInfoConfirm));
	msg->len=sizeof(TOnRspSettlementInfoConfirm_t);
	msg->data=(void*)data;
	msg->type=TOnRspSettlementInfoConfirm;
	this->ctptrader->post_msg(msg);
		LOG_DEBUG<<"spi OnRspSettlement ok"<<std::endl;
	}
	else {
		LOG_DEBUG<<"spi OnRspSettlement err"<<std::endl;
	}
}


void CtpTradeSpi::ReqQryInstrument(TThostFtdcInstrumentIDType instId)
{
	CThostFtdcQryInstrumentField req;
	memset(&req, 0, sizeof(req));
    	strcpy(req.InstrumentID, instId);//Ϊ�ձ�ʾ��ѯ���к�Լ
	int ret = this->api->ReqQryInstrument(&req, ++this->requestId);
	assert(ret==0);
}

void CtpTradeSpi::OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, 
         CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 	
	/*
	if ( !IsErrorRspInfo(pRspInfo) &&  pInstrument){
    		cerr<<" ��Ӧ | ��Լ:"<<pInstrument->InstrumentID
      		<<" ������:"<<pInstrument->DeliveryMonth
      		<<" ��ͷ��֤����:"<<pInstrument->LongMarginRatio
      		<<" ��ͷ��֤����:"<<pInstrument->ShortMarginRatio<<endl; 
  	}
  	if(bIsLast) sem.sem_v();
	*/
	if ( !IsErrorRspInfo(pRspInfo) &&  pInstrument){

	msg_t *msg=new(msg_t);
	TOnRspQryInstrument_t *data=new(TOnRspQryInstrument_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;
	data->pRspInfo=NULL;

	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(pRspInfo));
	} else {
		LOG_DEBUG<<"spi OnRspQryInstruent NULL pRspInfo"<<std::endl;
	}

	memcpy(&data->pInstrument,pInstrument,sizeof(*pInstrument));
	msg->len=sizeof(TOnRspQryInstrument_t);
	msg->data=(void*)data;
	msg->type=TOnRspQryInstrument;;
	this->ctptrader->post_msg(msg);
		LOG_DEBUG<<"spi OnRspQryInstruent ok"<<std::endl;
	} else
	{
		LOG_DEBUG<<"spi OnRspQryInstruent err"<<std::endl;
	}
}

void CtpTradeSpi::ReqQryTradingAccount()
{
	CThostFtdcQryTradingAccountField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->ctptrader->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->ctptrader->trader->username.c_str());
	int ret = this->api->ReqQryTradingAccount(&req, ++this->requestId);
	cerr<<" ���� | �����ʽ��ѯ..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;

}


void CtpTradeSpi::OnRspQryTradingAccount(
    CThostFtdcTradingAccountField *pTradingAccount, 
   CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 
	/*
	if (!IsErrorRspInfo(pRspInfo) &&  pTradingAccount){
    cerr<<" ��Ӧ | Ȩ��:"<<pTradingAccount->Balance
      <<" ����:"<<pTradingAccount->Available   
      <<" ��֤��:"<<pTradingAccount->CurrMargin
      <<" ƽ��ӯ��:"<<pTradingAccount->CloseProfit
      <<" �ֲ�ӯ��"<<pTradingAccount->PositionProfit
      <<" ������:"<<pTradingAccount->Commission
      <<" ���ᱣ֤��:"<<pTradingAccount->FrozenMargin
      //<<" ����������:"<<pTradingAccount->FrozenCommission 
      << endl;    
  }
  if(bIsLast) sem.sem_v();
	*/
	msg_t *msg=new(msg_t);
	TOnRspQryTradingAccount_t *data=new(TOnRspQryTradingAccount_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;

	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
	}else {
		LOG_DEBUG<<"spi OnRspQryTradingAccount"<<std::endl;
	}

	memcpy(&data->pTradingAccount,pTradingAccount,sizeof(*pTradingAccount));
	msg->len=sizeof(TOnRspQryTradingAccount_t);
	msg->data=(void*)data;
	msg->type=TOnRspQryTradingAccount;
	this->ctptrader->post_msg(msg);
}

void CtpTradeSpi::ReqQryInvestorPosition(TThostFtdcInstrumentIDType instId)
{
	CThostFtdcQryInvestorPositionField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->ctptrader->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->ctptrader->trader->username.c_str());
	strcpy(req.InstrumentID, this->ctptrader->trader->username.c_str());	
	int ret = this->api->ReqQryInvestorPosition(&req, ++this->requestId);
	cerr<<" ���� | ���ͳֲֲ�ѯ..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;
}



void CtpTradeSpi::OnRspQryInvestorPosition(
    CThostFtdcInvestorPositionField *pInvestorPosition, 
    CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 
	/*
  if( !IsErrorRspInfo(pRspInfo) &&  pInvestorPosition ){
    cerr<<" ��Ӧ | ��Լ:"<<pInvestorPosition->InstrumentID
      <<" ����:"<<MapDirection(pInvestorPosition->PosiDirection-2,false)
      <<" �ֲܳ�:"<<pInvestorPosition->Position
      <<" ���:"<<pInvestorPosition->YdPosition 
      <<" ���:"<<pInvestorPosition->TodayPosition
      <<" �ֲ�ӯ��:"<<pInvestorPosition->PositionProfit
      <<" ��֤��:"<<pInvestorPosition->UseMargin<<endl;
  }
  if(bIsLast) sem.sem_v();
	*/
	msg_t *msg=new(msg_t);
	TOnRspQryInvestorPosition_t *data=new(TOnRspQryInvestorPosition_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;

	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
	}else {
		LOG_DEBUG<<"spi OnRspQryInvestorPosition"<<std::endl;
	}
	memcpy(&data->pInvestorPosition,pInvestorPosition,sizeof(*pInvestorPosition));
	msg->len=sizeof(TOnRspQryInvestorPosition_t);
	msg->data=(void*)data;
	msg->type=TOnRspQryInvestorPosition;
	this->ctptrader->post_msg(msg);
}

void CtpTradeSpi::ReqOrderInsert(TThostFtdcInstrumentIDType instId,
    TThostFtdcDirectionType dir, TThostFtdcCombOffsetFlagType kpp,
    TThostFtdcPriceType price,   TThostFtdcVolumeType vol)
{
	/*
	CThostFtdcInputOrderField req;
	memset(&req, 0, sizeof(req));	
	strcpy(req.BrokerID, this->ctptrader->trader->brokerid.c_str());  //Ӧ�õ�Ԫ����	
	strcpy(req.InvestorID, this->ctptrader->trader->username.c_str()); //Ͷ���ߴ���	
	strcpy(req.InstrumentID, instId); //��Լ����	
	strcpy(req.OrderRef, orderRef);  //��������
	sprintf(req.OrderRef,"%d",this->nextOrderRef);
	this->nextOrderRef++;
  
	//int nextOrderRef = atoi(orderRef);
    //sprintf(orderRef, "%d", ++nextOrderRef);
  
  req.LimitPrice = price;	//�۸�
  if(0==req.LimitPrice){
	  req.OrderPriceType = THOST_FTDC_OPT_AnyPrice;//�۸�����=�м�
	  req.TimeCondition = THOST_FTDC_TC_IOC;//��Ч������:������ɣ�������
  }else{
    req.OrderPriceType = THOST_FTDC_OPT_LimitPrice;//�۸�����=�޼�	
    req.TimeCondition = THOST_FTDC_TC_GFD;  //��Ч������:������Ч
  }
    req.Direction = MapDirection(dir,true);  //��������	
	req.CombOffsetFlag[0] = MapOffset(kpp[0],true); //��Ͽ�ƽ��־:����
	req.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;	  //���Ͷ���ױ���־	
	req.VolumeTotalOriginal = vol;	///����		
	req.VolumeCondition = THOST_FTDC_VC_AV; //�ɽ�������:�κ�����
	req.MinVolume = 1;	//��С�ɽ���:1	
	req.ContingentCondition = THOST_FTDC_CC_Immediately;  //��������:����
	
  	//TThostFtdcPriceType	StopPrice;  //ֹ���
	req.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;	//ǿƽԭ��:��ǿƽ	
	req.IsAutoSuspend = 0;  //�Զ������־:��	
	req.UserForceClose = 0;   //�û�ǿ����־:��

	int ret = this->api->ReqOrderInsert(&req, ++this->requestId);
	*/
}


void CtpTradeSpi::OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, 
          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	/*
  if( !IsErrorRspInfo(pRspInfo) && pInputOrder ){
    cerr<<"��Ӧ | �����ύ�ɹ�...��������:"<<pInputOrder->OrderRef<<endl;  
  }
  if(bIsLast) sem.sem_v();	
	*/
	msg_t *msg=new(msg_t);
	TOnRspOrderInsert_t *data=new(TOnRspOrderInsert_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;

	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
	}else {
		LOG_DEBUG<<"spi OnRspOrderInsert"<<std::endl;
	}

	memcpy(&data->pInputOrder,pInputOrder,sizeof(*pInputOrder));
	msg->len=sizeof(TOnRspOrderInsert_t);
	msg->data=(void*)data;
	msg->type=TOnRspOrderInsert;
	this->ctptrader->post_msg(msg);
}

void CtpTradeSpi::ReqOrderAction(TThostFtdcSequenceNoType orderSeq)
{
	/*
	   bool found=false; unsigned int i=0;
	   for(i=0;i<orderList.size();i++){
	   if(orderList[i]->BrokerOrderSeq == orderSeq){ found = true; break;}
	   }
	   if(!found){cerr<<" ���� | ����������."<<endl; return;} 

	   CThostFtdcInputOrderActionField req;
	   memset(&req, 0, sizeof(req));
	   strcpy(req.BrokerID, this->ctptrader->trader->brokerid.c_str());   //���͹�˾����	
	   strcpy(req.InvestorID, this->ctptrader->trader->username.c_str()); //Ͷ���ߴ���
	//strcpy(req.OrderRef, pOrderRef); //��������	
	//req.FrontID = frontId;           //ǰ�ñ��	
	//req.SessionID = sessionId;       //�Ự���
	strcpy(req.ExchangeID, orderList[i]->ExchangeID);
	strcpy(req.OrderSysID, orderList[i]->OrderSysID);
	req.ActionFlag = THOST_FTDC_AF_Delete;  //������־ 
	int ret = this->api->ReqOrderAction(&req, ++this->requestId);
	*/
}

void CtpTradeSpi::OnRspOrderAction(
      CThostFtdcInputOrderActionField *pInputOrderAction, 
      CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{	
 /*
  if (!IsErrorRspInfo(pRspInfo) && pInputOrderAction){
    cerr<< " ��Ӧ | �����ɹ�..."
      << "������:"<<pInputOrderAction->ExchangeID
      <<" �������:"<<pInputOrderAction->OrderSysID<<endl;
  }
  if(bIsLast) sem.sem_v();	
*/
	msg_t *msg=new(msg_t);
	TOnRspOrderAction_t *data=new(TOnRspOrderAction_t);
	data->bIsLast=bIsLast;
	data->nRequestID=nRequestID;

	data->pRspInfo=NULL;
	if(pRspInfo) {
		data->pRspInfo=new(CThostFtdcRspInfoField);
		memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
	}else {
		LOG_DEBUG<<"spi OnRspOrderAction"<<std::endl;
	}

	memcpy(&data->pInputOrderAction,pInputOrderAction,sizeof(*pInputOrderAction));
	msg->len=sizeof(TOnRspOrderAction_t);
	msg->data=(void*)data;
	msg->type=TOnRspOrderAction;
	this->ctptrader->post_msg(msg);

}

///�����ر�
void CtpTradeSpi::OnRtnOrder(CThostFtdcOrderField *pOrder)
{	
	/*
  CThostFtdcOrderField* order = new CThostFtdcOrderField();
  memcpy(order,  pOrder, sizeof(CThostFtdcOrderField));
  bool founded=false;    unsigned int i=0;
  for(i=0; i<orderList.size(); i++){
    if(orderList[i]->BrokerOrderSeq == order->BrokerOrderSeq) {
      founded=true;    break;
    }
  }
  if(founded) orderList[i]= order;   
  else  orderList.push_back(order);
  */
	msg_t *msg=new(msg_t);
	TOnRtnOrder_t *data=new(TOnRtnOrder_t);
	memcpy(&data->pOrder,pOrder,sizeof(CThostFtdcOrderField));
	msg->len=sizeof(TOnRtnOrder_t);
	msg->data=(void*)data;
	msg->type=TOnRtnOrder;
	this->ctptrader->post_msg(msg);
}

///�ɽ�֪ͨ
void CtpTradeSpi::OnRtnTrade(CThostFtdcTradeField *pTrade)
{
	/*
	   CThostFtdcTradeField* trade = new CThostFtdcTradeField();
	   memcpy(trade,  pTrade, sizeof(CThostFtdcTradeField));
	   bool founded=false;     unsigned int i=0;
	   for(i=0; i<tradeList.size(); i++){
	   if(tradeList[i]->TradeID == trade->TradeID) {
	   founded=true;   break;
	   }
	   }
  	if(founded) tradeList[i] = trade;   
  	else  tradeList.push_back(trade);
  	sem.sem_v();
  	*/
	msg_t *msg=new(msg_t);
	TOnRtnTrade_t *data=new(TOnRtnTrade_t);
	memcpy(&data->pTrade,pTrade,sizeof( CThostFtdcTradeField));
	msg->len=sizeof(TOnRtnTrade_t);
	msg->data=(void*)data;
	msg->type=TOnRtnTrade;
	this->ctptrader->post_msg(msg);
}

void CtpTradeSpi::OnFrontDisconnected(int nReason)
{
	/*
	cerr<<" ��Ӧ | �����ж�..." 
	  << " reason=" << nReason << endl;
	*/
	msg_t *msg=new(msg_t);
	TOnFrontDisconnected_t *data=new(TOnFrontDisconnected_t);
	data->nReason=nReason;
	msg->len=sizeof(TOnFrontDisconnected_t);
	msg->data=(void*)data;
	msg->type=TOnFrontDisconnected;
	this->ctptrader->post_msg(msg);

}
		
void CtpTradeSpi::OnHeartBeatWarning(int nTimeLapse)
{
	/*
	cerr<<" ��Ӧ | ������ʱ����..." 
	  << " TimerLapse = " << nTimeLapse << endl;
	*/

	msg_t *msg=new(msg_t);
	TOnHeartBeatWarning_t *data=new(TOnHeartBeatWarning_t);
	data->nTimeLapse=nTimeLapse;
	msg->len=sizeof(TOnHeartBeatWarning_t);
	msg->data=(void*)data;
	msg->type=TOnHeartBeatWarning;
	this->ctptrader->post_msg(msg);

}

void CtpTradeSpi::OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	//IsErrorRspInfo(pRspInfo);
	if(!this->IsErrorRspInfo(pRspInfo)) {
		msg_t *msg=new(msg_t);
		TOnRspError_t *data=new(TOnRspError_t);
		data->bIsLast=bIsLast;
		data->nRequestID=nRequestID;
		data->pRspInfo=NULL;
		msg->len=sizeof(TOnRspError_t);
		msg->type=TOnRspError;
		if(pRspInfo) {
			data->pRspInfo=new(CThostFtdcRspInfoField);
			memcpy(data->pRspInfo,pRspInfo,sizeof(CThostFtdcRspInfoField));
		} else {
			LOG_DEBUG<<"spi OnRspInfo is NULL"<<std::endl;
		}
	} else {
		LOG_DEBUG<<"spi OnRspError pRspInfo error"<<std::endl;
	}
}

bool CtpTradeSpi::IsErrorRspInfo(CThostFtdcRspInfoField *pRspInfo)
{
	// ���ErrorID != 0, ˵���յ��˴������Ӧ
	bool ret = ((pRspInfo) && (pRspInfo->ErrorID != 0));
  if (ret){
    LOG_DEBUG<<"ERR MSG: "<<pRspInfo->ErrorMsg<<endl;
  }
	return ret;
}

void CtpTradeSpi::PrintOrders(){
  CThostFtdcOrderField* pOrder; 
  for(unsigned int i=0; i<orderList.size(); i++){
    pOrder = orderList[i];
    cerr<<" ���� | ��Լ:"<<pOrder->InstrumentID
      <<" ����:"<<MapDirection(pOrder->Direction,false)
      <<" ��ƽ:"<<MapOffset(pOrder->CombOffsetFlag[0],false)
      <<" �۸�:"<<pOrder->LimitPrice
      <<" ����:"<<pOrder->VolumeTotalOriginal
      <<" ���:"<<pOrder->BrokerOrderSeq 
      <<" �������:"<<pOrder->OrderSysID
      <<" ״̬:"<<pOrder->StatusMsg<<endl;
  }
  sem.sem_v();
}
void CtpTradeSpi::PrintTrades(){
  CThostFtdcTradeField* pTrade;
  for(unsigned int i=0; i<tradeList.size(); i++){
    pTrade = tradeList[i];
    cerr<<" �ɽ� | ��Լ:"<< pTrade->InstrumentID 
      <<" ����:"<<MapDirection(pTrade->Direction,false)
      <<" ��ƽ:"<<MapOffset(pTrade->OffsetFlag,false) 
      <<" �۸�:"<<pTrade->Price
      <<" ����:"<<pTrade->Volume
      <<" �������:"<<pTrade->OrderSysID
      <<" �ɽ����:"<<pTrade->TradeID<<endl;
  }
  sem.sem_v();
}
//char MapDirection(char src, bool toOrig=true);
//char MapOffset(char src, bool toOrig=true);
/*
CtpTrade::CtpTrade(Trader *trader, string localdir)
{
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(localdir.c_str());
	this->trade_api=trade_api;
	CtpTradeSpi* trade_spi = new CtpTradeSpi(trade_api,trader);
	this->trade_spi = trade_spi;

	trade_api->RegisterSpi((CThostFtdcTraderSpi*)trade_spi);			// ע���¼���
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// ע�ṫ����
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // ע��˽����
	trade_api->RegisterFront((char*)trader->trade_addr.c_str());	// ע�ύ��ǰ�õ�ַ
	

	
	CThostFtdcMdApi *quote_api = CThostFtdcMdApi::CreateFtdcMdApi(QUOTE_DIR);
	CtpQuoteSpi *quote_spi = new CtpQuoteSpi(quote_api,trader);
	quote_api->RegisterSpi((CThostFtdcMdSpi*)quote_spi);
	quote_api->RegisterFront((char*)trader->trade_addr.c_str());
	

	md->Init();
	cout<<"market init"<<endl;
	pUserApi->Init();
	//todo
	pUserApi->Join();
	
}*/



void CtpTradeSpi::OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus)
{
	msg_t *msg=new(msg_t);
	msg->len=sizeof(TOnRtnInstrumentStatus_t);
	TOnRtnInstrumentStatus_t *data=new(TOnRtnInstrumentStatus_t);
	memcpy(&data->pInstrumentStatus, pInstrumentStatus, sizeof(CThostFtdcInstrumentStatusField));
	/*
THOST_FTDC_IS_BeforeTrading '0'
THOST_FTDC_IS_NoTrading '1'
THOST_FTDC_IS_Continous '2'
THOST_FTDC_IS_AuctionOrdering '3'
THOST_FTDC_IS_AuctionBalance '4'
THOST_FTDC_IS_AuctionMatch '5'
THOST_FTDC_IS_Closed '6'
	*/
	msg->data=data;
	msg->type= TOnRtnInstrumentStatus;
	LOG_DEBUG<<"OnRtnInstrumentStatus: name"<<pInstrumentStatus->InstrumentID<<" Status:" <<pInstrumentStatus->InstrumentStatus <<std::endl;
    	this->ctptrader->post_msg(msg);
	return;
}
