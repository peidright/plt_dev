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
	cerr<<" ���ӽ���ǰ��...�ɹ�"<<endl;
	sem.sem_v();
	this->ReqUserLogin((char*)this->trader->brokerid.c_str(),
		(char*)this->trader->username.c_str(),
		(char*)this->trader->password.c_str()
		);
}

void CtpTradeSpi::ReqUserLogin(TThostFtdcBrokerIDType	vAppId,
	        TThostFtdcUserIDType	vUserId,	TThostFtdcPasswordType	vPasswd)
{
  
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
}

void CtpTradeSpi::OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,
		CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if ( !IsErrorRspInfo(pRspInfo) && pRspUserLogin ) {  
    // ����Ự����	
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
		//CThostFtdcSettlementInfoConfirmField f;
		//memset(&f, 0, sizeof(f));
		/*send Req SettlementInfoConfirm */
		//cout<<"send req settlement confirm"<<endl;
			//this->ReqSettlementInfoConfirm(&f, ++this->requestId);
		this->ReqSettlementInfoConfirm();
		//this->confirm=1;
	}
  if(bIsLast) sem.sem_v();
}


void CtpTradeSpi::ReqSettlementInfoConfirm()
{
	CThostFtdcSettlementInfoConfirmField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->trader->username.c_str());
	int ret = this->api->ReqSettlementInfoConfirm(&req, ++this->requestId);
	cerr<<" ���� | ���ͽ��㵥ȷ��..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;
}

void CtpTradeSpi::OnRspSettlementInfoConfirm(
        CThostFtdcSettlementInfoConfirmField  *pSettlementInfoConfirm, 
        CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{	
	if( !IsErrorRspInfo(pRspInfo) && pSettlementInfoConfirm){
    cerr<<" ��Ӧ | ���㵥..."<<pSettlementInfoConfirm->InvestorID
      <<"...<"<<pSettlementInfoConfirm->ConfirmDate
      <<" "<<pSettlementInfoConfirm->ConfirmTime<<">...ȷ��"<<endl;
	 this->confirm=1;
    }else {
	   cerr<<"fail settlement confirm"<<endl;
	}
  if(bIsLast) sem.sem_v();
}

void CtpTradeSpi::ReqQryInstrument(TThostFtdcInstrumentIDType instId)
{
	CThostFtdcQryInstrumentField req;
	memset(&req, 0, sizeof(req));
    strcpy(req.InstrumentID, instId);//Ϊ�ձ�ʾ��ѯ���к�Լ
	int ret = this->api->ReqQryInstrument(&req, ++this->requestId);
	cerr<<" ���� | ���ͺ�Լ��ѯ..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;
}

void CtpTradeSpi::OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, 
         CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 	
	if ( !IsErrorRspInfo(pRspInfo) &&  pInstrument){
    cerr<<" ��Ӧ | ��Լ:"<<pInstrument->InstrumentID
      <<" ������:"<<pInstrument->DeliveryMonth
      <<" ��ͷ��֤����:"<<pInstrument->LongMarginRatio
      <<" ��ͷ��֤����:"<<pInstrument->ShortMarginRatio<<endl; 
  }
  if(bIsLast) sem.sem_v();
}

void CtpTradeSpi::ReqQryTradingAccount()
{
	CThostFtdcQryTradingAccountField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->trader->username.c_str());
	int ret = this->api->ReqQryTradingAccount(&req, ++this->requestId);
	cerr<<" ���� | �����ʽ��ѯ..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;

}

void CtpTradeSpi::OnRspQryTradingAccount(
    CThostFtdcTradingAccountField *pTradingAccount, 
   CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 
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
}

void CtpTradeSpi::ReqQryInvestorPosition(TThostFtdcInstrumentIDType instId)
{
	CThostFtdcQryInvestorPositionField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->trader->brokerid.c_str());
	strcpy(req.InvestorID, this->trader->username.c_str());
	strcpy(req.InstrumentID, this->trader->username.c_str());	
	int ret = this->api->ReqQryInvestorPosition(&req, ++this->requestId);
	cerr<<" ���� | ���ͳֲֲ�ѯ..."<<((ret == 0)?"�ɹ�":"ʧ��")<<endl;
}

void CtpTradeSpi::OnRspQryInvestorPosition(
    CThostFtdcInvestorPositionField *pInvestorPosition, 
    CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{ 
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
}

void CtpTradeSpi::ReqOrderInsert(TThostFtdcInstrumentIDType instId,
    TThostFtdcDirectionType dir, TThostFtdcCombOffsetFlagType kpp,
    TThostFtdcPriceType price,   TThostFtdcVolumeType vol)
{
	CThostFtdcInputOrderField req;
	memset(&req, 0, sizeof(req));	
	strcpy(req.BrokerID, this->trader->brokerid.c_str());  //Ӧ�õ�Ԫ����	
	strcpy(req.InvestorID, this->trader->username.c_str()); //Ͷ���ߴ���	
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
	//cerr<<" ���� | ���ͱ���..."<<((ret == 0)?"�ɹ�":"ʧ��")<< endl;
}

void CtpTradeSpi::OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, 
          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
  if( !IsErrorRspInfo(pRspInfo) && pInputOrder ){
    cerr<<"��Ӧ | �����ύ�ɹ�...��������:"<<pInputOrder->OrderRef<<endl;  
  }
  if(bIsLast) sem.sem_v();	
}

void CtpTradeSpi::ReqOrderAction(TThostFtdcSequenceNoType orderSeq)
{
	/*???? need todo*/
  bool found=false; unsigned int i=0;
  for(i=0;i<orderList.size();i++){
    if(orderList[i]->BrokerOrderSeq == orderSeq){ found = true; break;}
  }
  if(!found){cerr<<" ���� | ����������."<<endl; return;} 

	CThostFtdcInputOrderActionField req;
	memset(&req, 0, sizeof(req));
	strcpy(req.BrokerID, this->trader->brokerid.c_str());   //���͹�˾����	
	strcpy(req.InvestorID, this->trader->username.c_str()); //Ͷ���ߴ���
	//strcpy(req.OrderRef, pOrderRef); //��������	
	//req.FrontID = frontId;           //ǰ�ñ��	
	//req.SessionID = sessionId;       //�Ự���
    strcpy(req.ExchangeID, orderList[i]->ExchangeID);
    strcpy(req.OrderSysID, orderList[i]->OrderSysID);
	req.ActionFlag = THOST_FTDC_AF_Delete;  //������־ 

	int ret = this->api->ReqOrderAction(&req, ++this->requestId);
	cerr<< " ���� | ���ͳ���..." <<((ret == 0)?"�ɹ�":"ʧ��") << endl;
}

void CtpTradeSpi::OnRspOrderAction(
      CThostFtdcInputOrderActionField *pInputOrderAction, 
      CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{	
  if (!IsErrorRspInfo(pRspInfo) && pInputOrderAction){
    cerr<< " ��Ӧ | �����ɹ�..."
      << "������:"<<pInputOrderAction->ExchangeID
      <<" �������:"<<pInputOrderAction->OrderSysID<<endl;
  }
  if(bIsLast) sem.sem_v();	
}

///�����ر�
void CtpTradeSpi::OnRtnOrder(CThostFtdcOrderField *pOrder)
{	
	/*todo orderlist*/
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
  //cerr<<" �ر� | �������ύ...���:"<<order->BrokerOrderSeq<<endl;
  sem.sem_v();	
}

///�ɽ�֪ͨ
void CtpTradeSpi::OnRtnTrade(CThostFtdcTradeField *pTrade)
{
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
  cerr<<" �ر� | �����ѳɽ�...�ɽ����:"<<trade->TradeID<<endl;
  sem.sem_v();
}

void CtpTradeSpi::OnFrontDisconnected(int nReason)
{
	cerr<<" ��Ӧ | �����ж�..." 
	  << " reason=" << nReason << endl;
}
		
void CtpTradeSpi::OnHeartBeatWarning(int nTimeLapse)
{
	cerr<<" ��Ӧ | ������ʱ����..." 
	  << " TimerLapse = " << nTimeLapse << endl;
}

void CtpTradeSpi::OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	cout<<"error"<<endl;
	IsErrorRspInfo(pRspInfo);
}

bool CtpTradeSpi::IsErrorRspInfo(CThostFtdcRspInfoField *pRspInfo)
{
	// ���ErrorID != 0, ˵���յ��˴������Ӧ
	bool ret = ((pRspInfo) && (pRspInfo->ErrorID != 0));
  if (ret){
    cerr<<" ��Ӧ | "<<pRspInfo->ErrorMsg<<endl;
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
CtpTrade::CtpTrade(Trader *trader)
{
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(TRADE_DIR);
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
