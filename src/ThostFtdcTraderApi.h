/////////////////////////////////////////////////////////////////////////
///@system ÐÂÒ»´ú½»Ò×ËùÏµÍ³
///@company ÉÏº£ÆÚ»õÐÅÏ¢¼¼ÊõÓÐÏÞ¹«Ë¾
///@file ThostFtdcTraderApi.h
///@brief ¶¨ÒåÁË¿Í»§¶Ë½Ó¿Ú
///@history 
///20060106	ÕÔºèê»		´´½¨¸ÃÎÄ¼þ
/////////////////////////////////////////////////////////////////////////

#if !defined(THOST_FTDCTRADERAPI_H)
#define THOST_FTDCTRADERAPI_H

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "ThostFtdcUserApiStruct.h"

#if defined(ISLIB) && defined(WIN32)
#ifdef LIB_TRADER_API_EXPORT
#define TRADER_API_EXPORT __declspec(dllexport)
#else
#define TRADER_API_EXPORT __declspec(dllimport)
#endif
#else
#define TRADER_API_EXPORT 
#endif

class CThostFtdcTraderSpi
{
public:
	///µ±¿Í»§¶ËÓë½»Ò×ºóÌ¨½¨Á¢ÆðÍ¨ÐÅÁ¬½ÓÊ±£¨»¹Î´µÇÂ¼Ç°£©£¬¸Ã·½·¨±»µ÷ÓÃ¡£
	virtual void OnFrontConnected(){};
	
	///µ±¿Í»§¶ËÓë½»Ò×ºóÌ¨Í¨ÐÅÁ¬½Ó¶Ï¿ªÊ±£¬¸Ã·½·¨±»µ÷ÓÃ¡£µ±·¢ÉúÕâ¸öÇé¿öºó£¬API»á×Ô¶¯ÖØÐÂÁ¬½Ó£¬¿Í»§¶Ë¿É²»×ö´¦Àí¡£
	///@param nReason ´íÎóÔ­Òò
	///        0x1001 ÍøÂç¶ÁÊ§°Ü
	///        0x1002 ÍøÂçÐ´Ê§°Ü
	///        0x2001 ½ÓÊÕÐÄÌø³¬Ê±
	///        0x2002 ·¢ËÍÐÄÌøÊ§°Ü
	///        0x2003 ÊÕµ½´íÎó±¨ÎÄ
	virtual void OnFrontDisconnected(int nReason){};
		
	///ÐÄÌø³¬Ê±¾¯¸æ¡£µ±³¤Ê±¼äÎ´ÊÕµ½±¨ÎÄÊ±£¬¸Ã·½·¨±»µ÷ÓÃ¡£
	///@param nTimeLapse ¾àÀëÉÏ´Î½ÓÊÕ±¨ÎÄµÄÊ±¼ä
	virtual void OnHeartBeatWarning(int nTimeLapse){};
	
	///¿Í»§¶ËÈÏÖ¤ÏìÓ¦
	virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
	

	///µÇÂ¼ÇëÇóÏìÓ¦
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///µÇ³öÇëÇóÏìÓ¦
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÓÃ»§¿ÚÁî¸üÐÂÇëÇóÏìÓ¦
	virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///×Ê½ðÕË»§¿ÚÁî¸üÐÂÇëÇóÏìÓ¦
	virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///±¨µ¥Â¼ÈëÇëÇóÏìÓ¦
	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///Ô¤Âñµ¥Â¼ÈëÇëÇóÏìÓ¦
	virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///Ô¤Âñ³·µ¥Â¼ÈëÇëÇóÏìÓ¦
	virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///±¨µ¥²Ù×÷ÇëÇóÏìÓ¦
	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///²éÑ¯×î´ó±¨µ¥ÊýÁ¿ÏìÓ¦
	virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///Í¶×ÊÕß½áËã½á¹ûÈ·ÈÏÏìÓ¦
	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///É¾³ýÔ¤Âñµ¥ÏìÓ¦
	virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///É¾³ýÔ¤Âñ³·µ¥ÏìÓ¦
	virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯±¨µ¥ÏìÓ¦
	virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯³É½»ÏìÓ¦
	virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²ÖÏìÓ¦
	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯×Ê½ðÕË»§ÏìÓ¦
	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕßÏìÓ¦
	virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½»Ò×±àÂëÏìÓ¦
	virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯ºÏÔ¼±£Ö¤½ðÂÊÏìÓ¦
	virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯ºÏÔ¼ÊÖÐø·ÑÂÊÏìÓ¦
	virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½»Ò×ËùÏìÓ¦
	virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯ºÏÔ¼ÏìÓ¦
	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯ÐÐÇéÏìÓ¦
	virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕß½áËã½á¹ûÏìÓ¦
	virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯×ªÕÊÒøÐÐÏìÓ¦
	virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²ÖÃ÷Ï¸ÏìÓ¦
	virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯¿Í»§Í¨ÖªÏìÓ¦
	virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½áËãÐÅÏ¢È·ÈÏÏìÓ¦
	virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²ÖÃ÷Ï¸ÏìÓ¦
	virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///²éÑ¯±£Ö¤½ð¼à¹ÜÏµÍ³¾­¼Í¹«Ë¾×Ê½ðÕË»§ÃÜÔ¿ÏìÓ¦
	virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯²Öµ¥ÕÛµÖÐÅÏ¢ÏìÓ¦
	virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Í¶×ÊÕßÆ·ÖÖ/¿çÆ·ÖÖ±£Ö¤½ðÏìÓ¦
	virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½»Ò×Ëù±£Ö¤½ðÂÊÏìÓ¦
	virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½»Ò×Ëùµ÷Õû±£Ö¤½ðÂÊÏìÓ¦
	virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯×ªÕÊÁ÷Ë®ÏìÓ¦
	virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯ÒøÆÚÇ©Ô¼¹ØÏµÏìÓ¦
	virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///´íÎóÓ¦´ð
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///±¨µ¥Í¨Öª
	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {};

	///³É½»Í¨Öª
	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {};

	///±¨µ¥Â¼Èë´íÎó»Ø±¨
	virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {};

	///±¨µ¥²Ù×÷´íÎó»Ø±¨
	virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {};

	///ºÏÔ¼½»Ò××´Ì¬Í¨Öª
	virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {};

	///½»Ò×Í¨Öª
	virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};

	///ÌáÊ¾Ìõ¼þµ¥Ð£Ñé´íÎó
	virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {};

	///ÇëÇó²éÑ¯Ç©Ô¼ÒøÐÐÏìÓ¦
	virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Ô¤Âñµ¥ÏìÓ¦
	virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯Ô¤Âñ³·µ¥ÏìÓ¦
	virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯½»Ò×Í¨ÖªÏìÓ¦
	virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯¾­¼Í¹«Ë¾½»Ò×²ÎÊýÏìÓ¦
	virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÇëÇó²éÑ¯¾­¼Í¹«Ë¾½»Ò×Ëã·¨ÏìÓ¦
	virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÒøÐÐ·¢ÆðÒøÐÐ×Ê½ð×ªÆÚ»õÍ¨Öª
	virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {};

	///ÒøÐÐ·¢ÆðÆÚ»õ×Ê½ð×ªÒøÐÐÍ¨Öª
	virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {};

	///ÒøÐÐ·¢Æð³åÕýÒøÐÐ×ªÆÚ»õÍ¨Öª
	virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÒøÐÐ·¢Æð³åÕýÆÚ»õ×ªÒøÐÐÍ¨Öª
	virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÆÚ»õ·¢ÆðÒøÐÐ×Ê½ð×ªÆÚ»õÍ¨Öª
	virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {};

	///ÆÚ»õ·¢ÆðÆÚ»õ×Ê½ð×ªÒøÐÐÍ¨Öª
	virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {};

	///ÏµÍ³ÔËÐÐÊ±ÆÚ»õ¶ËÊÖ¹¤·¢Æð³åÕýÒøÐÐ×ªÆÚ»õÇëÇó£¬ÒøÐÐ´¦ÀíÍê±Ïºó±¨ÅÌ·¢»ØµÄÍ¨Öª
	virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÏµÍ³ÔËÐÐÊ±ÆÚ»õ¶ËÊÖ¹¤·¢Æð³åÕýÆÚ»õ×ªÒøÐÐÇëÇó£¬ÒøÐÐ´¦ÀíÍê±Ïºó±¨ÅÌ·¢»ØµÄÍ¨Öª
	virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÆÚ»õ·¢Æð²éÑ¯ÒøÐÐÓà¶îÍ¨Öª
	virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {};

	///ÆÚ»õ·¢ÆðÒøÐÐ×Ê½ð×ªÆÚ»õ´íÎó»Ø±¨
	virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {};

	///ÆÚ»õ·¢ÆðÆÚ»õ×Ê½ð×ªÒøÐÐ´íÎó»Ø±¨
	virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {};

	///ÏµÍ³ÔËÐÐÊ±ÆÚ»õ¶ËÊÖ¹¤·¢Æð³åÕýÒøÐÐ×ªÆÚ»õ´íÎó»Ø±¨
	virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {};

	///ÏµÍ³ÔËÐÐÊ±ÆÚ»õ¶ËÊÖ¹¤·¢Æð³åÕýÆÚ»õ×ªÒøÐÐ´íÎó»Ø±¨
	virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {};

	///ÆÚ»õ·¢Æð²éÑ¯ÒøÐÐÓà¶î´íÎó»Ø±¨
	virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {};

	///ÆÚ»õ·¢Æð³åÕýÒøÐÐ×ªÆÚ»õÇëÇó£¬ÒøÐÐ´¦ÀíÍê±Ïºó±¨ÅÌ·¢»ØµÄÍ¨Öª
	virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÆÚ»õ·¢Æð³åÕýÆÚ»õ×ªÒøÐÐÇëÇó£¬ÒøÐÐ´¦ÀíÍê±Ïºó±¨ÅÌ·¢»ØµÄÍ¨Öª
	virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {};

	///ÆÚ»õ·¢ÆðÒøÐÐ×Ê½ð×ªÆÚ»õÓ¦´ð
	virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÆÚ»õ·¢ÆðÆÚ»õ×Ê½ð×ªÒøÐÐÓ¦´ð
	virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÆÚ»õ·¢Æð²éÑ¯ÒøÐÐÓà¶îÓ¦´ð
	virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///ÒøÐÐ·¢ÆðÒøÆÚ¿ª»§Í¨Öª
	virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {};

	///ÒøÐÐ·¢ÆðÒøÆÚÏú»§Í¨Öª
	virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {};

	///ÒøÐÐ·¢Æð±ä¸üÒøÐÐÕËºÅÍ¨Öª
	virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {};
};

class TRADER_API_EXPORT CThostFtdcTraderApi
{
public:
	///´´½¨TraderApi
	///@param pszFlowPath ´æÖü¶©ÔÄÐÅÏ¢ÎÄ¼þµÄÄ¿Â¼£¬Ä¬ÈÏÎªµ±Ç°Ä¿Â¼
	///@return ´´½¨³öµÄUserApi
	static CThostFtdcTraderApi *CreateFtdcTraderApi(const char *pszFlowPath = "");
	
	///É¾³ý½Ó¿Ú¶ÔÏó±¾Éí
	///@remark ²»ÔÙÊ¹ÓÃ±¾½Ó¿Ú¶ÔÏóÊ±,µ÷ÓÃ¸Ãº¯ÊýÉ¾³ý½Ó¿Ú¶ÔÏó
	virtual void Release() = 0;
	
	///³õÊ¼»¯
	///@remark ³õÊ¼»¯ÔËÐÐ»·¾³,Ö»ÓÐµ÷ÓÃºó,½Ó¿Ú²Å¿ªÊ¼¹¤×÷
	virtual void Init() = 0;
	
	///µÈ´ý½Ó¿ÚÏß³Ì½áÊøÔËÐÐ
	///@return Ïß³ÌÍË³ö´úÂë
	virtual int Join() = 0;
	
	///»ñÈ¡µ±Ç°½»Ò×ÈÕ
	///@retrun »ñÈ¡µ½µÄ½»Ò×ÈÕ
	///@remark Ö»ÓÐµÇÂ¼³É¹¦ºó,²ÅÄÜµÃµ½ÕýÈ·µÄ½»Ò×ÈÕ
	virtual const char *GetTradingDay() = 0;
	
	///×¢²áÇ°ÖÃ»úÍøÂçµØÖ·
	///@param pszFrontAddress£ºÇ°ÖÃ»úÍøÂçµØÖ·¡£
	///@remark ÍøÂçµØÖ·µÄ¸ñÊ½Îª£º¡°protocol://ipaddress:port¡±£¬Èç£º¡±tcp://127.0.0.1:17001¡±¡£ 
	///@remark ¡°tcp¡±´ú±í´«ÊäÐ­Òé£¬¡°127.0.0.1¡±´ú±í·þÎñÆ÷µØÖ·¡£¡±17001¡±´ú±í·þÎñÆ÷¶Ë¿ÚºÅ¡£
	virtual void RegisterFront(char *pszFrontAddress) = 0;
	
	///×¢²áÃû×Ö·þÎñÆ÷ÍøÂçµØÖ·
	///@param pszNsAddress£ºÃû×Ö·þÎñÆ÷ÍøÂçµØÖ·¡£
	///@remark ÍøÂçµØÖ·µÄ¸ñÊ½Îª£º¡°protocol://ipaddress:port¡±£¬Èç£º¡±tcp://127.0.0.1:12001¡±¡£ 
	///@remark ¡°tcp¡±´ú±í´«ÊäÐ­Òé£¬¡°127.0.0.1¡±´ú±í·þÎñÆ÷µØÖ·¡£¡±12001¡±´ú±í·þÎñÆ÷¶Ë¿ÚºÅ¡£
	///@remark RegisterNameServerÓÅÏÈÓÚRegisterFront
	virtual void RegisterNameServer(char *pszNsAddress) = 0;
	
	///×¢²áÃû×Ö·þÎñÆ÷ÓÃ»§ÐÅÏ¢
	///@param pFensUserInfo£ºÓÃ»§ÐÅÏ¢¡£
	virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;
	
	///×¢²á»Øµ÷½Ó¿Ú
	///@param pSpi ÅÉÉú×Ô»Øµ÷½Ó¿ÚÀàµÄÊµÀý
	virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;
	
	///¶©ÔÄË½ÓÐÁ÷¡£
	///@param nResumeType Ë½ÓÐÁ÷ÖØ´«·½Ê½  
	///        THOST_TERT_RESTART:´Ó±¾½»Ò×ÈÕ¿ªÊ¼ÖØ´«
	///        THOST_TERT_RESUME:´ÓÉÏ´ÎÊÕµ½µÄÐø´«
	///        THOST_TERT_QUICK:Ö»´«ËÍµÇÂ¼ºóË½ÓÐÁ÷µÄÄÚÈÝ
	///@remark ¸Ã·½·¨ÒªÔÚInit·½·¨Ç°µ÷ÓÃ¡£Èô²»µ÷ÓÃÔò²»»áÊÕµ½Ë½ÓÐÁ÷µÄÊý¾Ý¡£
	virtual void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;
	
	///¶©ÔÄ¹«¹²Á÷¡£
	///@param nResumeType ¹«¹²Á÷ÖØ´«·½Ê½  
	///        THOST_TERT_RESTART:´Ó±¾½»Ò×ÈÕ¿ªÊ¼ÖØ´«
	///        THOST_TERT_RESUME:´ÓÉÏ´ÎÊÕµ½µÄÐø´«
	///        THOST_TERT_QUICK:Ö»´«ËÍµÇÂ¼ºó¹«¹²Á÷µÄÄÚÈÝ
	///@remark ¸Ã·½·¨ÒªÔÚInit·½·¨Ç°µ÷ÓÃ¡£Èô²»µ÷ÓÃÔò²»»áÊÕµ½¹«¹²Á÷µÄÊý¾Ý¡£
	virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;

	///¿Í»§¶ËÈÏÖ¤ÇëÇó
	virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;

	///ÓÃ»§µÇÂ¼ÇëÇó
	virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;
	

	///µÇ³öÇëÇó
	virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;

	///ÓÃ»§¿ÚÁî¸üÐÂÇëÇó
	virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;

	///×Ê½ðÕË»§¿ÚÁî¸üÐÂÇëÇó
	virtual int ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) = 0;

	///±¨µ¥Â¼ÈëÇëÇó
	virtual int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) = 0;

	///Ô¤Âñµ¥Â¼ÈëÇëÇó
	virtual int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) = 0;

	///Ô¤Âñ³·µ¥Â¼ÈëÇëÇó
	virtual int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) = 0;

	///±¨µ¥²Ù×÷ÇëÇó
	virtual int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) = 0;

	///²éÑ¯×î´ó±¨µ¥ÊýÁ¿ÇëÇó
	virtual int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) = 0;

	///Í¶×ÊÕß½áËã½á¹ûÈ·ÈÏ
	virtual int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;

	///ÇëÇóÉ¾³ýÔ¤Âñµ¥
	virtual int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) = 0;

	///ÇëÇóÉ¾³ýÔ¤Âñ³·µ¥
	virtual int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;

	///ÇëÇó²éÑ¯±¨µ¥
	virtual int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) = 0;

	///ÇëÇó²éÑ¯³É½»
	virtual int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²Ö
	virtual int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) = 0;

	///ÇëÇó²éÑ¯×Ê½ðÕË»§
	virtual int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕß
	virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½»Ò×±àÂë
	virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;

	///ÇëÇó²éÑ¯ºÏÔ¼±£Ö¤½ðÂÊ
	virtual int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) = 0;

	///ÇëÇó²éÑ¯ºÏÔ¼ÊÖÐø·ÑÂÊ
	virtual int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½»Ò×Ëù
	virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;

	///ÇëÇó²éÑ¯ºÏÔ¼
	virtual int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) = 0;

	///ÇëÇó²éÑ¯ÐÐÇé
	virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕß½áËã½á¹û
	virtual int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) = 0;

	///ÇëÇó²éÑ¯×ªÕÊÒøÐÐ
	virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²ÖÃ÷Ï¸
	virtual int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) = 0;

	///ÇëÇó²éÑ¯¿Í»§Í¨Öª
	virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½áËãÐÅÏ¢È·ÈÏ
	virtual int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕß³Ö²ÖÃ÷Ï¸
	virtual int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) = 0;

	///ÇëÇó²éÑ¯±£Ö¤½ð¼à¹ÜÏµÍ³¾­¼Í¹«Ë¾×Ê½ðÕË»§ÃÜÔ¿
	virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;

	///ÇëÇó²éÑ¯²Öµ¥ÕÛµÖÐÅÏ¢
	virtual int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Í¶×ÊÕßÆ·ÖÖ/¿çÆ·ÖÖ±£Ö¤½ð
	virtual int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½»Ò×Ëù±£Ö¤½ðÂÊ
	virtual int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½»Ò×Ëùµ÷Õû±£Ö¤½ðÂÊ
	virtual int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) = 0;

	///ÇëÇó²éÑ¯×ªÕÊÁ÷Ë®
	virtual int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) = 0;

	///ÇëÇó²éÑ¯ÒøÆÚÇ©Ô¼¹ØÏµ
	virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Ç©Ô¼ÒøÐÐ
	virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Ô¤Âñµ¥
	virtual int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) = 0;

	///ÇëÇó²éÑ¯Ô¤Âñ³·µ¥
	virtual int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) = 0;

	///ÇëÇó²éÑ¯½»Ò×Í¨Öª
	virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;

	///ÇëÇó²éÑ¯¾­¼Í¹«Ë¾½»Ò×²ÎÊý
	virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;

	///ÇëÇó²éÑ¯¾­¼Í¹«Ë¾½»Ò×Ëã·¨
	virtual int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;

	///ÆÚ»õ·¢ÆðÒøÐÐ×Ê½ð×ªÆÚ»õÇëÇó
	virtual int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;

	///ÆÚ»õ·¢ÆðÆÚ»õ×Ê½ð×ªÒøÐÐÇëÇó
	virtual int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;

	///ÆÚ»õ·¢Æð²éÑ¯ÒøÐÐÓà¶îÇëÇó
	virtual int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) = 0;
protected:
	~CThostFtdcTraderApi(){};
};

#endif
