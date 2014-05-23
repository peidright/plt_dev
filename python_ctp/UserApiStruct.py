#-*- coding=utf-8 -*-
"""
A wrapper for CTP's Api library
author: Lvsoft@gmail.com
date: 2010-07-20

This file is part of python-ctp library

python-ctp is free software; you can redistribute it and/or modify it
under the terms of the GUL Lesser General Public License as published
by the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

python-ctp is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along the python-ctp; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
"""
"""

A wrapper for CTP's Api library
author: Lvsoft@gmail.com
date: 2010-07-20

This file is part of python-ctp library

python-ctp is free software; you can redistribute it and/or modify it
under the terms of the GUL Lesser General Public License as published
by the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

python-ctp is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along the python-ctp; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
"""

#This file is auto generated! Please don't edit directly.
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
        self.Digest=Digest
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'PinKey', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'MacKey', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('PinKey', u'PIN密钥'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('MacKey', u'MAC密钥'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTradingNoticeField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingAccountField:
    def __init__(self, FrozenTransferFee=0, Mortgage=0, ExchangeDeliveryMargin=0, FrozenMargin=0, WithdrawQuota=0, PositionProfit=0, TransferFee=0, Commission=0, Interest=0, ShortSellingAmount=0, CashIn=0, AccountID="", Available=0, LowLimitRatio=0, PreCredit=0, PreMortgage=0, CreditRatio=0, MarginTradingAvail=0, CreditAmount=0, InterestBase=0, ExchangeMargin=0, ConversionAmount=0, SSStockValue=0, PreMargin=0, SettlementID=0, DeliveryMargin=0, BondRepurchaseAmount=0, TradingDay="", BrokerID="", FrozenCash=0, Withdraw=0, ReverseRepurchaseAmount=0, StampTax=0, Balance=0, FrozenStampTax=0, Reserve=0, PreDeposit=0, ShortSellingAvail=0, Credit=0, PreBalance=0, CurrMargin=0, FrozenCommission=0, CloseProfit=0, StockValue=0, MarginTradingAmount=0, Deposit=0):
        self.FrozenTransferFee=FrozenTransferFee
        self.Mortgage=Mortgage
        self.ExchangeDeliveryMargin=ExchangeDeliveryMargin
        self.FrozenMargin=FrozenMargin
        self.WithdrawQuota=WithdrawQuota
        self.PositionProfit=PositionProfit
        self.TransferFee=TransferFee
        self.Commission=Commission
        self.Interest=Interest
        self.ShortSellingAmount=ShortSellingAmount
        self.CashIn=CashIn
        self.AccountID=AccountID
        self.Available=Available
        self.LowLimitRatio=LowLimitRatio
        self.PreCredit=PreCredit
        self.PreMortgage=PreMortgage
        self.CreditRatio=CreditRatio
        self.MarginTradingAvail=MarginTradingAvail
        self.CreditAmount=CreditAmount
        self.InterestBase=InterestBase
        self.ExchangeMargin=ExchangeMargin
        self.ConversionAmount=ConversionAmount
        self.SSStockValue=SSStockValue
        self.PreMargin=PreMargin
        self.SettlementID=SettlementID
        self.DeliveryMargin=DeliveryMargin
        self.BondRepurchaseAmount=BondRepurchaseAmount
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.FrozenCash=FrozenCash
        self.Withdraw=Withdraw
        self.ReverseRepurchaseAmount=ReverseRepurchaseAmount
        self.StampTax=StampTax
        self.Balance=Balance
        self.FrozenStampTax=FrozenStampTax
        self.Reserve=Reserve
        self.PreDeposit=PreDeposit
        self.ShortSellingAvail=ShortSellingAvail
        self.Credit=Credit
        self.PreBalance=PreBalance
        self.CurrMargin=CurrMargin
        self.FrozenCommission=FrozenCommission
        self.CloseProfit=CloseProfit
        self.StockValue=StockValue
        self.MarginTradingAmount=MarginTradingAmount
        self.Deposit=Deposit
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrozenTransferFee', 'Mortgage', 'ExchangeDeliveryMargin', 'FrozenMargin', 'WithdrawQuota', 'PositionProfit', 'TransferFee', 'Commission', 'Interest', 'ShortSellingAmount', 'CashIn', 'AccountID', 'Available', 'LowLimitRatio', 'PreCredit', 'PreMortgage', 'CreditRatio', 'MarginTradingAvail', 'CreditAmount', 'InterestBase', 'ExchangeMargin', 'ConversionAmount', 'SSStockValue', 'PreMargin', 'SettlementID', 'DeliveryMargin', 'BondRepurchaseAmount', 'TradingDay', 'BrokerID', 'FrozenCash', 'Withdraw', 'ReverseRepurchaseAmount', 'StampTax', 'Balance', 'FrozenStampTax', 'Reserve', 'PreDeposit', 'ShortSellingAvail', 'Credit', 'PreBalance', 'CurrMargin', 'FrozenCommission', 'CloseProfit', 'StockValue', 'MarginTradingAmount', 'Deposit']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrozenTransferFee', u'冻结的过户费'),('Mortgage', u'质押金额'),('ExchangeDeliveryMargin', u'交易所交割保证金'),('FrozenMargin', u'冻结的保证金'),('WithdrawQuota', u'可取资金'),('PositionProfit', u'融资持仓盈亏'),('TransferFee', u'过户费'),('Commission', u'手续费'),('Interest', u'利息收入'),('ShortSellingAmount', u'融券卖出金额'),('CashIn', u'资金差额'),('AccountID', u'投资者帐号'),('Available', u'现金'),('LowLimitRatio', u'最低维持担保比例'),('PreCredit', u'上次信用额度'),('PreMortgage', u'上次质押金额'),('CreditRatio', u'维持担保比例'),('MarginTradingAvail', u'融资买入可用金额'),('CreditAmount', u'授信额度'),('InterestBase', u'利息基数'),('ExchangeMargin', u'交易所保证金'),('ConversionAmount', u'折算金额'),('SSStockValue', u'融券总市值'),('PreMargin', u'上次占用的保证金'),('SettlementID', u'结算编号'),('DeliveryMargin', u'投资者交割保证金'),('BondRepurchaseAmount', u'债券正回购资金'),('TradingDay', u'交易日'),('BrokerID', u'经纪公司代码'),('FrozenCash', u'冻结的资金'),('Withdraw', u'出金金额'),('ReverseRepurchaseAmount', u'债券逆回购占用资金'),('StampTax', u'印花税'),('Balance', u'期货结算准备金'),('FrozenStampTax', u'冻结的印花税'),('Reserve', u'基本准备金'),('PreDeposit', u'上次存款额'),('ShortSellingAvail', u'融券卖出可用金额'),('Credit', u'保证金可用余额'),('PreBalance', u'上次结算准备金'),('CurrMargin', u'当前保证金总额'),('FrozenCommission', u'冻结的手续费'),('CloseProfit', u'融券持仓盈亏'),('StockValue', u'证券总价值'),('MarginTradingAmount', u'融资买入金额'),('Deposit', u'入金金额')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcAuthenticationInfoField:
    def __init__(self, UserID="", AuthInfo="", IsResult=0, BrokerID="", UserProductInfo=""):
        self.UserID=UserID
        self.AuthInfo=AuthInfo
        self.IsResult=IsResult
        self.BrokerID=BrokerID
        self.UserProductInfo=UserProductInfo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'AuthInfo', 'IsResult', 'BrokerID', 'UserProductInfo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('AuthInfo', u'认证信息'),('IsResult', u'是否为认证结果'),('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerTradingParamsField:
    def __init__(self, InvestorID="", MarginPriceType='1', BrokerID="", AvailIncludeCloseProfit='0', Algorithm='1'):
        self.InvestorID=InvestorID
        self.MarginPriceType=MarginPriceType
        self.BrokerID=BrokerID
        self.AvailIncludeCloseProfit=AvailIncludeCloseProfit
        self.Algorithm=Algorithm
        self.vcmap={'MarginPriceType': {"'1'": u'\u6628\u7ed3\u7b97\u4ef7', "'2'": u'\u6700\u65b0\u4ef7', "'3'": u'\u6210\u4ea4\u5747\u4ef7', "'4'": u'\u5f00\u4ed3\u4ef7'}, 'AvailIncludeCloseProfit': {"'2'": u'\u4e0d\u5305\u542b\u5e73\u4ed3\u76c8\u5229', "'0'": u'\u5305\u542b\u5e73\u4ed3\u76c8\u5229'}, 'Algorithm': {"'1'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u8ba1\u7b97', "'2'": u'\u6d6e\u76c8\u4e0d\u8ba1\uff0c\u6d6e\u4e8f\u8ba1', "'3'": u'\u6d6e\u76c8\u8ba1\uff0c\u6d6e\u4e8f\u4e0d\u8ba1', "'4'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u4e0d\u8ba1\u7b97'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'MarginPriceType', 'BrokerID', 'AvailIncludeCloseProfit', 'Algorithm']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('MarginPriceType', u'保证金价格类型'),('BrokerID', u'经纪公司代码'),('AvailIncludeCloseProfit', u'可用是否包含平仓盈利'),('Algorithm', u'盈亏算法')]])
    def getval(self, n):
        if n in ['MarginPriceType', 'AvailIncludeCloseProfit', 'Algorithm']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradeField:
    def __init__(self, TradeType='0', TraderID="", HedgeFlag='1', TradeTime="", Direction='0', ParticipantID="", Price="", ClientID="", Volume=0, OrderSysID="", ClearingPartID="", InstrumentID="", ExchangeID="", SettlementID=0, UserID="", TradingDay="", BrokerID="", OffsetFlag='0', OrderLocalID="", TradeID="", TradeDate="", BusinessUnit="", SequenceNo=0, OrderRef="", BrokerOrderSeq=0, InvestorID="", ExchangeInstID="", PriceSource='0', TradingRole='1'):
        self.TradeType=TradeType
        self.TraderID=TraderID
        self.HedgeFlag=HedgeFlag
        self.TradeTime=TradeTime
        self.Direction=Direction
        self.ParticipantID=ParticipantID
        self.Price=Price
        self.ClientID=ClientID
        self.Volume=Volume
        self.OrderSysID=OrderSysID
        self.ClearingPartID=ClearingPartID
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.SettlementID=SettlementID
        self.UserID=UserID
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.OffsetFlag=OffsetFlag
        self.OrderLocalID=OrderLocalID
        self.TradeID=TradeID
        self.TradeDate=TradeDate
        self.BusinessUnit=BusinessUnit
        self.SequenceNo=SequenceNo
        self.OrderRef=OrderRef
        self.BrokerOrderSeq=BrokerOrderSeq
        self.InvestorID=InvestorID
        self.ExchangeInstID=ExchangeInstID
        self.PriceSource=PriceSource
        self.TradingRole=TradingRole
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'TradeType': {"'5'": u'ETF\u7533\u8d2d', "'4'": u'\u7ec4\u5408\u884d\u751f\u6210\u4ea4', "'1'": u'\u671f\u6743\u6267\u884c', "'0'": u'\u666e\u901a\u6210\u4ea4', "'6'": u'ETF\u8d4e\u56de', "'2'": u'OTC\u6210\u4ea4', "'3'": u'\u671f\u8f6c\u73b0\u884d\u751f\u6210\u4ea4'}, 'OffsetFlag': {"'5'": u'\u5f3a\u51cf', "'4'": u'\u5e73\u6628', "'1'": u'\u5e73\u4ed3', "'0'": u'\u5f00\u4ed3', "'6'": u'\u672c\u5730\u5f3a\u5e73', "'2'": u'\u5f3a\u5e73', "'3'": u'\u5e73\u4eca'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'PriceSource': {"'1'": u'\u4e70\u59d4\u6258\u4ef7', "'2'": u'\u5356\u59d4\u6258\u4ef7', "'0'": u'\u524d\u6210\u4ea4\u4ef7'}, 'TradingRole': {"'1'": u'\u4ee3\u7406', "'2'": u'\u81ea\u8425', "'3'": u'\u505a\u5e02\u5546'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeType', 'TraderID', 'HedgeFlag', 'TradeTime', 'Direction', 'ParticipantID', 'Price', 'ClientID', 'Volume', 'OrderSysID', 'ClearingPartID', 'InstrumentID', 'ExchangeID', 'SettlementID', 'UserID', 'TradingDay', 'BrokerID', 'OffsetFlag', 'OrderLocalID', 'TradeID', 'TradeDate', 'BusinessUnit', 'SequenceNo', 'OrderRef', 'BrokerOrderSeq', 'InvestorID', 'ExchangeInstID', 'PriceSource', 'TradingRole']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradeType', u'成交类型'),('TraderID', u'交易所交易员代码'),('HedgeFlag', u'投机套保标志'),('TradeTime', u'成交时间'),('Direction', u'买卖方向'),('ParticipantID', u'会员代码'),('Price', u'价格'),('ClientID', u'客户代码'),('Volume', u'数量'),('OrderSysID', u'报单编号'),('ClearingPartID', u'结算会员编号'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('SettlementID', u'结算编号'),('UserID', u'用户代码'),('TradingDay', u'交易日'),('BrokerID', u'经纪公司代码'),('OffsetFlag', u'开平标志'),('OrderLocalID', u'本地报单编号'),('TradeID', u'成交编号'),('TradeDate', u'成交时期'),('BusinessUnit', u'业务单元'),('SequenceNo', u'序号'),('OrderRef', u'报单引用'),('BrokerOrderSeq', u'经纪公司报单编号'),('InvestorID', u'投资者代码'),('ExchangeInstID', u'合约在交易所的代码'),('PriceSource', u'成交价来源'),('TradingRole', u'交易角色')]])
    def getval(self, n):
        if n in ['TradeType', 'HedgeFlag', 'Direction', 'OffsetFlag', 'PriceSource', 'TradingRole']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryExchangeField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=ExchangeID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySettlementInfoField:
    def __init__(self, InvestorID="", BrokerID="", TradingDay=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.TradingDay=TradingDay
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqDayEndFileReadyField:
    def __init__(self, FileBusinessCode='0', TradeDate="", TradeCode="", LastFragment='0', BrokerBranchID="", BankSerial="", BankBranchID="", TradingDay="", SessionID=0, BrokerID="", BankID="", TradeTime="", PlateSerial=0, Digest=""):
        self.FileBusinessCode=FileBusinessCode
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.LastFragment=LastFragment
        self.BrokerBranchID=BrokerBranchID
        self.BankSerial=BankSerial
        self.BankBranchID=BankBranchID
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.BankID=BankID
        self.TradeTime=TradeTime
        self.PlateSerial=PlateSerial
        self.Digest=Digest
        self.vcmap={'FileBusinessCode': {"'9'": u'\u5ba2\u6237\u7ed3\u606f\u51c0\u989d\u660e\u7ec6', "'b'": u'\u6cd5\u4eba\u5b58\u7ba1\u94f6\u884c\u8d44\u91d1\u4ea4\u6536\u6c47\u603b', "'7'": u'\u5ba2\u6237\u8d44\u91d1\u4f59\u989d\u5bf9\u8d26\u7ed3\u679c', "'8'": u'\u5176\u5b83\u5bf9\u8d26\u5f02\u5e38\u7ed3\u679c\u6587\u4ef6', "'5'": u'\u5ba2\u6237\u8d44\u91d1\u53f0\u8d26\u4f59\u989d\u660e\u7ec6\u5bf9\u8d26', "'c'": u'\u4e3b\u4f53\u95f4\u8d44\u91d1\u4ea4\u6536\u6c47\u603b', "'4'": u'\u671f\u8d27\u8d26\u6237\u4fe1\u606f\u53d8\u66f4\u660e\u7ec6\u5bf9\u8d26', "'1'": u'\u8f6c\u8d26\u4ea4\u6613\u660e\u7ec6\u5bf9\u8d26', "'0'": u'\u5176\u4ed6', "'6'": u'\u5ba2\u6237\u9500\u6237\u7ed3\u606f\u660e\u7ec6\u5bf9\u8d26', "'2'": u'\u5ba2\u6237\u8d26\u6237\u72b6\u6001\u5bf9\u8d26', "'e'": u'\u5b58\u7ba1\u94f6\u884c\u5907\u4ed8\u91d1\u4f59\u989d', "'3'": u'\u8d26\u6237\u7c7b\u4ea4\u6613\u660e\u7ec6\u5bf9\u8d26', "'d'": u'\u603b\u5206\u5e73\u8861\u76d1\u7ba1\u6570\u636e', "'a'": u'\u5ba2\u6237\u8d44\u91d1\u4ea4\u6536\u660e\u7ec6', "'f'": u'\u534f\u529e\u5b58\u7ba1\u94f6\u884c\u8d44\u91d1\u76d1\u7ba1\u6570\u636e'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FileBusinessCode', 'TradeDate', 'TradeCode', 'LastFragment', 'BrokerBranchID', 'BankSerial', 'BankBranchID', 'TradingDay', 'SessionID', 'BrokerID', 'BankID', 'TradeTime', 'PlateSerial', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FileBusinessCode', u'文件业务功能'),('TradeDate', u'交易日期'),('TradeCode', u'业务功能码'),('LastFragment', u'最后分片标志'),('BrokerBranchID', u'期商分支机构代码'),('BankSerial', u'银行流水号'),('BankBranchID', u'银行分支机构代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BrokerID', u'期商代码'),('BankID', u'银行代码'),('TradeTime', u'交易时间'),('PlateSerial', u'银期平台消息流水号'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['FileBusinessCode', 'LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInvestorField:
    def __init__(self, SZBranchID="", InvestorName="", Mobile="", IdentifiedCardNo="", Telephone="", InvestorID="", IsCreditAccount=0, BrokerID="", SHBranchID="", Address="", InvestorGroupID="", OpenDate="", IsActive=0, IdentifiedCardType='0'):
        self.SZBranchID=SZBranchID
        self.InvestorName=InvestorName
        self.Mobile=Mobile
        self.IdentifiedCardNo=IdentifiedCardNo
        self.Telephone=Telephone
        self.InvestorID=InvestorID
        self.IsCreditAccount=IsCreditAccount
        self.BrokerID=BrokerID
        self.SHBranchID=SHBranchID
        self.Address=Address
        self.InvestorGroupID=InvestorGroupID
        self.OpenDate=OpenDate
        self.IsActive=IsActive
        self.IdentifiedCardType=IdentifiedCardType
        self.vcmap={'IdentifiedCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SZBranchID', 'InvestorName', 'Mobile', 'IdentifiedCardNo', 'Telephone', 'InvestorID', 'IsCreditAccount', 'BrokerID', 'SHBranchID', 'Address', 'InvestorGroupID', 'OpenDate', 'IsActive', 'IdentifiedCardType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SZBranchID', u'深圳营业部编号'),('InvestorName', u'投资者名称'),('Mobile', u'手机'),('IdentifiedCardNo', u'证件号码'),('Telephone', u'联系电话'),('InvestorID', u'投资者代码'),('IsCreditAccount', u'是否信用账户'),('BrokerID', u'经纪公司代码'),('SHBranchID', u'上海营业部编号'),('Address', u'通讯地址'),('InvestorGroupID', u'投资者分组代码'),('OpenDate', u'开户日期'),('IsActive', u'是否活跃'),('IdentifiedCardType', u'证件类型')]])
    def getval(self, n):
        if n in ['IdentifiedCardType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcCFMMCTradingAccountKeyField:
    def __init__(self, KeyID=0, BrokerID="", ParticipantID="", CurrentKey="", AccountID=""):
        self.KeyID=KeyID
        self.BrokerID=BrokerID
        self.ParticipantID=ParticipantID
        self.CurrentKey=CurrentKey
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['KeyID', 'BrokerID', 'ParticipantID', 'CurrentKey', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('KeyID', u'密钥编号'),('BrokerID', u'经纪公司代码'),('ParticipantID', u'经纪公司统一编码'),('CurrentKey', u'动态密钥'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySyncStatusField:
    def __init__(self, TradingDay=""):
        self.TradingDay=TradingDay
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInvestorPositionDetailField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcFundIOCTPAccountField:
    def __init__(self, PlateSerial=0, TradingDay="", ErrorMsg="", CTPSerial=0, ErrorID=0, UserID="", SettlementSerial="", InvestorID="", SessionID=0, BrokerID="", FundDirection='1', TradeTime="", Password="", TradeAmount=0, Digest="", AccountID=""):
        self.PlateSerial=PlateSerial
        self.TradingDay=TradingDay
        self.ErrorMsg=ErrorMsg
        self.CTPSerial=CTPSerial
        self.ErrorID=ErrorID
        self.UserID=UserID
        self.SettlementSerial=SettlementSerial
        self.InvestorID=InvestorID
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.FundDirection=FundDirection
        self.TradeTime=TradeTime
        self.Password=Password
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.AccountID=AccountID
        self.vcmap={'FundDirection': {"'1'": u'\u5165\u91d1', "'2'": u'\u51fa\u91d1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PlateSerial', 'TradingDay', 'ErrorMsg', 'CTPSerial', 'ErrorID', 'UserID', 'SettlementSerial', 'InvestorID', 'SessionID', 'BrokerID', 'FundDirection', 'TradeTime', 'Password', 'TradeAmount', 'Digest', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('PlateSerial', u'转账平台流水号'),('TradingDay', u'交易日'),('ErrorMsg', u'错误信息'),('CTPSerial', u'CTP核心流水号'),('ErrorID', u'错误代码'),('UserID', u'用户代码'),('SettlementSerial', u'第三方流水号'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('BrokerID', u'证券公司代码'),('FundDirection', u'出入金方向'),('TradeTime', u'转账时间'),('Password', u'资金帐户密码'),('TradeAmount', u'交易金额'),('Digest', u'摘要'),('AccountID', u'投资者资金帐号')]])
    def getval(self, n):
        if n in ['FundDirection']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferBankField:
    def __init__(self, BankName="", IsActive=0, BankBrchID="", BankID=""):
        self.BankName=BankName
        self.IsActive=IsActive
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankName', 'IsActive', 'BankBrchID', 'BankID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankName', u'银行名称'),('IsActive', u'是否活跃'),('BankBrchID', u'银行分中心代码'),('BankID', u'银行代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcOrderActionField:
    def __init__(self, ActionTime="", InvestorID="", TraderID="", UserID="", LimitPrice=0, ClientID="", InstallID=0, ParticipantID="", OrderActionRef=0, VolumeChange=0, SessionID=0, ActionFlag='0', InstrumentID="", ExchangeID="", StatusMsg="", BrokerID="", ActionDate="", OrderLocalID="", BranchID="", BusinessUnit="", OrderRef="", ActionLocalID="", RequestID=0, FrontID=0, OrderActionStatus='a'):
        self.ActionTime=ActionTime
        self.InvestorID=InvestorID
        self.TraderID=TraderID
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.ClientID=ClientID
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.OrderActionRef=OrderActionRef
        self.VolumeChange=VolumeChange
        self.SessionID=SessionID
        self.ActionFlag=ActionFlag
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.StatusMsg=StatusMsg
        self.BrokerID=BrokerID
        self.ActionDate=ActionDate
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.OrderRef=OrderRef
        self.ActionLocalID=ActionLocalID
        self.RequestID=RequestID
        self.FrontID=FrontID
        self.OrderActionStatus=OrderActionStatus
        self.vcmap={'OrderActionStatus': {"'a'": u'\u5df2\u7ecf\u63d0\u4ea4', "'b'": u'\u5df2\u7ecf\u63a5\u53d7', "'c'": u'\u5df2\u7ecf\u88ab\u62d2\u7edd'}, 'ActionFlag': {"'0'": u'\u5220\u9664', "'3'": u'\u4fee\u6539'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ActionTime', 'InvestorID', 'TraderID', 'UserID', 'LimitPrice', 'ClientID', 'InstallID', 'ParticipantID', 'OrderActionRef', 'VolumeChange', 'SessionID', 'ActionFlag', 'InstrumentID', 'ExchangeID', 'StatusMsg', 'BrokerID', 'ActionDate', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'OrderRef', 'ActionLocalID', 'RequestID', 'FrontID', 'OrderActionStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ActionTime', u'操作时间'),('InvestorID', u'投资者代码'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('OrderActionRef', u'报单操作引用'),('VolumeChange', u'数量变化'),('SessionID', u'会话编号'),('ActionFlag', u'操作标志'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('StatusMsg', u'状态信息'),('BrokerID', u'经纪公司代码'),('ActionDate', u'操作日期'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('OrderRef', u'报单引用'),('ActionLocalID', u'操作本地编号'),('RequestID', u'请求编号'),('FrontID', u'前置编号'),('OrderActionStatus', u'报单操作状态')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerUserEventField:
    def __init__(self, UserID="", BrokerID="", UserEventType=' '):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.UserEventType=UserEventType
        self.vcmap={'UserEventType': {"'9'": u'\u5176\u4ed6', "'5'": u'\u4fee\u6539\u5bc6\u7801', "'4'": u'\u4ea4\u6613\u5931\u8d25', "'1'": u'\u767b\u5f55', "'2'": u'\u767b\u51fa', "'3'": u'\u4ea4\u6613\u6210\u529f', "' '": u'\u6240\u6709'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID', 'UserEventType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码'),('UserEventType', u'用户事件类型')]])
    def getval(self, n):
        if n in ['UserEventType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMaxStockPositionLimitField:
    def __init__(self, InstrumentID="", ExchangeID="", Ratio=0, InvestorID="", BrokerID="", CapitalStockType='1'):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.Ratio=Ratio
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.CapitalStockType=CapitalStockType
        self.vcmap={'CapitalStockType': {"'1'": u'\u603b\u901a\u80a1\u672c', "'2'": u'\u6d41\u901a\u80a1\u672c'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'Ratio', 'InvestorID', 'BrokerID', 'CapitalStockType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('Ratio', u'最大持仓数量占股本的比例'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('CapitalStockType', u'股本类型')]])
    def getval(self, n):
        if n in ['CapitalStockType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqRepealField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", BankRepealFlag='0', RepealedTimes=0, TradeTime="", VerifyCertNoFlag='0', TID=0, FutureRepealSerial=0, AccountID="", BankAccount="", InstallID=0, SecuPwdFlag='0', CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, BankPwdFlag='0', RequestID=0, CustType='0', IdentifiedCardNo="", FeePayFlag='0', BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", TransferStatus='0', BrokerRepealFlag='0', IdCardType='0', Password="", FutureFetchAmount=0, TradeDate="", CurrencyID="", BrokerFee=0, BankAccType='1', LastFragment='0', FutureSerial=0, BankRepealSerial="", RepealTimeInterval=0, BankSecuAccType='1', BrokerIDByBank="", PlateRepealSerial=0, Message="", CustFee=0, TradeAmount=0, Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.BankRepealFlag=BankRepealFlag
        self.RepealedTimes=RepealedTimes
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.FutureRepealSerial=FutureRepealSerial
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.SecuPwdFlag=SecuPwdFlag
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.BankPwdFlag=BankPwdFlag
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.FeePayFlag=FeePayFlag
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TransferStatus=TransferStatus
        self.BrokerRepealFlag=BrokerRepealFlag
        self.IdCardType=IdCardType
        self.Password=Password
        self.FutureFetchAmount=FutureFetchAmount
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BrokerFee=BrokerFee
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankRepealSerial=BankRepealSerial
        self.RepealTimeInterval=RepealTimeInterval
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.PlateRepealSerial=PlateRepealSerial
        self.Message=Message
        self.CustFee=CustFee
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'BankRepealFlag': {"'1'": u'\u94f6\u884c\u5f85\u81ea\u52a8\u51b2\u6b63', "'2'": u'\u94f6\u884c\u5df2\u81ea\u52a8\u51b2\u6b63', "'0'": u'\u94f6\u884c\u65e0\u9700\u81ea\u52a8\u51b2\u6b63'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BrokerRepealFlag': {"'1'": u'\u671f\u5546\u5f85\u81ea\u52a8\u51b2\u6b63', "'2'": u'\u671f\u5546\u5df2\u81ea\u52a8\u51b2\u6b63', "'0'": u'\u671f\u5546\u65e0\u9700\u81ea\u52a8\u51b2\u6b63'}, 'TransferStatus': {"'1'": u'\u88ab\u51b2\u6b63', "'0'": u'\u6b63\u5e38'}, 'FeePayFlag': {"'1'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u8d39\u7528', "'2'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u53d1\u8d77\u7684\u8d39\u7528\uff0c\u53d7\u76ca\u65b9\u652f\u4ed8\u63a5\u53d7\u7684\u8d39\u7528', "'0'": u'\u7531\u53d7\u76ca\u65b9\u652f\u4ed8\u8d39\u7528'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'BankRepealFlag', 'RepealedTimes', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'FutureRepealSerial', 'AccountID', 'BankAccount', 'InstallID', 'SecuPwdFlag', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'BankPwdFlag', 'RequestID', 'CustType', 'IdentifiedCardNo', 'FeePayFlag', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'TransferStatus', 'BrokerRepealFlag', 'IdCardType', 'Password', 'FutureFetchAmount', 'TradeDate', 'CurrencyID', 'BrokerFee', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankRepealSerial', 'RepealTimeInterval', 'BankSecuAccType', 'BrokerIDByBank', 'PlateRepealSerial', 'Message', 'CustFee', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('BankRepealFlag', u'银行冲正标志'),('RepealedTimes', u'已经冲正次数'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('FutureRepealSerial', u'被冲正期货流水号'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('BankPwdFlag', u'银行密码标志'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('FeePayFlag', u'费用支付标志'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TransferStatus', u'转账交易状态'),('BrokerRepealFlag', u'期商冲正标志'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('FutureFetchAmount', u'期货可取金额'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BrokerFee', u'应收期货公司费用'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankRepealSerial', u'被冲正银行流水号'),('RepealTimeInterval', u'冲正时间间隔'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('PlateRepealSerial', u'被冲正平台流水号'),('Message', u'发送方给接收方的消息'),('CustFee', u'应收客户费用'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['BankRepealFlag', 'VerifyCertNoFlag', 'SecuPwdFlag', 'BankPwdFlag', 'CustType', 'FeePayFlag', 'TransferStatus', 'BrokerRepealFlag', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferSerialField:
    def __init__(self, BankNewAccount="", BrokerBranchID="", UserID="", TradeTime="", OperatorCode="", AccountID="", BankAccount="", TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, FutureAccType='1', ErrorID=0, BankSerial="", IdentifiedCardNo="", TradingDay="", BrokerID="", IdCardType='0', TradeDate="", CurrencyID="", BrokerFee=0, BankAccType='1', FutureSerial=0, InvestorID="", ErrorMsg="", CustFee=0, TradeAmount=0, Digest="", AvailabilityFlag='0'):
        self.BankNewAccount=BankNewAccount
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.OperatorCode=OperatorCode
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.FutureAccType=FutureAccType
        self.ErrorID=ErrorID
        self.BankSerial=BankSerial
        self.IdentifiedCardNo=IdentifiedCardNo
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.IdCardType=IdCardType
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BrokerFee=BrokerFee
        self.BankAccType=BankAccType
        self.FutureSerial=FutureSerial
        self.InvestorID=InvestorID
        self.ErrorMsg=ErrorMsg
        self.CustFee=CustFee
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.AvailabilityFlag=AvailabilityFlag
        self.vcmap={'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'AvailabilityFlag': {"'1'": u'\u6709\u6548', "'2'": u'\u51b2\u6b63', "'0'": u'\u672a\u786e\u8ba4'}, 'FutureAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankNewAccount', 'BrokerBranchID', 'UserID', 'TradeTime', 'OperatorCode', 'AccountID', 'BankAccount', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'FutureAccType', 'ErrorID', 'BankSerial', 'IdentifiedCardNo', 'TradingDay', 'BrokerID', 'IdCardType', 'TradeDate', 'CurrencyID', 'BrokerFee', 'BankAccType', 'FutureSerial', 'InvestorID', 'ErrorMsg', 'CustFee', 'TradeAmount', 'Digest', 'AvailabilityFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankNewAccount', u'新银行帐号'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户代码'),('TradeTime', u'交易时间'),('OperatorCode', u'操作员'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('TradeCode', u'交易代码'),('BankBranchID', u'银行分支机构编码'),('SessionID', u'会话编号'),('BankID', u'银行编码'),('PlateSerial', u'平台流水号'),('FutureAccType', u'期货公司帐号类型'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('IdentifiedCardNo', u'证件号码'),('TradingDay', u'交易日期'),('BrokerID', u'期货公司编码'),('IdCardType', u'证件类型'),('TradeDate', u'交易发起方日期'),('CurrencyID', u'币种代码'),('BrokerFee', u'应收期货公司费用'),('BankAccType', u'银行帐号类型'),('FutureSerial', u'期货公司流水号'),('InvestorID', u'投资者代码'),('ErrorMsg', u'错误信息'),('CustFee', u'应收客户费用'),('TradeAmount', u'交易金额'),('Digest', u'摘要'),('AvailabilityFlag', u'有效标志')]])
    def getval(self, n):
        if n in ['FutureAccType', 'IdCardType', 'BankAccType', 'AvailabilityFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorWithdrawAlgorithmField:
    def __init__(self, InvestorID="", BrokerID="", InvestorRange='1', UsingRatio=0):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.UsingRatio=UsingRatio
        self.vcmap={'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'InvestorRange', 'UsingRatio']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('UsingRatio', u'可提资金比例')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcUserLogoutField:
    def __init__(self, UserID="", BrokerID=""):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerUserEventField:
    def __init__(self, InstrumentID="", EventSequenceNo=0, EventTime="", UserID="", InvestorID="", BrokerID="", UserEventInfo="", EventDate="", UserEventType=' '):
        self.InstrumentID=InstrumentID
        self.EventSequenceNo=EventSequenceNo
        self.EventTime=EventTime
        self.UserID=UserID
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.UserEventInfo=UserEventInfo
        self.EventDate=EventDate
        self.UserEventType=UserEventType
        self.vcmap={'UserEventType': {"'9'": u'\u5176\u4ed6', "'5'": u'\u4fee\u6539\u5bc6\u7801', "'4'": u'\u4ea4\u6613\u5931\u8d25', "'1'": u'\u767b\u5f55', "'2'": u'\u767b\u51fa', "'3'": u'\u4ea4\u6613\u6210\u529f', "' '": u'\u6240\u6709'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'EventSequenceNo', 'EventTime', 'UserID', 'InvestorID', 'BrokerID', 'UserEventInfo', 'EventDate', 'UserEventType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('EventSequenceNo', u'用户事件序号'),('EventTime', u'事件发生时间'),('UserID', u'用户代码'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('UserEventInfo', u'用户事件信息'),('EventDate', u'事件发生日期'),('UserEventType', u'用户事件类型')]])
    def getval(self, n):
        if n in ['UserEventType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcVerifyInvestorPasswordField:
    def __init__(self, InvestorID="", Password="", BrokerID=""):
        self.InvestorID=InvestorID
        self.Password=Password
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'Password', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('Password', u'密码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspQueryTradeResultBySerialField:
    def __init__(self, OriginReturnCode="", OriginDescrInfoForReturnCode="", BrokerBranchID="", BankPassWord="", TradeTime="", AccountID="", BankAccount="", TradeCode="", BankBranchID="", RefrenceIssure="", SessionID=0, BankID="", PlateSerial=0, ErrorID=0, BankSerial="", TradingDay="", BrokerID="", RefrenceIssureType='0', Password="", Reference=0, TradeDate="", CurrencyID="", ErrorMsg="", LastFragment='0', TradeAmount=0, Digest=""):
        self.OriginReturnCode=OriginReturnCode
        self.OriginDescrInfoForReturnCode=OriginDescrInfoForReturnCode
        self.BrokerBranchID=BrokerBranchID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.RefrenceIssure=RefrenceIssure
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.ErrorID=ErrorID
        self.BankSerial=BankSerial
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.RefrenceIssureType=RefrenceIssureType
        self.Password=Password
        self.Reference=Reference
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.ErrorMsg=ErrorMsg
        self.LastFragment=LastFragment
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'RefrenceIssureType': {"'1'": u'\u671f\u5546', "'2'": u'\u5238\u5546', "'0'": u'\u94f6\u884c'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OriginReturnCode', 'OriginDescrInfoForReturnCode', 'BrokerBranchID', 'BankPassWord', 'TradeTime', 'AccountID', 'BankAccount', 'TradeCode', 'BankBranchID', 'RefrenceIssure', 'SessionID', 'BankID', 'PlateSerial', 'ErrorID', 'BankSerial', 'TradingDay', 'BrokerID', 'RefrenceIssureType', 'Password', 'Reference', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'LastFragment', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('OriginReturnCode', u'原始返回代码'),('OriginDescrInfoForReturnCode', u'原始返回码描述'),('BrokerBranchID', u'期商分支机构代码'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('RefrenceIssure', u'本流水号发布者机构编码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('RefrenceIssureType', u'本流水号发布者的机构类型'),('Password', u'期货密码'),('Reference', u'流水号'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['RefrenceIssureType', 'LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryParkedOrderField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcLinkManField:
    def __init__(self, PersonType='1', PersonName="", IdentifiedCardNo="", Telephone="", ZipCode="", Priority=0, InvestorID="", BrokerID="", Address="", IdentifiedCardType='0'):
        self.PersonType=PersonType
        self.PersonName=PersonName
        self.IdentifiedCardNo=IdentifiedCardNo
        self.Telephone=Telephone
        self.ZipCode=ZipCode
        self.Priority=Priority
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.Address=Address
        self.IdentifiedCardType=IdentifiedCardType
        self.vcmap={'PersonType': {"'1'": u'\u6307\u5b9a\u4e0b\u5355\u4eba', "'2'": u'\u5f00\u6237\u6388\u6743\u4eba', "'3'": u'\u8d44\u91d1\u8c03\u62e8\u4eba', "'4'": u'\u7ed3\u7b97\u5355\u786e\u8ba4\u4eba'}, 'IdentifiedCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PersonType', 'PersonName', 'IdentifiedCardNo', 'Telephone', 'ZipCode', 'Priority', 'InvestorID', 'BrokerID', 'Address', 'IdentifiedCardType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('PersonType', u'联系人类型'),('PersonName', u'名称'),('IdentifiedCardNo', u'证件号码'),('Telephone', u'联系电话'),('ZipCode', u'邮政编码'),('Priority', u'优先级'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('Address', u'通讯地址'),('IdentifiedCardType', u'证件类型')]])
    def getval(self, n):
        if n in ['PersonType', 'IdentifiedCardType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryLinkManField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspFutureSignOutField:
    def __init__(self, BrokerBranchID="", UserID="", TradeTime="", TID=0, InstallID=0, TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, ErrorID=0, BankSerial="", OperNo="", TradingDay="", BrokerID="", DeviceID="", TradeDate="", CurrencyID="", ErrorMsg="", LastFragment='0', RequestID=0, BrokerIDByBank="", Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.TID=TID
        self.InstallID=InstallID
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
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
        self.Digest=Digest
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqOpenAccountField:
    def __init__(self, MoneyAccountStatus='0', BrokerBranchID="", BankPassWord="", Telephone="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", Fax="", InstallID=0, CustomerName="", CountryCode="", TradeCode="", BankSecuAcc="", BankBranchID="", SessionID=0, Address="", PlateSerial=0, BankPwdFlag='0', CustType='0', IdentifiedCardNo="", BankID="", BankSerial="", OperNo="", TradingDay="", Gender='0', BrokerID="", CashExchangeCode='1', IdCardType='0', Password="", MobilePhone="", TradeDate="", CurrencyID="", BankAccType='1', LastFragment='0', ZipCode="", BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', EMail="", Digest="", DeviceID=""):
        self.MoneyAccountStatus=MoneyAccountStatus
        self.BrokerBranchID=BrokerBranchID
        self.BankPassWord=BankPassWord
        self.Telephone=Telephone
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.Fax=Fax
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.CountryCode=CountryCode
        self.TradeCode=TradeCode
        self.BankSecuAcc=BankSecuAcc
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.Address=Address
        self.PlateSerial=PlateSerial
        self.BankPwdFlag=BankPwdFlag
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankID=BankID
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.Gender=Gender
        self.BrokerID=BrokerID
        self.CashExchangeCode=CashExchangeCode
        self.IdCardType=IdCardType
        self.Password=Password
        self.MobilePhone=MobilePhone
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.ZipCode=ZipCode
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.EMail=EMail
        self.Digest=Digest
        self.DeviceID=DeviceID
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'Gender': {"'1'": u'\u7537', "'2'": u'\u5973', "'0'": u'\u672a\u77e5\u72b6\u6001'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'MoneyAccountStatus': {"'1'": u'\u9500\u6237', "'0'": u'\u6b63\u5e38'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'CashExchangeCode': {"'1'": u'\u6c47', "'2'": u'\u949e'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MoneyAccountStatus', 'BrokerBranchID', 'BankPassWord', 'Telephone', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'Fax', 'InstallID', 'CustomerName', 'CountryCode', 'TradeCode', 'BankSecuAcc', 'BankBranchID', 'SessionID', 'Address', 'PlateSerial', 'BankPwdFlag', 'CustType', 'IdentifiedCardNo', 'BankID', 'BankSerial', 'OperNo', 'TradingDay', 'Gender', 'BrokerID', 'CashExchangeCode', 'IdCardType', 'Password', 'MobilePhone', 'TradeDate', 'CurrencyID', 'BankAccType', 'LastFragment', 'ZipCode', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'EMail', 'Digest', 'DeviceID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MoneyAccountStatus', u'资金账户状态'),('BrokerBranchID', u'期商分支机构代码'),('BankPassWord', u'银行密码'),('Telephone', u'电话号码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('Fax', u'传真'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('CountryCode', u'国家代码'),('TradeCode', u'业务功能码'),('BankSecuAcc', u'期货单位帐号'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('Address', u'地址'),('PlateSerial', u'银期平台消息流水号'),('BankPwdFlag', u'银行密码标志'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankID', u'银行代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('Gender', u'性别'),('BrokerID', u'期商代码'),('CashExchangeCode', u'汇钞标志'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('MobilePhone', u'手机'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('ZipCode', u'邮编'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('EMail', u'电子邮件'),('Digest', u'摘要'),('DeviceID', u'渠道标志')]])
    def getval(self, n):
        if n in ['MoneyAccountStatus', 'VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'Gender', 'CashExchangeCode', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcLoginInfoField:
    def __init__(self, MacAddress="", MaxOrderRef="", UserProductInfo="", InterfaceProductInfo="", UserID="", LoginDate="", SystemName="", SessionID=0, BrokerID="", OneTimePassword="", FrontID=0, Password="", IPAddress="", LoginTime="", ProtocolInfo=""):
        self.MacAddress=MacAddress
        self.MaxOrderRef=MaxOrderRef
        self.UserProductInfo=UserProductInfo
        self.InterfaceProductInfo=InterfaceProductInfo
        self.UserID=UserID
        self.LoginDate=LoginDate
        self.SystemName=SystemName
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.OneTimePassword=OneTimePassword
        self.FrontID=FrontID
        self.Password=Password
        self.IPAddress=IPAddress
        self.LoginTime=LoginTime
        self.ProtocolInfo=ProtocolInfo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MacAddress', 'MaxOrderRef', 'UserProductInfo', 'InterfaceProductInfo', 'UserID', 'LoginDate', 'SystemName', 'SessionID', 'BrokerID', 'OneTimePassword', 'FrontID', 'Password', 'IPAddress', 'LoginTime', 'ProtocolInfo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MacAddress', u'Mac地址'),('MaxOrderRef', u'最大报单引用'),('UserProductInfo', u'用户端产品信息'),('InterfaceProductInfo', u'接口端产品信息'),('UserID', u'用户代码'),('LoginDate', u'登录日期'),('SystemName', u'系统名称'),('SessionID', u'会话编号'),('BrokerID', u'经纪公司代码'),('OneTimePassword', u'动态密码'),('FrontID', u'前置编号'),('Password', u'密码'),('IPAddress', u'IP地址'),('LoginTime', u'登录时间'),('ProtocolInfo', u'协议信息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcErrOrderField:
    def __init__(self, ContingentCondition='1', CombOffsetFlag="", UserID="", LimitPrice="", UserForceClose=0, Direction='0', VolumeTotalOriginal=0, OrderPriceType='1', TimeCondition='1', IsAutoSuspend=0, StopPrice=0, InstrumentID="", ExchangeID="", MinVolume=0, ForceCloseReason='0', ErrorID=0, BrokerID="", CombHedgeFlag="", GTDDate="", BusinessUnit="", ErrorMsg="", OrderRef="", InvestorID="", VolumeCondition='1', RequestID=0):
        self.ContingentCondition=ContingentCondition
        self.CombOffsetFlag=CombOffsetFlag
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.UserForceClose=UserForceClose
        self.Direction=Direction
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.OrderPriceType=OrderPriceType
        self.TimeCondition=TimeCondition
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.ForceCloseReason=ForceCloseReason
        self.ErrorID=ErrorID
        self.BrokerID=BrokerID
        self.CombHedgeFlag=CombHedgeFlag
        self.GTDDate=GTDDate
        self.BusinessUnit=BusinessUnit
        self.ErrorMsg=ErrorMsg
        self.OrderRef=OrderRef
        self.InvestorID=InvestorID
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.vcmap={'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'CombOffsetFlag', 'UserID', 'LimitPrice', 'UserForceClose', 'Direction', 'VolumeTotalOriginal', 'OrderPriceType', 'TimeCondition', 'IsAutoSuspend', 'StopPrice', 'InstrumentID', 'ExchangeID', 'MinVolume', 'ForceCloseReason', 'ErrorID', 'BrokerID', 'CombHedgeFlag', 'GTDDate', 'BusinessUnit', 'ErrorMsg', 'OrderRef', 'InvestorID', 'VolumeCondition', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('CombOffsetFlag', u'组合开平标志'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('UserForceClose', u'用户强评标志'),('Direction', u'买卖方向'),('VolumeTotalOriginal', u'数量'),('OrderPriceType', u'报单价格条件'),('TimeCondition', u'有效期类型'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('ErrorID', u'错误代码'),('BrokerID', u'经纪公司代码'),('CombHedgeFlag', u'组合投机套保标志'),('GTDDate', u'GTD日期'),('BusinessUnit', u'业务单元'),('ErrorMsg', u'错误信息'),('OrderRef', u'报单引用'),('InvestorID', u'投资者代码'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Direction', 'OrderPriceType', 'TimeCondition', 'ForceCloseReason', 'VolumeCondition']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcCFMMCBrokerKeyField:
    def __init__(self, KeyID=0, ParticipantID="", CreateDate="", KeyKind='R', BrokerID="", CreateTime="", CurrentKey=""):
        self.KeyID=KeyID
        self.ParticipantID=ParticipantID
        self.CreateDate=CreateDate
        self.KeyKind=KeyKind
        self.BrokerID=BrokerID
        self.CreateTime=CreateTime
        self.CurrentKey=CurrentKey
        self.vcmap={'KeyKind': {"'A'": u'CFMMC\u81ea\u52a8\u66f4\u65b0', "'R'": u'\u4e3b\u52a8\u8bf7\u6c42\u66f4\u65b0', "'M'": u'CFMMC\u624b\u52a8\u66f4\u65b0'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['KeyID', 'ParticipantID', 'CreateDate', 'KeyKind', 'BrokerID', 'CreateTime', 'CurrentKey']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('KeyID', u'密钥编号'),('ParticipantID', u'经纪公司统一编码'),('CreateDate', u'密钥生成日期'),('KeyKind', u'动态密钥类型'),('BrokerID', u'经纪公司代码'),('CreateTime', u'密钥生成时间'),('CurrentKey', u'动态密钥')]])
    def getval(self, n):
        if n in ['KeyKind']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingNoticeField:
    def __init__(self, SequenceSeries=0, SequenceNo=0, UserID="", FieldContent="", InvestorID="", BrokerID="", SendTime="", InvestorRange='1'):
        self.SequenceSeries=SequenceSeries
        self.SequenceNo=SequenceNo
        self.UserID=UserID
        self.FieldContent=FieldContent
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.SendTime=SendTime
        self.InvestorRange=InvestorRange
        self.vcmap={'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceSeries', 'SequenceNo', 'UserID', 'FieldContent', 'InvestorID', 'BrokerID', 'SendTime', 'InvestorRange']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SequenceSeries', u'序列系列号'),('SequenceNo', u'序列号'),('UserID', u'用户代码'),('FieldContent', u'消息正文'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('SendTime', u'发送时间'),('InvestorRange', u'投资者范围')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferBankToFutureRspField:
    def __init__(self, FutureAccount="", RetCode="", CurrencyCode="", TradeAmt=0, RetInfo="", CustFee=0):
        self.FutureAccount=FutureAccount
        self.RetCode=RetCode
        self.CurrencyCode=CurrencyCode
        self.TradeAmt=TradeAmt
        self.RetInfo=RetInfo
        self.CustFee=CustFee
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'CurrencyCode', 'TradeAmt', 'RetInfo', 'CustFee']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('CurrencyCode', u'币种'),('TradeAmt', u'转帐金额'),('RetInfo', u'响应信息'),('CustFee', u'应收客户手续费')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInstrumentStatusField:
    def __init__(self, ExchangeID="", ExchangeInstID=""):
        self.ExchangeID=ExchangeID
        self.ExchangeInstID=ExchangeInstID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'ExchangeInstID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('ExchangeInstID', u'合约在交易所的代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInvestorPositionField:
    def __init__(self, InstrumentID="", InvestorID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTradingAccountField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerSyncField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQueryBrokerDepositField:
    def __init__(self, ExchangeID="", BrokerID=""):
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByMoney=0, LongMarginRatioByMoney=0, HedgeFlag='1', BrokerID="", ShortMarginRatioByVolume=0, LongMarginRatioByVolume=0):
        self.InstrumentID=InstrumentID
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.HedgeFlag=HedgeFlag
        self.BrokerID=BrokerID
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByMoney', 'LongMarginRatioByMoney', 'HedgeFlag', 'BrokerID', 'ShortMarginRatioByVolume', 'LongMarginRatioByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByMoney', u'空头保证金率'),('LongMarginRatioByMoney', u'多头保证金率'),('HedgeFlag', u'投机套保标志'),('BrokerID', u'经纪公司代码'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByVolume', u'多头保证金费')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSettlementInfoConfirmField:
    def __init__(self, ConfirmTime="", InvestorID="", BrokerID="", ConfirmDate=""):
        self.ConfirmTime=ConfirmTime
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.ConfirmDate=ConfirmDate
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ConfirmTime', 'InvestorID', 'BrokerID', 'ConfirmDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ConfirmTime', u'确认时间'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('ConfirmDate', u'确认日期')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTraderField:
    def __init__(self, ExchangeID="", ParticipantID="", BranchID="", TraderID="", BrokerID="", InstallCount=0, Password=""):
        self.ExchangeID=ExchangeID
        self.ParticipantID=ParticipantID
        self.BranchID=BranchID
        self.TraderID=TraderID
        self.BrokerID=BrokerID
        self.InstallCount=InstallCount
        self.Password=Password
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'ParticipantID', 'BranchID', 'TraderID', 'BrokerID', 'InstallCount', 'Password']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('ParticipantID', u'会员代码'),('BranchID', u'营业部编号'),('TraderID', u'交易所交易员代码'),('BrokerID', u'经纪公司代码'),('InstallCount', u'安装数量'),('Password', u'密码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBondInterestField:
    def __init__(self, InstrumentID="", TradingDay="", ExchangeID="", Interest=0):
        self.InstrumentID=InstrumentID
        self.TradingDay=TradingDay
        self.ExchangeID=ExchangeID
        self.Interest=Interest
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'TradingDay', 'ExchangeID', 'Interest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('TradingDay', u'交易日'),('ExchangeID', u'交易所代码'),('Interest', u'利息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerUserFunctionField:
    def __init__(self, UserID="", BrokerID=""):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcPositionProfitAlgorithmField:
    def __init__(self, Memo="", BrokerID="", Algorithm='1', AccountID=""):
        self.Memo=Memo
        self.BrokerID=BrokerID
        self.Algorithm=Algorithm
        self.AccountID=AccountID
        self.vcmap={'Algorithm': {"'1'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u8ba1\u7b97', "'2'": u'\u6d6e\u76c8\u4e0d\u8ba1\uff0c\u6d6e\u4e8f\u8ba1', "'3'": u'\u6d6e\u76c8\u8ba1\uff0c\u6d6e\u4e8f\u4e0d\u8ba1', "'4'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u4e0d\u8ba1\u7b97'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Memo', 'BrokerID', 'Algorithm', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Memo', u'备注'),('BrokerID', u'经纪公司代码'),('Algorithm', u'盈亏算法'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in ['Algorithm']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataAsk45Field:
    def __init__(self, AskPrice5=0, AskPrice4=0, AskVolume5=0, AskVolume4=0):
        self.AskPrice5=AskPrice5
        self.AskPrice4=AskPrice4
        self.AskVolume5=AskVolume5
        self.AskVolume4=AskVolume4
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AskPrice5', 'AskPrice4', 'AskVolume5', 'AskVolume4']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('AskPrice5', u'申卖价五'),('AskPrice4', u'申卖价四'),('AskVolume5', u'申卖量五'),('AskVolume4', u'申卖量四')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferFutureToBankReqField:
    def __init__(self, FutureAccount="", FutureAccPwd="", CurrencyCode="", TradeAmt=0, FuturePwdFlag='0', CustFee=0):
        self.FutureAccount=FutureAccount
        self.FutureAccPwd=FutureAccPwd
        self.CurrencyCode=CurrencyCode
        self.TradeAmt=TradeAmt
        self.FuturePwdFlag=FuturePwdFlag
        self.CustFee=CustFee
        self.vcmap={'FuturePwdFlag': {"'1'": u'\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'FutureAccPwd', 'CurrencyCode', 'TradeAmt', 'FuturePwdFlag', 'CustFee']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户'),('FutureAccPwd', u'密码'),('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('TradeAmt', u'转账金额'),('FuturePwdFlag', u'密码标志'),('CustFee', u'客户手续费')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentStatusField:
    def __init__(self, InstrumentID="", ExchangeID="", EnterTime="", SettlementGroupID="", TradingSegmentSN=0, EnterReason='1', InstrumentStatus='0', ExchangeInstID=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.EnterTime=EnterTime
        self.SettlementGroupID=SettlementGroupID
        self.TradingSegmentSN=TradingSegmentSN
        self.EnterReason=EnterReason
        self.InstrumentStatus=InstrumentStatus
        self.ExchangeInstID=ExchangeInstID
        self.vcmap={'InstrumentStatus': {"'5'": u'\u96c6\u5408\u7ade\u4ef7\u64ae\u5408', "'4'": u'\u96c6\u5408\u7ade\u4ef7\u4ef7\u683c\u5e73\u8861', "'1'": u'\u975e\u4ea4\u6613', "'0'": u'\u5f00\u76d8\u524d', "'6'": u'\u6536\u76d8', "'2'": u'\u8fde\u7eed\u4ea4\u6613', "'3'": u'\u96c6\u5408\u7ade\u4ef7\u62a5\u5355'}, 'EnterReason': {"'1'": u'\u81ea\u52a8\u5207\u6362', "'2'": u'\u624b\u52a8\u5207\u6362', "'3'": u'\u7194\u65ad'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'EnterTime', 'SettlementGroupID', 'TradingSegmentSN', 'EnterReason', 'InstrumentStatus', 'ExchangeInstID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('EnterTime', u'进入本状态时间'),('SettlementGroupID', u'结算组代码'),('TradingSegmentSN', u'交易阶段编号'),('EnterReason', u'进入本状态原因'),('InstrumentStatus', u'合约交易状态'),('ExchangeInstID', u'合约在交易所的代码')]])
    def getval(self, n):
        if n in ['EnterReason', 'InstrumentStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySuperUserField:
    def __init__(self, UserID=""):
        self.UserID=UserID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataBid45Field:
    def __init__(self, BidPrice5=0, BidPrice4=0, BidVolume5=0, BidVolume4=0):
        self.BidPrice5=BidPrice5
        self.BidPrice4=BidPrice4
        self.BidVolume5=BidVolume5
        self.BidVolume4=BidVolume4
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BidPrice5', 'BidPrice4', 'BidVolume5', 'BidVolume4']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BidPrice5', u'申买价五'),('BidPrice4', u'申买价四'),('BidVolume5', u'申买量五'),('BidVolume4', u'申买量四')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerUserFunctionField:
    def __init__(self, UserID="", BrokerID="", BrokerFunctionCode='1'):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.BrokerFunctionCode=BrokerFunctionCode
        self.vcmap={'BrokerFunctionCode': {"'x'": u'\u51c0\u6301\u4ed3\u4fdd\u8bc1\u91d1\u6307\u6807', "'z'": u'\u6570\u636e\u5bfc\u51fa', "'d'": u'\u4ea4\u6613\u529f\u80fd\uff1a\u62a5\u5355\uff0c\u64a4\u5355', "'f'": u'\u98ce\u9669\u76d1\u63a7', "'7'": u'\u5168\u90e8\u67e5\u8be2', "'5'": u'\u62a5\u5355\u63d2\u5165', "'c'": u'\u4ea4\u6613\u67e5\u8be2\uff1a\u5982\u67e5\u6210\u4ea4\uff0c\u59d4\u6258', "'t'": u'\u4ea4\u6613\u7f16\u7801\u67e5\u8be2', "'1'": u'\u5f3a\u5236\u7528\u6237\u767b\u51fa', "'o'": u'\u884c\u60c5\u67e5\u8be2', "'p'": u'\u7528\u6237\u4e8b\u4ef6\u67e5\u8be2', "'m'": u'\u6210\u4ea4\u67e5\u8be2', "'v'": u'\u538b\u529b\u6d4b\u8bd5', "'i'": u'\u98ce\u63a7\u901a\u77e5\u53d1\u9001', "'r'": u'\u51fa\u5165\u91d1\u67e5\u8be2', "'3'": u'\u540c\u6b65\u7ecf\u7eaa\u516c\u53f8\u6570\u636e', "'k'": u'\u8d44\u91d1\u67e5\u8be2', "'y'": u'\u98ce\u9669\u9884\u7b97', "'g'": u'\u67e5\u8be2/\u7ba1\u7406\uff1a\u67e5\u8be2\u4f1a\u8bdd\uff0c\u8e22\u4eba\u7b49', "'e'": u'\u94f6\u671f\u8f6c\u8d26', "'a'": u'\u7cfb\u7edf\u529f\u80fd\uff1a\u767b\u5165/\u767b\u51fa/\u4fee\u6539\u5bc6\u7801\u7b49', "'b'": u'\u57fa\u672c\u67e5\u8be2\uff1a\u67e5\u8be2\u57fa\u7840\u6570\u636e\uff0c\u5982\u5408\u7ea6\uff0c\u4ea4\u6613\u6240\u7b49\u5e38\u91cf', "'w'": u'\u6743\u76ca\u53cd\u7b97', "'u'": u'\u5f3a\u5e73', "'4'": u'\u6279\u91cf\u540c\u6b65\u7ecf\u7eaa\u516c\u53f8\u6570\u636e', "'q'": u'\u98ce\u9669\u901a\u77e5\u67e5\u8be2', "'6'": u'\u62a5\u5355\u64cd\u4f5c', "'l'": u'\u62a5\u5355\u67e5\u8be2', "'2'": u'\u53d8\u66f4\u7528\u6237\u53e3\u4ee4', "'h'": u'\u98ce\u63a7\u901a\u77e5\u63a7\u5236', "'E'": u'\u540c\u6b65\u52a8\u6001\u4ee4\u724c', "'n'": u'\u6301\u4ed3\u67e5\u8be2', "'s'": u'\u6295\u8d44\u8005\u4fe1\u606f\u67e5\u8be2', "'A'": u'\u98ce\u63a7\u6307\u6807\u8bbe\u7f6e', "'j'": u'\u5bdf\u770b\u7ecf\u7eaa\u516c\u53f8\u8d44\u91d1\u6743\u9650'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID', 'BrokerFunctionCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码'),('BrokerFunctionCode', u'经纪公司功能代码')]])
    def getval(self, n):
        if n in ['BrokerFunctionCode']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcForceUserLogoutField:
    def __init__(self, UserID="", BrokerID=""):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTraderOfferField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=ExchangeID
        self.TraderID=TraderID
        self.ParticipantID=ParticipantID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryCFMMCBrokerKeyField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInstrumentMarginRateField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID="", HedgeFlag='1'):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.HedgeFlag=HedgeFlag
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID', 'HedgeFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('HedgeFlag', u'投机套保标志')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspSyncKeyField:
    def __init__(self, BrokerBranchID="", UserID="", TradeTime="", TID=0, InstallID=0, TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, ErrorID=0, BankSerial="", OperNo="", TradingDay="", BrokerID="", DeviceID="", TradeDate="", ErrorMsg="", LastFragment='0', RequestID=0, BrokerIDByBank="", Message=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.TID=TID
        self.InstallID=InstallID
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.ErrorID=ErrorID
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TradeDate=TradeDate
        self.ErrorMsg=ErrorMsg
        self.LastFragment=LastFragment
        self.RequestID=RequestID
        self.BrokerIDByBank=BrokerIDByBank
        self.Message=Message
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Message']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Message', u'交易核心给银期报盘的消息')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcVerifyFuturePasswordField:
    def __init__(self, BankAccount="", Password="", TradeDate="", TradeCode="", LastFragment='0', BrokerBranchID="", BankSerial="", BankBranchID="", BankPassWord="", TradingDay="", SessionID=0, InstallID=0, BrokerID="", BankID="", TID=0, TradeTime="", PlateSerial=0, AccountID=""):
        self.BankAccount=BankAccount
        self.Password=Password
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.LastFragment=LastFragment
        self.BrokerBranchID=BrokerBranchID
        self.BankSerial=BankSerial
        self.BankBranchID=BankBranchID
        self.BankPassWord=BankPassWord
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.InstallID=InstallID
        self.BrokerID=BrokerID
        self.BankID=BankID
        self.TID=TID
        self.TradeTime=TradeTime
        self.PlateSerial=PlateSerial
        self.AccountID=AccountID
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankAccount', 'Password', 'TradeDate', 'TradeCode', 'LastFragment', 'BrokerBranchID', 'BankSerial', 'BankBranchID', 'BankPassWord', 'TradingDay', 'SessionID', 'InstallID', 'BrokerID', 'BankID', 'TID', 'TradeTime', 'PlateSerial', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankAccount', u'银行帐号'),('Password', u'期货密码'),('TradeDate', u'交易日期'),('TradeCode', u'业务功能码'),('LastFragment', u'最后分片标志'),('BrokerBranchID', u'期商分支机构代码'),('BankSerial', u'银行流水号'),('BankBranchID', u'银行分支机构代码'),('BankPassWord', u'银行密码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('BankID', u'银行代码'),('TID', u'交易ID'),('TradeTime', u'交易时间'),('PlateSerial', u'银期平台消息流水号'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInstrumentMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByMoney=0, LongMarginRatioByMoney=0, IsRelative=0, HedgeFlag='1', InvestorID="", BrokerID="", InvestorRange='1', ShortMarginRatioByVolume=0, LongMarginRatioByVolume=0):
        self.InstrumentID=InstrumentID
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.IsRelative=IsRelative
        self.HedgeFlag=HedgeFlag
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByMoney', 'LongMarginRatioByMoney', 'IsRelative', 'HedgeFlag', 'InvestorID', 'BrokerID', 'InvestorRange', 'ShortMarginRatioByVolume', 'LongMarginRatioByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByMoney', u'空头保证金率'),('LongMarginRatioByMoney', u'多头保证金率'),('IsRelative', u'是否相对交易所收取'),('HedgeFlag', u'投机套保标志'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByVolume', u'多头保证金费')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcParkedOrderActionField:
    def __init__(self, InstrumentID="", Status='1', ExchangeID="", OrderActionRef=0, UserType='0', ErrorMsg="", UserID="", LimitPrice=0, OrderRef="", InvestorID="", SessionID=0, VolumeChange=0, BrokerID="", RequestID=0, ActionFlag='0', ParkedOrderActionID="", FrontID=0, ErrorID=0):
        self.InstrumentID=InstrumentID
        self.Status=Status
        self.ExchangeID=ExchangeID
        self.OrderActionRef=OrderActionRef
        self.UserType=UserType
        self.ErrorMsg=ErrorMsg
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.OrderRef=OrderRef
        self.InvestorID=InvestorID
        self.SessionID=SessionID
        self.VolumeChange=VolumeChange
        self.BrokerID=BrokerID
        self.RequestID=RequestID
        self.ActionFlag=ActionFlag
        self.ParkedOrderActionID=ParkedOrderActionID
        self.FrontID=FrontID
        self.ErrorID=ErrorID
        self.vcmap={'Status': {"'1'": u'\u672a\u53d1\u9001', "'2'": u'\u5df2\u53d1\u9001', "'3'": u'\u5df2\u5220\u9664'}, 'UserType': {"'1'": u'\u64cd\u4f5c\u5458', "'2'": u'\u7ba1\u7406\u5458', "'0'": u'\u6295\u8d44\u8005'}, 'ActionFlag': {"'0'": u'\u5220\u9664', "'3'": u'\u4fee\u6539'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'Status', 'ExchangeID', 'OrderActionRef', 'UserType', 'ErrorMsg', 'UserID', 'LimitPrice', 'OrderRef', 'InvestorID', 'SessionID', 'VolumeChange', 'BrokerID', 'RequestID', 'ActionFlag', 'ParkedOrderActionID', 'FrontID', 'ErrorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('Status', u'预埋撤单状态'),('ExchangeID', u'交易所代码'),('OrderActionRef', u'报单操作引用'),('UserType', u'用户类型'),('ErrorMsg', u'错误信息'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('OrderRef', u'报单引用'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('VolumeChange', u'数量变化'),('BrokerID', u'经纪公司代码'),('RequestID', u'请求编号'),('ActionFlag', u'操作标志'),('ParkedOrderActionID', u'预埋撤单单编号'),('FrontID', u'前置编号'),('ErrorID', u'错误代码')]])
    def getval(self, n):
        if n in ['Status', 'UserType', 'ActionFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerUserOTPParamField:
    def __init__(self, LastDrift=0, LastSuccess=0, SerialNumber="", UserID="", AuthKey="", BrokerID="", OTPVendorsID="", OTPType='0'):
        self.LastDrift=LastDrift
        self.LastSuccess=LastSuccess
        self.SerialNumber=SerialNumber
        self.UserID=UserID
        self.AuthKey=AuthKey
        self.BrokerID=BrokerID
        self.OTPVendorsID=OTPVendorsID
        self.OTPType=OTPType
        self.vcmap={'OTPType': {"'1'": u'\u65f6\u95f4\u4ee4\u724c', "'0'": u'\u65e0\u52a8\u6001\u4ee4\u724c'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastDrift', 'LastSuccess', 'SerialNumber', 'UserID', 'AuthKey', 'BrokerID', 'OTPVendorsID', 'OTPType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('LastDrift', u'漂移值'),('LastSuccess', u'成功值'),('SerialNumber', u'动态令牌序列号'),('UserID', u'用户代码'),('AuthKey', u'令牌密钥'),('BrokerID', u'经纪公司代码'),('OTPVendorsID', u'动态令牌提供商'),('OTPType', u'动态令牌类型')]])
    def getval(self, n):
        if n in ['OTPType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInstrumentCommissionRateField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMDTraderOfferField:
    def __init__(self, BranchID="", StartDate="", ExchangeID="", InstallID=0, LastReportDate="", ParticipantID="", OrderLocalID="", LastReportTime="", TraderID="", ConnectTime="", TraderConnectStatus='1', TradingDay="", ConnectRequestTime="", StartTime="", ConnectRequestDate="", BrokerID="", Password="", ConnectDate=""):
        self.BranchID=BranchID
        self.StartDate=StartDate
        self.ExchangeID=ExchangeID
        self.InstallID=InstallID
        self.LastReportDate=LastReportDate
        self.ParticipantID=ParticipantID
        self.OrderLocalID=OrderLocalID
        self.LastReportTime=LastReportTime
        self.TraderID=TraderID
        self.ConnectTime=ConnectTime
        self.TraderConnectStatus=TraderConnectStatus
        self.TradingDay=TradingDay
        self.ConnectRequestTime=ConnectRequestTime
        self.StartTime=StartTime
        self.ConnectRequestDate=ConnectRequestDate
        self.BrokerID=BrokerID
        self.Password=Password
        self.ConnectDate=ConnectDate
        self.vcmap={'TraderConnectStatus': {"'1'": u'\u6ca1\u6709\u4efb\u4f55\u8fde\u63a5', "'2'": u'\u5df2\u7ecf\u8fde\u63a5', "'3'": u'\u5df2\u7ecf\u53d1\u51fa\u5408\u7ea6\u67e5\u8be2\u8bf7\u6c42', "'4'": u'\u8ba2\u9605\u79c1\u6709\u6d41'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BranchID', 'StartDate', 'ExchangeID', 'InstallID', 'LastReportDate', 'ParticipantID', 'OrderLocalID', 'LastReportTime', 'TraderID', 'ConnectTime', 'TraderConnectStatus', 'TradingDay', 'ConnectRequestTime', 'StartTime', 'ConnectRequestDate', 'BrokerID', 'Password', 'ConnectDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BranchID', u'营业部编号'),('StartDate', u'启动日期'),('ExchangeID', u'交易所代码'),('InstallID', u'安装编号'),('LastReportDate', u'上次报告日期'),('ParticipantID', u'会员代码'),('OrderLocalID', u'本地报单编号'),('LastReportTime', u'上次报告时间'),('TraderID', u'交易所交易员代码'),('ConnectTime', u'完成连接时间'),('TraderConnectStatus', u'交易所交易员连接状态'),('TradingDay', u'交易日'),('ConnectRequestTime', u'发出连接请求的时间'),('StartTime', u'启动时间'),('ConnectRequestDate', u'发出连接请求的日期'),('BrokerID', u'经纪公司代码'),('Password', u'密码'),('ConnectDate', u'完成连接日期')]])
    def getval(self, n):
        if n in ['TraderConnectStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQueryMaxOrderVolumeWithPriceField:
    def __init__(self, InstrumentID="", Direction='0', OffsetFlag='0', Price=0, HedgeFlag='1', InvestorID="", BrokerID="", MaxVolume=0):
        self.InstrumentID=InstrumentID
        self.Direction=Direction
        self.OffsetFlag=OffsetFlag
        self.Price=Price
        self.HedgeFlag=HedgeFlag
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.MaxVolume=MaxVolume
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'OffsetFlag': {"'5'": u'\u5f3a\u51cf', "'4'": u'\u5e73\u6628', "'1'": u'\u5e73\u4ed3', "'0'": u'\u5f00\u4ed3', "'6'": u'\u672c\u5730\u5f3a\u5e73', "'2'": u'\u5f3a\u5e73', "'3'": u'\u5e73\u4eca'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'Direction', 'OffsetFlag', 'Price', 'HedgeFlag', 'InvestorID', 'BrokerID', 'MaxVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('Direction', u'买卖方向'),('OffsetFlag', u'开平标志'),('Price', u'报单价格'),('HedgeFlag', u'投机套保标志'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('MaxVolume', u'最大允许报单数量')]])
    def getval(self, n):
        if n in ['Direction', 'OffsetFlag', 'HedgeFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcCommPhaseField:
    def __init__(self, TradingDay="", CommPhaseNo=0):
        self.TradingDay=TradingDay
        self.CommPhaseNo=CommPhaseNo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'CommPhaseNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradingDay', u'交易日'),('CommPhaseNo', u'通讯时段编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSuperUserFunctionField:
    def __init__(self, FunctionCode='1', UserID=""):
        self.FunctionCode=FunctionCode
        self.UserID=UserID
        self.vcmap={'FunctionCode': {"'9'": u'\u540c\u6b65\u7ecf\u7eaa\u516c\u53f8\u6570\u636e', "'B'": u'\u8d85\u7ea7\u67e5\u8be2', "'7'": u'\u62a5\u5355\u64cd\u4f5c', "'8'": u'\u540c\u6b65\u7cfb\u7edf\u6570\u636e', "'5'": u'\u53d8\u66f4\u6295\u8d44\u8005\u53e3\u4ee4', "'C'": u'\u62a5\u5355\u63d2\u5165', "'4'": u'\u53d8\u66f4\u7ecf\u7eaa\u516c\u53f8\u53e3\u4ee4', "'1'": u'\u6570\u636e\u5f02\u6b65\u5316', "'6'": u'\u62a5\u5355\u63d2\u5165', "'2'": u'\u5f3a\u5236\u7528\u6237\u767b\u51fa', "'E'": u'\u540c\u6b65\u52a8\u6001\u4ee4\u724c', "'3'": u'\u53d8\u66f4\u7ba1\u7406\u7528\u6237\u53e3\u4ee4', "'D'": u'\u62a5\u5355\u64cd\u4f5c', "'A'": u'\u6279\u91cf\u540c\u6b65\u7ecf\u7eaa\u516c\u53f8\u6570\u636e'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FunctionCode', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FunctionCode', u'功能代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['FunctionCode']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferFutureToBankRspField:
    def __init__(self, FutureAccount="", RetCode="", CurrencyCode="", TradeAmt=0, RetInfo="", CustFee=0):
        self.FutureAccount=FutureAccount
        self.RetCode=RetCode
        self.CurrencyCode=CurrencyCode
        self.TradeAmt=TradeAmt
        self.RetInfo=RetInfo
        self.CustFee=CustFee
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'CurrencyCode', 'TradeAmt', 'RetInfo', 'CustFee']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('CurrencyCode', u'币种'),('TradeAmt', u'转帐金额'),('RetInfo', u'响应信息'),('CustFee', u'应收客户手续费')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataField:
    def __init__(self, HighestPrice=0, LowerLimitPrice=0, OpenPrice=0, PreClosePrice=0, PreSettlementPrice=0, UpdateTime="", UpdateMillisec=0, PreOpenInterest=0, Volume=0, UpperLimitPrice=0, InstrumentID="", ClosePrice=0, ExchangeID="", TradingDay="", PreDelta=0, OpenInterest=0, CurrDelta=0, Turnover=0, LastPrice=0, SettlementPrice=0, ExchangeInstID="", LowestPrice=0):
        self.HighestPrice=HighestPrice
        self.LowerLimitPrice=LowerLimitPrice
        self.OpenPrice=OpenPrice
        self.PreClosePrice=PreClosePrice
        self.PreSettlementPrice=PreSettlementPrice
        self.UpdateTime=UpdateTime
        self.UpdateMillisec=UpdateMillisec
        self.PreOpenInterest=PreOpenInterest
        self.Volume=Volume
        self.UpperLimitPrice=UpperLimitPrice
        self.InstrumentID=InstrumentID
        self.ClosePrice=ClosePrice
        self.ExchangeID=ExchangeID
        self.TradingDay=TradingDay
        self.PreDelta=PreDelta
        self.OpenInterest=OpenInterest
        self.CurrDelta=CurrDelta
        self.Turnover=Turnover
        self.LastPrice=LastPrice
        self.SettlementPrice=SettlementPrice
        self.ExchangeInstID=ExchangeInstID
        self.LowestPrice=LowestPrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['HighestPrice', 'LowerLimitPrice', 'OpenPrice', 'PreClosePrice', 'PreSettlementPrice', 'UpdateTime', 'UpdateMillisec', 'PreOpenInterest', 'Volume', 'UpperLimitPrice', 'InstrumentID', 'ClosePrice', 'ExchangeID', 'TradingDay', 'PreDelta', 'OpenInterest', 'CurrDelta', 'Turnover', 'LastPrice', 'SettlementPrice', 'ExchangeInstID', 'LowestPrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('HighestPrice', u'最高价'),('LowerLimitPrice', u'跌停板价'),('OpenPrice', u'今开盘'),('PreClosePrice', u'昨收盘'),('PreSettlementPrice', u'上次结算价'),('UpdateTime', u'最后修改时间'),('UpdateMillisec', u'最后修改毫秒'),('PreOpenInterest', u'昨持仓量'),('Volume', u'数量'),('UpperLimitPrice', u'涨停板价'),('InstrumentID', u'合约代码'),('ClosePrice', u'今收盘'),('ExchangeID', u'交易所代码'),('TradingDay', u'交易日'),('PreDelta', u'昨虚实度'),('OpenInterest', u'持仓量'),('CurrDelta', u'今虚实度'),('Turnover', u'成交金额'),('LastPrice', u'最新价'),('SettlementPrice', u'本次结算价'),('ExchangeInstID', u'合约在交易所的代码'),('LowestPrice', u'最低价')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingTradingAccountField:
    def __init__(self, FrozenTransferFee=0, Mortgage=0, ExchangeDeliveryMargin=0, FrozenMargin=0, WithdrawQuota=0, PositionProfit=0, TransferFee=0, Commission=0, Interest=0, ShortSellingAmount=0, CashIn=0, AccountID="", Available=0, LowLimitRatio=0, PreCredit=0, PreMortgage=0, CreditRatio=0, MarginTradingAvail=0, CreditAmount=0, InterestBase=0, ExchangeMargin=0, ConversionAmount=0, SSStockValue=0, PreMargin=0, SettlementID=0, DeliveryMargin=0, BondRepurchaseAmount=0, TradingDay="", BrokerID="", FrozenCash=0, Withdraw=0, ReverseRepurchaseAmount=0, StampTax=0, Balance=0, FrozenStampTax=0, Reserve=0, PreDeposit=0, ShortSellingAvail=0, Credit=0, PreBalance=0, CurrMargin=0, FrozenCommission=0, CloseProfit=0, StockValue=0, MarginTradingAmount=0, Deposit=0):
        self.FrozenTransferFee=FrozenTransferFee
        self.Mortgage=Mortgage
        self.ExchangeDeliveryMargin=ExchangeDeliveryMargin
        self.FrozenMargin=FrozenMargin
        self.WithdrawQuota=WithdrawQuota
        self.PositionProfit=PositionProfit
        self.TransferFee=TransferFee
        self.Commission=Commission
        self.Interest=Interest
        self.ShortSellingAmount=ShortSellingAmount
        self.CashIn=CashIn
        self.AccountID=AccountID
        self.Available=Available
        self.LowLimitRatio=LowLimitRatio
        self.PreCredit=PreCredit
        self.PreMortgage=PreMortgage
        self.CreditRatio=CreditRatio
        self.MarginTradingAvail=MarginTradingAvail
        self.CreditAmount=CreditAmount
        self.InterestBase=InterestBase
        self.ExchangeMargin=ExchangeMargin
        self.ConversionAmount=ConversionAmount
        self.SSStockValue=SSStockValue
        self.PreMargin=PreMargin
        self.SettlementID=SettlementID
        self.DeliveryMargin=DeliveryMargin
        self.BondRepurchaseAmount=BondRepurchaseAmount
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.FrozenCash=FrozenCash
        self.Withdraw=Withdraw
        self.ReverseRepurchaseAmount=ReverseRepurchaseAmount
        self.StampTax=StampTax
        self.Balance=Balance
        self.FrozenStampTax=FrozenStampTax
        self.Reserve=Reserve
        self.PreDeposit=PreDeposit
        self.ShortSellingAvail=ShortSellingAvail
        self.Credit=Credit
        self.PreBalance=PreBalance
        self.CurrMargin=CurrMargin
        self.FrozenCommission=FrozenCommission
        self.CloseProfit=CloseProfit
        self.StockValue=StockValue
        self.MarginTradingAmount=MarginTradingAmount
        self.Deposit=Deposit
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrozenTransferFee', 'Mortgage', 'ExchangeDeliveryMargin', 'FrozenMargin', 'WithdrawQuota', 'PositionProfit', 'TransferFee', 'Commission', 'Interest', 'ShortSellingAmount', 'CashIn', 'AccountID', 'Available', 'LowLimitRatio', 'PreCredit', 'PreMortgage', 'CreditRatio', 'MarginTradingAvail', 'CreditAmount', 'InterestBase', 'ExchangeMargin', 'ConversionAmount', 'SSStockValue', 'PreMargin', 'SettlementID', 'DeliveryMargin', 'BondRepurchaseAmount', 'TradingDay', 'BrokerID', 'FrozenCash', 'Withdraw', 'ReverseRepurchaseAmount', 'StampTax', 'Balance', 'FrozenStampTax', 'Reserve', 'PreDeposit', 'ShortSellingAvail', 'Credit', 'PreBalance', 'CurrMargin', 'FrozenCommission', 'CloseProfit', 'StockValue', 'MarginTradingAmount', 'Deposit']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrozenTransferFee', u'冻结的过户费'),('Mortgage', u'质押金额'),('ExchangeDeliveryMargin', u'交易所交割保证金'),('FrozenMargin', u'冻结的保证金'),('WithdrawQuota', u'可取资金'),('PositionProfit', u'融资持仓盈亏'),('TransferFee', u'过户费'),('Commission', u'手续费'),('Interest', u'利息收入'),('ShortSellingAmount', u'融券卖出金额'),('CashIn', u'资金差额'),('AccountID', u'投资者帐号'),('Available', u'现金'),('LowLimitRatio', u'最低维持担保比例'),('PreCredit', u'上次信用额度'),('PreMortgage', u'上次质押金额'),('CreditRatio', u'维持担保比例'),('MarginTradingAvail', u'融资买入可用金额'),('CreditAmount', u'授信额度'),('InterestBase', u'利息基数'),('ExchangeMargin', u'交易所保证金'),('ConversionAmount', u'折算金额'),('SSStockValue', u'融券总市值'),('PreMargin', u'上次占用的保证金'),('SettlementID', u'结算编号'),('DeliveryMargin', u'投资者交割保证金'),('BondRepurchaseAmount', u'债券正回购资金'),('TradingDay', u'交易日'),('BrokerID', u'经纪公司代码'),('FrozenCash', u'冻结的资金'),('Withdraw', u'出金金额'),('ReverseRepurchaseAmount', u'债券逆回购占用资金'),('StampTax', u'印花税'),('Balance', u'期货结算准备金'),('FrozenStampTax', u'冻结的印花税'),('Reserve', u'基本准备金'),('PreDeposit', u'上次存款额'),('ShortSellingAvail', u'融券卖出可用金额'),('Credit', u'保证金可用余额'),('PreBalance', u'上次结算准备金'),('CurrMargin', u'当前保证金总额'),('FrozenCommission', u'冻结的手续费'),('CloseProfit', u'融券持仓盈亏'),('StockValue', u'证券总价值'),('MarginTradingAmount', u'融资买入金额'),('Deposit', u'入金金额')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcFrontStatusField:
    def __init__(self, FrontID=0, LastReportDate="", IsActive=0, LastReportTime=""):
        self.FrontID=FrontID
        self.LastReportDate=LastReportDate
        self.IsActive=IsActive
        self.LastReportTime=LastReportTime
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID', 'LastReportDate', 'IsActive', 'LastReportTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrontID', u'前置编号'),('LastReportDate', u'上次报告日期'),('IsActive', u'是否活跃'),('LastReportTime', u'上次报告时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcCombinationLegField:
    def __init__(self, Direction='0', ImplyLevel=0, LegMultiple=0, LegID=0, LegInstrumentID="", CombInstrumentID=""):
        self.Direction=Direction
        self.ImplyLevel=ImplyLevel
        self.LegMultiple=LegMultiple
        self.LegID=LegID
        self.LegInstrumentID=LegInstrumentID
        self.CombInstrumentID=CombInstrumentID
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Direction', 'ImplyLevel', 'LegMultiple', 'LegID', 'LegInstrumentID', 'CombInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Direction', u'买卖方向'),('ImplyLevel', u'派生层数'),('LegMultiple', u'单腿乘数'),('LegID', u'单腿编号'),('LegInstrumentID', u'单腿合约代码'),('CombInstrumentID', u'组合合约代码')]])
    def getval(self, n):
        if n in ['Direction']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryErrOrderActionField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryExchangeOrderActionField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID="", ClientID=""):
        self.ExchangeID=ExchangeID
        self.TraderID=TraderID
        self.ParticipantID=ParticipantID
        self.ClientID=ClientID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID', 'ClientID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码'),('ClientID', u'客户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingTradingCodeField:
    def __init__(self, InvestorID="", ExchangeID="", BrokerID="", IsActive=0, ClientID=""):
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.IsActive=IsActive
        self.ClientID=ClientID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ExchangeID', 'BrokerID', 'IsActive', 'ClientID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('IsActive', u'是否活跃'),('ClientID', u'客户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentTradingRightField:
    def __init__(self, InstrumentID="", Direction='0', InstrumentRange='1', TradingRight='0', ExchangeID="", InvestorID="", BrokerID="", InvestorRange='1'):
        self.InstrumentID=InstrumentID
        self.Direction=Direction
        self.InstrumentRange=InstrumentRange
        self.TradingRight=TradingRight
        self.ExchangeID=ExchangeID
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'InstrumentRange': {"'1'": u'\u6240\u6709', "'2'": u'\u4ea7\u54c1', "'3'": u'\u80a1\u7968\u6743\u9650\u6a21\u7248', "'4'": u'\u80a1\u7968'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}, 'TradingRight': {"'2'": u'\u4e0d\u80fd\u4ea4\u6613', "'0'": u'\u53ef\u4ee5\u4ea4\u6613'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'Direction', 'InstrumentRange', 'TradingRight', 'ExchangeID', 'InvestorID', 'BrokerID', 'InvestorRange']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('Direction', u'买卖'),('InstrumentRange', u'股票权限分类'),('TradingRight', u'交易权限'),('ExchangeID', u'交易所代码'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围')]])
    def getval(self, n):
        if n in ['Direction', 'InstrumentRange', 'TradingRight', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorPositionDetailField:
    def __init__(self, ExchMargin=0, TradeType='0', HedgeFlag='1', PledgeInFrozenPosition=0, TransferFee=0, Commission=0, Direction='0', CloseAmount=0, RepurchasePosition=0, OpenPrice=0, Volume=0, LastSettlementPrice=0, CloseVolume=0, InstrumentID="", ExchangeID="", SettlementID=0, TradingDay="", Amount=0, BrokerID="", StampTax=0, Margin=0, TradeID="", PledgeInPosition=0, SettlementPrice=0, InvestorID="", OpenDate=""):
        self.ExchMargin=ExchMargin
        self.TradeType=TradeType
        self.HedgeFlag=HedgeFlag
        self.PledgeInFrozenPosition=PledgeInFrozenPosition
        self.TransferFee=TransferFee
        self.Commission=Commission
        self.Direction=Direction
        self.CloseAmount=CloseAmount
        self.RepurchasePosition=RepurchasePosition
        self.OpenPrice=OpenPrice
        self.Volume=Volume
        self.LastSettlementPrice=LastSettlementPrice
        self.CloseVolume=CloseVolume
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.SettlementID=SettlementID
        self.TradingDay=TradingDay
        self.Amount=Amount
        self.BrokerID=BrokerID
        self.StampTax=StampTax
        self.Margin=Margin
        self.TradeID=TradeID
        self.PledgeInPosition=PledgeInPosition
        self.SettlementPrice=SettlementPrice
        self.InvestorID=InvestorID
        self.OpenDate=OpenDate
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'TradeType': {"'5'": u'ETF\u7533\u8d2d', "'4'": u'\u7ec4\u5408\u884d\u751f\u6210\u4ea4', "'1'": u'\u671f\u6743\u6267\u884c', "'0'": u'\u666e\u901a\u6210\u4ea4', "'6'": u'ETF\u8d4e\u56de', "'2'": u'OTC\u6210\u4ea4', "'3'": u'\u671f\u8f6c\u73b0\u884d\u751f\u6210\u4ea4'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchMargin', 'TradeType', 'HedgeFlag', 'PledgeInFrozenPosition', 'TransferFee', 'Commission', 'Direction', 'CloseAmount', 'RepurchasePosition', 'OpenPrice', 'Volume', 'LastSettlementPrice', 'CloseVolume', 'InstrumentID', 'ExchangeID', 'SettlementID', 'TradingDay', 'Amount', 'BrokerID', 'StampTax', 'Margin', 'TradeID', 'PledgeInPosition', 'SettlementPrice', 'InvestorID', 'OpenDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchMargin', u'交易所保证金'),('TradeType', u'成交类型'),('HedgeFlag', u'投机套保标志'),('PledgeInFrozenPosition', u'今日质押入库冻结数量'),('TransferFee', u'过户费'),('Commission', u'手续费'),('Direction', u'买卖'),('CloseAmount', u'平仓金额'),('RepurchasePosition', u'正回购使用的标准券数量'),('OpenPrice', u'开仓价'),('Volume', u'数量'),('LastSettlementPrice', u'昨结算价'),('CloseVolume', u'平仓量'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('SettlementID', u'结算编号'),('TradingDay', u'交易日'),('Amount', u'融资融券金额'),('BrokerID', u'经纪公司代码'),('StampTax', u'印花税'),('Margin', u'投资者保证金'),('TradeID', u'成交编号'),('PledgeInPosition', u'质押入库数量'),('SettlementPrice', u'结算价'),('InvestorID', u'投资者代码'),('OpenDate', u'开仓日期')]])
    def getval(self, n):
        if n in ['TradeType', 'HedgeFlag', 'Direction']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryFundIOCTPAccountField:
    def __init__(self, BrokerID="", AccountID=""):
        self.BrokerID=BrokerID
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('AccountID', u'投资者资金帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcContractBankField:
    def __init__(self, BankName="", BrokerID="", BankBrchID="", BankID=""):
        self.BankName=BankName
        self.BrokerID=BrokerID
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankName', 'BrokerID', 'BankBrchID', 'BankID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankName', u'银行名称'),('BrokerID', u'经纪公司代码'),('BankBrchID', u'银行分中心代码'),('BankID', u'银行代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTransferSerialField:
    def __init__(self, BankID="", BrokerID="", AccountID=""):
        self.BankID=BankID
        self.BrokerID=BrokerID
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankID', u'银行编码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcManualSyncBrokerUserOTPField:
    def __init__(self, UserID="", BrokerID="", FirstOTP="", SecondOTP="", OTPType='0'):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.FirstOTP=FirstOTP
        self.SecondOTP=SecondOTP
        self.OTPType=OTPType
        self.vcmap={'OTPType': {"'1'": u'\u65f6\u95f4\u4ee4\u724c', "'0'": u'\u65e0\u52a8\u6001\u4ee4\u724c'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID', 'FirstOTP', 'SecondOTP', 'OTPType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码'),('FirstOTP', u'第一个动态密码'),('SecondOTP', u'第二个动态密码'),('OTPType', u'动态令牌类型')]])
    def getval(self, n):
        if n in ['OTPType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorAccountField:
    def __init__(self, InvestorID="", BrokerID="", AccountID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryOrderActionField:
    def __init__(self, InvestorID="", ExchangeID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcUserSessionField:
    def __init__(self, MacAddress="", UserProductInfo="", InterfaceProductInfo="", UserID="", LoginDate="", SessionID=0, BrokerID="", FrontID=0, IPAddress="", LoginTime="", ProtocolInfo=""):
        self.MacAddress=MacAddress
        self.UserProductInfo=UserProductInfo
        self.InterfaceProductInfo=InterfaceProductInfo
        self.UserID=UserID
        self.LoginDate=LoginDate
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.FrontID=FrontID
        self.IPAddress=IPAddress
        self.LoginTime=LoginTime
        self.ProtocolInfo=ProtocolInfo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MacAddress', 'UserProductInfo', 'InterfaceProductInfo', 'UserID', 'LoginDate', 'SessionID', 'BrokerID', 'FrontID', 'IPAddress', 'LoginTime', 'ProtocolInfo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MacAddress', u'Mac地址'),('UserProductInfo', u'用户端产品信息'),('InterfaceProductInfo', u'接口端产品信息'),('UserID', u'用户代码'),('LoginDate', u'登录日期'),('SessionID', u'会话编号'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('IPAddress', u'IP地址'),('LoginTime', u'登录时间'),('ProtocolInfo', u'协议信息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerTradingAlgosField:
    def __init__(self, InstrumentID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySuperUserFunctionField:
    def __init__(self, UserID=""):
        self.UserID=UserID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataStaticField:
    def __init__(self, ClosePrice=0, HighestPrice=0, SettlementPrice=0, OpenPrice=0, LowerLimitPrice=0, UpperLimitPrice=0, LowestPrice=0, CurrDelta=0):
        self.ClosePrice=ClosePrice
        self.HighestPrice=HighestPrice
        self.SettlementPrice=SettlementPrice
        self.OpenPrice=OpenPrice
        self.LowerLimitPrice=LowerLimitPrice
        self.UpperLimitPrice=UpperLimitPrice
        self.LowestPrice=LowestPrice
        self.CurrDelta=CurrDelta
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ClosePrice', 'HighestPrice', 'SettlementPrice', 'OpenPrice', 'LowerLimitPrice', 'UpperLimitPrice', 'LowestPrice', 'CurrDelta']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ClosePrice', u'今收盘'),('HighestPrice', u'最高价'),('SettlementPrice', u'本次结算价'),('OpenPrice', u'今开盘'),('LowerLimitPrice', u'跌停板价'),('UpperLimitPrice', u'涨停板价'),('LowestPrice', u'最低价'),('CurrDelta', u'今虚实度')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcDiscountField:
    def __init__(self, InvestorID="", BrokerID="", InvestorRange='1', Discount=0):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.Discount=Discount
        self.vcmap={'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'InvestorRange', 'Discount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('Discount', u'资金折扣比例')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcUserIPField:
    def __init__(self, MacAddress="", UserID="", IPMask="", BrokerID="", IPAddress=""):
        self.MacAddress=MacAddress
        self.UserID=UserID
        self.IPMask=IPMask
        self.BrokerID=BrokerID
        self.IPAddress=IPAddress
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MacAddress', 'UserID', 'IPMask', 'BrokerID', 'IPAddress']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MacAddress', u'Mac地址'),('UserID', u'用户代码'),('IPMask', u'IP地址掩码'),('BrokerID', u'经纪公司代码'),('IPAddress', u'IP地址')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerUserField:
    def __init__(self, UserID="", BrokerID=""):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqQueryAccountField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", InstallID=0, CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", Password="", BankPwdFlag='0', RequestID=0, CustType='0', IdentifiedCardNo="", BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", IdCardType='0', PlateSerial=0, TradeDate="", CurrencyID="", BankAccType='1', LastFragment='0', FutureSerial=0, BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.Password=Password
        self.BankPwdFlag=BankPwdFlag
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.IdCardType=IdCardType
        self.PlateSerial=PlateSerial
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'InstallID', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'Password', 'BankPwdFlag', 'RequestID', 'CustType', 'IdentifiedCardNo', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'IdCardType', 'PlateSerial', 'TradeDate', 'CurrencyID', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('Password', u'期货密码'),('BankPwdFlag', u'银行密码标志'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('IdCardType', u'证件类型'),('PlateSerial', u'银期平台消息流水号'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryHisOrderField:
    def __init__(self, InstrumentID="", ExchangeID="", SettlementID=0, InsertTimeStart="", InvestorID="", BrokerID="", OrderSysID="", TradingDay="", InsertTimeEnd=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.SettlementID=SettlementID
        self.InsertTimeStart=InsertTimeStart
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.OrderSysID=OrderSysID
        self.TradingDay=TradingDay
        self.InsertTimeEnd=InsertTimeEnd
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'SettlementID', 'InsertTimeStart', 'InvestorID', 'BrokerID', 'OrderSysID', 'TradingDay', 'InsertTimeEnd']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('SettlementID', u'结算编号'),('InsertTimeStart', u'开始时间'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('OrderSysID', u'报单编号'),('TradingDay', u'交易日'),('InsertTimeEnd', u'结束时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentCommissionRateField:
    def __init__(self, InstrumentID="", ExchangeID="", TradeFeeByMoney=0, Direction='0', MinTradeFee=0, StampTaxRateByMoney=0, InvestorID="", MarginByMoney=0, StampTaxRateByVolume=0, BrokerID="", InvestorRange='1', TransferFeeRateByVolume=0, TransferFeeRateByMoney=0, TradeFeeByVolume=0):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.TradeFeeByMoney=TradeFeeByMoney
        self.Direction=Direction
        self.MinTradeFee=MinTradeFee
        self.StampTaxRateByMoney=StampTaxRateByMoney
        self.InvestorID=InvestorID
        self.MarginByMoney=MarginByMoney
        self.StampTaxRateByVolume=StampTaxRateByVolume
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.TransferFeeRateByVolume=TransferFeeRateByVolume
        self.TransferFeeRateByMoney=TransferFeeRateByMoney
        self.TradeFeeByVolume=TradeFeeByVolume
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'TradeFeeByMoney', 'Direction', 'MinTradeFee', 'StampTaxRateByMoney', 'InvestorID', 'MarginByMoney', 'StampTaxRateByVolume', 'BrokerID', 'InvestorRange', 'TransferFeeRateByVolume', 'TransferFeeRateByMoney', 'TradeFeeByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('TradeFeeByMoney', u'交易费'),('Direction', u'买卖方向'),('MinTradeFee', u'最小过户费'),('StampTaxRateByMoney', u'印花税率'),('InvestorID', u'投资者代码'),('MarginByMoney', u'交易附加费率'),('StampTaxRateByVolume', u'印花税率(按手数)'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('TransferFeeRateByVolume', u'过户费率(按手数)'),('TransferFeeRateByMoney', u'过户费率'),('TradeFeeByVolume', u'交易费(按手数)')]])
    def getval(self, n):
        if n in ['Direction', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerUserField:
    def __init__(self, UserName="", UserID="", UserType='0', BrokerID="", IsUsingOTP=0, IsActive=0):
        self.UserName=UserName
        self.UserID=UserID
        self.UserType=UserType
        self.BrokerID=BrokerID
        self.IsUsingOTP=IsUsingOTP
        self.IsActive=IsActive
        self.vcmap={'UserType': {"'1'": u'\u64cd\u4f5c\u5458', "'2'": u'\u7ba1\u7406\u5458', "'0'": u'\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserName', 'UserID', 'UserType', 'BrokerID', 'IsUsingOTP', 'IsActive']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserName', u'用户名称'),('UserID', u'用户代码'),('UserType', u'用户类型'),('BrokerID', u'经纪公司代码'),('IsUsingOTP', u'是否使用令牌'),('IsActive', u'是否活跃')]])
    def getval(self, n):
        if n in ['UserType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncDepositField:
    def __init__(self, InvestorID="", DepositSeqNo="", BrokerID="", Deposit=0, IsForce=0):
        self.InvestorID=InvestorID
        self.DepositSeqNo=DepositSeqNo
        self.BrokerID=BrokerID
        self.Deposit=Deposit
        self.IsForce=IsForce
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'DepositSeqNo', 'BrokerID', 'Deposit', 'IsForce']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('DepositSeqNo', u'出入金流水号'),('BrokerID', u'经纪公司代码'),('Deposit', u'入金金额'),('IsForce', u'是否强制进行')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInstrumentTradingRightField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryCFMMCTradingAccountKeyField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqFundIOCTPAccountField:
    def __init__(self, PlateSerial=0, TradingDay="", CTPSerial=0, UserID="", SettlementSerial="", InvestorID="", SessionID=0, BrokerID="", TradeTime="", Password="", TradeAmount=0, Digest="", AccountID=""):
        self.PlateSerial=PlateSerial
        self.TradingDay=TradingDay
        self.CTPSerial=CTPSerial
        self.UserID=UserID
        self.SettlementSerial=SettlementSerial
        self.InvestorID=InvestorID
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.TradeTime=TradeTime
        self.Password=Password
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PlateSerial', 'TradingDay', 'CTPSerial', 'UserID', 'SettlementSerial', 'InvestorID', 'SessionID', 'BrokerID', 'TradeTime', 'Password', 'TradeAmount', 'Digest', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('PlateSerial', u'转账平台流水号'),('TradingDay', u'交易日'),('CTPSerial', u'CTP核心流水号'),('UserID', u'用户代码'),('SettlementSerial', u'第三方流水号'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('BrokerID', u'证券公司代码'),('TradeTime', u'转账时间'),('Password', u'资金帐户密码'),('TradeAmount', u'交易金额'),('Digest', u'摘要'),('AccountID', u'投资者资金帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcNoticeField:
    def __init__(self, Content="", SequenceLabel="", BrokerID=""):
        self.Content=Content
        self.SequenceLabel=SequenceLabel
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Content', 'SequenceLabel', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Content', u'消息正文'),('SequenceLabel', u'经纪公司通知内容序列号'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqTransferField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", InstallID=0, CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", Password="", BankPwdFlag='0', RequestID=0, CustType='0', IdentifiedCardNo="", FeePayFlag='0', BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", TransferStatus='0', IdCardType='0', PlateSerial=0, FutureFetchAmount=0, TradeDate="", CurrencyID="", BrokerFee=0, BankAccType='1', LastFragment='0', FutureSerial=0, BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', Message="", CustFee=0, TradeAmount=0, Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.Password=Password
        self.BankPwdFlag=BankPwdFlag
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.FeePayFlag=FeePayFlag
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TransferStatus=TransferStatus
        self.IdCardType=IdCardType
        self.PlateSerial=PlateSerial
        self.FutureFetchAmount=FutureFetchAmount
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BrokerFee=BrokerFee
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.Message=Message
        self.CustFee=CustFee
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'TransferStatus': {"'1'": u'\u88ab\u51b2\u6b63', "'0'": u'\u6b63\u5e38'}, 'FeePayFlag': {"'1'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u8d39\u7528', "'2'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u53d1\u8d77\u7684\u8d39\u7528\uff0c\u53d7\u76ca\u65b9\u652f\u4ed8\u63a5\u53d7\u7684\u8d39\u7528', "'0'": u'\u7531\u53d7\u76ca\u65b9\u652f\u4ed8\u8d39\u7528'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'InstallID', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'Password', 'BankPwdFlag', 'RequestID', 'CustType', 'IdentifiedCardNo', 'FeePayFlag', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'TransferStatus', 'IdCardType', 'PlateSerial', 'FutureFetchAmount', 'TradeDate', 'CurrencyID', 'BrokerFee', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'Message', 'CustFee', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('Password', u'期货密码'),('BankPwdFlag', u'银行密码标志'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('FeePayFlag', u'费用支付标志'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TransferStatus', u'转账交易状态'),('IdCardType', u'证件类型'),('PlateSerial', u'银期平台消息流水号'),('FutureFetchAmount', u'期货可取金额'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BrokerFee', u'应收期货公司费用'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('Message', u'发送方给接收方的消息'),('CustFee', u'应收客户费用'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'FeePayFlag', 'TransferStatus', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcErrOrderActionField:
    def __init__(self, ActionTime="", InvestorID="", TraderID="", UserID="", LimitPrice=0, ClientID="", InstallID=0, ParticipantID="", OrderActionRef=0, VolumeChange=0, SessionID=0, ActionFlag='0', ErrorID=0, InstrumentID="", ExchangeID="", StatusMsg="", BrokerID="", ActionDate="", OrderLocalID="", BranchID="", BusinessUnit="", ErrorMsg="", OrderRef="", ActionLocalID="", RequestID=0, FrontID=0, OrderActionStatus='a'):
        self.ActionTime=ActionTime
        self.InvestorID=InvestorID
        self.TraderID=TraderID
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.ClientID=ClientID
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.OrderActionRef=OrderActionRef
        self.VolumeChange=VolumeChange
        self.SessionID=SessionID
        self.ActionFlag=ActionFlag
        self.ErrorID=ErrorID
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.StatusMsg=StatusMsg
        self.BrokerID=BrokerID
        self.ActionDate=ActionDate
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.ErrorMsg=ErrorMsg
        self.OrderRef=OrderRef
        self.ActionLocalID=ActionLocalID
        self.RequestID=RequestID
        self.FrontID=FrontID
        self.OrderActionStatus=OrderActionStatus
        self.vcmap={'OrderActionStatus': {"'a'": u'\u5df2\u7ecf\u63d0\u4ea4', "'b'": u'\u5df2\u7ecf\u63a5\u53d7', "'c'": u'\u5df2\u7ecf\u88ab\u62d2\u7edd'}, 'ActionFlag': {"'0'": u'\u5220\u9664', "'3'": u'\u4fee\u6539'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ActionTime', 'InvestorID', 'TraderID', 'UserID', 'LimitPrice', 'ClientID', 'InstallID', 'ParticipantID', 'OrderActionRef', 'VolumeChange', 'SessionID', 'ActionFlag', 'ErrorID', 'InstrumentID', 'ExchangeID', 'StatusMsg', 'BrokerID', 'ActionDate', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'ErrorMsg', 'OrderRef', 'ActionLocalID', 'RequestID', 'FrontID', 'OrderActionStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ActionTime', u'操作时间'),('InvestorID', u'投资者代码'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('OrderActionRef', u'报单操作引用'),('VolumeChange', u'数量变化'),('SessionID', u'会话编号'),('ActionFlag', u'操作标志'),('ErrorID', u'错误代码'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('StatusMsg', u'状态信息'),('BrokerID', u'经纪公司代码'),('ActionDate', u'操作日期'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('ErrorMsg', u'错误信息'),('OrderRef', u'报单引用'),('ActionLocalID', u'操作本地编号'),('RequestID', u'请求编号'),('FrontID', u'前置编号'),('OrderActionStatus', u'报单操作状态')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcNotifyFutureSignInField:
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
        self.Digest=Digest
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'PinKey', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'MacKey', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('PinKey', u'PIN密钥'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('MacKey', u'MAC密钥'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInvestorField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryNoticeField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySyncDepositField:
    def __init__(self, DepositSeqNo="", BrokerID=""):
        self.DepositSeqNo=DepositSeqNo
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DepositSeqNo', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('DepositSeqNo', u'出入金流水号'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcUserRightField:
    def __init__(self, UserRightType='1', UserID="", BrokerID="", IsForbidden=0):
        self.UserRightType=UserRightType
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.IsForbidden=IsForbidden
        self.vcmap={'UserRightType': {"'1'": u'\u767b\u5f55', "'2'": u'\u94f6\u671f\u8f6c\u5e10', "'5'": u'\u6761\u4ef6\u5355', "'3'": u'\u90ae\u5bc4\u7ed3\u7b97\u5355', "'4'": u'\u4f20\u771f\u7ed3\u7b97\u5355'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserRightType', 'UserID', 'BrokerID', 'IsForbidden']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserRightType', u'客户权限类型'),('UserID', u'用户代码'),('BrokerID', u'经纪公司代码'),('IsForbidden', u'是否禁止')]])
    def getval(self, n):
        if n in ['UserRightType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQueryMaxOrderVolumeField:
    def __init__(self, InstrumentID="", Direction='0', OffsetFlag='0', HedgeFlag='1', InvestorID="", BrokerID="", MaxVolume=0):
        self.InstrumentID=InstrumentID
        self.Direction=Direction
        self.OffsetFlag=OffsetFlag
        self.HedgeFlag=HedgeFlag
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.MaxVolume=MaxVolume
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'OffsetFlag': {"'5'": u'\u5f3a\u51cf', "'4'": u'\u5e73\u6628', "'1'": u'\u5e73\u4ed3', "'0'": u'\u5f00\u4ed3', "'6'": u'\u672c\u5730\u5f3a\u5e73', "'2'": u'\u5f3a\u5e73', "'3'": u'\u5e73\u4eca'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'Direction', 'OffsetFlag', 'HedgeFlag', 'InvestorID', 'BrokerID', 'MaxVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('Direction', u'买卖方向'),('OffsetFlag', u'开平标志'),('HedgeFlag', u'投机套保标志'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('MaxVolume', u'最大允许报单数量')]])
    def getval(self, n):
        if n in ['Direction', 'OffsetFlag', 'HedgeFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeTradeField:
    def __init__(self, ExchangeID="", TradeType='0', ParticipantID="", TradeID="", TradeDate="", BusinessUnit="", SequenceNo=0, Price="", TraderID="", HedgeFlag='1', Direction='0', ClientID="", Volume=0, ExchangeInstID="", TradeTime="", OrderLocalID="", OrderSysID="", ClearingPartID="", PriceSource='0', TradingRole='1', OffsetFlag='0'):
        self.ExchangeID=ExchangeID
        self.TradeType=TradeType
        self.ParticipantID=ParticipantID
        self.TradeID=TradeID
        self.TradeDate=TradeDate
        self.BusinessUnit=BusinessUnit
        self.SequenceNo=SequenceNo
        self.Price=Price
        self.TraderID=TraderID
        self.HedgeFlag=HedgeFlag
        self.Direction=Direction
        self.ClientID=ClientID
        self.Volume=Volume
        self.ExchangeInstID=ExchangeInstID
        self.TradeTime=TradeTime
        self.OrderLocalID=OrderLocalID
        self.OrderSysID=OrderSysID
        self.ClearingPartID=ClearingPartID
        self.PriceSource=PriceSource
        self.TradingRole=TradingRole
        self.OffsetFlag=OffsetFlag
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'TradeType': {"'5'": u'ETF\u7533\u8d2d', "'4'": u'\u7ec4\u5408\u884d\u751f\u6210\u4ea4', "'1'": u'\u671f\u6743\u6267\u884c', "'0'": u'\u666e\u901a\u6210\u4ea4', "'6'": u'ETF\u8d4e\u56de', "'2'": u'OTC\u6210\u4ea4', "'3'": u'\u671f\u8f6c\u73b0\u884d\u751f\u6210\u4ea4'}, 'OffsetFlag': {"'5'": u'\u5f3a\u51cf', "'4'": u'\u5e73\u6628', "'1'": u'\u5e73\u4ed3', "'0'": u'\u5f00\u4ed3', "'6'": u'\u672c\u5730\u5f3a\u5e73', "'2'": u'\u5f3a\u5e73', "'3'": u'\u5e73\u4eca'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'PriceSource': {"'1'": u'\u4e70\u59d4\u6258\u4ef7', "'2'": u'\u5356\u59d4\u6258\u4ef7', "'0'": u'\u524d\u6210\u4ea4\u4ef7'}, 'TradingRole': {"'1'": u'\u4ee3\u7406', "'2'": u'\u81ea\u8425', "'3'": u'\u505a\u5e02\u5546'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TradeType', 'ParticipantID', 'TradeID', 'TradeDate', 'BusinessUnit', 'SequenceNo', 'Price', 'TraderID', 'HedgeFlag', 'Direction', 'ClientID', 'Volume', 'ExchangeInstID', 'TradeTime', 'OrderLocalID', 'OrderSysID', 'ClearingPartID', 'PriceSource', 'TradingRole', 'OffsetFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TradeType', u'成交类型'),('ParticipantID', u'会员代码'),('TradeID', u'成交编号'),('TradeDate', u'成交时期'),('BusinessUnit', u'业务单元'),('SequenceNo', u'序号'),('Price', u'价格'),('TraderID', u'交易所交易员代码'),('HedgeFlag', u'投机套保标志'),('Direction', u'买卖方向'),('ClientID', u'客户代码'),('Volume', u'数量'),('ExchangeInstID', u'合约在交易所的代码'),('TradeTime', u'成交时间'),('OrderLocalID', u'本地报单编号'),('OrderSysID', u'报单编号'),('ClearingPartID', u'结算会员编号'),('PriceSource', u'成交价来源'),('TradingRole', u'交易角色'),('OffsetFlag', u'开平标志')]])
    def getval(self, n):
        if n in ['TradeType', 'HedgeFlag', 'Direction', 'PriceSource', 'TradingRole', 'OffsetFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcFutureSignIOField:
    def __init__(self, InstallID=0, TradeDate="", TradeCode="", LastFragment='0', BrokerBranchID="", BrokerIDByBank="", BankSerial="", BankBranchID="", OperNo="", TradingDay="", SessionID=0, BrokerID="", DeviceID="", UserID="", BankID="", TID=0, TradeTime="", PlateSerial=0, CurrencyID="", Digest="", RequestID=0):
        self.InstallID=InstallID
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.LastFragment=LastFragment
        self.BrokerBranchID=BrokerBranchID
        self.BrokerIDByBank=BrokerIDByBank
        self.BankSerial=BankSerial
        self.BankBranchID=BankBranchID
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.UserID=UserID
        self.BankID=BankID
        self.TID=TID
        self.TradeTime=TradeTime
        self.PlateSerial=PlateSerial
        self.CurrencyID=CurrencyID
        self.Digest=Digest
        self.RequestID=RequestID
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstallID', 'TradeDate', 'TradeCode', 'LastFragment', 'BrokerBranchID', 'BrokerIDByBank', 'BankSerial', 'BankBranchID', 'OperNo', 'TradingDay', 'SessionID', 'BrokerID', 'DeviceID', 'UserID', 'BankID', 'TID', 'TradeTime', 'PlateSerial', 'CurrencyID', 'Digest', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstallID', u'安装编号'),('TradeDate', u'交易日期'),('TradeCode', u'业务功能码'),('LastFragment', u'最后分片标志'),('BrokerBranchID', u'期商分支机构代码'),('BrokerIDByBank', u'期货公司银行编码'),('BankSerial', u'银行流水号'),('BankBranchID', u'银行分支机构代码'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('UserID', u'用户标识'),('BankID', u'银行代码'),('TID', u'交易ID'),('TradeTime', u'交易时间'),('PlateSerial', u'银期平台消息流水号'),('CurrencyID', u'币种代码'),('Digest', u'摘要'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInputOrderActionField:
    def __init__(self, InstrumentID="", ExchangeID="", OrderLocalID="", OrderActionRef=0, TraderID="", UserID="", LimitPrice=0, OrderRef="", InvestorID="", SessionID=0, VolumeChange=0, BrokerID="", RequestID=0, ActionFlag='0', FrontID=0):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.OrderLocalID=OrderLocalID
        self.OrderActionRef=OrderActionRef
        self.TraderID=TraderID
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.OrderRef=OrderRef
        self.InvestorID=InvestorID
        self.SessionID=SessionID
        self.VolumeChange=VolumeChange
        self.BrokerID=BrokerID
        self.RequestID=RequestID
        self.ActionFlag=ActionFlag
        self.FrontID=FrontID
        self.vcmap={'ActionFlag': {"'0'": u'\u5220\u9664', "'3'": u'\u4fee\u6539'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'OrderLocalID', 'OrderActionRef', 'TraderID', 'UserID', 'LimitPrice', 'OrderRef', 'InvestorID', 'SessionID', 'VolumeChange', 'BrokerID', 'RequestID', 'ActionFlag', 'FrontID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('OrderLocalID', u'本地报单编号'),('OrderActionRef', u'报单操作引用'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('OrderRef', u'报单引用'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('VolumeChange', u'数量变化'),('BrokerID', u'经纪公司代码'),('RequestID', u'请求编号'),('ActionFlag', u'操作标志'),('FrontID', u'前置编号')]])
    def getval(self, n):
        if n in ['ActionFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferQryDetailRspField:
    def __init__(self, BankAccount="", FutureAccount="", TradeDate="", TradeCode="", CurrencyCode="", BankSerial=0, FutureSerial=0, FutureID="", CertCode="", TxAmount=0, Flag='0', TradeTime="", BankBrchID="", BankID=""):
        self.BankAccount=BankAccount
        self.FutureAccount=FutureAccount
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.CurrencyCode=CurrencyCode
        self.BankSerial=BankSerial
        self.FutureSerial=FutureSerial
        self.FutureID=FutureID
        self.CertCode=CertCode
        self.TxAmount=TxAmount
        self.Flag=Flag
        self.TradeTime=TradeTime
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.vcmap={'Flag': {"'1'": u'\u6709\u6548', "'2'": u'\u51b2\u6b63', "'0'": u'\u65e0\u6548\u6216\u5931\u8d25'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankAccount', 'FutureAccount', 'TradeDate', 'TradeCode', 'CurrencyCode', 'BankSerial', 'FutureSerial', 'FutureID', 'CertCode', 'TxAmount', 'Flag', 'TradeTime', 'BankBrchID', 'BankID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankAccount', u'银行账号'),('FutureAccount', u'资金帐号'),('TradeDate', u'交易日期'),('TradeCode', u'交易代码'),('CurrencyCode', u'货币代码'),('BankSerial', u'银行流水号'),('FutureSerial', u'期货流水号'),('FutureID', u'期货公司代码'),('CertCode', u'证件号码'),('TxAmount', u'发生金额'),('Flag', u'有效标志'),('TradeTime', u'交易时间'),('BankBrchID', u'银行分中心代码'),('BankID', u'银行代码')]])
    def getval(self, n):
        if n in ['Flag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeField:
    def __init__(self, ExchangeProperty='0', ExchangeID="", ExchangeName=""):
        self.ExchangeProperty=ExchangeProperty
        self.ExchangeID=ExchangeID
        self.ExchangeName=ExchangeName
        self.vcmap={'ExchangeProperty': {"'1'": u'\u6839\u636e\u6210\u4ea4\u751f\u6210\u62a5\u5355', "'0'": u'\u6b63\u5e38'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeProperty', 'ExchangeID', 'ExchangeName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeProperty', u'交易所属性'),('ExchangeID', u'交易所代码'),('ExchangeName', u'交易所名称')]])
    def getval(self, n):
        if n in ['ExchangeProperty']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferQryBankReqField:
    def __init__(self, CurrencyCode="", FutureAccount="", FuturePwdFlag='0', FutureAccPwd=""):
        self.CurrencyCode=CurrencyCode
        self.FutureAccount=FutureAccount
        self.FuturePwdFlag=FuturePwdFlag
        self.FutureAccPwd=FutureAccPwd
        self.vcmap={'FuturePwdFlag': {"'1'": u'\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CurrencyCode', 'FutureAccount', 'FuturePwdFlag', 'FutureAccPwd']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('FutureAccount', u'期货资金账户'),('FuturePwdFlag', u'密码标志'),('FutureAccPwd', u'密码')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferBankToFutureReqField:
    def __init__(self, FutureAccount="", FutureAccPwd="", CurrencyCode="", TradeAmt=0, FuturePwdFlag='0', CustFee=0):
        self.FutureAccount=FutureAccount
        self.FutureAccPwd=FutureAccPwd
        self.CurrencyCode=CurrencyCode
        self.TradeAmt=TradeAmt
        self.FuturePwdFlag=FuturePwdFlag
        self.CustFee=CustFee
        self.vcmap={'FuturePwdFlag': {"'1'": u'\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'FutureAccPwd', 'CurrencyCode', 'TradeAmt', 'FuturePwdFlag', 'CustFee']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户'),('FutureAccPwd', u'密码'),('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('TradeAmt', u'转账金额'),('FuturePwdFlag', u'密码标志'),('CustFee', u'客户手续费')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryUserSessionField:
    def __init__(self, FrontID=0, SessionID=0, BrokerID="", UserID=""):
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.UserID=UserID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID', 'SessionID', 'BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrontID', u'前置编号'),('SessionID', u'会话编号'),('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeMarginRateAdjustField:
    def __init__(self, InstrumentID="", ShortMarginRatioByMoney=0, ExchLongMarginRatioByMoney=0, ExchShortMarginRatioByMoney=0, LongMarginRatioByMoney=0, ExchShortMarginRatioByVolume=0, ExchLongMarginRatioByVolume=0, NoShortMarginRatioByMoney=0, NoLongMarginRatioByMoney=0, HedgeFlag='1', NoLongMarginRatioByVolume=0, NoShortMarginRatioByVolume=0, BrokerID="", ShortMarginRatioByVolume=0, LongMarginRatioByVolume=0):
        self.InstrumentID=InstrumentID
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.ExchLongMarginRatioByMoney=ExchLongMarginRatioByMoney
        self.ExchShortMarginRatioByMoney=ExchShortMarginRatioByMoney
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.ExchShortMarginRatioByVolume=ExchShortMarginRatioByVolume
        self.ExchLongMarginRatioByVolume=ExchLongMarginRatioByVolume
        self.NoShortMarginRatioByMoney=NoShortMarginRatioByMoney
        self.NoLongMarginRatioByMoney=NoLongMarginRatioByMoney
        self.HedgeFlag=HedgeFlag
        self.NoLongMarginRatioByVolume=NoLongMarginRatioByVolume
        self.NoShortMarginRatioByVolume=NoShortMarginRatioByVolume
        self.BrokerID=BrokerID
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByMoney', 'ExchLongMarginRatioByMoney', 'ExchShortMarginRatioByMoney', 'LongMarginRatioByMoney', 'ExchShortMarginRatioByVolume', 'ExchLongMarginRatioByVolume', 'NoShortMarginRatioByMoney', 'NoLongMarginRatioByMoney', 'HedgeFlag', 'NoLongMarginRatioByVolume', 'NoShortMarginRatioByVolume', 'BrokerID', 'ShortMarginRatioByVolume', 'LongMarginRatioByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByMoney', u'跟随交易所投资者空头保证金率'),('ExchLongMarginRatioByMoney', u'交易所多头保证金率'),('ExchShortMarginRatioByMoney', u'交易所空头保证金率'),('LongMarginRatioByMoney', u'跟随交易所投资者多头保证金率'),('ExchShortMarginRatioByVolume', u'交易所空头保证金费'),('ExchLongMarginRatioByVolume', u'交易所多头保证金费'),('NoShortMarginRatioByMoney', u'不跟随交易所投资者空头保证金率'),('NoLongMarginRatioByMoney', u'不跟随交易所投资者多头保证金率'),('HedgeFlag', u'投机套保标志'),('NoLongMarginRatioByVolume', u'不跟随交易所投资者多头保证金费'),('NoShortMarginRatioByVolume', u'不跟随交易所投资者空头保证金费'),('BrokerID', u'经纪公司代码'),('ShortMarginRatioByVolume', u'跟随交易所投资者空头保证金费'),('LongMarginRatioByVolume', u'跟随交易所投资者多头保证金费')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspAuthenticateField:
    def __init__(self, UserID="", BrokerID="", UserProductInfo=""):
        self.UserID=UserID
        self.BrokerID=BrokerID
        self.UserProductInfo=UserProductInfo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'BrokerID', 'UserProductInfo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTradingCodeField:
    def __init__(self, InvestorID="", ExchangeID="", BrokerID="", ClientID=""):
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.ClientID=ClientID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ExchangeID', 'BrokerID', 'ClientID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('ClientID', u'客户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataLastMatchField:
    def __init__(self, Volume=0, OpenInterest=0, LastPrice=0, Turnover=0):
        self.Volume=Volume
        self.OpenInterest=OpenInterest
        self.LastPrice=LastPrice
        self.Turnover=Turnover
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Volume', 'OpenInterest', 'LastPrice', 'Turnover']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Volume', u'数量'),('OpenInterest', u'持仓量'),('LastPrice', u'最新价'),('Turnover', u'成交金额')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataExchangeField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=ExchangeID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcDisseminationField:
    def __init__(self, SequenceNo=0, SequenceSeries=0):
        self.SequenceNo=SequenceNo
        self.SequenceSeries=SequenceSeries
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceNo', 'SequenceSeries']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SequenceNo', u'序列号'),('SequenceSeries', u'序列系列号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRemoveParkedOrderField:
    def __init__(self, InvestorID="", BrokerID="", ParkedOrderID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.ParkedOrderID=ParkedOrderID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'ParkedOrderID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('ParkedOrderID', u'预埋报单编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryOrderField:
    def __init__(self, InstrumentID="", ExchangeID="", InsertTimeStart="", InvestorID="", BrokerID="", OrderSysID="", InsertTimeEnd=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.InsertTimeStart=InsertTimeStart
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.OrderSysID=OrderSysID
        self.InsertTimeEnd=InsertTimeEnd
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'InsertTimeStart', 'InvestorID', 'BrokerID', 'OrderSysID', 'InsertTimeEnd']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('InsertTimeStart', u'开始时间'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('OrderSysID', u'报单编号'),('InsertTimeEnd', u'结束时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInstrumentTradingRightField:
    def __init__(self, InstrumentID="", Direction='0', InstrumentRange='1', TradingRight='0', ExchangeID="", InvestorID="", BrokerID="", InvestorRange='1'):
        self.InstrumentID=InstrumentID
        self.Direction=Direction
        self.InstrumentRange=InstrumentRange
        self.TradingRight=TradingRight
        self.ExchangeID=ExchangeID
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'InstrumentRange': {"'1'": u'\u6240\u6709', "'2'": u'\u4ea7\u54c1', "'3'": u'\u80a1\u7968\u6743\u9650\u6a21\u7248', "'4'": u'\u80a1\u7968'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}, 'TradingRight': {"'2'": u'\u4e0d\u80fd\u4ea4\u6613', "'0'": u'\u53ef\u4ee5\u4ea4\u6613'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'Direction', 'InstrumentRange', 'TradingRight', 'ExchangeID', 'InvestorID', 'BrokerID', 'InvestorRange']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('Direction', u'买卖'),('InstrumentRange', u'股票权限分类'),('TradingRight', u'交易权限'),('ExchangeID', u'交易所代码'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围')]])
    def getval(self, n):
        if n in ['Direction', 'InstrumentRange', 'TradingRight', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataBestPriceField:
    def __init__(self, AskVolume1=0, BidPrice1=0, AskPrice1=0, BidVolume1=0):
        self.AskVolume1=AskVolume1
        self.BidPrice1=BidPrice1
        self.AskPrice1=AskPrice1
        self.BidVolume1=BidVolume1
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AskVolume1', 'BidPrice1', 'AskPrice1', 'BidVolume1']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('AskVolume1', u'申卖量一'),('BidPrice1', u'申买价一'),('AskPrice1', u'申卖价一'),('BidVolume1', u'申买量一')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferHeaderField:
    def __init__(self, TradeDate="", TradeCode="", FutureID="", OperNo="", SessionID=0, Version="", TradeTime="", DeviceID="", BankBrchID="", BankID="", RecordNum="", TradeSerial="", RequestID=0):
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.FutureID=FutureID
        self.OperNo=OperNo
        self.SessionID=SessionID
        self.Version=Version
        self.TradeTime=TradeTime
        self.DeviceID=DeviceID
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.RecordNum=RecordNum
        self.TradeSerial=TradeSerial
        self.RequestID=RequestID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeDate', 'TradeCode', 'FutureID', 'OperNo', 'SessionID', 'Version', 'TradeTime', 'DeviceID', 'BankBrchID', 'BankID', 'RecordNum', 'TradeSerial', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradeDate', u'交易日期，必填，格式：yyyymmdd'),('TradeCode', u'交易代码，必填'),('FutureID', u'期货公司代码，必填'),('OperNo', u'操作员，N/A'),('SessionID', u'会话编号，N/A'),('Version', u'版本号，常量，1.0'),('TradeTime', u'交易时间，必填，格式：hhmmss'),('DeviceID', u'交易设备类型，N/A'),('BankBrchID', u'银行分中心代码，根据查询银行得到，必填'),('BankID', u'银行代码，根据查询银行得到，必填'),('RecordNum', u'记录数，N/A'),('TradeSerial', u'发起方流水号，N/A'),('RequestID', u'请求编号，N/A')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQrySettlementInfoConfirmField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqCancelAccountField:
    def __init__(self, MoneyAccountStatus='0', BrokerBranchID="", BankPassWord="", Telephone="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", Fax="", InstallID=0, CustomerName="", CountryCode="", TradeCode="", BankSecuAcc="", BankBranchID="", SessionID=0, Address="", PlateSerial=0, BankPwdFlag='0', CustType='0', IdentifiedCardNo="", BankID="", BankSerial="", OperNo="", TradingDay="", Gender='0', BrokerID="", CashExchangeCode='1', IdCardType='0', Password="", MobilePhone="", TradeDate="", CurrencyID="", BankAccType='1', LastFragment='0', ZipCode="", BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', EMail="", Digest="", DeviceID=""):
        self.MoneyAccountStatus=MoneyAccountStatus
        self.BrokerBranchID=BrokerBranchID
        self.BankPassWord=BankPassWord
        self.Telephone=Telephone
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.Fax=Fax
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.CountryCode=CountryCode
        self.TradeCode=TradeCode
        self.BankSecuAcc=BankSecuAcc
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.Address=Address
        self.PlateSerial=PlateSerial
        self.BankPwdFlag=BankPwdFlag
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankID=BankID
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.Gender=Gender
        self.BrokerID=BrokerID
        self.CashExchangeCode=CashExchangeCode
        self.IdCardType=IdCardType
        self.Password=Password
        self.MobilePhone=MobilePhone
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.ZipCode=ZipCode
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.EMail=EMail
        self.Digest=Digest
        self.DeviceID=DeviceID
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'Gender': {"'1'": u'\u7537', "'2'": u'\u5973', "'0'": u'\u672a\u77e5\u72b6\u6001'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'MoneyAccountStatus': {"'1'": u'\u9500\u6237', "'0'": u'\u6b63\u5e38'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'CashExchangeCode': {"'1'": u'\u6c47', "'2'": u'\u949e'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MoneyAccountStatus', 'BrokerBranchID', 'BankPassWord', 'Telephone', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'Fax', 'InstallID', 'CustomerName', 'CountryCode', 'TradeCode', 'BankSecuAcc', 'BankBranchID', 'SessionID', 'Address', 'PlateSerial', 'BankPwdFlag', 'CustType', 'IdentifiedCardNo', 'BankID', 'BankSerial', 'OperNo', 'TradingDay', 'Gender', 'BrokerID', 'CashExchangeCode', 'IdCardType', 'Password', 'MobilePhone', 'TradeDate', 'CurrencyID', 'BankAccType', 'LastFragment', 'ZipCode', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'EMail', 'Digest', 'DeviceID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MoneyAccountStatus', u'资金账户状态'),('BrokerBranchID', u'期商分支机构代码'),('BankPassWord', u'银行密码'),('Telephone', u'电话号码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('Fax', u'传真'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('CountryCode', u'国家代码'),('TradeCode', u'业务功能码'),('BankSecuAcc', u'期货单位帐号'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('Address', u'地址'),('PlateSerial', u'银期平台消息流水号'),('BankPwdFlag', u'银行密码标志'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankID', u'银行代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('Gender', u'性别'),('BrokerID', u'期商代码'),('CashExchangeCode', u'汇钞标志'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('MobilePhone', u'手机'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('ZipCode', u'邮编'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('EMail', u'电子邮件'),('Digest', u'摘要'),('DeviceID', u'渠道标志')]])
    def getval(self, n):
        if n in ['MoneyAccountStatus', 'VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'Gender', 'CashExchangeCode', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInstrumentField:
    def __init__(self, InstrumentID="", ExchangeID="", ExchangeInstID="", ProductID=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.ExchangeInstID=ExchangeInstID
        self.ProductID=ProductID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'ExchangeInstID', 'ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('ExchangeInstID', u'合约在交易所的代码'),('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReturnResultField:
    def __init__(self, ReturnCode="", DescrInfoForReturnCode=""):
        self.ReturnCode=ReturnCode
        self.DescrInfoForReturnCode=DescrInfoForReturnCode
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ReturnCode', 'DescrInfoForReturnCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ReturnCode', u'返回代码'),('DescrInfoForReturnCode', u'返回码描述')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcVerifyFuturePasswordAndCustInfoField:
    def __init__(self, CustType='0', CustomerName="", IdCardType='0', IdentifiedCardNo="", Password="", AccountID=""):
        self.CustType=CustType
        self.CustomerName=CustomerName
        self.IdCardType=IdCardType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.Password=Password
        self.AccountID=AccountID
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CustType', 'CustomerName', 'IdCardType', 'IdentifiedCardNo', 'Password', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('CustType', u'客户类型'),('CustomerName', u'客户姓名'),('IdCardType', u'证件类型'),('IdentifiedCardNo', u'证件号码'),('Password', u'期货密码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in ['CustType', 'IdCardType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspFundIOCTPAccountField:
    def __init__(self, PlateSerial=0, TradingDay="", CTPSerial=0, UserID="", SettlementSerial="", InvestorID="", SessionID=0, BrokerID="", FundDirection='1', TradeTime="", Password="", TradeAmount=0, Digest="", AccountID=""):
        self.PlateSerial=PlateSerial
        self.TradingDay=TradingDay
        self.CTPSerial=CTPSerial
        self.UserID=UserID
        self.SettlementSerial=SettlementSerial
        self.InvestorID=InvestorID
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.FundDirection=FundDirection
        self.TradeTime=TradeTime
        self.Password=Password
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.AccountID=AccountID
        self.vcmap={'FundDirection': {"'1'": u'\u5165\u91d1', "'2'": u'\u51fa\u91d1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PlateSerial', 'TradingDay', 'CTPSerial', 'UserID', 'SettlementSerial', 'InvestorID', 'SessionID', 'BrokerID', 'FundDirection', 'TradeTime', 'Password', 'TradeAmount', 'Digest', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('PlateSerial', u'转账平台流水号'),('TradingDay', u'交易日'),('CTPSerial', u'CTP核心流水号'),('UserID', u'用户代码'),('SettlementSerial', u'第三方流水号'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('BrokerID', u'证券公司代码'),('FundDirection', u'出入金方向'),('TradeTime', u'转账时间'),('Password', u'资金帐户密码'),('TradeAmount', u'交易金额'),('Digest', u'摘要'),('AccountID', u'投资者资金帐号')]])
    def getval(self, n):
        if n in ['FundDirection']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqFutureSignOutField:
    def __init__(self, InstallID=0, TradeDate="", TradeCode="", LastFragment='0', BrokerBranchID="", BrokerIDByBank="", BankSerial="", BankBranchID="", OperNo="", TradingDay="", SessionID=0, BrokerID="", DeviceID="", UserID="", BankID="", TID=0, TradeTime="", PlateSerial=0, CurrencyID="", Digest="", RequestID=0):
        self.InstallID=InstallID
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.LastFragment=LastFragment
        self.BrokerBranchID=BrokerBranchID
        self.BrokerIDByBank=BrokerIDByBank
        self.BankSerial=BankSerial
        self.BankBranchID=BankBranchID
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.UserID=UserID
        self.BankID=BankID
        self.TID=TID
        self.TradeTime=TradeTime
        self.PlateSerial=PlateSerial
        self.CurrencyID=CurrencyID
        self.Digest=Digest
        self.RequestID=RequestID
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstallID', 'TradeDate', 'TradeCode', 'LastFragment', 'BrokerBranchID', 'BrokerIDByBank', 'BankSerial', 'BankBranchID', 'OperNo', 'TradingDay', 'SessionID', 'BrokerID', 'DeviceID', 'UserID', 'BankID', 'TID', 'TradeTime', 'PlateSerial', 'CurrencyID', 'Digest', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstallID', u'安装编号'),('TradeDate', u'交易日期'),('TradeCode', u'业务功能码'),('LastFragment', u'最后分片标志'),('BrokerBranchID', u'期商分支机构代码'),('BrokerIDByBank', u'期货公司银行编码'),('BankSerial', u'银行流水号'),('BankBranchID', u'银行分支机构代码'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('UserID', u'用户标识'),('BankID', u'银行代码'),('TID', u'交易ID'),('TradeTime', u'交易时间'),('PlateSerial', u'银期平台消息流水号'),('CurrencyID', u'币种代码'),('Digest', u'摘要'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcUserPasswordUpdateField:
    def __init__(self, UserID="", NewPassword="", OldPassword="", BrokerID=""):
        self.UserID=UserID
        self.NewPassword=NewPassword
        self.OldPassword=OldPassword
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'NewPassword', 'OldPassword', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('NewPassword', u'新的口令'),('OldPassword', u'原来的口令'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingCodeField:
    def __init__(self, InvestorID="", ExchangeID="", BrokerID="", IsActive=0, ClientID=""):
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.IsActive=IsActive
        self.ClientID=ClientID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ExchangeID', 'BrokerID', 'IsActive', 'ClientID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('IsActive', u'是否活跃'),('ClientID', u'客户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqUserLoginField:
    def __init__(self, MacAddress="", UserProductInfo="", UserID="", TradingDay="", InterfaceProductInfo="", BrokerID="", ClientIPAddress="", OneTimePassword="", ProtocolInfo="", Password=""):
        self.MacAddress=MacAddress
        self.UserProductInfo=UserProductInfo
        self.UserID=UserID
        self.TradingDay=TradingDay
        self.InterfaceProductInfo=InterfaceProductInfo
        self.BrokerID=BrokerID
        self.ClientIPAddress=ClientIPAddress
        self.OneTimePassword=OneTimePassword
        self.ProtocolInfo=ProtocolInfo
        self.Password=Password
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MacAddress', 'UserProductInfo', 'UserID', 'TradingDay', 'InterfaceProductInfo', 'BrokerID', 'ClientIPAddress', 'OneTimePassword', 'ProtocolInfo', 'Password']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MacAddress', u'Mac地址'),('UserProductInfo', u'用户端产品信息'),('UserID', u'用户代码'),('TradingDay', u'交易日'),('InterfaceProductInfo', u'接口端产品信息'),('BrokerID', u'经纪公司代码'),('ClientIPAddress', u'终端IP地址'),('OneTimePassword', u'动态密码'),('ProtocolInfo', u'协议信息'),('Password', u'密码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInstrumentCommissionRateField:
    def __init__(self, InstrumentID="", ExchangeID="", TradeFeeByMoney=0, Direction='0', MinTradeFee=0, StampTaxRateByMoney=0, InvestorID="", MarginByMoney=0, StampTaxRateByVolume=0, BrokerID="", InvestorRange='1', TransferFeeRateByVolume=0, TransferFeeRateByMoney=0, TradeFeeByVolume=0):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.TradeFeeByMoney=TradeFeeByMoney
        self.Direction=Direction
        self.MinTradeFee=MinTradeFee
        self.StampTaxRateByMoney=StampTaxRateByMoney
        self.InvestorID=InvestorID
        self.MarginByMoney=MarginByMoney
        self.StampTaxRateByVolume=StampTaxRateByVolume
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.TransferFeeRateByVolume=TransferFeeRateByVolume
        self.TransferFeeRateByMoney=TransferFeeRateByMoney
        self.TradeFeeByVolume=TradeFeeByVolume
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'TradeFeeByMoney', 'Direction', 'MinTradeFee', 'StampTaxRateByMoney', 'InvestorID', 'MarginByMoney', 'StampTaxRateByVolume', 'BrokerID', 'InvestorRange', 'TransferFeeRateByVolume', 'TransferFeeRateByMoney', 'TradeFeeByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('TradeFeeByMoney', u'交易费'),('Direction', u'买卖方向'),('MinTradeFee', u'最小过户费'),('StampTaxRateByMoney', u'印花税率'),('InvestorID', u'投资者代码'),('MarginByMoney', u'交易附加费率'),('StampTaxRateByVolume', u'印花税率(按手数)'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('TransferFeeRateByVolume', u'过户费率(按手数)'),('TransferFeeRateByMoney', u'过户费率'),('TradeFeeByVolume', u'交易费(按手数)')]])
    def getval(self, n):
        if n in ['Direction', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSpecificInstrumentField:
    def __init__(self, InstrumentID="", ExchangeID=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryErrOrderField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSuperUserField:
    def __init__(self, UserName="", Password="", UserID="", IsActive=0):
        self.UserName=UserName
        self.Password=Password
        self.UserID=UserID
        self.IsActive=IsActive
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserName', 'Password', 'UserID', 'IsActive']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserName', u'用户名称'),('Password', u'密码'),('UserID', u'用户代码'),('IsActive', u'是否活跃')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingAccountPasswordField:
    def __init__(self, Password="", BrokerID="", AccountID=""):
        self.Password=Password
        self.BrokerID=BrokerID
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Password', u'密码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcLogoutAllField:
    def __init__(self, FrontID=0, SessionID=0, SystemName=""):
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.SystemName=SystemName
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID', 'SessionID', 'SystemName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrontID', u'前置编号'),('SessionID', u'会话编号'),('SystemName', u'系统名称')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcOrderField:
    def __init__(self, ContingentCondition='1', NotifySequence=0, ActiveUserID="", VolumeTraded=0, UserProductInfo="", CombOffsetFlag="", TraderID="", UserID="", LimitPrice="", UserForceClose=0, RelativeOrderSysID="", AccountID="", Direction='0', InstallID=0, ParticipantID="", VolumeTotalOriginal=0, ExchangeInstID="", ClientID="", VolumeTotal=0, OrderPriceType='1', SessionID=0, TimeCondition='1', OrderStatus='0', OrderSysID="", OrderSubmitStatus='0', IsETF=0, IsAutoSuspend=0, StopPrice=0, InstrumentID="", ExchangeID="", MinVolume=0, StatusMsg="", SettlementID=0, ForceCloseReason='0', OrderType='0', UpdateTime="", TradingDay="", ActiveTime="", BrokerID="", InsertTime="", FrontID=0, SuspendTime="", ClearingPartID="", CombHedgeFlag="", CancelTime="", GTDDate="", OrderLocalID="", BranchID="", BusinessUnit="", InsertDate="", SequenceNo=0, OrderRef="", BrokerOrderSeq=0, InvestorID="", VolumeCondition='1', RequestID=0, OrderSource='0', TradeAmount=0, ActiveTraderID=""):
        self.ContingentCondition=ContingentCondition
        self.NotifySequence=NotifySequence
        self.ActiveUserID=ActiveUserID
        self.VolumeTraded=VolumeTraded
        self.UserProductInfo=UserProductInfo
        self.CombOffsetFlag=CombOffsetFlag
        self.TraderID=TraderID
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.UserForceClose=UserForceClose
        self.RelativeOrderSysID=RelativeOrderSysID
        self.AccountID=AccountID
        self.Direction=Direction
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.ExchangeInstID=ExchangeInstID
        self.ClientID=ClientID
        self.VolumeTotal=VolumeTotal
        self.OrderPriceType=OrderPriceType
        self.SessionID=SessionID
        self.TimeCondition=TimeCondition
        self.OrderStatus=OrderStatus
        self.OrderSysID=OrderSysID
        self.OrderSubmitStatus=OrderSubmitStatus
        self.IsETF=IsETF
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.StatusMsg=StatusMsg
        self.SettlementID=SettlementID
        self.ForceCloseReason=ForceCloseReason
        self.OrderType=OrderType
        self.UpdateTime=UpdateTime
        self.TradingDay=TradingDay
        self.ActiveTime=ActiveTime
        self.BrokerID=BrokerID
        self.InsertTime=InsertTime
        self.FrontID=FrontID
        self.SuspendTime=SuspendTime
        self.ClearingPartID=ClearingPartID
        self.CombHedgeFlag=CombHedgeFlag
        self.CancelTime=CancelTime
        self.GTDDate=GTDDate
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.InsertDate=InsertDate
        self.SequenceNo=SequenceNo
        self.OrderRef=OrderRef
        self.BrokerOrderSeq=BrokerOrderSeq
        self.InvestorID=InvestorID
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.OrderSource=OrderSource
        self.TradeAmount=TradeAmount
        self.ActiveTraderID=ActiveTraderID
        self.vcmap={'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderType': {"'5'": u'\u4e92\u6362\u5355', "'4'": u'\u6761\u4ef6\u5355', "'1'": u'\u62a5\u4ef7\u884d\u751f', "'0'": u'\u6b63\u5e38', "'2'": u'\u7ec4\u5408\u884d\u751f', "'3'": u'\u7ec4\u5408\u62a5\u5355'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}, 'OrderSource': {"'1'": u'\u6765\u81ea\u7ba1\u7406\u5458', "'0'": u'\u6765\u81ea\u53c2\u4e0e\u8005'}, 'OrderStatus': {"'b'": u'\u5c1a\u672a\u89e6\u53d1', "'5'": u'\u64a4\u5355', "'c'": u'\u5df2\u89e6\u53d1', "'4'": u'\u672a\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'1'": u'\u90e8\u5206\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'0'": u'\u5168\u90e8\u6210\u4ea4', "'2'": u'\u90e8\u5206\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'3'": u'\u672a\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'a'": u'\u672a\u77e5'}, 'OrderSubmitStatus': {"'5'": u'\u64a4\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'4'": u'\u62a5\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'1'": u'\u64a4\u5355\u5df2\u7ecf\u63d0\u4ea4', "'0'": u'\u5df2\u7ecf\u63d0\u4ea4', "'6'": u'\u6539\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'2'": u'\u4fee\u6539\u5df2\u7ecf\u63d0\u4ea4', "'3'": u'\u5df2\u7ecf\u63a5\u53d7'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'NotifySequence', 'ActiveUserID', 'VolumeTraded', 'UserProductInfo', 'CombOffsetFlag', 'TraderID', 'UserID', 'LimitPrice', 'UserForceClose', 'RelativeOrderSysID', 'AccountID', 'Direction', 'InstallID', 'ParticipantID', 'VolumeTotalOriginal', 'ExchangeInstID', 'ClientID', 'VolumeTotal', 'OrderPriceType', 'SessionID', 'TimeCondition', 'OrderStatus', 'OrderSysID', 'OrderSubmitStatus', 'IsETF', 'IsAutoSuspend', 'StopPrice', 'InstrumentID', 'ExchangeID', 'MinVolume', 'StatusMsg', 'SettlementID', 'ForceCloseReason', 'OrderType', 'UpdateTime', 'TradingDay', 'ActiveTime', 'BrokerID', 'InsertTime', 'FrontID', 'SuspendTime', 'ClearingPartID', 'CombHedgeFlag', 'CancelTime', 'GTDDate', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'InsertDate', 'SequenceNo', 'OrderRef', 'BrokerOrderSeq', 'InvestorID', 'VolumeCondition', 'RequestID', 'OrderSource', 'TradeAmount', 'ActiveTraderID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('NotifySequence', u'报单提示序号'),('ActiveUserID', u'操作用户代码'),('VolumeTraded', u'今成交数量'),('UserProductInfo', u'用户端产品信息'),('CombOffsetFlag', u'组合开平标志'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('UserForceClose', u'用户强评标志'),('RelativeOrderSysID', u'相关报单'),('AccountID', u'资金帐号'),('Direction', u'买卖方向'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('VolumeTotalOriginal', u'数量'),('ExchangeInstID', u'合约在交易所的代码'),('ClientID', u'客户代码'),('VolumeTotal', u'剩余数量'),('OrderPriceType', u'报单价格条件'),('SessionID', u'会话编号'),('TimeCondition', u'有效期类型'),('OrderStatus', u'报单状态'),('OrderSysID', u'报单编号'),('OrderSubmitStatus', u'报单提交状态'),('IsETF', u'是否ETF'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('StatusMsg', u'状态信息'),('SettlementID', u'结算编号'),('ForceCloseReason', u'强平原因'),('OrderType', u'报单类型'),('UpdateTime', u'最后修改时间'),('TradingDay', u'交易日'),('ActiveTime', u'激活时间'),('BrokerID', u'经纪公司代码'),('InsertTime', u'委托时间'),('FrontID', u'前置编号'),('SuspendTime', u'挂起时间'),('ClearingPartID', u'结算会员编号'),('CombHedgeFlag', u'组合投机套保标志'),('CancelTime', u'撤销时间'),('GTDDate', u'GTD日期'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('InsertDate', u'报单日期'),('SequenceNo', u'序号'),('OrderRef', u'报单引用'),('BrokerOrderSeq', u'经纪公司报单编号'),('InvestorID', u'投资者代码'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号'),('OrderSource', u'报单来源'),('TradeAmount', u'成交数量'),('ActiveTraderID', u'最后修改交易所交易员代码')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Direction', 'OrderPriceType', 'TimeCondition', 'OrderStatus', 'OrderSubmitStatus', 'ForceCloseReason', 'OrderType', 'VolumeCondition', 'OrderSource']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqChangeAccountField:
    def __init__(self, MoneyAccountStatus='0', NewBankPassWord="", BrokerBranchID="", BankPassWord="", Telephone="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", Fax="", InstallID=0, CustomerName="", CountryCode="", TradeCode="", BankBranchID="", SessionID=0, NewBankAccount="", Address="", PlateSerial=0, BankPwdFlag='0', CustType='0', IdentifiedCardNo="", BankID="", BankSerial="", TradingDay="", Gender='0', BrokerID="", IdCardType='0', Password="", MobilePhone="", TradeDate="", CurrencyID="", BankAccType='1', LastFragment='0', ZipCode="", BrokerIDByBank="", SecuPwdFlag='0', EMail="", Digest=""):
        self.MoneyAccountStatus=MoneyAccountStatus
        self.NewBankPassWord=NewBankPassWord
        self.BrokerBranchID=BrokerBranchID
        self.BankPassWord=BankPassWord
        self.Telephone=Telephone
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.Fax=Fax
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.CountryCode=CountryCode
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.NewBankAccount=NewBankAccount
        self.Address=Address
        self.PlateSerial=PlateSerial
        self.BankPwdFlag=BankPwdFlag
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankID=BankID
        self.BankSerial=BankSerial
        self.TradingDay=TradingDay
        self.Gender=Gender
        self.BrokerID=BrokerID
        self.IdCardType=IdCardType
        self.Password=Password
        self.MobilePhone=MobilePhone
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.ZipCode=ZipCode
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.EMail=EMail
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'Gender': {"'1'": u'\u7537', "'2'": u'\u5973', "'0'": u'\u672a\u77e5\u72b6\u6001'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'MoneyAccountStatus': {"'1'": u'\u9500\u6237', "'0'": u'\u6b63\u5e38'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MoneyAccountStatus', 'NewBankPassWord', 'BrokerBranchID', 'BankPassWord', 'Telephone', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'Fax', 'InstallID', 'CustomerName', 'CountryCode', 'TradeCode', 'BankBranchID', 'SessionID', 'NewBankAccount', 'Address', 'PlateSerial', 'BankPwdFlag', 'CustType', 'IdentifiedCardNo', 'BankID', 'BankSerial', 'TradingDay', 'Gender', 'BrokerID', 'IdCardType', 'Password', 'MobilePhone', 'TradeDate', 'CurrencyID', 'BankAccType', 'LastFragment', 'ZipCode', 'BrokerIDByBank', 'SecuPwdFlag', 'EMail', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MoneyAccountStatus', u'资金账户状态'),('NewBankPassWord', u'新银行密码'),('BrokerBranchID', u'期商分支机构代码'),('BankPassWord', u'银行密码'),('Telephone', u'电话号码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('Fax', u'传真'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('CountryCode', u'国家代码'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('NewBankAccount', u'新银行帐号'),('Address', u'地址'),('PlateSerial', u'银期平台消息流水号'),('BankPwdFlag', u'银行密码标志'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankID', u'银行代码'),('BankSerial', u'银行流水号'),('TradingDay', u'交易系统日期'),('Gender', u'性别'),('BrokerID', u'期商代码'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('MobilePhone', u'手机'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('ZipCode', u'邮编'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('EMail', u'电子邮件'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['MoneyAccountStatus', 'VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'Gender', 'IdCardType', 'BankAccType', 'LastFragment', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryFrontStatusField:
    def __init__(self, FrontID=0):
        self.FrontID=FrontID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FrontID', u'前置编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcNotifyFutureSignOutField:
    def __init__(self, BrokerBranchID="", UserID="", TradeTime="", TID=0, InstallID=0, TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, ErrorID=0, BankSerial="", OperNo="", TradingDay="", BrokerID="", DeviceID="", TradeDate="", CurrencyID="", ErrorMsg="", LastFragment='0', RequestID=0, BrokerIDByBank="", Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.TID=TID
        self.InstallID=InstallID
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
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
        self.Digest=Digest
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInvestorPositionCombineDetailField:
    def __init__(self, InvestorID="", BrokerID="", CombInstrumentID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.CombInstrumentID=CombInstrumentID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'CombInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('CombInstrumentID', u'组合持仓合约编码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerWithdrawAlgorithmField:
    def __init__(self, IncludeCloseProfit='0', IsBrokerUserEvent=0, AvailIncludeCloseProfit='0', UsingRatio=0, BrokerID="", AllWithoutTrade='0', WithdrawAlgorithm='1'):
        self.IncludeCloseProfit=IncludeCloseProfit
        self.IsBrokerUserEvent=IsBrokerUserEvent
        self.AvailIncludeCloseProfit=AvailIncludeCloseProfit
        self.UsingRatio=UsingRatio
        self.BrokerID=BrokerID
        self.AllWithoutTrade=AllWithoutTrade
        self.WithdrawAlgorithm=WithdrawAlgorithm
        self.vcmap={'AvailIncludeCloseProfit': {"'2'": u'\u4e0d\u5305\u542b\u5e73\u4ed3\u76c8\u5229', "'0'": u'\u5305\u542b\u5e73\u4ed3\u76c8\u5229'}, 'WithdrawAlgorithm': {"'1'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u8ba1\u7b97', "'2'": u'\u6d6e\u76c8\u4e0d\u8ba1\uff0c\u6d6e\u4e8f\u8ba1', "'3'": u'\u6d6e\u76c8\u8ba1\uff0c\u6d6e\u4e8f\u4e0d\u8ba1', "'4'": u'\u6d6e\u76c8\u6d6e\u4e8f\u90fd\u4e0d\u8ba1\u7b97'}, 'IncludeCloseProfit': {"'2'": u'\u4e0d\u5305\u542b\u5e73\u4ed3\u76c8\u5229', "'0'": u'\u5305\u542b\u5e73\u4ed3\u76c8\u5229'}, 'AllWithoutTrade': {"'2'": u'\u53d7\u53ef\u63d0\u6bd4\u4f8b\u9650\u5236', "'0'": u'\u4e0d\u53d7\u53ef\u63d0\u6bd4\u4f8b\u9650\u5236'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IncludeCloseProfit', 'IsBrokerUserEvent', 'AvailIncludeCloseProfit', 'UsingRatio', 'BrokerID', 'AllWithoutTrade', 'WithdrawAlgorithm']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('IncludeCloseProfit', u'可提是否包含平仓盈利'),('IsBrokerUserEvent', u'是否启用用户事件'),('AvailIncludeCloseProfit', u'可用是否包含平仓盈利'),('UsingRatio', u'资金使用率'),('BrokerID', u'经纪公司代码'),('AllWithoutTrade', u'本日无仓且无成交客户是否受可提比例限制'),('WithdrawAlgorithm', u'可提资金算法')]])
    def getval(self, n):
        if n in ['IncludeCloseProfit', 'AvailIncludeCloseProfit', 'AllWithoutTrade', 'WithdrawAlgorithm']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcProductField:
    def __init__(self, MaxLimitOrderVolume=0, ExchangeID="", PositionDateType='1', MinLimitOrderVolume=0, MaxMarketOrderVolume=0, PriceTick=0, ProductName="", VolumeMultiple=0, PositionType='1', MinMarketOrderVolume=0, ProductClass='1', EFTMinTradeVolume=0, ProductID=""):
        self.MaxLimitOrderVolume=MaxLimitOrderVolume
        self.ExchangeID=ExchangeID
        self.PositionDateType=PositionDateType
        self.MinLimitOrderVolume=MinLimitOrderVolume
        self.MaxMarketOrderVolume=MaxMarketOrderVolume
        self.PriceTick=PriceTick
        self.ProductName=ProductName
        self.VolumeMultiple=VolumeMultiple
        self.PositionType=PositionType
        self.MinMarketOrderVolume=MinMarketOrderVolume
        self.ProductClass=ProductClass
        self.EFTMinTradeVolume=EFTMinTradeVolume
        self.ProductID=ProductID
        self.vcmap={'ProductClass': {"'9'": u'ETF\u7533\u8d4e', "'7'": u'\u8bc1\u5238B\u80a1', "'8'": u'ETF', "'5'": u'\u671f\u8f6c\u73b0', "'4'": u'\u5373\u671f', "'1'": u'\u671f\u8d27', "'6'": u'\u8bc1\u5238A\u80a1', "'2'": u'\u671f\u6743', "'3'": u'\u7ec4\u5408'}, 'PositionDateType': {"'1'": u'\u4f7f\u7528\u5386\u53f2\u6301\u4ed3', "'2'": u'\u4e0d\u4f7f\u7528\u5386\u53f2\u6301\u4ed3'}, 'PositionType': {"'1'": u'\u51c0\u6301\u4ed3', "'2'": u'\u7efc\u5408\u6301\u4ed3'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MaxLimitOrderVolume', 'ExchangeID', 'PositionDateType', 'MinLimitOrderVolume', 'MaxMarketOrderVolume', 'PriceTick', 'ProductName', 'VolumeMultiple', 'PositionType', 'MinMarketOrderVolume', 'ProductClass', 'EFTMinTradeVolume', 'ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MaxLimitOrderVolume', u'限价单最大下单量'),('ExchangeID', u'交易所代码'),('PositionDateType', u'持仓日期类型'),('MinLimitOrderVolume', u'限价单最小下单量'),('MaxMarketOrderVolume', u'市价单最大下单量'),('PriceTick', u'最小变动价位'),('ProductName', u'产品名称'),('VolumeMultiple', u'合约数量乘数'),('PositionType', u'持仓类型'),('MinMarketOrderVolume', u'市价单最小下单量'),('ProductClass', u'产品类型'),('EFTMinTradeVolume', u'ETF最小交易单位'),('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in ['PositionDateType', 'PositionType', 'ProductClass']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeOrderField:
    def __init__(self, ContingentCondition='1', NotifySequence=0, VolumeTraded=0, CombOffsetFlag="", TraderID="", LimitPrice="", Direction='0', InstallID=0, ParticipantID="", VolumeTotalOriginal=0, ExchangeInstID="", ClientID="", VolumeTotal=0, OrderPriceType='1', TimeCondition='1', OrderStatus='0', OrderSysID="", OrderSubmitStatus='0', IsAutoSuspend=0, StopPrice=0, ExchangeID="", MinVolume=0, SettlementID=0, ForceCloseReason='0', OrderType='0', UpdateTime="", TradingDay="", ActiveTime="", OrderSource='0', InsertTime="", SuspendTime="", ClearingPartID="", CombHedgeFlag="", CancelTime="", GTDDate="", OrderLocalID="", BranchID="", BusinessUnit="", InsertDate="", SequenceNo=0, VolumeCondition='1', RequestID=0, ActiveTraderID=""):
        self.ContingentCondition=ContingentCondition
        self.NotifySequence=NotifySequence
        self.VolumeTraded=VolumeTraded
        self.CombOffsetFlag=CombOffsetFlag
        self.TraderID=TraderID
        self.LimitPrice=LimitPrice
        self.Direction=Direction
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.ExchangeInstID=ExchangeInstID
        self.ClientID=ClientID
        self.VolumeTotal=VolumeTotal
        self.OrderPriceType=OrderPriceType
        self.TimeCondition=TimeCondition
        self.OrderStatus=OrderStatus
        self.OrderSysID=OrderSysID
        self.OrderSubmitStatus=OrderSubmitStatus
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.SettlementID=SettlementID
        self.ForceCloseReason=ForceCloseReason
        self.OrderType=OrderType
        self.UpdateTime=UpdateTime
        self.TradingDay=TradingDay
        self.ActiveTime=ActiveTime
        self.OrderSource=OrderSource
        self.InsertTime=InsertTime
        self.SuspendTime=SuspendTime
        self.ClearingPartID=ClearingPartID
        self.CombHedgeFlag=CombHedgeFlag
        self.CancelTime=CancelTime
        self.GTDDate=GTDDate
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.InsertDate=InsertDate
        self.SequenceNo=SequenceNo
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.ActiveTraderID=ActiveTraderID
        self.vcmap={'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderType': {"'5'": u'\u4e92\u6362\u5355', "'4'": u'\u6761\u4ef6\u5355', "'1'": u'\u62a5\u4ef7\u884d\u751f', "'0'": u'\u6b63\u5e38', "'2'": u'\u7ec4\u5408\u884d\u751f', "'3'": u'\u7ec4\u5408\u62a5\u5355'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}, 'OrderSource': {"'1'": u'\u6765\u81ea\u7ba1\u7406\u5458', "'0'": u'\u6765\u81ea\u53c2\u4e0e\u8005'}, 'OrderStatus': {"'b'": u'\u5c1a\u672a\u89e6\u53d1', "'5'": u'\u64a4\u5355', "'c'": u'\u5df2\u89e6\u53d1', "'4'": u'\u672a\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'1'": u'\u90e8\u5206\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'0'": u'\u5168\u90e8\u6210\u4ea4', "'2'": u'\u90e8\u5206\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'3'": u'\u672a\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'a'": u'\u672a\u77e5'}, 'OrderSubmitStatus': {"'5'": u'\u64a4\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'4'": u'\u62a5\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'1'": u'\u64a4\u5355\u5df2\u7ecf\u63d0\u4ea4', "'0'": u'\u5df2\u7ecf\u63d0\u4ea4', "'6'": u'\u6539\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'2'": u'\u4fee\u6539\u5df2\u7ecf\u63d0\u4ea4', "'3'": u'\u5df2\u7ecf\u63a5\u53d7'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'NotifySequence', 'VolumeTraded', 'CombOffsetFlag', 'TraderID', 'LimitPrice', 'Direction', 'InstallID', 'ParticipantID', 'VolumeTotalOriginal', 'ExchangeInstID', 'ClientID', 'VolumeTotal', 'OrderPriceType', 'TimeCondition', 'OrderStatus', 'OrderSysID', 'OrderSubmitStatus', 'IsAutoSuspend', 'StopPrice', 'ExchangeID', 'MinVolume', 'SettlementID', 'ForceCloseReason', 'OrderType', 'UpdateTime', 'TradingDay', 'ActiveTime', 'OrderSource', 'InsertTime', 'SuspendTime', 'ClearingPartID', 'CombHedgeFlag', 'CancelTime', 'GTDDate', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'InsertDate', 'SequenceNo', 'VolumeCondition', 'RequestID', 'ActiveTraderID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('NotifySequence', u'报单提示序号'),('VolumeTraded', u'今成交数量'),('CombOffsetFlag', u'组合开平标志'),('TraderID', u'交易所交易员代码'),('LimitPrice', u'价格'),('Direction', u'买卖方向'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('VolumeTotalOriginal', u'数量'),('ExchangeInstID', u'合约在交易所的代码'),('ClientID', u'客户代码'),('VolumeTotal', u'剩余数量'),('OrderPriceType', u'报单价格条件'),('TimeCondition', u'有效期类型'),('OrderStatus', u'报单状态'),('OrderSysID', u'报单编号'),('OrderSubmitStatus', u'报单提交状态'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('SettlementID', u'结算编号'),('ForceCloseReason', u'强平原因'),('OrderType', u'报单类型'),('UpdateTime', u'最后修改时间'),('TradingDay', u'交易日'),('ActiveTime', u'激活时间'),('OrderSource', u'报单来源'),('InsertTime', u'委托时间'),('SuspendTime', u'挂起时间'),('ClearingPartID', u'结算会员编号'),('CombHedgeFlag', u'组合投机套保标志'),('CancelTime', u'撤销时间'),('GTDDate', u'GTD日期'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('InsertDate', u'报单日期'),('SequenceNo', u'序号'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号'),('ActiveTraderID', u'最后修改交易所交易员代码')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Direction', 'OrderPriceType', 'TimeCondition', 'OrderStatus', 'OrderSubmitStatus', 'ForceCloseReason', 'OrderType', 'OrderSource', 'VolumeCondition']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRemoveParkedOrderActionField:
    def __init__(self, InvestorID="", BrokerID="", ParkedOrderActionID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.ParkedOrderActionID=ParkedOrderActionID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID', 'ParkedOrderActionID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('ParkedOrderActionID', u'预埋撤单编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcCurrentTimeField:
    def __init__(self, CurrTime="", CurrDate="", CurrMillisec=0):
        self.CurrTime=CurrTime
        self.CurrDate=CurrDate
        self.CurrMillisec=CurrMillisec
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CurrTime', 'CurrDate', 'CurrMillisec']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('CurrTime', u'当前时间'),('CurrDate', u'当前日期'),('CurrMillisec', u'当前时间（毫秒）')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTradeField:
    def __init__(self, InstrumentID="", TradeTimeStart="", ExchangeID="", TradeID="", InvestorID="", BrokerID="", TradeTimeEnd=""):
        self.InstrumentID=InstrumentID
        self.TradeTimeStart=TradeTimeStart
        self.ExchangeID=ExchangeID
        self.TradeID=TradeID
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.TradeTimeEnd=TradeTimeEnd
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'TradeTimeStart', 'ExchangeID', 'TradeID', 'InvestorID', 'BrokerID', 'TradeTimeEnd']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('TradeTimeStart', u'开始时间'),('ExchangeID', u'交易所代码'),('TradeID', u'成交编号'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('TradeTimeEnd', u'结束时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSettlementInfoField:
    def __init__(self, SettlementID=0, InvestorID="", SequenceNo=0, Content="", TradingDay="", BrokerID=""):
        self.SettlementID=SettlementID
        self.InvestorID=InvestorID
        self.SequenceNo=SequenceNo
        self.Content=Content
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SettlementID', 'InvestorID', 'SequenceNo', 'Content', 'TradingDay', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SettlementID', u'结算编号'),('InvestorID', u'投资者代码'),('SequenceNo', u'序号'),('Content', u'消息正文'),('TradingDay', u'交易日'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcDepthMarketDataField:
    def __init__(self, HighestPrice=0, BidPrice5=0, BidPrice4=0, BidPrice1=0, BidPrice3=0, BidPrice2=0, LowerLimitPrice=0, OpenPrice=0, AskPrice5=0, AskPrice4=0, AskPrice3=0, PreClosePrice=0, AskPrice1=0, PreSettlementPrice=0, AskVolume1=0, UpdateTime="", UpdateMillisec=0, AveragePrice=0, BidVolume5=0, BidVolume4=0, BidVolume3=0, BidVolume2=0, PreOpenInterest=0, AskPrice2=0, Volume=0, AskVolume3=0, AskVolume2=0, AskVolume5=0, AskVolume4=0, UpperLimitPrice=0, BidVolume1=0, InstrumentID="", ClosePrice=0, ExchangeID="", TradingDay="", PreDelta=0, OpenInterest=0, CurrDelta=0, Turnover=0, LastPrice=0, SettlementPrice=0, ExchangeInstID="", LowestPrice=0):
        self.HighestPrice=HighestPrice
        self.BidPrice5=BidPrice5
        self.BidPrice4=BidPrice4
        self.BidPrice1=BidPrice1
        self.BidPrice3=BidPrice3
        self.BidPrice2=BidPrice2
        self.LowerLimitPrice=LowerLimitPrice
        self.OpenPrice=OpenPrice
        self.AskPrice5=AskPrice5
        self.AskPrice4=AskPrice4
        self.AskPrice3=AskPrice3
        self.PreClosePrice=PreClosePrice
        self.AskPrice1=AskPrice1
        self.PreSettlementPrice=PreSettlementPrice
        self.AskVolume1=AskVolume1
        self.UpdateTime=UpdateTime
        self.UpdateMillisec=UpdateMillisec
        self.AveragePrice=AveragePrice
        self.BidVolume5=BidVolume5
        self.BidVolume4=BidVolume4
        self.BidVolume3=BidVolume3
        self.BidVolume2=BidVolume2
        self.PreOpenInterest=PreOpenInterest
        self.AskPrice2=AskPrice2
        self.Volume=Volume
        self.AskVolume3=AskVolume3
        self.AskVolume2=AskVolume2
        self.AskVolume5=AskVolume5
        self.AskVolume4=AskVolume4
        self.UpperLimitPrice=UpperLimitPrice
        self.BidVolume1=BidVolume1
        self.InstrumentID=InstrumentID
        self.ClosePrice=ClosePrice
        self.ExchangeID=ExchangeID
        self.TradingDay=TradingDay
        self.PreDelta=PreDelta
        self.OpenInterest=OpenInterest
        self.CurrDelta=CurrDelta
        self.Turnover=Turnover
        self.LastPrice=LastPrice
        self.SettlementPrice=SettlementPrice
        self.ExchangeInstID=ExchangeInstID
        self.LowestPrice=LowestPrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['HighestPrice', 'BidPrice5', 'BidPrice4', 'BidPrice1', 'BidPrice3', 'BidPrice2', 'LowerLimitPrice', 'OpenPrice', 'AskPrice5', 'AskPrice4', 'AskPrice3', 'PreClosePrice', 'AskPrice1', 'PreSettlementPrice', 'AskVolume1', 'UpdateTime', 'UpdateMillisec', 'AveragePrice', 'BidVolume5', 'BidVolume4', 'BidVolume3', 'BidVolume2', 'PreOpenInterest', 'AskPrice2', 'Volume', 'AskVolume3', 'AskVolume2', 'AskVolume5', 'AskVolume4', 'UpperLimitPrice', 'BidVolume1', 'InstrumentID', 'ClosePrice', 'ExchangeID', 'TradingDay', 'PreDelta', 'OpenInterest', 'CurrDelta', 'Turnover', 'LastPrice', 'SettlementPrice', 'ExchangeInstID', 'LowestPrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('HighestPrice', u'最高价'),('BidPrice5', u'申买价五'),('BidPrice4', u'申买价四'),('BidPrice1', u'申买价一'),('BidPrice3', u'申买价三'),('BidPrice2', u'申买价二'),('LowerLimitPrice', u'跌停板价'),('OpenPrice', u'今开盘'),('AskPrice5', u'申卖价五'),('AskPrice4', u'申卖价四'),('AskPrice3', u'申卖价三'),('PreClosePrice', u'昨收盘'),('AskPrice1', u'申卖价一'),('PreSettlementPrice', u'上次结算价'),('AskVolume1', u'申卖量一'),('UpdateTime', u'最后修改时间'),('UpdateMillisec', u'最后修改毫秒'),('AveragePrice', u'当日均价'),('BidVolume5', u'申买量五'),('BidVolume4', u'申买量四'),('BidVolume3', u'申买量三'),('BidVolume2', u'申买量二'),('PreOpenInterest', u'昨持仓量'),('AskPrice2', u'申卖价二'),('Volume', u'数量'),('AskVolume3', u'申卖量三'),('AskVolume2', u'申卖量二'),('AskVolume5', u'申卖量五'),('AskVolume4', u'申卖量四'),('UpperLimitPrice', u'涨停板价'),('BidVolume1', u'申买量一'),('InstrumentID', u'合约代码'),('ClosePrice', u'今收盘'),('ExchangeID', u'交易所代码'),('TradingDay', u'交易日'),('PreDelta', u'昨虚实度'),('OpenInterest', u'持仓量'),('CurrDelta', u'今虚实度'),('Turnover', u'成交金额'),('LastPrice', u'最新价'),('SettlementPrice', u'本次结算价'),('ExchangeInstID', u'合约在交易所的代码'),('LowestPrice', u'最低价')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqSyncKeyField:
    def __init__(self, InstallID=0, TradeDate="", TradeCode="", LastFragment='0', BrokerBranchID="", BrokerIDByBank="", BankSerial="", BankBranchID="", OperNo="", TradingDay="", SessionID=0, BrokerID="", DeviceID="", UserID="", BankID="", TID=0, TradeTime="", Message="", PlateSerial=0, RequestID=0):
        self.InstallID=InstallID
        self.TradeDate=TradeDate
        self.TradeCode=TradeCode
        self.LastFragment=LastFragment
        self.BrokerBranchID=BrokerBranchID
        self.BrokerIDByBank=BrokerIDByBank
        self.BankSerial=BankSerial
        self.BankBranchID=BankBranchID
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.UserID=UserID
        self.BankID=BankID
        self.TID=TID
        self.TradeTime=TradeTime
        self.Message=Message
        self.PlateSerial=PlateSerial
        self.RequestID=RequestID
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstallID', 'TradeDate', 'TradeCode', 'LastFragment', 'BrokerBranchID', 'BrokerIDByBank', 'BankSerial', 'BankBranchID', 'OperNo', 'TradingDay', 'SessionID', 'BrokerID', 'DeviceID', 'UserID', 'BankID', 'TID', 'TradeTime', 'Message', 'PlateSerial', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstallID', u'安装编号'),('TradeDate', u'交易日期'),('TradeCode', u'业务功能码'),('LastFragment', u'最后分片标志'),('BrokerBranchID', u'期商分支机构代码'),('BrokerIDByBank', u'期货公司银行编码'),('BankSerial', u'银行流水号'),('BankBranchID', u'银行分支机构代码'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('UserID', u'用户标识'),('BankID', u'银行代码'),('TID', u'交易ID'),('TradeTime', u'交易时间'),('Message', u'交易核心给银期报盘的消息'),('PlateSerial', u'银期平台消息流水号'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspTransferField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", InstallID=0, CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", Password="", BankPwdFlag='0', ErrorID=0, RequestID=0, CustType='0', IdentifiedCardNo="", FeePayFlag='0', BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", TransferStatus='0', IdCardType='0', PlateSerial=0, FutureFetchAmount=0, TradeDate="", CurrencyID="", BrokerFee=0, BankAccType='1', LastFragment='0', FutureSerial=0, ErrorMsg="", BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', Message="", CustFee=0, TradeAmount=0, Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.Password=Password
        self.BankPwdFlag=BankPwdFlag
        self.ErrorID=ErrorID
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.FeePayFlag=FeePayFlag
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TransferStatus=TransferStatus
        self.IdCardType=IdCardType
        self.PlateSerial=PlateSerial
        self.FutureFetchAmount=FutureFetchAmount
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BrokerFee=BrokerFee
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.ErrorMsg=ErrorMsg
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.Message=Message
        self.CustFee=CustFee
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'TransferStatus': {"'1'": u'\u88ab\u51b2\u6b63', "'0'": u'\u6b63\u5e38'}, 'FeePayFlag': {"'1'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u8d39\u7528', "'2'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u53d1\u8d77\u7684\u8d39\u7528\uff0c\u53d7\u76ca\u65b9\u652f\u4ed8\u63a5\u53d7\u7684\u8d39\u7528', "'0'": u'\u7531\u53d7\u76ca\u65b9\u652f\u4ed8\u8d39\u7528'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'InstallID', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'Password', 'BankPwdFlag', 'ErrorID', 'RequestID', 'CustType', 'IdentifiedCardNo', 'FeePayFlag', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'TransferStatus', 'IdCardType', 'PlateSerial', 'FutureFetchAmount', 'TradeDate', 'CurrencyID', 'BrokerFee', 'BankAccType', 'LastFragment', 'FutureSerial', 'ErrorMsg', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'Message', 'CustFee', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('Password', u'期货密码'),('BankPwdFlag', u'银行密码标志'),('ErrorID', u'错误代码'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('FeePayFlag', u'费用支付标志'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TransferStatus', u'转账交易状态'),('IdCardType', u'证件类型'),('PlateSerial', u'银期平台消息流水号'),('FutureFetchAmount', u'期货可取金额'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BrokerFee', u'应收期货公司费用'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('Message', u'发送方给接收方的消息'),('CustFee', u'应收客户费用'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'FeePayFlag', 'TransferStatus', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcPartBrokerField:
    def __init__(self, ExchangeID="", BrokerID="", ParticipantID="", IsActive=0):
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.ParticipantID=ParticipantID
        self.IsActive=IsActive
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'BrokerID', 'ParticipantID', 'IsActive']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('ParticipantID', u'会员代码'),('IsActive', u'是否活跃')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTraderField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=ExchangeID
        self.TraderID=TraderID
        self.ParticipantID=ParticipantID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferQryBankRspField:
    def __init__(self, FutureAccount="", RetCode="", CurrencyCode="", TradeAmt=0, UseAmt=0, RetInfo="", FetchAmt=0):
        self.FutureAccount=FutureAccount
        self.RetCode=RetCode
        self.CurrencyCode=CurrencyCode
        self.TradeAmt=TradeAmt
        self.UseAmt=UseAmt
        self.RetInfo=RetInfo
        self.FetchAmt=FetchAmt
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'CurrencyCode', 'TradeAmt', 'UseAmt', 'RetInfo', 'FetchAmt']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('CurrencyCode', u'币种'),('TradeAmt', u'银行余额'),('UseAmt', u'银行可用余额'),('RetInfo', u'响应信息'),('FetchAmt', u'银行可取余额')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeOrderActionField:
    def __init__(self, ActionDate="", ExchangeID="", ActionTime="", ParticipantID="", OrderLocalID="", BranchID="", BusinessUnit="", TraderID="", UserID="", VolumeChange=0, ActionLocalID="", InstallID=0, LimitPrice=0, ActionFlag='0', ClientID="", OrderActionStatus='a'):
        self.ActionDate=ActionDate
        self.ExchangeID=ExchangeID
        self.ActionTime=ActionTime
        self.ParticipantID=ParticipantID
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.TraderID=TraderID
        self.UserID=UserID
        self.VolumeChange=VolumeChange
        self.ActionLocalID=ActionLocalID
        self.InstallID=InstallID
        self.LimitPrice=LimitPrice
        self.ActionFlag=ActionFlag
        self.ClientID=ClientID
        self.OrderActionStatus=OrderActionStatus
        self.vcmap={'OrderActionStatus': {"'a'": u'\u5df2\u7ecf\u63d0\u4ea4', "'b'": u'\u5df2\u7ecf\u63a5\u53d7', "'c'": u'\u5df2\u7ecf\u88ab\u62d2\u7edd'}, 'ActionFlag': {"'0'": u'\u5220\u9664', "'3'": u'\u4fee\u6539'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ActionDate', 'ExchangeID', 'ActionTime', 'ParticipantID', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'TraderID', 'UserID', 'VolumeChange', 'ActionLocalID', 'InstallID', 'LimitPrice', 'ActionFlag', 'ClientID', 'OrderActionStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ActionDate', u'操作日期'),('ExchangeID', u'交易所代码'),('ActionTime', u'操作时间'),('ParticipantID', u'会员代码'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('VolumeChange', u'数量变化'),('ActionLocalID', u'操作本地编号'),('InstallID', u'安装编号'),('LimitPrice', u'价格'),('ActionFlag', u'操作标志'),('ClientID', u'客户代码'),('OrderActionStatus', u'报单操作状态')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcNotifyQueryAccountField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", InstallID=0, CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", Password="", BankPwdFlag='0', ErrorID=0, RequestID=0, CustType='0', IdentifiedCardNo="", BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", BankUseAmount=0, IdCardType='0', PlateSerial=0, TradeDate="", CurrencyID="", ErrorMsg="", BankAccType='1', LastFragment='0', FutureSerial=0, BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', Digest="", BankFetchAmount=0):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.Password=Password
        self.BankPwdFlag=BankPwdFlag
        self.ErrorID=ErrorID
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.BankUseAmount=BankUseAmount
        self.IdCardType=IdCardType
        self.PlateSerial=PlateSerial
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.ErrorMsg=ErrorMsg
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.Digest=Digest
        self.BankFetchAmount=BankFetchAmount
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'InstallID', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'Password', 'BankPwdFlag', 'ErrorID', 'RequestID', 'CustType', 'IdentifiedCardNo', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'BankUseAmount', 'IdCardType', 'PlateSerial', 'TradeDate', 'CurrencyID', 'ErrorMsg', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'Digest', 'BankFetchAmount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('Password', u'期货密码'),('BankPwdFlag', u'银行密码标志'),('ErrorID', u'错误代码'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('BankUseAmount', u'银行可用金额'),('IdCardType', u'证件类型'),('PlateSerial', u'银期平台消息流水号'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('Digest', u'摘要'),('BankFetchAmount', u'银行可取金额')]])
    def getval(self, n):
        if n in ['VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspQueryAccountField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", TradeTime="", VerifyCertNoFlag='0', TID=0, AccountID="", BankAccount="", InstallID=0, CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", Password="", BankPwdFlag='0', RequestID=0, CustType='0', IdentifiedCardNo="", BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", BankUseAmount=0, IdCardType='0', PlateSerial=0, TradeDate="", CurrencyID="", BankAccType='1', LastFragment='0', FutureSerial=0, BankSecuAccType='1', BrokerIDByBank="", SecuPwdFlag='0', Digest="", BankFetchAmount=0):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.Password=Password
        self.BankPwdFlag=BankPwdFlag
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.BankUseAmount=BankUseAmount
        self.IdCardType=IdCardType
        self.PlateSerial=PlateSerial
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.SecuPwdFlag=SecuPwdFlag
        self.Digest=Digest
        self.BankFetchAmount=BankFetchAmount
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'AccountID', 'BankAccount', 'InstallID', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'Password', 'BankPwdFlag', 'RequestID', 'CustType', 'IdentifiedCardNo', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'BankUseAmount', 'IdCardType', 'PlateSerial', 'TradeDate', 'CurrencyID', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankSecuAccType', 'BrokerIDByBank', 'SecuPwdFlag', 'Digest', 'BankFetchAmount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('Password', u'期货密码'),('BankPwdFlag', u'银行密码标志'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('BankUseAmount', u'银行可用金额'),('IdCardType', u'证件类型'),('PlateSerial', u'银期平台消息流水号'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('SecuPwdFlag', u'期货资金密码核对标志'),('Digest', u'摘要'),('BankFetchAmount', u'银行可取金额')]])
    def getval(self, n):
        if n in ['VerifyCertNoFlag', 'BankPwdFlag', 'CustType', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType', 'SecuPwdFlag']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcLoadSettlementInfoField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingAccountPasswordUpdateV1Field:
    def __init__(self, InvestorID="", NewPassword="", OldPassword="", BrokerID=""):
        self.InvestorID=InvestorID
        self.NewPassword=NewPassword
        self.OldPassword=OldPassword
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'NewPassword', 'OldPassword', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('NewPassword', u'新的口令'),('OldPassword', u'原来的口令'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspRepealField:
    def __init__(self, BrokerBranchID="", UserID="", BankPassWord="", BankRepealFlag='0', RepealedTimes=0, TradeTime="", VerifyCertNoFlag='0', TID=0, FutureRepealSerial=0, AccountID="", BankAccount="", InstallID=0, SecuPwdFlag='0', CustomerName="", TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, BankPwdFlag='0', ErrorID=0, RequestID=0, CustType='0', IdentifiedCardNo="", FeePayFlag='0', BankSerial="", OperNo="", TradingDay="", BankSecuAcc="", BrokerID="", DeviceID="", TransferStatus='0', BrokerRepealFlag='0', IdCardType='0', Password="", FutureFetchAmount=0, TradeDate="", CurrencyID="", BrokerFee=0, BankAccType='1', LastFragment='0', FutureSerial=0, BankRepealSerial="", ErrorMsg="", RepealTimeInterval=0, BankSecuAccType='1', BrokerIDByBank="", PlateRepealSerial=0, Message="", CustFee=0, TradeAmount=0, Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.BankPassWord=BankPassWord
        self.BankRepealFlag=BankRepealFlag
        self.RepealedTimes=RepealedTimes
        self.TradeTime=TradeTime
        self.VerifyCertNoFlag=VerifyCertNoFlag
        self.TID=TID
        self.FutureRepealSerial=FutureRepealSerial
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.InstallID=InstallID
        self.SecuPwdFlag=SecuPwdFlag
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.BankPwdFlag=BankPwdFlag
        self.ErrorID=ErrorID
        self.RequestID=RequestID
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.FeePayFlag=FeePayFlag
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BankSecuAcc=BankSecuAcc
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TransferStatus=TransferStatus
        self.BrokerRepealFlag=BrokerRepealFlag
        self.IdCardType=IdCardType
        self.Password=Password
        self.FutureFetchAmount=FutureFetchAmount
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.BrokerFee=BrokerFee
        self.BankAccType=BankAccType
        self.LastFragment=LastFragment
        self.FutureSerial=FutureSerial
        self.BankRepealSerial=BankRepealSerial
        self.ErrorMsg=ErrorMsg
        self.RepealTimeInterval=RepealTimeInterval
        self.BankSecuAccType=BankSecuAccType
        self.BrokerIDByBank=BrokerIDByBank
        self.PlateRepealSerial=PlateRepealSerial
        self.Message=Message
        self.CustFee=CustFee
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'BankAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'BankPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'BankRepealFlag': {"'1'": u'\u94f6\u884c\u5f85\u81ea\u52a8\u51b2\u6b63', "'2'": u'\u94f6\u884c\u5df2\u81ea\u52a8\u51b2\u6b63', "'0'": u'\u94f6\u884c\u65e0\u9700\u81ea\u52a8\u51b2\u6b63'}, 'SecuPwdFlag': {"'1'": u'\u660e\u6587\u6838\u5bf9', "'2'": u'\u5bc6\u6587\u6838\u5bf9', "'0'": u'\u4e0d\u6838\u5bf9'}, 'VerifyCertNoFlag': {"'1'": u'\u5426', "'0'": u'\u662f'}, 'BrokerRepealFlag': {"'1'": u'\u671f\u5546\u5f85\u81ea\u52a8\u51b2\u6b63', "'2'": u'\u671f\u5546\u5df2\u81ea\u52a8\u51b2\u6b63', "'0'": u'\u671f\u5546\u65e0\u9700\u81ea\u52a8\u51b2\u6b63'}, 'TransferStatus': {"'1'": u'\u88ab\u51b2\u6b63', "'0'": u'\u6b63\u5e38'}, 'FeePayFlag': {"'1'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u8d39\u7528', "'2'": u'\u7531\u53d1\u9001\u65b9\u652f\u4ed8\u53d1\u8d77\u7684\u8d39\u7528\uff0c\u53d7\u76ca\u65b9\u652f\u4ed8\u63a5\u53d7\u7684\u8d39\u7528', "'0'": u'\u7531\u53d7\u76ca\u65b9\u652f\u4ed8\u8d39\u7528'}, 'BankSecuAccType': {"'1'": u'\u94f6\u884c\u5b58\u6298', "'2'": u'\u50a8\u84c4\u5361', "'3'": u'\u4fe1\u7528\u5361'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'BankPassWord', 'BankRepealFlag', 'RepealedTimes', 'TradeTime', 'VerifyCertNoFlag', 'TID', 'FutureRepealSerial', 'AccountID', 'BankAccount', 'InstallID', 'SecuPwdFlag', 'CustomerName', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'BankPwdFlag', 'ErrorID', 'RequestID', 'CustType', 'IdentifiedCardNo', 'FeePayFlag', 'BankSerial', 'OperNo', 'TradingDay', 'BankSecuAcc', 'BrokerID', 'DeviceID', 'TransferStatus', 'BrokerRepealFlag', 'IdCardType', 'Password', 'FutureFetchAmount', 'TradeDate', 'CurrencyID', 'BrokerFee', 'BankAccType', 'LastFragment', 'FutureSerial', 'BankRepealSerial', 'ErrorMsg', 'RepealTimeInterval', 'BankSecuAccType', 'BrokerIDByBank', 'PlateRepealSerial', 'Message', 'CustFee', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('BankPassWord', u'银行密码'),('BankRepealFlag', u'银行冲正标志'),('RepealedTimes', u'已经冲正次数'),('TradeTime', u'交易时间'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('TID', u'交易ID'),('FutureRepealSerial', u'被冲正期货流水号'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('BankPwdFlag', u'银行密码标志'),('ErrorID', u'错误代码'),('RequestID', u'请求编号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('FeePayFlag', u'费用支付标志'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BankSecuAcc', u'期货单位帐号'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TransferStatus', u'转账交易状态'),('BrokerRepealFlag', u'期商冲正标志'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('FutureFetchAmount', u'期货可取金额'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('BrokerFee', u'应收期货公司费用'),('BankAccType', u'银行帐号类型'),('LastFragment', u'最后分片标志'),('FutureSerial', u'期货公司流水号'),('BankRepealSerial', u'被冲正银行流水号'),('ErrorMsg', u'错误信息'),('RepealTimeInterval', u'冲正时间间隔'),('BankSecuAccType', u'期货单位帐号类型'),('BrokerIDByBank', u'期货公司银行编码'),('PlateRepealSerial', u'被冲正平台流水号'),('Message', u'发送方给接收方的消息'),('CustFee', u'应收客户费用'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['BankRepealFlag', 'VerifyCertNoFlag', 'SecuPwdFlag', 'BankPwdFlag', 'CustType', 'FeePayFlag', 'TransferStatus', 'BrokerRepealFlag', 'IdCardType', 'BankAccType', 'LastFragment', 'BankSecuAccType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryParkedOrderActionField:
    def __init__(self, InstrumentID="", InvestorID="", ExchangeID="", BrokerID=""):
        self.InstrumentID=InstrumentID
        self.InvestorID=InvestorID
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'ExchangeID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcDepositResultInformField:
    def __init__(self, ReturnCode="", DepositSeqNo="", InvestorID="", BrokerID="", Deposit=0, DescrInfoForReturnCode="", RequestID=0):
        self.ReturnCode=ReturnCode
        self.DepositSeqNo=DepositSeqNo
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.Deposit=Deposit
        self.DescrInfoForReturnCode=DescrInfoForReturnCode
        self.RequestID=RequestID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ReturnCode', 'DepositSeqNo', 'InvestorID', 'BrokerID', 'Deposit', 'DescrInfoForReturnCode', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ReturnCode', u'返回代码'),('DepositSeqNo', u'出入金流水号，该流水号为银期报盘返回的流水号'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('Deposit', u'入金金额'),('DescrInfoForReturnCode', u'返回码描述'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryProductField:
    def __init__(self, ExchangeID="", ProductID=""):
        self.ExchangeID=ExchangeID
        self.ProductID=ProductID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryExchangeOrderField:
    def __init__(self, ExchangeInstID="", TraderID="", ExchangeID="", ParticipantID="", ClientID=""):
        self.ExchangeInstID=ExchangeInstID
        self.TraderID=TraderID
        self.ExchangeID=ExchangeID
        self.ParticipantID=ParticipantID
        self.ClientID=ClientID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeInstID', 'TraderID', 'ExchangeID', 'ParticipantID', 'ClientID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeInstID', u'合约在交易所的代码'),('TraderID', u'交易所交易员代码'),('ExchangeID', u'交易所代码'),('ParticipantID', u'会员代码'),('ClientID', u'客户代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqAuthenticateField:
    def __init__(self, UserID="", AuthCode="", BrokerID="", UserProductInfo=""):
        self.UserID=UserID
        self.AuthCode=AuthCode
        self.BrokerID=BrokerID
        self.UserProductInfo=UserProductInfo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'AuthCode', 'BrokerID', 'UserProductInfo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('AuthCode', u'认证码'),('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryExchangeSequenceField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=ExchangeID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcParkedOrderField:
    def __init__(self, ContingentCondition='1', CombOffsetFlag="", UserID="", LimitPrice="", UserForceClose=0, Status='1', Direction='0', UserType='0', VolumeTotalOriginal=0, OrderPriceType='1', TimeCondition='1', IsAutoSuspend=0, StopPrice=0, InstrumentID="", ExchangeID="", MinVolume=0, ForceCloseReason='0', ErrorID=0, ParkedOrderID="", BrokerID="", CombHedgeFlag="", GTDDate="", BusinessUnit="", ErrorMsg="", OrderRef="", InvestorID="", VolumeCondition='1', RequestID=0):
        self.ContingentCondition=ContingentCondition
        self.CombOffsetFlag=CombOffsetFlag
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.UserForceClose=UserForceClose
        self.Status=Status
        self.Direction=Direction
        self.UserType=UserType
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.OrderPriceType=OrderPriceType
        self.TimeCondition=TimeCondition
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.ForceCloseReason=ForceCloseReason
        self.ErrorID=ErrorID
        self.ParkedOrderID=ParkedOrderID
        self.BrokerID=BrokerID
        self.CombHedgeFlag=CombHedgeFlag
        self.GTDDate=GTDDate
        self.BusinessUnit=BusinessUnit
        self.ErrorMsg=ErrorMsg
        self.OrderRef=OrderRef
        self.InvestorID=InvestorID
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.vcmap={'Status': {"'1'": u'\u672a\u53d1\u9001', "'2'": u'\u5df2\u53d1\u9001', "'3'": u'\u5df2\u5220\u9664'}, 'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'UserType': {"'1'": u'\u64cd\u4f5c\u5458', "'2'": u'\u7ba1\u7406\u5458', "'0'": u'\u6295\u8d44\u8005'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'CombOffsetFlag', 'UserID', 'LimitPrice', 'UserForceClose', 'Status', 'Direction', 'UserType', 'VolumeTotalOriginal', 'OrderPriceType', 'TimeCondition', 'IsAutoSuspend', 'StopPrice', 'InstrumentID', 'ExchangeID', 'MinVolume', 'ForceCloseReason', 'ErrorID', 'ParkedOrderID', 'BrokerID', 'CombHedgeFlag', 'GTDDate', 'BusinessUnit', 'ErrorMsg', 'OrderRef', 'InvestorID', 'VolumeCondition', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('CombOffsetFlag', u'组合开平标志'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('UserForceClose', u'用户强评标志'),('Status', u'预埋单状态'),('Direction', u'买卖方向'),('UserType', u'用户类型'),('VolumeTotalOriginal', u'数量'),('OrderPriceType', u'报单价格条件'),('TimeCondition', u'有效期类型'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('ErrorID', u'错误代码'),('ParkedOrderID', u'预埋报单编号'),('BrokerID', u'经纪公司代码'),('CombHedgeFlag', u'组合投机套保标志'),('GTDDate', u'GTD日期'),('BusinessUnit', u'业务单元'),('ErrorMsg', u'错误信息'),('OrderRef', u'报单引用'),('InvestorID', u'投资者代码'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Status', 'Direction', 'UserType', 'OrderPriceType', 'TimeCondition', 'ForceCloseReason', 'VolumeCondition']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataAveragePriceField:
    def __init__(self, AveragePrice=0):
        self.AveragePrice=AveragePrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AveragePrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('AveragePrice', u'当日均价')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataBid23Field:
    def __init__(self, BidVolume3=0, BidVolume2=0, BidPrice3=0, BidPrice2=0):
        self.BidVolume3=BidVolume3
        self.BidVolume2=BidVolume2
        self.BidPrice3=BidPrice3
        self.BidPrice2=BidPrice2
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BidVolume3', 'BidVolume2', 'BidPrice3', 'BidPrice2']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BidVolume3', u'申买量三'),('BidVolume2', u'申买量二'),('BidPrice3', u'申买价三'),('BidPrice2', u'申买价二')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingNoticeInfoField:
    def __init__(self, SequenceSeries=0, SequenceNo=0, FieldContent="", InvestorID="", BrokerID="", SendTime=""):
        self.SequenceSeries=SequenceSeries
        self.SequenceNo=SequenceNo
        self.FieldContent=FieldContent
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.SendTime=SendTime
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceSeries', 'SequenceNo', 'FieldContent', 'InvestorID', 'BrokerID', 'SendTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SequenceSeries', u'序列系列号'),('SequenceNo', u'序列号'),('FieldContent', u'消息正文'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('SendTime', u'发送时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeOrderActionErrorField:
    def __init__(self, ExchangeID="", InstallID=0, OrderLocalID="", ErrorMsg="", TraderID="", ActionLocalID="", OrderSysID="", ErrorID=0):
        self.ExchangeID=ExchangeID
        self.InstallID=InstallID
        self.OrderLocalID=OrderLocalID
        self.ErrorMsg=ErrorMsg
        self.TraderID=TraderID
        self.ActionLocalID=ActionLocalID
        self.OrderSysID=OrderSysID
        self.ErrorID=ErrorID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'InstallID', 'OrderLocalID', 'ErrorMsg', 'TraderID', 'ActionLocalID', 'OrderSysID', 'ErrorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('InstallID', u'安装编号'),('OrderLocalID', u'本地报单编号'),('ErrorMsg', u'错误信息'),('TraderID', u'交易所交易员代码'),('ActionLocalID', u'操作本地编号'),('OrderSysID', u'报单编号'),('ErrorID', u'错误代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTradingAccountPasswordUpdateField:
    def __init__(self, NewPassword="", OldPassword="", BrokerID="", AccountID=""):
        self.NewPassword=NewPassword
        self.OldPassword=OldPassword
        self.BrokerID=BrokerID
        self.AccountID=AccountID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['NewPassword', 'OldPassword', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('NewPassword', u'新的口令'),('OldPassword', u'原来的口令'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSettlementRefField:
    def __init__(self, TradingDay="", SettlementID=0):
        self.TradingDay=TradingDay
        self.SettlementID=SettlementID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'SettlementID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradingDay', u'交易日'),('SettlementID', u'结算编号')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataUpdateTimeField:
    def __init__(self, InstrumentID="", UpdateTime="", UpdateMillisec=0):
        self.InstrumentID=InstrumentID
        self.UpdateTime=UpdateTime
        self.UpdateMillisec=UpdateMillisec
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'UpdateTime', 'UpdateMillisec']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('UpdateTime', u'最后修改时间'),('UpdateMillisec', u'最后修改毫秒')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTraderOfferField:
    def __init__(self, BranchID="", StartDate="", ExchangeID="", InstallID=0, LastReportDate="", ParticipantID="", OrderLocalID="", LastReportTime="", TraderID="", ConnectTime="", TraderConnectStatus='1', TradingDay="", ConnectRequestTime="", StartTime="", ConnectRequestDate="", BrokerID="", Password="", ConnectDate=""):
        self.BranchID=BranchID
        self.StartDate=StartDate
        self.ExchangeID=ExchangeID
        self.InstallID=InstallID
        self.LastReportDate=LastReportDate
        self.ParticipantID=ParticipantID
        self.OrderLocalID=OrderLocalID
        self.LastReportTime=LastReportTime
        self.TraderID=TraderID
        self.ConnectTime=ConnectTime
        self.TraderConnectStatus=TraderConnectStatus
        self.TradingDay=TradingDay
        self.ConnectRequestTime=ConnectRequestTime
        self.StartTime=StartTime
        self.ConnectRequestDate=ConnectRequestDate
        self.BrokerID=BrokerID
        self.Password=Password
        self.ConnectDate=ConnectDate
        self.vcmap={'TraderConnectStatus': {"'1'": u'\u6ca1\u6709\u4efb\u4f55\u8fde\u63a5', "'2'": u'\u5df2\u7ecf\u8fde\u63a5', "'3'": u'\u5df2\u7ecf\u53d1\u51fa\u5408\u7ea6\u67e5\u8be2\u8bf7\u6c42', "'4'": u'\u8ba2\u9605\u79c1\u6709\u6d41'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BranchID', 'StartDate', 'ExchangeID', 'InstallID', 'LastReportDate', 'ParticipantID', 'OrderLocalID', 'LastReportTime', 'TraderID', 'ConnectTime', 'TraderConnectStatus', 'TradingDay', 'ConnectRequestTime', 'StartTime', 'ConnectRequestDate', 'BrokerID', 'Password', 'ConnectDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BranchID', u'营业部编号'),('StartDate', u'启动日期'),('ExchangeID', u'交易所代码'),('InstallID', u'安装编号'),('LastReportDate', u'上次报告日期'),('ParticipantID', u'会员代码'),('OrderLocalID', u'本地报单编号'),('LastReportTime', u'上次报告时间'),('TraderID', u'交易所交易员代码'),('ConnectTime', u'完成连接时间'),('TraderConnectStatus', u'交易所交易员连接状态'),('TradingDay', u'交易日'),('ConnectRequestTime', u'发出连接请求的时间'),('StartTime', u'启动时间'),('ConnectRequestDate', u'发出连接请求的日期'),('BrokerID', u'经纪公司代码'),('Password', u'密码'),('ConnectDate', u'完成连接日期')]])
    def getval(self, n):
        if n in ['TraderConnectStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspInfoField:
    def __init__(self, ErrorMsg="", ErrorID=0):
        self.ErrorMsg=ErrorMsg
        self.ErrorID=ErrorID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ErrorMsg', 'ErrorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ErrorMsg', u'错误信息'),('ErrorID', u'错误代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeSequenceField:
    def __init__(self, ExchangeID="", SequenceNo=0, MarketStatus='0'):
        self.ExchangeID=ExchangeID
        self.SequenceNo=SequenceNo
        self.MarketStatus=MarketStatus
        self.vcmap={'MarketStatus': {"'5'": u'\u96c6\u5408\u7ade\u4ef7\u64ae\u5408', "'4'": u'\u96c6\u5408\u7ade\u4ef7\u4ef7\u683c\u5e73\u8861', "'1'": u'\u975e\u4ea4\u6613', "'0'": u'\u5f00\u76d8\u524d', "'6'": u'\u6536\u76d8', "'2'": u'\u8fde\u7eed\u4ea4\u6613', "'3'": u'\u96c6\u5408\u7ade\u4ef7\u62a5\u5355'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'SequenceNo', 'MarketStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('SequenceNo', u'序号'),('MarketStatus', u'合约交易状态')]])
    def getval(self, n):
        if n in ['MarketStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBondInterestField:
    def __init__(self, InstrumentID="", ExchangeID=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcRspUserLoginField:
    def __init__(self, CZCETime="", SHFETime="", MaxOrderRef="", UserID="", TradingDay="", SessionID=0, SystemName="", FrontID=0, FFEXTime="", BrokerID="", DCETime="", LoginTime=""):
        self.CZCETime=CZCETime
        self.SHFETime=SHFETime
        self.MaxOrderRef=MaxOrderRef
        self.UserID=UserID
        self.TradingDay=TradingDay
        self.SessionID=SessionID
        self.SystemName=SystemName
        self.FrontID=FrontID
        self.FFEXTime=FFEXTime
        self.BrokerID=BrokerID
        self.DCETime=DCETime
        self.LoginTime=LoginTime
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CZCETime', 'SHFETime', 'MaxOrderRef', 'UserID', 'TradingDay', 'SessionID', 'SystemName', 'FrontID', 'FFEXTime', 'BrokerID', 'DCETime', 'LoginTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('CZCETime', u'郑商所时间'),('SHFETime', u'上期所时间'),('MaxOrderRef', u'最大报单引用'),('UserID', u'用户代码'),('TradingDay', u'交易日'),('SessionID', u'会话编号'),('SystemName', u'交易系统名称'),('FrontID', u'前置编号'),('FFEXTime', u'中金所时间'),('BrokerID', u'经纪公司代码'),('DCETime', u'大商所时间'),('LoginTime', u'登录成功时间')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerDepositField:
    def __init__(self, Available=0, ExchangeID="", ParticipantID="", FrozenMargin=0, PreBalance=0, CurrMargin=0, TradingDay="", BrokerID="", Deposit=0, Withdraw=0, CloseProfit=0, Balance=0, Reserve=0):
        self.Available=Available
        self.ExchangeID=ExchangeID
        self.ParticipantID=ParticipantID
        self.FrozenMargin=FrozenMargin
        self.PreBalance=PreBalance
        self.CurrMargin=CurrMargin
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.Deposit=Deposit
        self.Withdraw=Withdraw
        self.CloseProfit=CloseProfit
        self.Balance=Balance
        self.Reserve=Reserve
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Available', 'ExchangeID', 'ParticipantID', 'FrozenMargin', 'PreBalance', 'CurrMargin', 'TradingDay', 'BrokerID', 'Deposit', 'Withdraw', 'CloseProfit', 'Balance', 'Reserve']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('Available', u'可提资金'),('ExchangeID', u'交易所代码'),('ParticipantID', u'会员代码'),('FrozenMargin', u'冻结的保证金'),('PreBalance', u'上次结算准备金'),('CurrMargin', u'当前保证金总额'),('TradingDay', u'交易日期'),('BrokerID', u'经纪公司代码'),('Deposit', u'入金金额'),('Withdraw', u'出金金额'),('CloseProfit', u'平仓盈亏'),('Balance', u'期货结算准备金'),('Reserve', u'基本准备金')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryCombinationLegField:
    def __init__(self, LegInstrumentID="", LegID=0, CombInstrumentID=""):
        self.LegInstrumentID=LegInstrumentID
        self.LegID=LegID
        self.CombInstrumentID=CombInstrumentID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LegInstrumentID', 'LegID', 'CombInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('LegInstrumentID', u'单腿合约代码'),('LegID', u'单腿编号'),('CombInstrumentID', u'组合合约代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcReqQueryTradeResultBySerialField:
    def __init__(self, BrokerBranchID="", BankPassWord="", TradeTime="", AccountID="", BankAccount="", CustomerName="", TradeCode="", BankBranchID="", RefrenceIssure="", SessionID=0, BankID="", PlateSerial=0, CustType='0', IdentifiedCardNo="", BankSerial="", TradingDay="", BrokerID="", RefrenceIssureType='0', IdCardType='0', Password="", Reference=0, TradeDate="", CurrencyID="", LastFragment='0', TradeAmount=0, Digest=""):
        self.BrokerBranchID=BrokerBranchID
        self.BankPassWord=BankPassWord
        self.TradeTime=TradeTime
        self.AccountID=AccountID
        self.BankAccount=BankAccount
        self.CustomerName=CustomerName
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.RefrenceIssure=RefrenceIssure
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.BankSerial=BankSerial
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.RefrenceIssureType=RefrenceIssureType
        self.IdCardType=IdCardType
        self.Password=Password
        self.Reference=Reference
        self.TradeDate=TradeDate
        self.CurrencyID=CurrencyID
        self.LastFragment=LastFragment
        self.TradeAmount=TradeAmount
        self.Digest=Digest
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'RefrenceIssureType': {"'1'": u'\u671f\u5546', "'2'": u'\u5238\u5546', "'0'": u'\u94f6\u884c'}, 'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'BankPassWord', 'TradeTime', 'AccountID', 'BankAccount', 'CustomerName', 'TradeCode', 'BankBranchID', 'RefrenceIssure', 'SessionID', 'BankID', 'PlateSerial', 'CustType', 'IdentifiedCardNo', 'BankSerial', 'TradingDay', 'BrokerID', 'RefrenceIssureType', 'IdCardType', 'Password', 'Reference', 'TradeDate', 'CurrencyID', 'LastFragment', 'TradeAmount', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('BankPassWord', u'银行密码'),('TradeTime', u'交易时间'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('CustomerName', u'客户姓名'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('RefrenceIssure', u'本流水号发布者机构编码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('BankSerial', u'银行流水号'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('RefrenceIssureType', u'本流水号发布者的机构类型'),('IdCardType', u'证件类型'),('Password', u'期货密码'),('Reference', u'流水号'),('TradeDate', u'交易日期'),('CurrencyID', u'币种代码'),('LastFragment', u'最后分片标志'),('TradeAmount', u'转帐金额'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['CustType', 'RefrenceIssureType', 'IdCardType', 'LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryBrokerTradingParamsField:
    def __init__(self, InvestorID="", BrokerID=""):
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentField:
    def __init__(self, IsTrading=0, ExpireDate="", PositionDateType='1', OrderCanBeWithdraw=0, PositionType='1', ProductClass='1', MinSellVolume=0, InstrumentName="", RightModelID="", VolumeMultiple=0, DeliveryYear=0, CreateDate="", InstrumentID="", MaxLimitOrderVolume=0, ExchangeID="", MinLimitOrderVolume=0, MaxMarketOrderVolume=0, StartDelivDate="", DeliveryMonth=0, MinBuyVolume=0, PriceTick=0, InstLifePhase='0', ExchangeInstID="", MinMarketOrderVolume=0, EndDelivDate="", OpenDate="", ProductID=""):
        self.IsTrading=IsTrading
        self.ExpireDate=ExpireDate
        self.PositionDateType=PositionDateType
        self.OrderCanBeWithdraw=OrderCanBeWithdraw
        self.PositionType=PositionType
        self.ProductClass=ProductClass
        self.MinSellVolume=MinSellVolume
        self.InstrumentName=InstrumentName
        self.RightModelID=RightModelID
        self.VolumeMultiple=VolumeMultiple
        self.DeliveryYear=DeliveryYear
        self.CreateDate=CreateDate
        self.InstrumentID=InstrumentID
        self.MaxLimitOrderVolume=MaxLimitOrderVolume
        self.ExchangeID=ExchangeID
        self.MinLimitOrderVolume=MinLimitOrderVolume
        self.MaxMarketOrderVolume=MaxMarketOrderVolume
        self.StartDelivDate=StartDelivDate
        self.DeliveryMonth=DeliveryMonth
        self.MinBuyVolume=MinBuyVolume
        self.PriceTick=PriceTick
        self.InstLifePhase=InstLifePhase
        self.ExchangeInstID=ExchangeInstID
        self.MinMarketOrderVolume=MinMarketOrderVolume
        self.EndDelivDate=EndDelivDate
        self.OpenDate=OpenDate
        self.ProductID=ProductID
        self.vcmap={'ProductClass': {"'9'": u'ETF\u7533\u8d4e', "'7'": u'\u8bc1\u5238B\u80a1', "'8'": u'ETF', "'5'": u'\u671f\u8f6c\u73b0', "'4'": u'\u5373\u671f', "'1'": u'\u671f\u8d27', "'6'": u'\u8bc1\u5238A\u80a1', "'2'": u'\u671f\u6743', "'3'": u'\u7ec4\u5408'}, 'PositionDateType': {"'1'": u'\u4f7f\u7528\u5386\u53f2\u6301\u4ed3', "'2'": u'\u4e0d\u4f7f\u7528\u5386\u53f2\u6301\u4ed3'}, 'InstLifePhase': {"'1'": u'\u4e0a\u5e02', "'2'": u'\u505c\u724c', "'0'": u'\u672a\u4e0a\u5e02', "'3'": u'\u5230\u671f'}, 'PositionType': {"'1'": u'\u51c0\u6301\u4ed3', "'2'": u'\u7efc\u5408\u6301\u4ed3'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsTrading', 'ExpireDate', 'PositionDateType', 'OrderCanBeWithdraw', 'PositionType', 'ProductClass', 'MinSellVolume', 'InstrumentName', 'RightModelID', 'VolumeMultiple', 'DeliveryYear', 'CreateDate', 'InstrumentID', 'MaxLimitOrderVolume', 'ExchangeID', 'MinLimitOrderVolume', 'MaxMarketOrderVolume', 'StartDelivDate', 'DeliveryMonth', 'MinBuyVolume', 'PriceTick', 'InstLifePhase', 'ExchangeInstID', 'MinMarketOrderVolume', 'EndDelivDate', 'OpenDate', 'ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('IsTrading', u'当前是否交易'),('ExpireDate', u'到期日'),('PositionDateType', u'持仓日期类型'),('OrderCanBeWithdraw', u'报单能否撤单'),('PositionType', u'持仓类型'),('ProductClass', u'产品类型'),('MinSellVolume', u'最小卖下单单位'),('InstrumentName', u'合约名称'),('RightModelID', u'股票权限模版代码'),('VolumeMultiple', u'合约数量乘数'),('DeliveryYear', u'交割年份'),('CreateDate', u'创建日'),('InstrumentID', u'合约代码'),('MaxLimitOrderVolume', u'限价单最大下单量'),('ExchangeID', u'交易所代码'),('MinLimitOrderVolume', u'限价单最小下单量'),('MaxMarketOrderVolume', u'市价单最大下单量'),('StartDelivDate', u'开始交割日'),('DeliveryMonth', u'交割月'),('MinBuyVolume', u'最小买下单单位'),('PriceTick', u'最小变动价位'),('InstLifePhase', u'合约生命周期状态'),('ExchangeInstID', u'合约在交易所的代码'),('MinMarketOrderVolume', u'市价单最小下单量'),('EndDelivDate', u'结束交割日'),('OpenDate', u'上市日'),('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in ['PositionDateType', 'PositionType', 'ProductClass', 'InstLifePhase']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInvestorPositionField:
    def __init__(self, MarginTradeAmount=0, ShortFrozenAmount=0, TodaySSPosition=0, HedgeFlag='1', PositionProfit=0, PledgeInFrozenPosition=0, TransferFee=0, Commission=0, ShortSellVolume=0, TodayPurRedVolume=0, CashIn=0, PreSettlementPrice=0, CloseAmount=0, PledgeInPosition=0, PosiDirection='1', RepurchasePosition=0, MarginTradeVolume=0, YdPosition=0, MarginTradeFrozenVolume=0, ConversionRate=0, ShortSellFrozenVolume=0, OpenVolume=0, TodayMTPosition=0, CloseVolume=0, ConversionAmount=0, SSStockValue=0, InstrumentID="", PositionDate='1', ExchangeID="", SettlementID=0, MarginTradeFrozenAmount=0, ShortFrozen=0, LongFrozen=0, TodayPosition=0, TradingDay="", PositionCost=0, MarginTradeConversionAmount=0, BrokerID="", FrozenCash=0, OpenAmount=0, OpenCost=0, StampTax=0, Position=0, ExchangeMargin=0, ShortSellFrozenAmount=0, SettlementPrice=0, LongFrozenAmount=0, InvestorID="", ShortSellConversionAmount=0, CloseProfit=0, StockValue=0, ShortSellAmount=0):
        self.MarginTradeAmount=MarginTradeAmount
        self.ShortFrozenAmount=ShortFrozenAmount
        self.TodaySSPosition=TodaySSPosition
        self.HedgeFlag=HedgeFlag
        self.PositionProfit=PositionProfit
        self.PledgeInFrozenPosition=PledgeInFrozenPosition
        self.TransferFee=TransferFee
        self.Commission=Commission
        self.ShortSellVolume=ShortSellVolume
        self.TodayPurRedVolume=TodayPurRedVolume
        self.CashIn=CashIn
        self.PreSettlementPrice=PreSettlementPrice
        self.CloseAmount=CloseAmount
        self.PledgeInPosition=PledgeInPosition
        self.PosiDirection=PosiDirection
        self.RepurchasePosition=RepurchasePosition
        self.MarginTradeVolume=MarginTradeVolume
        self.YdPosition=YdPosition
        self.MarginTradeFrozenVolume=MarginTradeFrozenVolume
        self.ConversionRate=ConversionRate
        self.ShortSellFrozenVolume=ShortSellFrozenVolume
        self.OpenVolume=OpenVolume
        self.TodayMTPosition=TodayMTPosition
        self.CloseVolume=CloseVolume
        self.ConversionAmount=ConversionAmount
        self.SSStockValue=SSStockValue
        self.InstrumentID=InstrumentID
        self.PositionDate=PositionDate
        self.ExchangeID=ExchangeID
        self.SettlementID=SettlementID
        self.MarginTradeFrozenAmount=MarginTradeFrozenAmount
        self.ShortFrozen=ShortFrozen
        self.LongFrozen=LongFrozen
        self.TodayPosition=TodayPosition
        self.TradingDay=TradingDay
        self.PositionCost=PositionCost
        self.MarginTradeConversionAmount=MarginTradeConversionAmount
        self.BrokerID=BrokerID
        self.FrozenCash=FrozenCash
        self.OpenAmount=OpenAmount
        self.OpenCost=OpenCost
        self.StampTax=StampTax
        self.Position=Position
        self.ExchangeMargin=ExchangeMargin
        self.ShortSellFrozenAmount=ShortSellFrozenAmount
        self.SettlementPrice=SettlementPrice
        self.LongFrozenAmount=LongFrozenAmount
        self.InvestorID=InvestorID
        self.ShortSellConversionAmount=ShortSellConversionAmount
        self.CloseProfit=CloseProfit
        self.StockValue=StockValue
        self.ShortSellAmount=ShortSellAmount
        self.vcmap={'PositionDate': {"'1'": u'\u4eca\u65e5\u6301\u4ed3', "'2'": u'\u5386\u53f2\u6301\u4ed3'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'PosiDirection': {"'1'": u'\u51c0', "'2'": u'\u591a\u5934', "'5'": u'\u878d\u5238', "'3'": u'\u7a7a\u5934', "'4'": u'\u878d\u8d44'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MarginTradeAmount', 'ShortFrozenAmount', 'TodaySSPosition', 'HedgeFlag', 'PositionProfit', 'PledgeInFrozenPosition', 'TransferFee', 'Commission', 'ShortSellVolume', 'TodayPurRedVolume', 'CashIn', 'PreSettlementPrice', 'CloseAmount', 'PledgeInPosition', 'PosiDirection', 'RepurchasePosition', 'MarginTradeVolume', 'YdPosition', 'MarginTradeFrozenVolume', 'ConversionRate', 'ShortSellFrozenVolume', 'OpenVolume', 'TodayMTPosition', 'CloseVolume', 'ConversionAmount', 'SSStockValue', 'InstrumentID', 'PositionDate', 'ExchangeID', 'SettlementID', 'MarginTradeFrozenAmount', 'ShortFrozen', 'LongFrozen', 'TodayPosition', 'TradingDay', 'PositionCost', 'MarginTradeConversionAmount', 'BrokerID', 'FrozenCash', 'OpenAmount', 'OpenCost', 'StampTax', 'Position', 'ExchangeMargin', 'ShortSellFrozenAmount', 'SettlementPrice', 'LongFrozenAmount', 'InvestorID', 'ShortSellConversionAmount', 'CloseProfit', 'StockValue', 'ShortSellAmount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MarginTradeAmount', u'融资买入金额'),('ShortFrozenAmount', u'开仓冻结金额'),('TodaySSPosition', u'今日融券持仓'),('HedgeFlag', u'投机套保标志'),('PositionProfit', u'持仓盈亏'),('PledgeInFrozenPosition', u'今日质押入库冻结数量'),('TransferFee', u'过户费'),('Commission', u'手续费'),('ShortSellVolume', u'融券卖出数量'),('TodayPurRedVolume', u'今日申购赎回数量'),('CashIn', u'资金差额'),('PreSettlementPrice', u'上次结算价'),('CloseAmount', u'平仓金额'),('PledgeInPosition', u'质押入库数量'),('PosiDirection', u'持仓多空方向'),('RepurchasePosition', u'正回购使用的标准券数量'),('MarginTradeVolume', u'融资买入出数量'),('YdPosition', u'上日持仓'),('MarginTradeFrozenVolume', u'融资买入冻结数量'),('ConversionRate', u'折算率'),('ShortSellFrozenVolume', u'融券卖出冻结数量'),('OpenVolume', u'开仓量'),('TodayMTPosition', u'今日融资持仓'),('CloseVolume', u'平仓量'),('ConversionAmount', u'折算金额'),('SSStockValue', u'融券总市值'),('InstrumentID', u'合约代码'),('PositionDate', u'持仓日期'),('ExchangeID', u'交易所代码'),('SettlementID', u'结算编号'),('MarginTradeFrozenAmount', u'融资买入冻结金额'),('ShortFrozen', u'空头冻结'),('LongFrozen', u'多头冻结'),('TodayPosition', u'今日持仓'),('TradingDay', u'交易日'),('PositionCost', u'持仓成本'),('MarginTradeConversionAmount', u'融资买入盈亏'),('BrokerID', u'经纪公司代码'),('FrozenCash', u'冻结的资金'),('OpenAmount', u'开仓金额'),('OpenCost', u'开仓成本'),('StampTax', u'印花税'),('Position', u'今日持仓'),('ExchangeMargin', u'交易所保证金'),('ShortSellFrozenAmount', u'融券卖出冻结金额'),('SettlementPrice', u'本次结算价'),('LongFrozenAmount', u'开仓冻结金额'),('InvestorID', u'投资者代码'),('ShortSellConversionAmount', u'融券卖出盈亏'),('CloseProfit', u'平仓盈亏'),('StockValue', u'证券价值'),('ShortSellAmount', u'融券卖出金额')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'PosiDirection', 'PositionDate']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcTransferQryDetailReqField:
    def __init__(self, FutureAccount=""):
        self.FutureAccount=FutureAccount
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentMarginRateAdjustField:
    def __init__(self, InstrumentID="", ShortMarginRatioByMoney=0, LongMarginRatioByMoney=0, IsRelative=0, HedgeFlag='1', InvestorID="", BrokerID="", InvestorRange='1', ShortMarginRatioByVolume=0, LongMarginRatioByVolume=0):
        self.InstrumentID=InstrumentID
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.IsRelative=IsRelative
        self.HedgeFlag=HedgeFlag
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByMoney', 'LongMarginRatioByMoney', 'IsRelative', 'HedgeFlag', 'InvestorID', 'BrokerID', 'InvestorRange', 'ShortMarginRatioByVolume', 'LongMarginRatioByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByMoney', u'空头保证金率'),('LongMarginRatioByMoney', u'多头保证金率'),('IsRelative', u'是否相对交易所收取'),('HedgeFlag', u'投机套保标志'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByVolume', u'多头保证金费')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryContractBankField:
    def __init__(self, BrokerID="", BankBrchID="", BankID=""):
        self.BrokerID=BrokerID
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'BankBrchID', 'BankID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('BankBrchID', u'银行分中心代码'),('BankID', u'银行代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorPositionField:
    def __init__(self, MarginTradeAmount=0, ShortFrozenAmount=0, TodaySSPosition=0, HedgeFlag='1', PositionProfit=0, PledgeInFrozenPosition=0, TransferFee=0, Commission=0, ShortSellVolume=0, TodayPurRedVolume=0, CashIn=0, PreSettlementPrice=0, CloseAmount=0, PledgeInPosition=0, PosiDirection='1', RepurchasePosition=0, MarginTradeVolume=0, YdPosition=0, MarginTradeFrozenVolume=0, ConversionRate=0, ShortSellFrozenVolume=0, OpenVolume=0, TodayMTPosition=0, CloseVolume=0, ConversionAmount=0, SSStockValue=0, InstrumentID="", PositionDate='1', ExchangeID="", SettlementID=0, MarginTradeFrozenAmount=0, ShortFrozen=0, LongFrozen=0, TodayPosition=0, TradingDay="", PositionCost=0, MarginTradeConversionAmount=0, BrokerID="", FrozenCash=0, OpenAmount=0, OpenCost=0, StampTax=0, Position=0, ExchangeMargin=0, ShortSellFrozenAmount=0, SettlementPrice=0, LongFrozenAmount=0, InvestorID="", ShortSellConversionAmount=0, CloseProfit=0, StockValue=0, ShortSellAmount=0):
        self.MarginTradeAmount=MarginTradeAmount
        self.ShortFrozenAmount=ShortFrozenAmount
        self.TodaySSPosition=TodaySSPosition
        self.HedgeFlag=HedgeFlag
        self.PositionProfit=PositionProfit
        self.PledgeInFrozenPosition=PledgeInFrozenPosition
        self.TransferFee=TransferFee
        self.Commission=Commission
        self.ShortSellVolume=ShortSellVolume
        self.TodayPurRedVolume=TodayPurRedVolume
        self.CashIn=CashIn
        self.PreSettlementPrice=PreSettlementPrice
        self.CloseAmount=CloseAmount
        self.PledgeInPosition=PledgeInPosition
        self.PosiDirection=PosiDirection
        self.RepurchasePosition=RepurchasePosition
        self.MarginTradeVolume=MarginTradeVolume
        self.YdPosition=YdPosition
        self.MarginTradeFrozenVolume=MarginTradeFrozenVolume
        self.ConversionRate=ConversionRate
        self.ShortSellFrozenVolume=ShortSellFrozenVolume
        self.OpenVolume=OpenVolume
        self.TodayMTPosition=TodayMTPosition
        self.CloseVolume=CloseVolume
        self.ConversionAmount=ConversionAmount
        self.SSStockValue=SSStockValue
        self.InstrumentID=InstrumentID
        self.PositionDate=PositionDate
        self.ExchangeID=ExchangeID
        self.SettlementID=SettlementID
        self.MarginTradeFrozenAmount=MarginTradeFrozenAmount
        self.ShortFrozen=ShortFrozen
        self.LongFrozen=LongFrozen
        self.TodayPosition=TodayPosition
        self.TradingDay=TradingDay
        self.PositionCost=PositionCost
        self.MarginTradeConversionAmount=MarginTradeConversionAmount
        self.BrokerID=BrokerID
        self.FrozenCash=FrozenCash
        self.OpenAmount=OpenAmount
        self.OpenCost=OpenCost
        self.StampTax=StampTax
        self.Position=Position
        self.ExchangeMargin=ExchangeMargin
        self.ShortSellFrozenAmount=ShortSellFrozenAmount
        self.SettlementPrice=SettlementPrice
        self.LongFrozenAmount=LongFrozenAmount
        self.InvestorID=InvestorID
        self.ShortSellConversionAmount=ShortSellConversionAmount
        self.CloseProfit=CloseProfit
        self.StockValue=StockValue
        self.ShortSellAmount=ShortSellAmount
        self.vcmap={'PositionDate': {"'1'": u'\u4eca\u65e5\u6301\u4ed3', "'2'": u'\u5386\u53f2\u6301\u4ed3'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'PosiDirection': {"'1'": u'\u51c0', "'2'": u'\u591a\u5934', "'5'": u'\u878d\u5238', "'3'": u'\u7a7a\u5934', "'4'": u'\u878d\u8d44'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MarginTradeAmount', 'ShortFrozenAmount', 'TodaySSPosition', 'HedgeFlag', 'PositionProfit', 'PledgeInFrozenPosition', 'TransferFee', 'Commission', 'ShortSellVolume', 'TodayPurRedVolume', 'CashIn', 'PreSettlementPrice', 'CloseAmount', 'PledgeInPosition', 'PosiDirection', 'RepurchasePosition', 'MarginTradeVolume', 'YdPosition', 'MarginTradeFrozenVolume', 'ConversionRate', 'ShortSellFrozenVolume', 'OpenVolume', 'TodayMTPosition', 'CloseVolume', 'ConversionAmount', 'SSStockValue', 'InstrumentID', 'PositionDate', 'ExchangeID', 'SettlementID', 'MarginTradeFrozenAmount', 'ShortFrozen', 'LongFrozen', 'TodayPosition', 'TradingDay', 'PositionCost', 'MarginTradeConversionAmount', 'BrokerID', 'FrozenCash', 'OpenAmount', 'OpenCost', 'StampTax', 'Position', 'ExchangeMargin', 'ShortSellFrozenAmount', 'SettlementPrice', 'LongFrozenAmount', 'InvestorID', 'ShortSellConversionAmount', 'CloseProfit', 'StockValue', 'ShortSellAmount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('MarginTradeAmount', u'融资买入金额'),('ShortFrozenAmount', u'开仓冻结金额'),('TodaySSPosition', u'今日融券持仓'),('HedgeFlag', u'投机套保标志'),('PositionProfit', u'持仓盈亏'),('PledgeInFrozenPosition', u'今日质押入库冻结数量'),('TransferFee', u'过户费'),('Commission', u'手续费'),('ShortSellVolume', u'融券卖出数量'),('TodayPurRedVolume', u'今日申购赎回数量'),('CashIn', u'资金差额'),('PreSettlementPrice', u'上次结算价'),('CloseAmount', u'平仓金额'),('PledgeInPosition', u'质押入库数量'),('PosiDirection', u'持仓多空方向'),('RepurchasePosition', u'正回购使用的标准券数量'),('MarginTradeVolume', u'融资买入出数量'),('YdPosition', u'上日持仓'),('MarginTradeFrozenVolume', u'融资买入冻结数量'),('ConversionRate', u'折算率'),('ShortSellFrozenVolume', u'融券卖出冻结数量'),('OpenVolume', u'开仓量'),('TodayMTPosition', u'今日融资持仓'),('CloseVolume', u'平仓量'),('ConversionAmount', u'折算金额'),('SSStockValue', u'融券总市值'),('InstrumentID', u'合约代码'),('PositionDate', u'持仓日期'),('ExchangeID', u'交易所代码'),('SettlementID', u'结算编号'),('MarginTradeFrozenAmount', u'融资买入冻结金额'),('ShortFrozen', u'空头冻结'),('LongFrozen', u'多头冻结'),('TodayPosition', u'今日持仓'),('TradingDay', u'交易日'),('PositionCost', u'持仓成本'),('MarginTradeConversionAmount', u'融资买入盈亏'),('BrokerID', u'经纪公司代码'),('FrozenCash', u'冻结的资金'),('OpenAmount', u'开仓金额'),('OpenCost', u'开仓成本'),('StampTax', u'印花税'),('Position', u'今日持仓'),('ExchangeMargin', u'交易所保证金'),('ShortSellFrozenAmount', u'融券卖出冻结金额'),('SettlementPrice', u'本次结算价'),('LongFrozenAmount', u'开仓冻结金额'),('InvestorID', u'投资者代码'),('ShortSellConversionAmount', u'融券卖出盈亏'),('CloseProfit', u'平仓盈亏'),('StockValue', u'证券价值'),('ShortSellAmount', u'融券卖出金额')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'PosiDirection', 'PositionDate']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerUserPasswordField:
    def __init__(self, UserID="", Password="", BrokerID=""):
        self.UserID=UserID
        self.Password=Password
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID', 'Password', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('UserID', u'用户代码'),('Password', u'密码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerTradingAlgosField:
    def __init__(self, InstrumentID="", HandlePositionAlgoID='1', ExchangeID="", FindMarginRateAlgoID='1', BrokerID="", HandleTradingAccountAlgoID='1'):
        self.InstrumentID=InstrumentID
        self.HandlePositionAlgoID=HandlePositionAlgoID
        self.ExchangeID=ExchangeID
        self.FindMarginRateAlgoID=FindMarginRateAlgoID
        self.BrokerID=BrokerID
        self.HandleTradingAccountAlgoID=HandleTradingAccountAlgoID
        self.vcmap={'HandlePositionAlgoID': {"'1'": u'\u57fa\u672c', "'2'": u'\u5927\u8fde\u5546\u54c1\u4ea4\u6613\u6240', "'5'": u'\u8bc1\u5238', "'3'": u'\u90d1\u5dde\u5546\u54c1\u4ea4\u6613\u6240', "'4'": u'\u975e\u4ea4\u6613'}, 'HandleTradingAccountAlgoID': {"'1'": u'\u57fa\u672c', "'2'": u'\u5927\u8fde\u5546\u54c1\u4ea4\u6613\u6240', "'3'": u'\u90d1\u5dde\u5546\u54c1\u4ea4\u6613\u6240'}, 'FindMarginRateAlgoID': {"'1'": u'\u57fa\u672c', "'2'": u'\u5927\u8fde\u5546\u54c1\u4ea4\u6613\u6240', "'3'": u'\u90d1\u5dde\u5546\u54c1\u4ea4\u6613\u6240'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'HandlePositionAlgoID', 'ExchangeID', 'FindMarginRateAlgoID', 'BrokerID', 'HandleTradingAccountAlgoID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('HandlePositionAlgoID', u'持仓处理算法编号'),('ExchangeID', u'交易所代码'),('FindMarginRateAlgoID', u'寻找保证金率算法编号'),('BrokerID', u'经纪公司代码'),('HandleTradingAccountAlgoID', u'资金处理算法编号')]])
    def getval(self, n):
        if n in ['HandlePositionAlgoID', 'FindMarginRateAlgoID', 'HandleTradingAccountAlgoID']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInstrumentMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByMoney=0, LongMarginRatioByMoney=0, IsRelative=0, HedgeFlag='1', InvestorID="", BrokerID="", InvestorRange='1', ShortMarginRatioByVolume=0, LongMarginRatioByVolume=0):
        self.InstrumentID=InstrumentID
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.IsRelative=IsRelative
        self.HedgeFlag=HedgeFlag
        self.InvestorID=InvestorID
        self.BrokerID=BrokerID
        self.InvestorRange=InvestorRange
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.vcmap={'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}, 'InvestorRange': {"'1'": u'\u6240\u6709', "'2'": u'\u6295\u8d44\u8005\u7ec4', "'3'": u'\u5355\u4e00\u6295\u8d44\u8005'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByMoney', 'LongMarginRatioByMoney', 'IsRelative', 'HedgeFlag', 'InvestorID', 'BrokerID', 'InvestorRange', 'ShortMarginRatioByVolume', 'LongMarginRatioByVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByMoney', u'空头保证金率'),('LongMarginRatioByMoney', u'多头保证金率'),('IsRelative', u'是否相对交易所收取'),('HedgeFlag', u'投机套保标志'),('InvestorID', u'投资者代码'),('BrokerID', u'经纪公司代码'),('InvestorRange', u'投资者范围'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByVolume', u'多头保证金费')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcVerifyCustInfoField:
    def __init__(self, CustType='0', IdentifiedCardNo="", CustomerName="", IdCardType='0'):
        self.CustType=CustType
        self.IdentifiedCardNo=IdentifiedCardNo
        self.CustomerName=CustomerName
        self.IdCardType=IdCardType
        self.vcmap={'CustType': {"'1'": u'\u673a\u6784\u6237', "'0'": u'\u81ea\u7136\u4eba'}, 'IdCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CustType', 'IdentifiedCardNo', 'CustomerName', 'IdCardType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('CustType', u'客户类型'),('IdentifiedCardNo', u'证件号码'),('CustomerName', u'客户姓名'),('IdCardType', u'证件类型')]])
    def getval(self, n):
        if n in ['CustType', 'IdCardType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInputOrderField:
    def __init__(self, ContingentCondition='1', CombOffsetFlag="", UserID="", LimitPrice="", UserForceClose=0, Direction='0', VolumeTotalOriginal=0, OrderPriceType='1', TimeCondition='1', IsAutoSuspend=0, StopPrice=0, InstrumentID="", ExchangeID="", MinVolume=0, ForceCloseReason='0', BrokerID="", CombHedgeFlag="", GTDDate="", BusinessUnit="", OrderRef="", InvestorID="", VolumeCondition='1', RequestID=0):
        self.ContingentCondition=ContingentCondition
        self.CombOffsetFlag=CombOffsetFlag
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.UserForceClose=UserForceClose
        self.Direction=Direction
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.OrderPriceType=OrderPriceType
        self.TimeCondition=TimeCondition
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.ForceCloseReason=ForceCloseReason
        self.BrokerID=BrokerID
        self.CombHedgeFlag=CombHedgeFlag
        self.GTDDate=GTDDate
        self.BusinessUnit=BusinessUnit
        self.OrderRef=OrderRef
        self.InvestorID=InvestorID
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.vcmap={'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'CombOffsetFlag', 'UserID', 'LimitPrice', 'UserForceClose', 'Direction', 'VolumeTotalOriginal', 'OrderPriceType', 'TimeCondition', 'IsAutoSuspend', 'StopPrice', 'InstrumentID', 'ExchangeID', 'MinVolume', 'ForceCloseReason', 'BrokerID', 'CombHedgeFlag', 'GTDDate', 'BusinessUnit', 'OrderRef', 'InvestorID', 'VolumeCondition', 'RequestID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('CombOffsetFlag', u'组合开平标志'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('UserForceClose', u'用户强评标志'),('Direction', u'买卖方向'),('VolumeTotalOriginal', u'数量'),('OrderPriceType', u'报单价格条件'),('TimeCondition', u'有效期类型'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('BrokerID', u'经纪公司代码'),('CombHedgeFlag', u'组合投机套保标志'),('GTDDate', u'GTD日期'),('BusinessUnit', u'业务单元'),('OrderRef', u'报单引用'),('InvestorID', u'投资者代码'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Direction', 'OrderPriceType', 'TimeCondition', 'ForceCloseReason', 'VolumeCondition']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcErrorConditionalOrderField:
    def __init__(self, ContingentCondition='1', NotifySequence=0, ActiveUserID="", VolumeTraded=0, UserProductInfo="", CombOffsetFlag="", TraderID="", UserID="", LimitPrice="", UserForceClose=0, RelativeOrderSysID="", AccountID="", Direction='0', InstallID=0, ParticipantID="", VolumeTotalOriginal=0, ExchangeInstID="", ClientID="", VolumeTotal=0, OrderPriceType='1', SessionID=0, TimeCondition='1', OrderStatus='0', OrderSysID="", OrderSubmitStatus='0', IsETF=0, IsAutoSuspend=0, StopPrice=0, InstrumentID="", ExchangeID="", MinVolume=0, StatusMsg="", SettlementID=0, ForceCloseReason='0', OrderType='0', ErrorID=0, UpdateTime="", TradingDay="", ActiveTime="", BrokerID="", InsertTime="", FrontID=0, SuspendTime="", ClearingPartID="", CombHedgeFlag="", CancelTime="", GTDDate="", OrderLocalID="", BranchID="", BusinessUnit="", InsertDate="", SequenceNo=0, OrderRef="", BrokerOrderSeq=0, InvestorID="", VolumeCondition='1', RequestID=0, ErrorMsg="", OrderSource='0', TradeAmount=0, ActiveTraderID=""):
        self.ContingentCondition=ContingentCondition
        self.NotifySequence=NotifySequence
        self.ActiveUserID=ActiveUserID
        self.VolumeTraded=VolumeTraded
        self.UserProductInfo=UserProductInfo
        self.CombOffsetFlag=CombOffsetFlag
        self.TraderID=TraderID
        self.UserID=UserID
        self.LimitPrice=LimitPrice
        self.UserForceClose=UserForceClose
        self.RelativeOrderSysID=RelativeOrderSysID
        self.AccountID=AccountID
        self.Direction=Direction
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.ExchangeInstID=ExchangeInstID
        self.ClientID=ClientID
        self.VolumeTotal=VolumeTotal
        self.OrderPriceType=OrderPriceType
        self.SessionID=SessionID
        self.TimeCondition=TimeCondition
        self.OrderStatus=OrderStatus
        self.OrderSysID=OrderSysID
        self.OrderSubmitStatus=OrderSubmitStatus
        self.IsETF=IsETF
        self.IsAutoSuspend=IsAutoSuspend
        self.StopPrice=StopPrice
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MinVolume=MinVolume
        self.StatusMsg=StatusMsg
        self.SettlementID=SettlementID
        self.ForceCloseReason=ForceCloseReason
        self.OrderType=OrderType
        self.ErrorID=ErrorID
        self.UpdateTime=UpdateTime
        self.TradingDay=TradingDay
        self.ActiveTime=ActiveTime
        self.BrokerID=BrokerID
        self.InsertTime=InsertTime
        self.FrontID=FrontID
        self.SuspendTime=SuspendTime
        self.ClearingPartID=ClearingPartID
        self.CombHedgeFlag=CombHedgeFlag
        self.CancelTime=CancelTime
        self.GTDDate=GTDDate
        self.OrderLocalID=OrderLocalID
        self.BranchID=BranchID
        self.BusinessUnit=BusinessUnit
        self.InsertDate=InsertDate
        self.SequenceNo=SequenceNo
        self.OrderRef=OrderRef
        self.BrokerOrderSeq=BrokerOrderSeq
        self.InvestorID=InvestorID
        self.VolumeCondition=VolumeCondition
        self.RequestID=RequestID
        self.ErrorMsg=ErrorMsg
        self.OrderSource=OrderSource
        self.TradeAmount=TradeAmount
        self.ActiveTraderID=ActiveTraderID
        self.vcmap={'ContingentCondition': {"'9'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'B'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'7'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7', "'8'": u'\u6700\u65b0\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'5'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'C'": u'\u5356\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'4'": u'\u9884\u57cb\u5355', "'1'": u'\u7acb\u5373', "'6'": u'\u6700\u65b0\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'2'": u'\u6b62\u635f', "'H'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'E'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'3'": u'\u6b62\u8d62', "'D'": u'\u4e70\u4e00\u4ef7\u5927\u4e8e\u6761\u4ef6\u4ef7', "'A'": u'\u5356\u4e00\u4ef7\u5927\u4e8e\u7b49\u4e8e\u6761\u4ef6\u4ef7', "'F'": u'\u4e70\u4e00\u4ef7\u5c0f\u4e8e\u6761\u4ef6\u4ef7'}, 'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'ForceCloseReason': {"'5'": u'\u8fdd\u89c4', "'4'": u'\u6301\u4ed3\u975e\u6574\u6570\u500d', "'1'": u'\u8d44\u91d1\u4e0d\u8db3', "'0'": u'\u975e\u5f3a\u5e73', "'6'": u'\u5176\u5b83', "'2'": u'\u5ba2\u6237\u8d85\u4ed3', "'3'": u'\u4f1a\u5458\u8d85\u4ed3'}, 'OrderType': {"'5'": u'\u4e92\u6362\u5355', "'4'": u'\u6761\u4ef6\u5355', "'1'": u'\u62a5\u4ef7\u884d\u751f', "'0'": u'\u6b63\u5e38', "'2'": u'\u7ec4\u5408\u884d\u751f', "'3'": u'\u7ec4\u5408\u62a5\u5355'}, 'OrderPriceType': {"'9'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'B'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'W'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8d4e\u56de', "'U'": u'\u6743\u8bc1\u884c\u6743', "'Q'": u'\u8981\u7ea6\u6536\u8d2d\u64a4\u9500', "'L'": u'\u6307\u5b9a\u64a4\u9500', "'H'": u'\u6ce8\u9500A\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'N'": u'\u8bc1\u5238\u53c2\u4e0e\u7533\u8d2d', "'S'": u'\u53ef\u8f6c\u503a\u8f6c\u6362\u767b\u8bb0', "'d'": u'ETF\u7533\u8d2d', "'J'": u'\u6ce8\u9500B\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'f'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'7'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'X'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8ba4\u8d2d', "'5'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'c'": u'\u503a\u5238\u51fa\u5e93', "'1'": u'\u4efb\u610f\u4ef7', "'Z'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8bbe\u7f6e\u5206\u7ea2\u65b9\u5f0f', "'i'": u'\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u81ea\u8425\u8d26\u6237', "'3'": u'\u6700\u4f18\u4ef7', "'D'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e1\u4e2aticks', "'F'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e3\u4e2aticks', "'8'": u'\u5356\u4e00\u4ef7', "'C'": u'\u4e70\u4e00\u4ef7', "'T'": u'\u53ef\u8f6c\u503a\u56de\u552e\u767b\u8bb0', "'O'": u'\u8bc1\u5238\u53c2\u4e0e\u914d\u80a1', "'P'": u'\u8981\u7ea6\u6536\u8d2d\u767b\u8bb0', "'M'": u'\u6307\u5b9a\u767b\u8bb0', "'V'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u7533\u8d2d', "'I'": u'\u6fc0\u6d3bB\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'R'": u'\u8bc1\u5238\u6295\u7968', "'g'": u'\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u878d\u5238\u4e13\u7528\u8d26\u6237', "'e'": u'ETF\u8d4e\u56de', "'a'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6362\u4e3a\u5176\u4ed6\u57fa\u91d1', "'K'": u'\u56de\u8d2d\u6ce8\u9500', "'Y'": u'\u5f00\u653e\u5f0f\u57fa\u91d1\u8f6c\u6258\u7ba1\u8f6c\u51fa', "'b'": u'\u503a\u5238\u5165\u5e93', "'4'": u'\u6700\u65b0\u4ef7', "'6'": u'\u6700\u65b0\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'2'": u'\u9650\u4ef7', "'G'": u'\u6fc0\u6d3bA\u80a1\u7f51\u7edc\u5bc6\u7801\u670d\u52a1\u4ee3\u7801', "'h'": u'\u6295\u8d44\u8005\u666e\u901a\u8bc1\u5238\u8d26\u6237\u8fc7\u6237\u5230\u8bc1\u5238\u516c\u53f8\u4fe1\u7528\u4ea4\u6613\u62c5\u4fdd\u8bc1\u5238\u8d26\u6237', "'E'": u'\u4e70\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks', "'A'": u'\u5356\u4e00\u4ef7\u6d6e\u52a8\u4e0a\u6d6e2\u4e2aticks'}, 'VolumeCondition': {"'1'": u'\u4efb\u4f55\u6570\u91cf', "'2'": u'\u6700\u5c0f\u6570\u91cf', "'3'": u'\u5168\u90e8\u6570\u91cf'}, 'TimeCondition': {"'5'": u'\u64a4\u9500\u524d\u6709\u6548', "'4'": u'\u6307\u5b9a\u65e5\u671f\u524d\u6709\u6548', "'1'": u'\u7acb\u5373\u5b8c\u6210\uff0c\u5426\u5219\u64a4\u9500', "'6'": u'\u96c6\u5408\u7ade\u4ef7\u6709\u6548', "'2'": u'\u672c\u8282\u6709\u6548', "'3'": u'\u5f53\u65e5\u6709\u6548'}, 'OrderSource': {"'1'": u'\u6765\u81ea\u7ba1\u7406\u5458', "'0'": u'\u6765\u81ea\u53c2\u4e0e\u8005'}, 'OrderStatus': {"'b'": u'\u5c1a\u672a\u89e6\u53d1', "'5'": u'\u64a4\u5355', "'c'": u'\u5df2\u89e6\u53d1', "'4'": u'\u672a\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'1'": u'\u90e8\u5206\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'0'": u'\u5168\u90e8\u6210\u4ea4', "'2'": u'\u90e8\u5206\u6210\u4ea4\u4e0d\u5728\u961f\u5217\u4e2d', "'3'": u'\u672a\u6210\u4ea4\u8fd8\u5728\u961f\u5217\u4e2d', "'a'": u'\u672a\u77e5'}, 'OrderSubmitStatus': {"'5'": u'\u64a4\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'4'": u'\u62a5\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'1'": u'\u64a4\u5355\u5df2\u7ecf\u63d0\u4ea4', "'0'": u'\u5df2\u7ecf\u63d0\u4ea4', "'6'": u'\u6539\u5355\u5df2\u7ecf\u88ab\u62d2\u7edd', "'2'": u'\u4fee\u6539\u5df2\u7ecf\u63d0\u4ea4', "'3'": u'\u5df2\u7ecf\u63a5\u53d7'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ContingentCondition', 'NotifySequence', 'ActiveUserID', 'VolumeTraded', 'UserProductInfo', 'CombOffsetFlag', 'TraderID', 'UserID', 'LimitPrice', 'UserForceClose', 'RelativeOrderSysID', 'AccountID', 'Direction', 'InstallID', 'ParticipantID', 'VolumeTotalOriginal', 'ExchangeInstID', 'ClientID', 'VolumeTotal', 'OrderPriceType', 'SessionID', 'TimeCondition', 'OrderStatus', 'OrderSysID', 'OrderSubmitStatus', 'IsETF', 'IsAutoSuspend', 'StopPrice', 'InstrumentID', 'ExchangeID', 'MinVolume', 'StatusMsg', 'SettlementID', 'ForceCloseReason', 'OrderType', 'ErrorID', 'UpdateTime', 'TradingDay', 'ActiveTime', 'BrokerID', 'InsertTime', 'FrontID', 'SuspendTime', 'ClearingPartID', 'CombHedgeFlag', 'CancelTime', 'GTDDate', 'OrderLocalID', 'BranchID', 'BusinessUnit', 'InsertDate', 'SequenceNo', 'OrderRef', 'BrokerOrderSeq', 'InvestorID', 'VolumeCondition', 'RequestID', 'ErrorMsg', 'OrderSource', 'TradeAmount', 'ActiveTraderID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ContingentCondition', u'触发条件'),('NotifySequence', u'报单提示序号'),('ActiveUserID', u'操作用户代码'),('VolumeTraded', u'今成交数量'),('UserProductInfo', u'用户端产品信息'),('CombOffsetFlag', u'组合开平标志'),('TraderID', u'交易所交易员代码'),('UserID', u'用户代码'),('LimitPrice', u'价格'),('UserForceClose', u'用户强评标志'),('RelativeOrderSysID', u'相关报单'),('AccountID', u'资金帐号'),('Direction', u'买卖方向'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('VolumeTotalOriginal', u'数量'),('ExchangeInstID', u'合约在交易所的代码'),('ClientID', u'客户代码'),('VolumeTotal', u'剩余数量'),('OrderPriceType', u'报单价格条件'),('SessionID', u'会话编号'),('TimeCondition', u'有效期类型'),('OrderStatus', u'报单状态'),('OrderSysID', u'报单编号'),('OrderSubmitStatus', u'报单提交状态'),('IsETF', u'是否ETF'),('IsAutoSuspend', u'自动挂起标志'),('StopPrice', u'止损价'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MinVolume', u'最小成交量'),('StatusMsg', u'状态信息'),('SettlementID', u'结算编号'),('ForceCloseReason', u'强平原因'),('OrderType', u'报单类型'),('ErrorID', u'错误代码'),('UpdateTime', u'最后修改时间'),('TradingDay', u'交易日'),('ActiveTime', u'激活时间'),('BrokerID', u'经纪公司代码'),('InsertTime', u'委托时间'),('FrontID', u'前置编号'),('SuspendTime', u'挂起时间'),('ClearingPartID', u'结算会员编号'),('CombHedgeFlag', u'组合投机套保标志'),('CancelTime', u'撤销时间'),('GTDDate', u'GTD日期'),('OrderLocalID', u'本地报单编号'),('BranchID', u'营业部编号'),('BusinessUnit', u'业务单元'),('InsertDate', u'报单日期'),('SequenceNo', u'序号'),('OrderRef', u'报单引用'),('BrokerOrderSeq', u'经纪公司报单编号'),('InvestorID', u'投资者代码'),('VolumeCondition', u'成交量类型'),('RequestID', u'请求编号'),('ErrorMsg', u'错误信息'),('OrderSource', u'报单来源'),('TradeAmount', u'成交数量'),('ActiveTraderID', u'最后修改交易所交易员代码')]])
    def getval(self, n):
        if n in ['ContingentCondition', 'Direction', 'OrderPriceType', 'TimeCondition', 'OrderStatus', 'OrderSubmitStatus', 'ForceCloseReason', 'OrderType', 'VolumeCondition', 'OrderSource']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcNotifySyncKeyField:
    def __init__(self, BrokerBranchID="", UserID="", TradeTime="", TID=0, InstallID=0, TradeCode="", BankBranchID="", SessionID=0, BankID="", PlateSerial=0, ErrorID=0, BankSerial="", OperNo="", TradingDay="", BrokerID="", DeviceID="", TradeDate="", ErrorMsg="", LastFragment='0', RequestID=0, BrokerIDByBank="", Message=""):
        self.BrokerBranchID=BrokerBranchID
        self.UserID=UserID
        self.TradeTime=TradeTime
        self.TID=TID
        self.InstallID=InstallID
        self.TradeCode=TradeCode
        self.BankBranchID=BankBranchID
        self.SessionID=SessionID
        self.BankID=BankID
        self.PlateSerial=PlateSerial
        self.ErrorID=ErrorID
        self.BankSerial=BankSerial
        self.OperNo=OperNo
        self.TradingDay=TradingDay
        self.BrokerID=BrokerID
        self.DeviceID=DeviceID
        self.TradeDate=TradeDate
        self.ErrorMsg=ErrorMsg
        self.LastFragment=LastFragment
        self.RequestID=RequestID
        self.BrokerIDByBank=BrokerIDByBank
        self.Message=Message
        self.vcmap={'LastFragment': {"'1'": u'\u4e0d\u662f\u6700\u540e\u5206\u7247', "'0'": u'\u662f\u6700\u540e\u5206\u7247'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerBranchID', 'UserID', 'TradeTime', 'TID', 'InstallID', 'TradeCode', 'BankBranchID', 'SessionID', 'BankID', 'PlateSerial', 'ErrorID', 'BankSerial', 'OperNo', 'TradingDay', 'BrokerID', 'DeviceID', 'TradeDate', 'ErrorMsg', 'LastFragment', 'RequestID', 'BrokerIDByBank', 'Message']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('TID', u'交易ID'),('InstallID', u'安装编号'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('PlateSerial', u'银期平台消息流水号'),('ErrorID', u'错误代码'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('TradingDay', u'交易系统日期'),('BrokerID', u'期商代码'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('ErrorMsg', u'错误信息'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BrokerIDByBank', u'期货公司银行编码'),('Message', u'交易核心给银期报盘的消息')]])
    def getval(self, n):
        if n in ['LastFragment']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncStatusField:
    def __init__(self, TradingDay="", DataSyncStatus='1'):
        self.TradingDay=TradingDay
        self.DataSyncStatus=DataSyncStatus
        self.vcmap={'DataSyncStatus': {"'1'": u'\u672a\u540c\u6b65', "'2'": u'\u540c\u6b65\u4e2d', "'3'": u'\u5df2\u540c\u6b65'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DataSyncStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradingDay', u'交易日'),('DataSyncStatus', u'数据同步状态')]])
    def getval(self, n):
        if n in ['DataSyncStatus']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcSyncingInvestorGroupField:
    def __init__(self, InvestorGroupID="", BrokerID="", InvestorGroupName=""):
        self.InvestorGroupID=InvestorGroupID
        self.BrokerID=BrokerID
        self.InvestorGroupName=InvestorGroupName
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorGroupID', 'BrokerID', 'InvestorGroupName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorGroupID', u'投资者分组代码'),('BrokerID', u'经纪公司代码'),('InvestorGroupName', u'投资者分组名称')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataBaseField:
    def __init__(self, TradingDay="", PreDelta=0, PreClosePrice=0, PreOpenInterest=0, PreSettlementPrice=0):
        self.TradingDay=TradingDay
        self.PreDelta=PreDelta
        self.PreClosePrice=PreClosePrice
        self.PreOpenInterest=PreOpenInterest
        self.PreSettlementPrice=PreSettlementPrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'PreDelta', 'PreClosePrice', 'PreOpenInterest', 'PreSettlementPrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('TradingDay', u'交易日'),('PreDelta', u'昨虚实度'),('PreClosePrice', u'昨收盘'),('PreOpenInterest', u'昨持仓量'),('PreSettlementPrice', u'上次结算价')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorPositionCombineDetailField:
    def __init__(self, InstrumentID="", ExchangeID="", MarginRateByVolume=0, ComTradeID="", SettlementID=0, InvestorID="", TotalAmt=0, Margin=0, ExchMargin=0, LegMultiple=0, HedgeFlag='1', TradeID="", LegID=0, TradingDay="", MarginRateByMoney=0, Direction='0', BrokerID="", CombInstrumentID="", OpenDate=""):
        self.InstrumentID=InstrumentID
        self.ExchangeID=ExchangeID
        self.MarginRateByVolume=MarginRateByVolume
        self.ComTradeID=ComTradeID
        self.SettlementID=SettlementID
        self.InvestorID=InvestorID
        self.TotalAmt=TotalAmt
        self.Margin=Margin
        self.ExchMargin=ExchMargin
        self.LegMultiple=LegMultiple
        self.HedgeFlag=HedgeFlag
        self.TradeID=TradeID
        self.LegID=LegID
        self.TradingDay=TradingDay
        self.MarginRateByMoney=MarginRateByMoney
        self.Direction=Direction
        self.BrokerID=BrokerID
        self.CombInstrumentID=CombInstrumentID
        self.OpenDate=OpenDate
        self.vcmap={'Direction': {"'9'": u'\u76f4\u63a5\u8fd8\u5238', "'b'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u51fa\u4fe1\u7528\u8d26\u6237', "'7'": u'\u4e70\u5238\u8fd8\u5238', "'8'": u'\u76f4\u63a5\u8fd8\u6b3e', "'5'": u'\u878d\u5238\u5356\u51fa', "'c'": u'\u73b0\u91d1\u66ff\u4ee3\uff0c\u53ea\u7528\u4f5c\u56de\u62a5', "'4'": u'\u878d\u8d44\u4e70\u5165', "'1'": u'\u5356', "'0'": u'\u4e70', "'6'": u'\u5356\u5238\u8fd8\u6b3e', "'2'": u'ETF\u7533\u8d2d', "'e'": u'\u503a\u5238\u8d28\u62bc\u51fa\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'3'": u'ETF\u8d4e\u56de', "'d'": u'\u503a\u5238\u8d28\u62bc\u5165\u5e93,\u6df1\u5733\u65e0\u8d28\u62bc\u4ee3\u7801,\u4ee5\u6b64\u533a\u5206\u662f\u8d28\u62bc\u5165\u5e93', "'a'": u'\u62c5\u4fdd\u54c1\u5212\u8f6c\u5165\u4fe1\u7528\u8d26\u6237', "'f'": u'\u914d\u80a1'}, 'HedgeFlag': {"'1'": u'\u6295\u673a', "'3'": u'\u5957\u4fdd'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ExchangeID', 'MarginRateByVolume', 'ComTradeID', 'SettlementID', 'InvestorID', 'TotalAmt', 'Margin', 'ExchMargin', 'LegMultiple', 'HedgeFlag', 'TradeID', 'LegID', 'TradingDay', 'MarginRateByMoney', 'Direction', 'BrokerID', 'CombInstrumentID', 'OpenDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('MarginRateByVolume', u'保证金率(按手数)'),('ComTradeID', u'组合编号'),('SettlementID', u'结算编号'),('InvestorID', u'投资者代码'),('TotalAmt', u'持仓量'),('Margin', u'投资者保证金'),('ExchMargin', u'交易所保证金'),('LegMultiple', u'单腿乘数'),('HedgeFlag', u'投机套保标志'),('TradeID', u'撮合编号'),('LegID', u'单腿编号'),('TradingDay', u'交易日'),('MarginRateByMoney', u'保证金率'),('Direction', u'买卖'),('BrokerID', u'经纪公司代码'),('CombInstrumentID', u'组合持仓合约编码'),('OpenDate', u'开仓日期')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'Direction']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryInvestorGroupField:
    def __init__(self, BrokerID=""):
        self.BrokerID=BrokerID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryTransferBankField:
    def __init__(self, BankBrchID="", BankID=""):
        self.BankBrchID=BankBrchID
        self.BankID=BankID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankBrchID', 'BankID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BankBrchID', u'银行分中心代码'),('BankID', u'银行代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryMDTraderOfferField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=ExchangeID
        self.TraderID=TraderID
        self.ParticipantID=ParticipantID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcMarketDataAsk23Field:
    def __init__(self, AskVolume3=0, AskVolume2=0, AskPrice3=0, AskPrice2=0):
        self.AskVolume3=AskVolume3
        self.AskVolume2=AskVolume2
        self.AskPrice3=AskPrice3
        self.AskPrice2=AskPrice2
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AskVolume3', 'AskVolume2', 'AskPrice3', 'AskPrice2']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('AskVolume3', u'申卖量三'),('AskVolume2', u'申卖量二'),('AskPrice3', u'申卖价三'),('AskPrice2', u'申卖价二')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcBrokerField:
    def __init__(self, BrokerAbbr="", BrokerID="", BrokerName="", IsActive=0):
        self.BrokerAbbr=BrokerAbbr
        self.BrokerID=BrokerID
        self.BrokerName=BrokerName
        self.IsActive=IsActive
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerAbbr', 'BrokerID', 'BrokerName', 'IsActive']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('BrokerAbbr', u'经纪公司简称'),('BrokerID', u'经纪公司代码'),('BrokerName', u'经纪公司名称'),('IsActive', u'是否活跃')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcExchangeOrderInsertErrorField:
    def __init__(self, ExchangeID="", InstallID=0, ParticipantID="", OrderLocalID="", ErrorMsg="", TraderID="", ErrorID=0):
        self.ExchangeID=ExchangeID
        self.InstallID=InstallID
        self.ParticipantID=ParticipantID
        self.OrderLocalID=OrderLocalID
        self.ErrorMsg=ErrorMsg
        self.TraderID=TraderID
        self.ErrorID=ErrorID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'InstallID', 'ParticipantID', 'OrderLocalID', 'ErrorMsg', 'TraderID', 'ErrorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('InstallID', u'安装编号'),('ParticipantID', u'会员代码'),('OrderLocalID', u'本地报单编号'),('ErrorMsg', u'错误信息'),('TraderID', u'交易所交易员代码'),('ErrorID', u'错误代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorField:
    def __init__(self, SZBranchID="", InvestorName="", Mobile="", IdentifiedCardNo="", Telephone="", InvestorID="", IsCreditAccount=0, BrokerID="", SHBranchID="", Address="", InvestorGroupID="", OpenDate="", IsActive=0, IdentifiedCardType='0'):
        self.SZBranchID=SZBranchID
        self.InvestorName=InvestorName
        self.Mobile=Mobile
        self.IdentifiedCardNo=IdentifiedCardNo
        self.Telephone=Telephone
        self.InvestorID=InvestorID
        self.IsCreditAccount=IsCreditAccount
        self.BrokerID=BrokerID
        self.SHBranchID=SHBranchID
        self.Address=Address
        self.InvestorGroupID=InvestorGroupID
        self.OpenDate=OpenDate
        self.IsActive=IsActive
        self.IdentifiedCardType=IdentifiedCardType
        self.vcmap={'IdentifiedCardType': {"'9'": u'\u8425\u4e1a\u6267\u7167\u53f7', "'7'": u'\u53f0\u80de\u8bc1', "'x'": u'\u5176\u4ed6\u8bc1\u4ef6', "'5'": u'\u6237\u53e3\u7c3f', "'4'": u'\u58eb\u5175\u8bc1', "'1'": u'\u8eab\u4efd\u8bc1', "'0'": u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801', "'6'": u'\u62a4\u7167', "'2'": u'\u519b\u5b98\u8bc1', "'8'": u'\u56de\u4e61\u8bc1', "'3'": u'\u8b66\u5b98\u8bc1'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SZBranchID', 'InvestorName', 'Mobile', 'IdentifiedCardNo', 'Telephone', 'InvestorID', 'IsCreditAccount', 'BrokerID', 'SHBranchID', 'Address', 'InvestorGroupID', 'OpenDate', 'IsActive', 'IdentifiedCardType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('SZBranchID', u'深圳营业部编号'),('InvestorName', u'投资者名称'),('Mobile', u'手机'),('IdentifiedCardNo', u'证件号码'),('Telephone', u'联系电话'),('InvestorID', u'投资者代码'),('IsCreditAccount', u'是否信用账户'),('BrokerID', u'经纪公司代码'),('SHBranchID', u'上海营业部编号'),('Address', u'通讯地址'),('InvestorGroupID', u'投资者分组代码'),('OpenDate', u'开户日期'),('IsActive', u'是否活跃'),('IdentifiedCardType', u'证件类型')]])
    def getval(self, n):
        if n in ['IdentifiedCardType']:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryDepthMarketDataField:
    def __init__(self, InstrumentID=""):
        self.InstrumentID=InstrumentID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcInvestorGroupField:
    def __init__(self, InvestorGroupID="", BrokerID="", InvestorGroupName=""):
        self.InvestorGroupID=InvestorGroupID
        self.BrokerID=BrokerID
        self.InvestorGroupName=InvestorGroupName
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorGroupID', 'BrokerID', 'InvestorGroupName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('InvestorGroupID', u'投资者分组代码'),('BrokerID', u'经纪公司代码'),('InvestorGroupName', u'投资者分组名称')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
class CZQThostFtdcQryPartBrokerField:
    def __init__(self, ExchangeID="", BrokerID="", ParticipantID=""):
        self.ExchangeID=ExchangeID
        self.BrokerID=BrokerID
        self.ParticipantID=ParticipantID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'BrokerID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y.encode("utf-8"), self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('BrokerID', u'经纪公司代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            return self.vcmap[n][getattr(self, n)].encode("utf-8")
        else: return getattr(self, n)
# Set short name alias for the stupid Hungarian Notation
RspFutureSignIn=CZQThostFtdcRspFutureSignInField
QryTradingNotice=CZQThostFtdcQryTradingNoticeField
TradingAccount=CZQThostFtdcTradingAccountField
AuthenticationInfo=CZQThostFtdcAuthenticationInfoField
BrokerTradingParams=CZQThostFtdcBrokerTradingParamsField
QryBroker=CZQThostFtdcQryBrokerField
Trade=CZQThostFtdcTradeField
QryExchange=CZQThostFtdcQryExchangeField
QrySettlementInfo=CZQThostFtdcQrySettlementInfoField
ReqDayEndFileReady=CZQThostFtdcReqDayEndFileReadyField
SyncingInvestor=CZQThostFtdcSyncingInvestorField
CFMMCTradingAccountKey=CZQThostFtdcCFMMCTradingAccountKeyField
QrySyncStatus=CZQThostFtdcQrySyncStatusField
QryInvestorPositionDetail=CZQThostFtdcQryInvestorPositionDetailField
FundIOCTPAccount=CZQThostFtdcFundIOCTPAccountField
TransferBank=CZQThostFtdcTransferBankField
OrderAction=CZQThostFtdcOrderActionField
QryBrokerUserEvent=CZQThostFtdcQryBrokerUserEventField
MaxStockPositionLimit=CZQThostFtdcMaxStockPositionLimitField
ReqRepeal=CZQThostFtdcReqRepealField
TransferSerial=CZQThostFtdcTransferSerialField
InvestorWithdrawAlgorithm=CZQThostFtdcInvestorWithdrawAlgorithmField
UserLogout=CZQThostFtdcUserLogoutField
BrokerUserEvent=CZQThostFtdcBrokerUserEventField
VerifyInvestorPassword=CZQThostFtdcVerifyInvestorPasswordField
RspQueryTradeResultBySerial=CZQThostFtdcRspQueryTradeResultBySerialField
QryParkedOrder=CZQThostFtdcQryParkedOrderField
LinkMan=CZQThostFtdcLinkManField
QryLinkMan=CZQThostFtdcQryLinkManField
RspFutureSignOut=CZQThostFtdcRspFutureSignOutField
ReqOpenAccount=CZQThostFtdcReqOpenAccountField
LoginInfo=CZQThostFtdcLoginInfoField
ErrOrder=CZQThostFtdcErrOrderField
CFMMCBrokerKey=CZQThostFtdcCFMMCBrokerKeyField
TradingNotice=CZQThostFtdcTradingNoticeField
TransferBankToFutureRsp=CZQThostFtdcTransferBankToFutureRspField
QryInstrumentStatus=CZQThostFtdcQryInstrumentStatusField
QryInvestorPosition=CZQThostFtdcQryInvestorPositionField
QryTradingAccount=CZQThostFtdcQryTradingAccountField
BrokerSync=CZQThostFtdcBrokerSyncField
QueryBrokerDeposit=CZQThostFtdcQueryBrokerDepositField
ExchangeMarginRate=CZQThostFtdcExchangeMarginRateField
SettlementInfoConfirm=CZQThostFtdcSettlementInfoConfirmField
Trader=CZQThostFtdcTraderField
BondInterest=CZQThostFtdcBondInterestField
QryBrokerUserFunction=CZQThostFtdcQryBrokerUserFunctionField
PositionProfitAlgorithm=CZQThostFtdcPositionProfitAlgorithmField
MarketDataAsk45=CZQThostFtdcMarketDataAsk45Field
TransferFutureToBankReq=CZQThostFtdcTransferFutureToBankReqField
InstrumentStatus=CZQThostFtdcInstrumentStatusField
QrySuperUser=CZQThostFtdcQrySuperUserField
MarketDataBid45=CZQThostFtdcMarketDataBid45Field
BrokerUserFunction=CZQThostFtdcBrokerUserFunctionField
ForceUserLogout=CZQThostFtdcForceUserLogoutField
QryTraderOffer=CZQThostFtdcQryTraderOfferField
QryCFMMCBrokerKey=CZQThostFtdcQryCFMMCBrokerKeyField
QryInstrumentMarginRate=CZQThostFtdcQryInstrumentMarginRateField
RspSyncKey=CZQThostFtdcRspSyncKeyField
VerifyFuturePassword=CZQThostFtdcVerifyFuturePasswordField
SyncingInstrumentMarginRate=CZQThostFtdcSyncingInstrumentMarginRateField
ParkedOrderAction=CZQThostFtdcParkedOrderActionField
BrokerUserOTPParam=CZQThostFtdcBrokerUserOTPParamField
QryInstrumentCommissionRate=CZQThostFtdcQryInstrumentCommissionRateField
MDTraderOffer=CZQThostFtdcMDTraderOfferField
QueryMaxOrderVolumeWithPrice=CZQThostFtdcQueryMaxOrderVolumeWithPriceField
CommPhase=CZQThostFtdcCommPhaseField
SuperUserFunction=CZQThostFtdcSuperUserFunctionField
TransferFutureToBankRsp=CZQThostFtdcTransferFutureToBankRspField
MarketData=CZQThostFtdcMarketDataField
SyncingTradingAccount=CZQThostFtdcSyncingTradingAccountField
FrontStatus=CZQThostFtdcFrontStatusField
CombinationLeg=CZQThostFtdcCombinationLegField
QryErrOrderAction=CZQThostFtdcQryErrOrderActionField
QryExchangeOrderAction=CZQThostFtdcQryExchangeOrderActionField
SyncingTradingCode=CZQThostFtdcSyncingTradingCodeField
InstrumentTradingRight=CZQThostFtdcInstrumentTradingRightField
InvestorPositionDetail=CZQThostFtdcInvestorPositionDetailField
QryFundIOCTPAccount=CZQThostFtdcQryFundIOCTPAccountField
ContractBank=CZQThostFtdcContractBankField
QryTransferSerial=CZQThostFtdcQryTransferSerialField
ManualSyncBrokerUserOTP=CZQThostFtdcManualSyncBrokerUserOTPField
InvestorAccount=CZQThostFtdcInvestorAccountField
QryOrderAction=CZQThostFtdcQryOrderActionField
UserSession=CZQThostFtdcUserSessionField
QryBrokerTradingAlgos=CZQThostFtdcQryBrokerTradingAlgosField
QrySuperUserFunction=CZQThostFtdcQrySuperUserFunctionField
MarketDataStatic=CZQThostFtdcMarketDataStaticField
Discount=CZQThostFtdcDiscountField
UserIP=CZQThostFtdcUserIPField
QryBrokerUser=CZQThostFtdcQryBrokerUserField
ReqQueryAccount=CZQThostFtdcReqQueryAccountField
QryHisOrder=CZQThostFtdcQryHisOrderField
InstrumentCommissionRate=CZQThostFtdcInstrumentCommissionRateField
BrokerUser=CZQThostFtdcBrokerUserField
SyncDeposit=CZQThostFtdcSyncDepositField
QryInstrumentTradingRight=CZQThostFtdcQryInstrumentTradingRightField
QryCFMMCTradingAccountKey=CZQThostFtdcQryCFMMCTradingAccountKeyField
ReqFundIOCTPAccount=CZQThostFtdcReqFundIOCTPAccountField
Notice=CZQThostFtdcNoticeField
ReqTransfer=CZQThostFtdcReqTransferField
ErrOrderAction=CZQThostFtdcErrOrderActionField
NotifyFutureSignIn=CZQThostFtdcNotifyFutureSignInField
QryInvestor=CZQThostFtdcQryInvestorField
QryNotice=CZQThostFtdcQryNoticeField
QrySyncDeposit=CZQThostFtdcQrySyncDepositField
UserRight=CZQThostFtdcUserRightField
QueryMaxOrderVolume=CZQThostFtdcQueryMaxOrderVolumeField
ExchangeTrade=CZQThostFtdcExchangeTradeField
FutureSignIO=CZQThostFtdcFutureSignIOField
InputOrderAction=CZQThostFtdcInputOrderActionField
TransferQryDetailRsp=CZQThostFtdcTransferQryDetailRspField
Exchange=CZQThostFtdcExchangeField
TransferQryBankReq=CZQThostFtdcTransferQryBankReqField
TransferBankToFutureReq=CZQThostFtdcTransferBankToFutureReqField
QryUserSession=CZQThostFtdcQryUserSessionField
ExchangeMarginRateAdjust=CZQThostFtdcExchangeMarginRateAdjustField
RspAuthenticate=CZQThostFtdcRspAuthenticateField
QryTradingCode=CZQThostFtdcQryTradingCodeField
MarketDataLastMatch=CZQThostFtdcMarketDataLastMatchField
MarketDataExchange=CZQThostFtdcMarketDataExchangeField
Dissemination=CZQThostFtdcDisseminationField
RemoveParkedOrder=CZQThostFtdcRemoveParkedOrderField
QryOrder=CZQThostFtdcQryOrderField
SyncingInstrumentTradingRight=CZQThostFtdcSyncingInstrumentTradingRightField
MarketDataBestPrice=CZQThostFtdcMarketDataBestPriceField
TransferHeader=CZQThostFtdcTransferHeaderField
QrySettlementInfoConfirm=CZQThostFtdcQrySettlementInfoConfirmField
ReqCancelAccount=CZQThostFtdcReqCancelAccountField
QryInstrument=CZQThostFtdcQryInstrumentField
ReturnResult=CZQThostFtdcReturnResultField
VerifyFuturePasswordAndCustInfo=CZQThostFtdcVerifyFuturePasswordAndCustInfoField
RspFundIOCTPAccount=CZQThostFtdcRspFundIOCTPAccountField
ReqFutureSignOut=CZQThostFtdcReqFutureSignOutField
UserPasswordUpdate=CZQThostFtdcUserPasswordUpdateField
TradingCode=CZQThostFtdcTradingCodeField
ReqUserLogin=CZQThostFtdcReqUserLoginField
SyncingInstrumentCommissionRate=CZQThostFtdcSyncingInstrumentCommissionRateField
SpecificInstrument=CZQThostFtdcSpecificInstrumentField
QryErrOrder=CZQThostFtdcQryErrOrderField
SuperUser=CZQThostFtdcSuperUserField
TradingAccountPassword=CZQThostFtdcTradingAccountPasswordField
LogoutAll=CZQThostFtdcLogoutAllField
Order=CZQThostFtdcOrderField
ReqChangeAccount=CZQThostFtdcReqChangeAccountField
QryFrontStatus=CZQThostFtdcQryFrontStatusField
NotifyFutureSignOut=CZQThostFtdcNotifyFutureSignOutField
QryInvestorPositionCombineDetail=CZQThostFtdcQryInvestorPositionCombineDetailField
BrokerWithdrawAlgorithm=CZQThostFtdcBrokerWithdrawAlgorithmField
Product=CZQThostFtdcProductField
ExchangeOrder=CZQThostFtdcExchangeOrderField
RemoveParkedOrderAction=CZQThostFtdcRemoveParkedOrderActionField
CurrentTime=CZQThostFtdcCurrentTimeField
QryTrade=CZQThostFtdcQryTradeField
SettlementInfo=CZQThostFtdcSettlementInfoField
DepthMarketData=CZQThostFtdcDepthMarketDataField
ReqSyncKey=CZQThostFtdcReqSyncKeyField
RspTransfer=CZQThostFtdcRspTransferField
PartBroker=CZQThostFtdcPartBrokerField
QryTrader=CZQThostFtdcQryTraderField
TransferQryBankRsp=CZQThostFtdcTransferQryBankRspField
ExchangeOrderAction=CZQThostFtdcExchangeOrderActionField
NotifyQueryAccount=CZQThostFtdcNotifyQueryAccountField
RspQueryAccount=CZQThostFtdcRspQueryAccountField
LoadSettlementInfo=CZQThostFtdcLoadSettlementInfoField
TradingAccountPasswordUpdateV1=CZQThostFtdcTradingAccountPasswordUpdateV1Field
RspRepeal=CZQThostFtdcRspRepealField
QryParkedOrderAction=CZQThostFtdcQryParkedOrderActionField
DepositResultInform=CZQThostFtdcDepositResultInformField
QryProduct=CZQThostFtdcQryProductField
QryExchangeOrder=CZQThostFtdcQryExchangeOrderField
ReqAuthenticate=CZQThostFtdcReqAuthenticateField
QryExchangeSequence=CZQThostFtdcQryExchangeSequenceField
ParkedOrder=CZQThostFtdcParkedOrderField
MarketDataAveragePrice=CZQThostFtdcMarketDataAveragePriceField
MarketDataBid23=CZQThostFtdcMarketDataBid23Field
TradingNoticeInfo=CZQThostFtdcTradingNoticeInfoField
ExchangeOrderActionError=CZQThostFtdcExchangeOrderActionErrorField
TradingAccountPasswordUpdate=CZQThostFtdcTradingAccountPasswordUpdateField
SettlementRef=CZQThostFtdcSettlementRefField
MarketDataUpdateTime=CZQThostFtdcMarketDataUpdateTimeField
TraderOffer=CZQThostFtdcTraderOfferField
RspInfo=CZQThostFtdcRspInfoField
ExchangeSequence=CZQThostFtdcExchangeSequenceField
QryBondInterest=CZQThostFtdcQryBondInterestField
RspUserLogin=CZQThostFtdcRspUserLoginField
BrokerDeposit=CZQThostFtdcBrokerDepositField
QryCombinationLeg=CZQThostFtdcQryCombinationLegField
ReqQueryTradeResultBySerial=CZQThostFtdcReqQueryTradeResultBySerialField
QryBrokerTradingParams=CZQThostFtdcQryBrokerTradingParamsField
Instrument=CZQThostFtdcInstrumentField
SyncingInvestorPosition=CZQThostFtdcSyncingInvestorPositionField
TransferQryDetailReq=CZQThostFtdcTransferQryDetailReqField
InstrumentMarginRateAdjust=CZQThostFtdcInstrumentMarginRateAdjustField
QryContractBank=CZQThostFtdcQryContractBankField
InvestorPosition=CZQThostFtdcInvestorPositionField
BrokerUserPassword=CZQThostFtdcBrokerUserPasswordField
BrokerTradingAlgos=CZQThostFtdcBrokerTradingAlgosField
InstrumentMarginRate=CZQThostFtdcInstrumentMarginRateField
VerifyCustInfo=CZQThostFtdcVerifyCustInfoField
InputOrder=CZQThostFtdcInputOrderField
ErrorConditionalOrder=CZQThostFtdcErrorConditionalOrderField
NotifySyncKey=CZQThostFtdcNotifySyncKeyField
SyncStatus=CZQThostFtdcSyncStatusField
SyncingInvestorGroup=CZQThostFtdcSyncingInvestorGroupField
MarketDataBase=CZQThostFtdcMarketDataBaseField
InvestorPositionCombineDetail=CZQThostFtdcInvestorPositionCombineDetailField
QryInvestorGroup=CZQThostFtdcQryInvestorGroupField
QryTransferBank=CZQThostFtdcQryTransferBankField
QryMDTraderOffer=CZQThostFtdcQryMDTraderOfferField
MarketDataAsk23=CZQThostFtdcMarketDataAsk23Field
Broker=CZQThostFtdcBrokerField
ExchangeOrderInsertError=CZQThostFtdcExchangeOrderInsertErrorField
Investor=CZQThostFtdcInvestorField
QryDepthMarketData=CZQThostFtdcQryDepthMarketDataField
InvestorGroup=CZQThostFtdcInvestorGroupField
QryPartBroker=CZQThostFtdcQryPartBrokerField
