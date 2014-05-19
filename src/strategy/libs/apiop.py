

class apiop:
    def __init__(self):
        self.op_vec=[];
        self.op_map={};
    def ReqAuthenticate(self,req):
        #CThostFtdcReqAuthenticateField 
        pass
    def ReqUserLogin(self,req):
        #CThostFtdcReqUserLoginField *pReqUserLoginField
        pass
    def ReqUserLogout(self,req):
        #CThostFtdcUserLogoutField *pUserLogout
        pass
    def ReqUserPasswordUpdate(self,req):
        #CThostFtdcUserPasswordUpdateField 
        pass
    def ReqTradingAccountPasswordUpdate(self,req):
        #CThostFtdcTradingAccountPasswordUpdateField 
        pass
    def ReqOrderInsert(self,req):
        #TThostFtdcInstrumentIDType instId,
        #TThostFtdcDirectionType dir, TThostFtdcCombOffsetFlagType kpp,
        #TThostFtdcPriceType price,   TThostFtdcVolumeType vol)
        pass
    def ReqParkedOrderInsert(self,req):
        #CThostFtdcParkedOrderField 
        pass
    def ReqParkedOrderAction(self,req):
        #CThostFtdcParkedOrderActionField 
        pass
    def ReqOrderAction(self,req):
        #TThostFtdcSequenceNoType 
        pass
    def ReqQueryMaxOrderVolume(self,req):
        #CThostFtdcQueryMaxOrderVolumeField 
        pass
    def ReqSettlementInfoConfirm(self,req):
        #CThostFtdcSettlementInfoConfirmField 
        pass
    def ReqRemoveParkedOrder(self,req):
        #CThostFtdcRemoveParkedOrderField 
        pass
    def ReqRemoveParkedOrderAction(self,req):
        #CThostFtdcRemoveParkedOrderActionField 
        pass
    def ReqQryOrder(self,req):
        #CThostFtdcQryOrderField 
        pass
    def ReqQryTrade(self,req):
        #CThostFtdcQryTradeField 
        pass
    def ReqQryInvestorPosition(self,req):
        #CThostFtdcQryInvestorPositionField 
        pass
    def ReqQryTradingAccount(self,req):
        #CThostFtdcQryTradingAccountField 
        pass
    def ReqQryInvestor(self,req):
        #CThostFtdcQryInvestorField 
        pass
    def ReqQryTradingCode(self,req):
        #CThostFtdcQryTradingCodeField 
        pass
    def ReqQryInstrumentMarginRate(self,req):
        #CThostFtdcQryInstrumentMarginRateField 
        pass
    def ReqQryInstrumentCommissionRate(self,req):
        #CThostFtdcQryInstrumentCommissionRateField 
        pass
    def ReqQryExchange(self,req):
        #CThostFtdcQryExchangeField 
        pass
    def ReqQryInstrument(self,req):
        #CThostFtdcQryInstrumentField 
        pass
    def ReqQryDepthMarketData(self,req):
        #CThostFtdcQryDepthMarketDataField 
        pass
    def ReqQrySettlementInfo(self,req):
        #CThostFtdcQrySettlementInfoField 
        pass
    def ReqQryTransferBank(self,req):
        #CThostFtdcQryTransferBankField 
        pass
    def ReqQryInvestorPositionDetail(self,req):
        #CThostFtdcQryInvestorPositionDetailField 
        pass
    def ReqQryNotice(self,req):
        #CThostFtdcQryNoticeField 
        pass
    def ReqQrySettlementInfoConfirm(self,req):
        #CThostFtdcQrySettlementInfoConfirmField 
        pass
    def ReqQryInvestorPositionCombineDetail(self,req):
        #CThostFtdcQryInvestorPositionCombineDetailField 
        pass
    def ReqQryCFMMCTradingAccountKey(self,req):
        #CThostFtdcQryCFMMCTradingAccountKeyField
        pass
    def ReqQryEWarrantOffset(self,req):
        #CThostFtdcQryEWarrantOffsetField 
        pass
    def ReqQryInvestorProductGroupMargin(self,req):
        #CThostFtdcQryInvestorProductGroupMarginField
        pass
    def ReqQryExchangeMarginRate(self,req):
        #CThostFtdcQryExchangeMarginRateField 
        pass
    def ReqQryExchangeMarginRateAdjust(self,req):
        #CThostFtdcQryExchangeMarginRateAdjustField
        pass
    def ReqQryTransferSerial(self,req):
        #CThostFtdcQryTransferSerialField 
        pass
    def ReqQryAccountregister(self,req):
        #CThostFtdcQryAccountregisterField
        pass
    def ReqQryContractBank(self,req):
        #CThostFtdcQryContractBankField
        pass
    def ReqQryParkedOrder(self,req):
        #CThostFtdcQryParkedOrderField 
        pass
    def ReqQryParkedOrderAction(self,req):
        #CThostFtdcQryParkedOrderActionField 
        pass
    def ReqQryTradingNotice(self,req):
        #CThostFtdcQryTradingNoticeField 
        pass
    def ReqQryBrokerTradingParams(self,req):
        #CThostFtdcQryBrokerTradingParamsField 
        pass
    def ReqQryBrokerTradingAlgos(self,req):
        #CThostFtdcQryBrokerTradingAlgosField 
        pass
    def ReqFromBankToFutureByFuture(self,req):
        #CThostFtdcReqTransferField 
        pass
    def ReqFromFutureToBankByFuture(self,req):
        #CThostFtdcReqTransferField 
        pass
    def ReqQueryBankAccountMoneyByFuture(self,req):
        #CThostFtdcReqQueryAccountField 
        pass
    def buy(self,lots,price,type):
        #
        pass
    def sell(self,lots,price,type):
        #
        pass
    def buycover(self,lots,price,type):
        #
        pass
    def sellcover(self,lots,price,type):
        #
        pass
