#ifndef MSGQUEUE1_H_
#define MSGQUEUE1_H_
#include <iostream>
#include <vector>
//#include <sys/sem.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
//#include "CtpTrade.h"
#include "ThostFtdcTraderApi.h"

//#include "CtpQuote.h"
#include "boosthelp.h"



enum msgtype {
    MSG_NULL=0,
	TChange=6,
	KChange=7,
	TMessage=8,
	TSTOP=9,
	TSTART=10,
	TOnFrontConnected=11,
	TReqUserLogin=12,
	TOnRspUserLogin=13,

	TReqSettlementInfoConfirm=14,
	TOnRspSettlementInfoConfirm=15,
	
	TReqQryInstrument=16,
	TOnRspQryInstrument=17,
	
	TReqQryTradingAccount=18,
	TOnRspQryTradingAccount=19,

	TReqQryInvestorPosition=20,
	TOnRspQryInvestorPosition=21,

	TReqOrderInsert=22,
	TOnRspOrderInsert=23,

	TReqOrderAction=24,
	TOnRspOrderAction=25,
	TOnRtnInstrumentStatus=26,


	TOnRtnOrder=27,
	TOnRtnTrade=28,
	TOnFrontDisconnected=29,
	TOnHeartBeatWarning=30,
	TOnRspError=31,

	TRADE_QUOTE=64,
	QSTOP=65,
	QSTART=66,
	QOnFrontConnected=67,
	QOnFrontDisconnected=68,
	QOnHeartBeatWarning=69,
	QOnRspError=70,
	QReqSubscribeMarketData=71,
    	QOnRspSubMarketData=72,
	QOnRspUnSubMarketData=73,
	QReqUserLogin=74,
	QOnRspUserLogin=75,
	QOnRspUserLogout=76,
	QOnRtnDepthMarketData=77,

    TRADE_STRATEGY=128,

    SRegMdInst=129,
    SRegMdPeriod=130,
    SRegMdStrategy=131,
    SRegRspCommon =196,
};


typedef struct  msg_s{
	msgtype type;
	int     len;
	void    *data;
}msg_t;

/*
class msg_t {
public:
	msgtype type;
	int     len;
	void    *data;
};*/

typedef struct  {
}TOnFrontConnected_t;

typedef struct {
	struct CThostFtdcRspUserLoginField pRspUserLogin;
	struct CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspUserLogin_t;

typedef struct {
	CThostFtdcSettlementInfoConfirmField  pSettlementInfoConfirm;
	struct CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspSettlementInfoConfirm_t;

typedef struct {
	CThostFtdcInstrumentField pInstrument;
    	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspQryInstrument_t;

typedef struct {
	CThostFtdcTradingAccountField pTradingAccount;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspQryTradingAccount_t;

typedef struct {
	CThostFtdcInvestorPositionField pInvestorPosition;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspQryInvestorPosition_t;

typedef struct {
    	CThostFtdcInputOrderField pInputOrder;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspOrderInsert_t;

typedef struct {
	  CThostFtdcInputOrderActionField pInputOrderAction;
      	  CThostFtdcRspInfoField *pRspInfo;
	  int nRequestID;
	  bool bIsLast;
}TOnRspOrderAction_t;

typedef struct {
	CThostFtdcInstrumentStatusField pInstrumentStatus;
}TOnRtnInstrumentStatus_t;

typedef struct {
	  CThostFtdcOrderField  pOrder;
}TOnRtnOrder_t;

typedef struct {
	CThostFtdcTradeField pTrade;
}TOnRtnTrade_t;

typedef struct {
	int nReason;
}TOnFrontDisconnected_t;
	

typedef struct {
	int nTimeLapse;
}TOnHeartBeatWarning_t;

typedef struct {
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}TOnRspError_t;

typedef struct {
}QOnFrontConnected_t;

typedef struct {
	int nReason;
}QOnFrontDisconnected_t;
typedef struct {
	int nTimeLapse;
}QOnHeartBeatWarning_t;

typedef struct {
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}QOnRspError_t;

typedef struct {
	CThostFtdcSpecificInstrumentField pSpecificInstrument;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}QOnRspSubMarketData_t;

typedef struct {
	CThostFtdcSpecificInstrumentField pSpecificInstrument;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}QOnRspUnSubMarketData_t;

typedef struct {
	CThostFtdcRspUserLoginField  pRspUserLogin;
	CThostFtdcRspInfoField       *pRspInfo;
	int nRequestID;
	bool bIsLast;
}QOnRspUserLogin_t;

typedef struct {
	CThostFtdcUserLogoutField pUserLogout;
	CThostFtdcRspInfoField *pRspInfo;
	int nRequestID;
	bool bIsLast;
}QOnRspUserLogout_t;

typedef struct {
	CThostFtdcDepthMarketDataField pDepthMarketData;
}QOnRtnDepthMarketData_t;

typedef struct  {
	int subtype;
	float v;
}TChange_t;

typedef struct  {
	int subtype;
	float o;
	float c;
	float h;
	float l;
}KChange_t;

typedef struct {
    //int regmd_strategy(string instn, int sid, int period);
}SRegMdInst_t;
typedef struct {
	//int regmd_period(string contract,period_type ptype, int period);
    //if period==0,is MIRCO,else is ...
    string instn;
    int period;
}SRegMdPeriod_t;

typedef struct {
    string instn;
    int sid;
    int period;
}SRegMdStrategy_t;

typedef struct {
    int ret;
}SRegRspCommon_t;

#endif
