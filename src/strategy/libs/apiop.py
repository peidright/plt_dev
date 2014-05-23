import json
import sframe_agent
import apiop
import apistruct

type2valmap={
        "MSG_NULL":0,
        "TChange":6,
        "KChange":7,
        "TMessage":8,
        "TSTOP":9,
        "TSTART":10,
        "TOnFrontConnected":11,
        "TReqUserLogin":12,
        "TOnRspUserLogin":13,

        "TReqSettlementInfoConfirm":14,
        "TOnRspSettlementInfoConfirm":15,

        "TReqQryInstrument":16,
        "TOnRspQryInstrument":17,

        "TReqQryTradingAccount":18,
        "TOnRspQryTradingAccount":19,

        "TReqQryInvestorPosition":20,
        "TOnRspQryInvestorPosition":21,

        "TReqOrderInsert":22,
        "TOnRspOrderInsert":23,

        "TReqOrderAction":24,
        "TOnRspOrderAction":25,
        "TOnRtnInstrumentStatus":26,

        "TOnRtnOrder":27,
        "TOnRtnTrade":28,
        "TOnFrontDisconnected":29,
        "TOnHeartBeatWarning":30,
        "TOnRspError":31,

        "TRADE_QUOTE":64,
        "QSTOP":65,
        "QSTART":66,
        "QOnFrontConnected":67,
        "QOnFrontDisconnected":68,
        "QOnHeartBeatWarning":69,
        "QOnRspError":70,
        "QReqSubscribeMarketData":71,
        "QOnRspSubMarketData":72,
        "QOnRspUnSubMarketData":73,
        "QReqUserLogin":74,
        "QOnRspUserLogin":75,
        "QOnRspUserLogout":76,
        "QOnRtnDepthMarketData":77,

"TRADE_STRATEGY":128,

    "SRegMdInst":129,
    "SRegMdPeriod":130,
    "SRegMdStrategy":131,
    "SRegRspCommon":196,
}
op2req={
        "TReqAuthenticate":{},
        "TReqUserLogin":{},
        "TReqUserLogout":{},
        "TReqUserLogout":{},
        "TReqQryInstrument":{"instn":"","sid":-1},
        "TReqQryTradingAccount":{"sid":-1},
        "TReqQryInvestorPosition":{"instn":"","sid":-1},
        "TReqOrderInsert":{"instn":"","dir":-1,"price":0,"vol":0,"sid":-1},
        "TReqOrderAction":{"exchangeid":-1,"ordersysid":-1,"sid":-1},
        "SRegMdStrategy":{},
}

class apiop:
    agent=None;
    sid  =None;
    def ReqAuthenticate(self,req):
        #CThostFtdcReqAuthenticateField 
        return {"retmsg":"not implement"};
        pass
    def ReqUserLogin(self,req):
        #CThostFtdcReqUserLoginField *pReqUserLoginField
        return {"retmsg":"not implement"};
        pass
    def ReqUserLogout(self,req):
        #CThostFtdcUserLogoutField *pUserLogout
        return {"retmsg":"not implement"};
        pass
    def ReqUserPasswordUpdate(self,req):
        #CThostFtdcUserPasswordUpdateField 
        return {"retmsg":"not implement"};
        pass
    def ReqTradingAccountPasswordUpdate(self,req):
        #CThostFtdcTradingAccountPasswordUpdateField 
        return {"retmsg":"not implement"};
        pass
    def ReqOrderInsert(self,req):
        #TThostFtdcInstrumentIDType instId,
        #TThostFtdcDirectionType dir, TThostFtdcCombOffsetFlagType kpp,
        #TThostFtdcPriceType price,   TThostFtdcVolumeType vol)
        return {"retmsg":"not implement"};
        pass
    def ReqParkedOrderInsert(self,req):
        #CThostFtdcParkedOrderField 
        return {"retmsg":"not implement"};
        pass
    def ReqParkedOrderAction(self,req):
        #CThostFtdcParkedOrderActionField 
        return {"retmsg":"not implement"};
        pass
    def ReqOrderAction(self,req):
        #TThostFtdcSequenceNoType 
        return {"retmsg":"not implement"};
        pass
    def ReqQueryMaxOrderVolume(self,req):
        return {"retmsg":"not implement"};
        #CThostFtdcQueryMaxOrderVolumeField 
        pass
    def ReqSettlementInfoConfirm(self,req):
        #CThostFtdcSettlementInfoConfirmField 
        return {"retmsg":"not implement"};


        pass
    def ReqRemoveParkedOrder(self,req):
        #CThostFtdcRemoveParkedOrderField 
        return {"retmsg":"not implement"};

        pass
    def ReqRemoveParkedOrderAction(self,req):
        #CThostFtdcRemoveParkedOrderActionField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryOrder(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryOrderField 
        pass
    def ReqQryTrade(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryTradeField 
        pass
    def ReqQryInvestorPosition(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryInvestorPositionField 
        pass
    def ReqQryTradingAccount(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryTradingAccountField 
        pass
    def ReqQryInvestor(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryInvestorField 
        pass
    def ReqQryTradingCode(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryTradingCodeField 
        pass
    def ReqQryInstrumentMarginRate(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryInstrumentMarginRateField 
        pass
    def ReqQryInstrumentCommissionRate(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryInstrumentCommissionRateField 
        pass
    def ReqQryExchange(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryExchangeField 
        pass
    def ReqQryInstrument(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryInstrumentField 
        pass
    def ReqQryDepthMarketData(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQryDepthMarketDataField 
        pass
    def ReqQrySettlementInfo(self,req):
        return {"retmsg":"not implement"};

        #CThostFtdcQrySettlementInfoField 
        pass
    def ReqQryTransferBank(self,req):
        #CThostFtdcQryTransferBankField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryInvestorPositionDetail(self,req):
        #CThostFtdcQryInvestorPositionDetailField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryNotice(self,req):
        #CThostFtdcQryNoticeField 
        return {"retmsg":"not implement"};

        pass
    def ReqQrySettlementInfoConfirm(self,req):
        #CThostFtdcQrySettlementInfoConfirmField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryInvestorPositionCombineDetail(self,req):
        #CThostFtdcQryInvestorPositionCombineDetailField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryCFMMCTradingAccountKey(self,req):
        #CThostFtdcQryCFMMCTradingAccountKeyField
        return {"retmsg":"not implement"};

        pass
    def ReqQryEWarrantOffset(self,req):
        #CThostFtdcQryEWarrantOffsetField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryInvestorProductGroupMargin(self,req):
        #CThostFtdcQryInvestorProductGroupMarginField
        return {"retmsg":"not implement"};

        pass
    def ReqQryExchangeMarginRate(self,req):
        #CThostFtdcQryExchangeMarginRateField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryExchangeMarginRateAdjust(self,req):
        #CThostFtdcQryExchangeMarginRateAdjustField
        return {"retmsg":"not implement"};

        pass
    def ReqQryTransferSerial(self,req):
        #CThostFtdcQryTransferSerialField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryAccountregister(self,req):
        #CThostFtdcQryAccountregisterField
        return {"retmsg":"not implement"};

        pass
    def ReqQryContractBank(self,req):
        #CThostFtdcQryContractBankField
        return {"retmsg":"not implement"};

        pass
    def ReqQryParkedOrder(self,req):
        #CThostFtdcQryParkedOrderField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryParkedOrderAction(self,req):
        #CThostFtdcQryParkedOrderActionField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryTradingNotice(self,req):
        #CThostFtdcQryTradingNoticeField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryBrokerTradingParams(self,req):
        #CThostFtdcQryBrokerTradingParamsField 
        return {"retmsg":"not implement"};

        pass
    def ReqQryBrokerTradingAlgos(self,req):
        #CThostFtdcQryBrokerTradingAlgosField 
        return {"retmsg":"not implement"};

        pass
    def ReqFromBankToFutureByFuture(self,req):
        #CThostFtdcReqTransferField 
        return {"retmsg":"not implement"};

        pass
    def ReqFromFutureToBankByFuture(self,req):
        #CThostFtdcReqTransferField 
        return {"retmsg":"not implement"};

        pass
    def ReqQueryBankAccountMoneyByFuture(self,req):
        #CThostFtdcReqQueryAccountField 
        return {"retmsg":"not implement"};
        pass
    def buy(self,lots,price,type):
        return {"retmsg":"not implement"};
        pass
    def sell(self,lots,price,type):
        return {"retmsg":"not implement"};
        pass
    def buycover(self,lots,price,type):
        return {"retmsg":"not implement"};
        pass
    def sellcover(self,lots,price,type):
        return {"retmsg":"not implement"};
        pass
