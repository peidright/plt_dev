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
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",OrderRef="", UserID="", OrderPriceType=0,
            Direction=0, CombOffsetFlag="", LimitPrice=0.0, VolumeTotalOriginal=0, TimeCondition=0,
            GTDDate="", VolumeCondition=0, MinVolume=0,ContingentCondition=0,StopPrice=0.0,
            ForceCloseReason=0,IsAutoSuspend=0,BusinessUnit=0,RequestID=0,UserForceClose=0,
            IsSwapOrder=0
            ):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.OrderRef=OrderRef;
        self.UserID=UserID;
        self.OrderPriceType=OrderPriceType;
        self.Direction=Direction;
        self.CombOffsetFlag=CombOffsetFlag;
        self.LimitPrice=LimitPrice;
        self.VolumeTotalOriginal=VolumeTotalOriginal;
        self.TimeCondition=TimeCondition;
        self.GTDDate=GTDDate;
        self.VolumeCondition=VolumeCondition;
        self.MinVolume=MinVolume;
        self.ContingentCondition=ContingentCondition;
        self.StopPrice=StopPrice;
        self.ForceCloseReason=ForceCloseReason;
        self.IsAutoSuspend=IsAutoSuspend;
        self.BusinessUnit=BusinessUnit;
        self.RequestID=RequestID;
        self.UserForceClose=UserForceClose;
        self.IsSwapOrder=IsSwapOrder;

class CThostFtdcParkedOrderField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",OrderRef="", UserID="", OrderPriceType=0,
            Direction=0, CombOffsetFlag="",CombHedgeFlag="", LimitPrice=0.0, VolumeTotalOriginal=0, 
            TimeCondition=0,GTDDate="", VolumeCondition=0, MinVolume=0,ContingentCondition=0,
            StopPrice=0.0,ForceCloseReason=0,IsAutoSuspend=0,BusinessUnit=0,RequestID=0,UserForceClose=0,
            ExchangeID="",ParkedOrderID="",UserType=0,Status=0,ErrorID=0,ErrorMsg="",IsSwapOrder=0
            ):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.OrderRef=OrderRef;
        self.UserID=UserID;
        self.OrderPriceType=OrderPriceType;
        self.Direction=Direction;
        self.CombOffsetFlag=CombOffsetFlag;
        self.CombHedgeFlag=CombHedgeFlag;
        self.LimitPrice=LimitPrice;
        self.VolumeTotalOriginal=VolumeTotalOriginal;
        self.TimeCondition=TimeCondition;
        self.GTDDate=GTDDate;
        self.VolumeCondition=VolumeCondition;
        self.MinVolume=MinVolume;
        self.ContingentCondition=ContingentCondition;
        self.StopPrice=StopPrice;
        self.ForceCloseReason=ForceCloseReason;
        self.IsAutoSuspend=IsAutoSuspend;
        self.BusinessUnit=BusinessUnit;
        self.RequestID=RequestID;
        self.UserForceClose=UserForceClose;
        self.ExchangeID=ExchangeID;
        self.ParkedOrderID=ParkedOrderID;
        self.UserType=UserType;
        self.Status=Status;
        self.ErrorID=ErrorID;
        self.ErrorMsg=ErrorMsg;
        self.IsSwapOrder=IsSwapOrder;

class CThostFtdcParkedOrderActionField:
    def __init__(self,BrokerID="",InvestorID="",OrderActionRef=0,OrderRef="",RequestID=0,FrontID=0,
            SessionID=0,ExchangeID="",OrderSysID="",ActionFlag=0,LimitPrice=0.0,
            VolumeChange=0,UserID="",InstrumentID="",ParkedOrderActionID="",UserType=0,
            Status=0,ErrorID=0,ErrorMsg=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.OrderActionRef=OrderActionRef;
        self.OrderRef=OrderRef;
        self.RequestID=RequestID;
        self.FrontID=FrontID;
        self.SessionID=SessionID;
        self.ExchangeID=ExchangeID;
        self.OrderSysID=OrderSysID;
        self.ActionFlag=ActionFlag;
        self.LimitPrice=LimitPrice;
        self.VolumeChange=VolumeChange;
        self.UserID=UserID;
        self.InstrumentID=InstrumentID;
        self.ParkedOrderActionID=ParkedOrderActionID;
        self.UserType=UserType;
        self.Status=Status;
        self.ErrorID=ErrorID;
        self.ErrorMsg=ErrorMsg;

class CThostFtdcInputOrderActionField:
    def __init__(self,BrokerID="",InvestorID="",OrderActionRef=0,OrderRef="",RequestID=0,
            FrontID=0,SessionID=0,ExchangeID="",OrderSysID="",ActionFlag=0,
            LimitPrice=0,VolumeChange=0,UserID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.OrderActionRef=OrderActionRef;
        self.OrderRef=OrderRef;
        self.RequestID=RequestID;
        self.FrontID=FrontID;
        self.SessionID=SessionID;
        self.ExchangeID=ExchangeID;
        self.OrderSysID=OrderSysID;
        self.ActionFlag=ActionFlag;
        self.LimitPrice=LimitPrice;
        self.VolumeChange=VolumeChange;
        self.UserID=UserID;
        self.InstrumentID=InstrumentID;

class CThostFtdcQueryMaxOrderVolumeField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",Direction=0,
            OffsetFlag=0,HedgeFlag=0,MaxVolume=0):
        self.Direction=Direction;
        self.OffsetFlag=OffsetFlag;
        self.HedgeFlag=HedgeFlag;
        self.MaxVolume=MaxVolume;

class CThostFtdcSettlementInfoConfirmField:
    def __init__(self,BrokerID="",InvestorID="",ConfirmDate="",ConfirmTime=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ConfirmDate=ConfirmDate;
        self.ConfirmTime=ConfirmTime;

class CThostFtdcRemoveParkedOrderField:
    def __init__(self,BrokerID="",InvestorID="",ParkedOrderID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ParkedOrderID=ParkedOrderID;

class CThostFtdcRemoveParkedOrderActionField:
    def __init__(self,BrokerID="",InvestorID="",ParkedOrderActionID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ParkedOrderActionID=ParkedOrderActionID;

class CThostFtdcQryOrderField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",ExchangeID="",
            OrderSysID="",InsertTimeStart="",InsertTimeEnd=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.ExchangeID=ExchangeID;
        self.OrderSysID=OrderSysID;
        self.InsertTimeStart=InsertTimeStart;
        self.InsertTimeEnd=InsertTimeEnd;

class CThostFtdcQryTradeField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",ExchangeID="",
            TradeID="",TradeTimeStart="",TradeTimeEnd=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.ExchangeID=ExchangeID;
        self.TradeID=TradeID;
        self.TradeTimeStart=TradeTimeStart;
        self.TradeTimeEnd=TradeTimeEnd;

class CThostFtdcQryInvestorPositionField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        pass

class CThostFtdcQryTradingAccountField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;

class CThostFtdcQryInvestorField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;

class CThostFtdcQryTradingCodeField:
    def __init__(self,BrokerID="",InvestorID="",ExchangeID="",ClientID="",ClientIDType=0):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ExchangeID=ExchangeID;
        self.ClientID=ClientID;
        self.ClientIDType=ClientIDType;

class CThostFtdcQryInstrumentMarginRateField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",HedgeFlag=0):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.HedgeFlag=HedgeFlag;

class CThostFtdcQryInstrumentCommissionRateField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        pass

class CThostFtdcQryExchangeField:
    def __init__(self,ExchangeID=""):
        self.ExchangeID=ExchangeID;
        pass

class CThostFtdcQryInstrumentField:
    def __init__(self,InstrumentID="",ExchangeID="",ExchangeInstID="",ProductID=""):
        self.InstrumentID=InstrumentID;
        self.ExchangeID=ExchangeID;
        self.ExchangeInstID=ExchaneInstID;
        self.ProductID=ProductID;
        pass

class CThostFtdcQryDepthMarketDataField:
    def __init__(self,InstrumentID=""):
        self.InstrumentID=InstrumentID;
        pass

class CThostFtdcQrySettlementInfoField:
    def __init__(self,BrokerID="",InvestorID="",TradingDay=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.TradingDay=TradingDay;
        pass

class CThostFtdcQryTransferBankField:
    def __init__(self,BankID="",BankBrchID=""):
        self.BankID=BankID;
        self.BankBrchID=BankBrchID;
        pass

class CThostFtdcQryInvestorPositionDetailField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        pass
class CThostFtdcQryNoticeField:
    def __init__(self,BrokerID=""):
        self.BrokerID=BrokerID;

class CThostFtdcQrySettlementInfoConfirmField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        pass


class CThostFtdcQryInvestorPositionCombineDetailField:
    def __init__(self,BrokerID="",InvestorID="",CombInstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.CombInstrumentID=CombInstrumentID;
        pass

class CThostFtdcQryCFMMCTradingAccountKeyField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        pass

class CThostFtdcQryEWarrantOffsetField:
    def __init__(self,BrokerID="",InvestorID="",ExchangeID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ExchangeID=ExchangeID;
        self.InstrumentID=InstrumentID;
        pass

class CThostFtdcQryInvestorProductGroupMarginField:
    def __init__(self,BrokerID="",InvestorID="",ProductGroupID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.ProductGroupID=ProductGroupID;
        pass

class CThostFtdcQryExchangeMarginRateField:
    def __init__(self,BrokerID="",InstrumentID="",HedgeFlag=0):
        self.BrokerID=BrokerID;
        self.InstrumentID=InstrumentID;
        self.HedgeFlag=HedgeFlag;
        pass

class CThostFtdcQryExchangeMarginRateAdjustField:
    def __init__(self,BrokerID="",InstrumentID="",HedgeFlag=0):
        self.BrokerID=BrokerID;
        self.InstrumentID=InstrumentID;
        self.HedgeFlag=HedgeFlag;
        pass

class CThostFtdcQryTransferSerialField:
    def __init__(self,BrokerID="",AccountID="",BankID=""):
        self.BrokerID=BrokerID;
        self.AccountID=AccountID;
        self.BankID=BankID;
        pass

class CThostFtdcQryAccountregisterField:
    def __init__(self,BrokerID="",AccountID="",BankID=""):
        self.BrokerID=BrokerID;
        self.AccountID=AccountID;
        self.BankID=BankID;
        pass

class CThostFtdcQryContractBankField:
    def __init__(self,BrokerID="",BankID="",BankBrchID=""):
        self.BrokerID=BrokerID;
        self.BankID=BankID;
        self.BankBrchID=BankBrchID;
        pass

class CThostFtdcQryParkedOrderField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",ExchangeID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.ExchangeID=ExchangeID;
        pass

class CThostFtdcQryParkedOrderActionField:
    def __init__(self,BrokerID="",InvestorID="",InstrumentID="",ExchangeID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        self.InstrumentID=InstrumentID;
        self.ExchangeID=ExchangeID;
        pass

class CThostFtdcQryTradingNoticeField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;
        pass

class CThostFtdcQryBrokerTradingParamsField:
    def __init__(self,BrokerID="",InvestorID=""):
        self.BrokerID=BrokerID;
        self.InvestorID=InvestorID;

class CThostFtdcQryBrokerTradingAlgosField:
    def __init__(self,BrokerID="",ExchangeID="",InstrumentID=""):
        self.BrokerID=BrokerID;
        self.ExchangeID=ExchangeID;
        self.InstrumentID=InstrumentID;
        pass

class CThostFtdcReqTransferField:
    def __init__(self,TradeCode="",BankID="",BankBranchID="",BrokerID="",BrokerBranchID="",
            TradeDate="",TradeTime="",BankSerial="",TradingDay="",PlateSerial=0,
            LastFragment=0,SessionID=0,CustomerName="",IdCardType=0,IdentifiedCardNo="",
            CustType=0,BankAccount="",BankPassWord="",AccountID="",Password="",InstallID="",
            FutureSerial=0,UserID="",VerifyCertNoFlag=0,CurrencyID="",TradeAmount=0.0,
            FutureFetchAmount=0.0,FeePayFlag=0,CustFee=0.0,BrokerFee=0.0,Message="",
            Digest="",BankAccType=0,DeviceID="",BankSecuAccType=0,BrokerIDByBank="",
            BankSecuAcc="",BankPwdFlag=0,SecuPwdFlag=0,OperNo="",RequestID=0,
            TID=0,TransferStatus=0):
        self.TradeCode=TradeCode;
        self.BankID=BankID;
        self.BankBranchID=BankBranchID;
        self.BrokerID=BrokerID;
        self.BrokerBranchID=BrokerBranchID;
        self.TradeDate=TradeDate;
        self.TradeTime=TradeTime;
        self.BankSerial=BankSerial;
        self.TradingDay=TradingDay;
        self.PlateSerial=PlateSerial;
        self.LastFragment=LastFragment;
        self.SessionID=SessionID;
        self.CustomerName=CustomerName;
        self.IdCardType=IdCardType;
        self.IdentifiedCardNo=IdentifiedCardNo;
        self.CustType=CustType;
        self.BankAccount=BankAccount;
        self.BankPassWord=BankPassWord;
        self.AccountID=AccountID;
        self.Password=Password;
        self.InstallID=InstallID;
        self.FutureSerial=FutureSerial;
        self.UserID=UserID;
        self.VerifyCertNoFlag=VerifyCertNoFlag;
        self.CurrencyID=CurrencyID;
        self.TradeAmount=TradeAmount;
        self.FutureFetchAmount=FutureFetchAmount;
        self.FeePayFlag=FeePayFlag;
        self.CustFee=CustFee;
        self.BrokerFee=BrokerFee;
        self.Message=Message;
        self.Digest=Digest;
        self.BankAccType=BankAccType;
        self.DeviceID=DeviceID;
        self.BankSecuAccType=BankSecuAccType;
        self.BrokerIDByBank=BrokerIDByBank;
        self.BankSecuAcc=BankSecuAcc;
        self.BankPwdFlag=BankPwdFlag;
        self.SecuPwdFlag=SecuPwdFlag;
        self.OperNo=OperNo;
        self.RequestID=RequestID;
        self.TID=TID;
        self.TransferStatus=TransferStatus;
        pass

class CThostFtdcReqQueryAccountField:
    def __init__(self,TradeCode="",BankID="",BankBranchID="",BrokerID="",BrokerBranchID="",
            TradeDate="",TradeTime="",BankSerial="",TradingDay="",PlateSerial=0,
            LastFragment=0,SessionID=0,CustomerName="",IdCardType=0,IdentifiedCardNo="",
            CustType=0,BankAccount="",BankPassWord="",AccountID="",Password="",InstallID="",
            FutureSerial=0,UserID="",VerifyCertNoFlag=0,CurrencyID="",
            Digest="",BankAccType=0,DeviceID="",BankSecuAccType=0,BrokerIDByBank="",
            BankSecuAcc="",BankPwdFlag=0,SecuPwdFlag=0,OperNo="",RequestID=0,
            TID=0):
        self.TradeCode=TradeCode;
        self.BankID=BankID;
        self.BankBranchID=BankBranchID;
        self.BrokerID=BrokerID;
        self.BrokerBranchID=BrokerBranchID;
        self.TradeDate=TradeDate;
        self.TradeTime=TradeTime;
        self.BankSerial=BankSerial;
        self.TradingDay=TradingDay;
        self.PlateSerial=PlateSerial;
        self.LastFragment=LastFragment;
        self.SessionID=SessionID;
        self.CustomerName=CustomerName;
        self.IdCardType=IdCardType;
        self.IdentifiedCardNo=IdentifiedCardNo;
        self.CustType=CustType;
        self.BankAccount=BankAccount;
        self.BankPassWord=BankPassWord;
        self.AccountID=AccountID;
        self.Password=Password;
        self.InstallID=InstallID;
        self.FutureSerial=FutureSerial;
        self.UserID=UserID;
        self.VerifyCertNoFlag=VerifyCertNoFlag;
        self.CurrencyID=CurrencyID;
        #self.TradeAmount=TradeAmount;
        #self.FutureFetchAmount=FutureFetchAmount;
        #self.FeePayFlag=FeePayFlag;
        #self.CustFee=CustFee;
        #self.BrokerFee=BrokerFee;
        #self.Message=Message;
        self.Digest=Digest;
        self.BankAccType=BankAccType;
        self.DeviceID=DeviceID;
        self.BankSecuAccType=BankSecuAccType;
        self.BrokerIDByBank=BrokerIDByBank;
        self.BankSecuAcc=BankSecuAcc;
        self.BankPwdFlag=BankPwdFlag;
        self.SecuPwdFlag=SecuPwdFlag;
        self.OperNo=OperNo;
        self.RequestID=RequestID;
        self.TID=TID;
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
