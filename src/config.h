#ifndef CONFIG_H_
#define CONFIG_H_


#include <iostream>
#include <vector>
//#include <sys/sem.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "CtpTrade.h"
#include "ThostFtdcTraderApi.h"
#include "CtpTraderSpi.h"
#include "CSem.h"


using namespace std;
extern TThostFtdcBrokerIDType appId;		// 应用单元
extern TThostFtdcUserIDType userId;		// 投资者代码

extern int requestId; 
extern CSem sem;
#define PROD_INFO "Q7 7994"
#define CTP_WORK_THREAD_NUM 8
// 会话参数
extern int	 frontId;	//前置编号
extern int	 sessionId;	//会话编号
extern char orderRef[13];

#define TRADE_DIR "./tlog"
#define QUOTE_DIR "./qlog"

typedef enum LoginStatus {
	SUCESS=0,
	LOGIN=1,
	FAIL=2
}LoginStatus;


#define MAX_INSTS 1000

extern string g_username;
extern string g_password;
extern string g_brokerid;
extern string g_trade_addr;
extern string g_quote_addr;
extern vector<string> g_product_list;
extern string g_db_tdata;
extern string g_db_kdata;
extern string g_db_sdata;

#endif
