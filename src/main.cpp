#include <iostream>
#include "CtpTraderSpi.h"
#include "CSem.h"
#include <algorithm>
#include <vector>
#include "sqlite3.h"
#include "CtpTrader.h"
#include "CtpQuoter.h"
#include "config.h"
#include "trader.h"
#include "datalocal.h"
#include "ntp.h"
#include "luajit_support.h"
#include <boost/regex.hpp>
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>
#include "mdseries.h"
#include "boosthelp.h"

#include "quote_io.h"
#include "log.h"

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
Trader *g_trader;
CtpQuoter *g_ctp_quoter;
CtpTrader *g_ctp_trader;
mdservice *g_mdservice;
dmgr      *g_dmgr;

int ctp_trade_init()
{
		g_trader=new Trader(g_username,g_password,g_brokerid,g_trade_addr);
		g_ctp_trader=new CtpTrader(g_trader,g_dmgr,TRADE_DIR);
		g_ctp_trader->init();
		g_trade_tg.add_thread(new boost::thread(trader_loop,g_ctp_trader,0));
		g_ctp_trader->start();
		LOG_DEBUG<<"g_ctp_trader started"<<std::endl;
		return 0;
}


int ctp_quote_init()
{
		int i;
		g_quoter=new Quoter(g_username,g_password,g_brokerid,g_quote_addr);
		printf("Quoter\n");
		g_ctp_quoter=new CtpQuoter(g_quoter,QUOTE_DIR);
		g_mdservice=new mdservice();

		g_ctp_quoter->init(g_mdservice);
		g_ctp_quoter->mds->regmd("IF1404");
		for (i=0;i< CTP_WORK_THREAD_NUM;i++){
			g_quote_tg.add_thread(new boost::thread(DepthMarketProcess,g_ctp_quoter,i));
		}
		g_quote_tg.add_thread(new boost::thread(quote_loop,g_ctp_quoter));
		g_ctp_quoter->start();
		g_io_tg.add_thread(new boost::thread(quote_io_work));

}

int  ctp_work()
{
		//ctp_quote_init();
		ctp_trade_init();
#if 0
		msg_t *msg=new(msg_t);
		msg->len=sizeof(QOnFrontConnected_t);
		msg->data=new(QOnFrontConnected_t);
		msg->type=QOnFrontConnected;
		printf("OnFront Connect DEBUG\n");
    		g_ctp_quoter->post_msg(msg);
#endif


		/*

		创建一组线程，负责各个合约的定时更新行情。
		*/
		while(1){
			sleep(1);
			cerr<<" main loop sleep 1"<<std::endl;
		}
		getchar();
		return 0;
}


int main(int argc, char * argv[]){
	log_init();

	datalocal *dt=new datalocal(g_db_tdata);
	datalocal *ds=new datalocal(g_db_sdata);
	datalocal *dk=new datalocal(g_db_kdata);

	dt->create_tdata_table("IF1404");
	g_dmgr=new (dmgr);
	g_dmgr->regdb("tdata",dt);
	g_dmgr->regdb("sdata",ds);
	g_dmgr->regdb("kdata",dk);
	g_dmgr->init();


	vector<map<string,string> > rows;
	dt->exe_cmd("select name from sqlite_master where type='table'",rows);
	dt->get_product_list(g_product_list);
		for(int i=0;i<g_product_list.size();i++) {
		printf("%s\n",g_product_list[i].c_str());
	}

	g_quote_io.reg_dmgr(g_dmgr);
	ctp_work();
	getchar();
	
	/*
	  CThostFtdcTraderApi* pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("./tlog");
	  pUserApi->Join();
	  pUserApi->Release();
	*/

    	/*
	   test1();
	   getchar();
	   std::string line;
       boost::regex pat( "^Subject: (Re: |Aw: )*(.*)" );
       while (std::cin)
       {
       break;
       std::getline(std::cin, line);
       boost::smatch matches;
       if (boost::regex_match(line, matches, pat))
       std::cout << matches[2] << std::endl;
       }
       ntpdate();
       luajit_demo();
	*/
	return 0;
}
