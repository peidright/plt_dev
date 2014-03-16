#include <iostream>
#include "CtpTraderSpi.h"
#include "CSem.h"
#include <algorithm>
#include <vector>
#include "sqlite3.h"
#include "../CtpTrader.h"
#include "../CtpQuoter.h"
#include "../config.h"
#include "../trader.h"
#include "../datalocal.h"
#include "../ntp.h"
#include "../luajit_support.h"
#include <boost/regex.hpp>
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>
#include "../mdseries.h"
#include "../boosthelp.h"
using namespace std;

//请求编号
int requestId=0;

// 前置地址
char tradeFront[]="tcp://asp-sim2-front1.financial-trading-platform.com:26205";

CSem sem(0);

//vector<struct CThostFtdcOrderField *> orderList;
//vector<struct CThostFtdcTradeField *> tradeList;
extern void test1();

boost::thread_group g_quote_tg;
boost::thread_group g_trade_tg;
boost::thread_group g_io_tg;
Quoter *g_quoter;
CtpQuoter *g_ctp_quoter;
mdservice *g_mdservice;
int  ctp_work()
{
		int i;
		/*
		初始化行情登录
		*/
		g_quoter=new Quoter(g_username,g_password,g_brokerid,g_quote_addr);
		printf("Quoter\n");
		g_ctp_quoter=new CtpQuoter(g_quoter);
		printf("Ctpquoted\n");
		g_mdservice=new mdservice();
		/*
		创建线程，专门处理行情的消息
		*/
		/*
		for (i=0;i< CTP_WORK_THREAD_NUM;i++){
			g_quote_tg.add_thread(new boost::thread(DepthMarketProcess,g_ctp_quoter,i));
		}*/
		printf("mdsed\n");
		g_ctp_quoter->init(g_mdservice);
		printf("inited\n");
		g_ctp_quoter->start();
		printf("started\n");
		/*
		创建线程，专门处理交易的信息
		for (i=0;i<CTP_WORK_THREAD_NUM;i++){
			g_trade_tg.add_thread(new boost::thread(DepthMarketProcess,g_ctp_quoter,i));
		}
		*/

		/*
		创建线程，专门负责将行情信息，刷进sqlite
		for (i=0;i<CTP_WORK_THREAD_NUM;i++){
		g_io_tg.add_thread(new boost::thread(DepthMarketProcess,g_ctp_quoter,i));
		}
		*/


		/*
		创建一组线程，负责各个合约的定时更新行情。
		*/
		getchar();
		return 0;
}


int main(int argc, char * argv[]){
	test1();
	getchar();
	std::string line;
    /*
	boost::regex pat( "^Subject: (Re: |Aw: )*(.*)" );

    while (std::cin)
    {
		break;
        std::getline(std::cin, line);
        boost::smatch matches;
        if (boost::regex_match(line, matches, pat))
            std::cout << matches[2] << std::endl;
    }*/

//int main(){
	//ntpdate();
	//exit(0);
	//CThostFtdcTraderApi* pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("./tlog");
	//getchar();
	//return 0;
	//datalocal *dl=new datalocal();
	//luajit_demo();
	getchar();
	//return 0;
	cout<<"ddd1"<<endl;
	datalocal *dl=new datalocal();
	vector<map<string,string>> rows;
	cout<<"ddd2"<<endl;
	dl->exe_cmd("select name from sqlite_master where type='table'",rows);
	getchar();
	
	dl->get_product_list(g_product_list);
		for(int i=0;i<g_product_list.size();i++) {
		printf("%s\n",g_product_list[i].c_str());
	}
	
	//getchar();

	//Trader *trader=new Trader(g_username,g_password,g_brokerid,g_trade_addr);
	//CtpTrader *ctp_trader=new CtpTrader(trader);
	ctp_work();
	getchar();
	/*
	api = CThostFtdcTraderApi::CreateFtdcTraderApi("./tlog");
	api->RegisterSpi((CThostFtdcTraderSpi*)t);
	api->RegisterFront("tcp://ctpmn1-front1.citicsf.com:51205");
	api->Init();
    getchar();
	*/

	//CtpTraderSpi* pUserSpi = new CtpTraderSpi(pUserApi);
	//pUserApi->RegisterSpi((CThostFtdcTraderSpi*)pUserSpi);			// 注册事件类
	//pUserApi->SubscribePublicTopic(THOST_TERT_RESTART);					// 注册公有流
	//pUserApi->SubscribePrivateTopic(THOST_TERT_RESTART);			  // 注册私有流
	//pUserApi->RegisterFront(tradeFront);							// 注册交易前置地址
	//pUserApi->Init();
	//todo
	
	/*
	  CThostFtdcTraderApi* pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("./tlog");
	  pUserApi->Join();
	*/
    //pUserapi->
	//pUserApi->Release();
	return 0;
}
