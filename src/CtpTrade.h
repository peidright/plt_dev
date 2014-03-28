#ifndef CTP_TRADERSPI_H_
#define CTP_TRADERSPI_H_

#include "config.h"
#include "ThostFtdcTraderApi.h"
#include "trader.h"
#include "CtpTrader.h"


class CtpTrader;
class CtpTradeApi : public CThostFtdcTraderApi
{
	

};




class CtpTradeSpi : public CThostFtdcTraderSpi
{
public:
	int requestId;
	int frontId;
	int sessionId;
	int nextOrderRef;
	int confirm;
	int login_status;


	CThostFtdcTraderApi *api;
	string test;
	CtpTrader* ctptrader;

	//Quoter *quoter;
	///���ͻ����뽻�׺�̨������ͨ������ʱ����δ��¼ǰ�����÷��������á�
	CtpTradeSpi(CThostFtdcTraderApi* api, CtpTrader *ctptrader):api(api){this->ctptrader=ctptrader;
		this->frontId=0;
		this->sessionId=0;
		this->nextOrderRef=0;
		this->confirm=0;
		this->login_status=0;
	};

	/*
   CtpTradeSpi(CThostFtdcTraderApi* api, Trader *trader):api(api){

	   this->trader=trader;
	   this->frontId=0;
	   this->sessionId=0;
	   this->nextOrderRef=0;
	   this->confirm=0;
	   this->login_status=0;
   };
	*/
   ~CtpTradeSpi(){};

	///���ͻ����뽻�׺�̨������ͨ������ʱ����δ��¼ǰ�����÷��������á�
	virtual void OnFrontConnected();

	///��¼������Ӧ
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,	CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///Ͷ���߽�����ȷ����Ӧ
	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	
	///�����ѯ��Լ��Ӧ
	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///�����ѯ�ʽ��˻���Ӧ
	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///�����ѯͶ���ֲ߳���Ӧ
	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///����¼��������Ӧ
	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///��������������Ӧ
	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	///����Ӧ��
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	
	///���ͻ����뽻�׺�̨ͨ�����ӶϿ�ʱ���÷��������á���������������API���Զ��������ӣ��ͻ��˿ɲ�������
	virtual void OnFrontDisconnected(int nReason);
		
	///������ʱ���档����ʱ��δ�յ�����ʱ���÷��������á�
	virtual void OnHeartBeatWarning(int nTimeLapse);
	
	///����֪ͨ
	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder);

	///�ɽ�֪ͨ
	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade);

public:
	///�û���¼����
	void ReqUserLogin(TThostFtdcBrokerIDType	appId,
	        TThostFtdcUserIDType	userId,	TThostFtdcPasswordType	passwd);
	///Ͷ���߽�����ȷ��
	//void ReqSettlementInfoConfirm();
	void   ReqSettlementInfoConfirm(const char * brokerid, const char *userid);
	
	///�����ѯ��Լ
	void ReqQryInstrument(TThostFtdcInstrumentIDType instId);
	///�����ѯ�ʽ��˻�
	void ReqQryTradingAccount();
	///�����ѯͶ���ֲ߳�
	void ReqQryInvestorPosition(TThostFtdcInstrumentIDType instId);
	///����¼������
  void ReqOrderInsert(TThostFtdcInstrumentIDType instId,
        TThostFtdcDirectionType dir, TThostFtdcCombOffsetFlagType kpp,
        TThostFtdcPriceType price,   TThostFtdcVolumeType vol);
	///������������
	void ReqOrderAction(TThostFtdcSequenceNoType orderSeq);

	// �Ƿ��յ��ɹ�����Ӧ
	bool IsErrorRspInfo(CThostFtdcRspInfoField *pRspInfo);

  void PrintOrders();
  void PrintTrades();

private:
  //CThostFtdcTraderApi* api;
  //CtpTradeApi *api;

};

#endif
