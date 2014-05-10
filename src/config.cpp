#include "config.h"
#include <vector>
using namespace std;

TThostFtdcBrokerIDType appId;		// 应用单元
TThostFtdcUserIDType userId;		// 投资者代码

extern int requestId; 
extern CSem sem;

// 会话参数
int	 frontId;	//前置编号
int	 sessionId;	//会话编号
char orderRef[13];


//Trader *trader= Trader(string username,string password,string brokerid,string trade_addr);
#if 0
string g_username="00000071";
string g_password="123456";
string g_brokerid="1017";
string g_trade_addr="tcp://ctpmn1-front1.citicsf.com:51205";
string g_quote_addr="tcp://ctpmn1-front1.citicsf.com:51213";

#else
string g_username="000000";
string g_password="2xxx";
string g_brokerid="6000";
string g_trade_addr="tcp://180.166.132.66:41205";
string g_quote_addr="tcp://180.166.132.66:41213";
#endif
string g_db_tdata="tdata.sdb";
string g_db_kdata="kdata.sdb";
string g_db_sdata="sdata.sdb";

vector<string> g_product_list;
