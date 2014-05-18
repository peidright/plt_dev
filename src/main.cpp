#include <iostream>
#include "CtpTraderSpi.h"
#include "CSem.h"
#include <algorithm>
#include <vector>
#include <sqlite/sqlite3.h>
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

#include "StrategyFrame.h" 
#include "Python.h"
#include "demo.h"

#include "quote_io.h"
#include "log.h"

#include "tm.h"

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
quote_io *g_quote_io;
CtpQuoter *g_ctp_quoter;
CtpTrader *g_ctp_trader;
mdservice *g_mdservice;
dmgr      *g_dmgr;
instmgr   *g_instmgr;

int ctp_trade_init(string tradedir)
{
		g_trader=new Trader(g_username,g_password,g_brokerid,g_trade_addr);
		g_ctp_trader=new CtpTrader(g_trader,g_dmgr,g_instmgr,tradedir);
		g_ctp_trader->init();
		g_trade_tg.add_thread(new boost::thread(trader_loop,g_ctp_trader,0));
		g_ctp_trader->start();
		return 0;
}


int ctp_quote_init(string quotedir)
{
		int ret=0;
		int i,count;
		char **ppinstn;

		g_quoter=new Quoter(g_username,g_password,g_brokerid,g_quote_addr);
		g_ctp_quoter=new CtpQuoter(g_quoter,g_dmgr,g_instmgr,quotedir);
		g_mdservice=new mdservice();
		g_ctp_quoter->init(g_mdservice);
		/*
		 *todo regmd all
		 * */

		/*-1=get old, 1=get new, 0=get all*/
		g_ctp_quoter->pinstmgr->get_inst_list(&ppinstn,&count, 0);
        LOG_DEBUG<<"get_inst_list count:"<<count<<std::endl;
		for(i=0;i<count;i++) {
			//regmd
			//1.to fix this code, rebuild. 2. if new inst, we need regmd...
			g_ctp_quoter->mds->regmd(ppinstn[i], g_ctp_quoter->pinstmgr->instmap[ppinstn[i]]);

			//reg one minute k
			ret=g_ctp_quoter->mds->regmd_period(ppinstn[i],MINUTE,1);
			assert(ret==0);
			g_ctp_quoter->mds->loadmd_period(ppinstn[i], 1, g_dmgr);
		}
		LOG_DEBUG<<"ctp_quote_init get all inst and reg all the md"<<std::endl;

		for (i=0;i< CTP_WORK_THREAD_NUM;i++){
			g_quote_tg.add_thread(new boost::thread(DepthMarketProcess,g_ctp_quoter,i));
		}
		g_quote_tg.add_thread(new boost::thread(quote_loop,g_ctp_quoter));
		g_ctp_quoter->start();
		g_io_tg.add_thread(new boost::thread(quote_io_work));
}

int ctp_db_init()
{
	g_quote_io=new quote_io;

	datalocal *dt=new datalocal("datadir",g_db_tdata);
	datalocal *ds=new datalocal("datadir",g_db_sdata);
	datalocal *dk=new datalocal("datadir",g_db_kdata);

	//dt->create_tdata_table("IF1405");

	g_dmgr=new (dmgr);
	g_dmgr->regdb("tdata",dt);
	g_dmgr->regdb("sdata",ds);
	g_dmgr->regdb("kdata",dk);

	g_instmgr=new instmgr(g_dmgr);
    g_instmgr->create_inst_sdata();

	g_instmgr->load_inst();
    LOG_DEBUG<<"g_instmgr finished"<<std::endl;

	g_dmgr->pquote_io=g_quote_io;
	g_dmgr->init();

    LOG_DEBUG<<"g_dmgr    finished"<<std::endl;
    
    /*
	vector<map<string,string> > rows;
	dt->exe_cmd("select name from sqlite_master where type='table'",rows);
	dt->get_product_list(g_product_list);
		for(int i=0;i<g_product_list.size();i++) {
		printf("%s\n",g_product_list[i].c_str());
	}*/

	g_quote_io->reg_dmgr(g_dmgr);
	return 0;
}

int ctp_stragte_init()
{
	return 0;
}

int ctp_wait_loop()
{
	while(1){
		sleep(10);
		cerr<<" main loop sleep 1"<<std::endl;
	}
	return 0;
}

int ctp_debug_plug()
{
#if 0
		/*send debug msg to test all compent*/
		msg_t *msg=new(msg_t);
		msg->len=sizeof(QOnFrontConnected_t);
		msg->data=new(QOnFrontConnected_t);
		msg->type=QOnFrontConnected;
		printf("OnFront Connect DEBUG\n");
    		g_ctp_quoter->post_msg(msg);
#endif
		return 0;
}

int  ctp_work()
{
		int i=0;
		ctp_db_init();
		LOG_DEBUG<<"CTP_DB_INIT finished"<<std::endl;
		ctp_trade_init(TRADE_DIR);
		LOG_DEBUG<<"CTP_TRADE_INIT finished"<<std::endl;

		
		while(g_instmgr->is_last()==0) {
			LOG_DEBUG<<"wait for instmgr is_last"<<std::endl;
			sleep(1);
			i++;
			if(i%3==0) {
				LOG_DEBUG<<"for debug set last"<<std::endl;
				g_instmgr->set_last(1);
			}
		}
		LOG_DEBUG<<"TRADE_FINISHED"<<std::endl;
		i=0;
		ctp_quote_init(QUOTE_DIR);
        sleep(10);
        cout<<"sleep 10 finished"<<std::endl;
        g_sframe.init(g_ctp_quoter,g_ctp_trader);
        LOG_DEBUG<<"strategy begin"<<std::endl;
	    strategy_demo();

        LOG_DEBUG<<"strategy end"<<std::endl;

		ctp_wait_loop();
		while(g_ctp_quoter->is_sub()==0) {
			LOG_DEBUG<<"wait for sub market is_last"<<std::endl;
			sleep(10);
			i++;
			if(i%3==0) {
				LOG_DEBUG<<"for debug set status"<<std::endl;
				g_ctp_quoter->set_status(1);
			}

		}
		LOG_DEBUG<<"QUOTE_FINISHED"<<std::endl;

		ctp_stragte_init();
		//ctp_debug_plug();
		ctp_wait_loop();
		return 0;
}



int main(int argc, char * argv[]){

	//ctp_wait_loop();
	//python_demo();
	//exit(0);
	/*
     *
	*/
	log_init();
	ctp_work();
	getchar();
	return 0;
}
