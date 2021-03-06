/////////////////////////////////////////////////////////////////////////
///@system 0400060307¨²050306¡Á09¨´03080106
///@company 070302050403030104030304040408010704030701000906
///@file ThostFtdcMdApi.h
///@brief 09¡§06020909070103¡ì090905070703
///@history 
///20060106	090802¨¨¨º03		070705¡§000102020406
/////////////////////////////////////////////////////////////////////////

#if !defined(THOST_FTDCMDAPI_H)
#define THOST_FTDCMDAPI_H

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "ThostFtdcUserApiStruct.h"

#if defined(ISLIB) && defined(WIN32)
#ifdef LIB_MD_API_EXPORT
#define MD_API_EXPORT __declspec(dllexport)
#else
#define MD_API_EXPORT __declspec(dllimport)
#endif
#else
#define MD_API_EXPORT 
#endif

class CThostFtdcMdSpi
{
public:
	///08¡À070103¡ì09090705050306¡Á02¨®00¡§05¡§0904040801¡§04030901050708¡À05¡§030102070805000405¡ã050805010001¡¤05¡¤¡§¡À0308¡Â07010305
	virtual void OnFrontConnected(){};
	
	///08¡À070103¡ì09090705050306¡Á02¨®00¡§01¡§0403090105070903070908¡À05010001¡¤05¡¤¡§¡À0308¡Â0701030508¡À¡¤0407¨²0909000205¨¦070202¨®0501API03¨¢¡Á08090400010400090105070501070103¡ì090907070503¡Á02070708¨ª0305
	///@param nReason 07¨ª02¨®080206¨°
	///        0x1001 01030004090908¡ì¡ã05
	///        0x1002 01030004040708¡ì¡ã05
	///        0x2001 0507080904020003060108¡À
	///        0x2002 ¡¤0409010402000308¡ì¡ã05
	///        0x2003 0809080507¨ª02¨®¡À¡§0202
	virtual void OnFrontDisconnected(int nReason){};
		
	///04020003060108¡À06040003030508¡À06¡è08¡À0401020708090805¡À¡§020208¡À05010001¡¤05¡¤¡§¡À0308¡Â07010305
	///@param nTimeLapse 06¨¤08050703070205070809¡À¡§0202080208¡À0401
	virtual void OnHeartBeatWarning(int nTimeLapse){};
	

	///08050004050505¨®03¨¬0707
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///08050602050505¨®03¨¬0707
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///07¨ª02¨®07070708
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///09080802040405¨¦07070708
	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///0603030409080802040405¨¦07070708
	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///07060906040405¨¦01¡§0009
	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {};
};

class MD_API_EXPORT CThostFtdcMdApi
{
public:
	///070705¡§MdApi
	///@param pszFlowPath 070300¨¹090808020403030402020406080202070004050102010603020908¡À05¡ã02070004
	///@return 070705¡§06020802UserApi
	///modify for udp marketdata
	static CThostFtdcMdApi *CreateFtdcMdApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false);
	
	///0706060505070703090803¨®¡À0607¨ª
	///@remark 0503080208010701¡À0605070703090803¨®08¡À,08¡Â07010001020408050706060505070703090803¨®
	virtual void Release() = 0;
	
	///060108040304
	///@remark 0601080403040809040403¡¤0606,0003070408¡Â070102¨®,0507070305030709080401¡è¡Á¡Â
	virtual void Init() = 0;
	
	///08060705050707030308060005¨¢080308090404
	///@return 030806000109060207¨²0005
	virtual int Join() = 0;
	
	///0309060308¡À05¡ã050306¡Á0609
	///@retrun 0309060308050802050306¡Á0609
	///@remark 00030704080500040607010702¨®,0503020508010805090506¡¤0802050306¡Á0609
	virtual const char *GetTradingDay() = 0;
	
	///¡Á0405¨¢05¡ã000103¨²01030004080100¡¤
	///@param pszFrontAddress050205¡ã000103¨²01030004080100¡¤0305
	///@remark 01030004080100¡¤0802000908050209050203¡ãprotocol://ipaddress:port03¡À05010604050203¡Àtcp://127.0.0.1:1700103¡À0305 
	///@remark 03¡ãtcp03¡À07¨²¡À¨ª07000801040206¨¦050103¡ã127.0.0.103¡À07¨²¡À¨ª¡¤06020904¡Â080100¡¤030503¡À1700103¡À07¨²¡À¨ª¡¤06020904¡Â0909070302030305
	virtual void RegisterFront(char *pszFrontAddress) = 0;
	
	///¡Á0405¨¢0104¡Á00¡¤06020904¡Â01030004080100¡¤
	///@param pszNsAddress05020104¡Á00¡¤06020904¡Â01030004080100¡¤0305
	///@remark 01030004080100¡¤0802000908050209050203¡ãprotocol://ipaddress:port03¡À05010604050203¡Àtcp://127.0.0.1:1200103¡À0305 
	///@remark 03¡ãtcp03¡À07¨²¡À¨ª07000801040206¨¦050103¡ã127.0.0.103¡À07¨²¡À¨ª¡¤06020904¡Â080100¡¤030503¡À1200103¡À07¨²¡À¨ª¡¤06020904¡Â0909070302030305
	///@remark RegisterNameServer070303060703RegisterFront
	virtual void RegisterNameServer(char *pszNsAddress) = 0;
	
	///¡Á0405¨¢0104¡Á00¡¤06020904¡Â070103¡ì04030304
	///@param pFensUserInfo0502070103¡ì040303040305
	virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;
	
	///¡Á0405¨¢030108¡Â05070703
	///@param pSpi 030707¨²¡Á08030108¡Â0507070308¨¤080208080805
	virtual void RegisterSpi(CThostFtdcMdSpi *pSpi) = 0;
	
	///09080802040405¨¦0305
	///@param ppInstrumentID 02030804ID  
	///@param nCount 060909080802/01090908040405¨¦08020203080400020805
	///@remark 
	virtual int SubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;

	///01090908040405¨¦0305
	///@param ppInstrumentID 02030804ID  
	///@param nCount 060909080802/01090908040405¨¦08020203080400020805
	///@remark 
	virtual int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;

	///070103¡ì08050004050505¨®
	virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;
	

	///08050602050505¨®
	virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;
protected:
	~CThostFtdcMdApi(){};
};

#endif
