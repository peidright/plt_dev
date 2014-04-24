#-*- coding=utf-8 -*-

class CZQThostFtdcRspFutureSignInField:
    def __init__(self, BrokerBranchID="", UserID="", TradeTime="", TID=0, InstallID=0, PinKey="", TradeCode="", BankBranchID="", SessionID=0, BankID="", MacKey="", PlateSerial=0, ErrorID=0, BankSerial="", OperNo="", TradingDay="", BrokerID="", DeviceID="", TradeDate="", CurrencyID="", ErrorMsg="", LastFragment='0', RequestID=0, BrokerIDByBank="", Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.TID=TID
        self.InstallID=InstallID
        self.PinKey=PinKey
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.MacKey=MacKey
        self.PlateSerial=PlateSerial
        self.ErrorID=ErrorID
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.ErrorMsg=ErrorMsg
        self.LastFragment=LastFragment
        self.RequestID=RequestID
        self.BrokerIDByBank=BrokerIDByBank


class CThostFtdcReqAuthenticateField:
    def __init__(self, BrokerID="",UserID="",UserProductInfo="",AuthCode=""):
        self.BrokerID=BrokerID;
        self.UserID=UserID;
        self.UserProductInfo=UserProductInfo;
        self.AuthCode=AuthCode;

class CThostFtdcReqUserLoginField:
    def __init__(self,TradingDay="",BrokerID="",UserID="",Password="",UserProductInfo="",InterfaceProductInfo="",
            ProtocolInfo="", MacAddress="",OneTimePassword="",ClientIPAddress=""):
        self.TradingDay=TradingDay;
	    self.BrokerID=BrokerID;
	    self.UserID=UserID;
	    self.Password=Password;
	    self.UserProductInfo=UserProductInfo;
	    self.InterfaceProductInfo=InterfaceProductInfo;
	    self.ProtocolInfo=ProtocolInfo;
	    self.MacAddress=MacAddress;
	    self.OneTimePassword=OneTimePassword;
	    self.ClientIPAddress=ClientIPAddress;

class CThostFtdcUserLogoutField:
    def __init__(self, BrokerID="",UserID=""):
        self.BrokerID=BrokerID;
        self.UserID=UserID;
        pass

class CThostFtdcUserPasswordUpdateField:
    def __init__(self,BrokerID="",UserID="",OldPassword="",NewPassword=""):
        self.BrokerID=BrokerID;
        self.UserID=UserID;
        self.OldPassword=OldPassword;
        self.NewPassword=NewPassword;

class CThostFtdcTradingAccountPasswordUpdateField:
    def __init__(self,BrokerID="",UserID="",OldPassword="",NewPassword=""):
        self.BrokerID=BrokerID;
        self.UserID=UserID;
        self.OldPassword=OldPassword;
        self.NewPassword=NewPassword;

class CThostFtdcInputOrderField:
    def __init__(self,

{
	///¾­¼Í¹«Ë¾´úÂë
	TThostFtdcBrokerIDType	BrokerID;
	///Í¶×ÊÕß´úÂë
	TThostFtdcInvestorIDType	InvestorID;
	///ºÏÔ¼´úÂë
	TThostFtdcInstrumentIDType	InstrumentID;
	///±¨µ¥ÒýÓÃ
	TThostFtdcOrderRefType	OrderRef;
	///ÓÃ»§´úÂë
	TThostFtdcUserIDType	UserID;
	///±¨µ¥¼Û¸ñÌõ¼þ
	TThostFtdcOrderPriceTypeType	OrderPriceType;
	///ÂòÂô·½Ïò
	TThostFtdcDirectionType	Direction;
	///×éºÏ¿ªÆ½±êÖ¾
	TThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///×éºÏÍ¶»úÌ×±£±êÖ¾
	TThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///¼Û¸ñ
	TThostFtdcPriceType	LimitPrice;
	///ÊýÁ¿
	TThostFtdcVolumeType	VolumeTotalOriginal;
	///ÓÐÐ§ÆÚÀàÐÍ
	TThostFtdcTimeConditionType	TimeCondition;
	///GTDÈÕÆÚ
	TThostFtdcDateType	GTDDate;
	///³É½»Á¿ÀàÐÍ
	TThostFtdcVolumeConditionType	VolumeCondition;
	///×îÐ¡³É½»Á¿
	TThostFtdcVolumeType	MinVolume;
	///´¥·¢Ìõ¼þ
	TThostFtdcContingentConditionType	ContingentCondition;
	///Ö¹Ëð¼Û
	TThostFtdcPriceType	StopPrice;
	///Ç¿Æ½Ô­Òò
	TThostFtdcForceCloseReasonType	ForceCloseReason;
	///×Ô¶¯¹ÒÆð±êÖ¾
	TThostFtdcBoolType	IsAutoSuspend;
	///ÒµÎñµ¥Ôª
	TThostFtdcBusinessUnitType	BusinessUnit;
	///ÇëÇó±àºÅ
	TThostFtdcRequestIDType	RequestID;
	///ÓÃ»§Ç¿ÆÀ±êÖ¾
	TThostFtdcBoolType	UserForceClose;
	///»¥»»µ¥±êÖ¾
	TThostFtdcBoolType	IsSwapOrder;
};


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
