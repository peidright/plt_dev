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

#include "StrategyFrame.h" 
#include "Python.h"

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
		LOG_DEBUG<<"g_ctp_trader started"<<std::endl;
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
		for(i=0;i<count;i++) {
			//regmd
			//1.to fix this code, rebuild. 2. if new inst, we need regmd...
			g_ctp_quoter->mds->regmd(ppinstn[i], g_ctp_quoter->pinstmgr->instmap[ppinstn[i]]);

			//reg one minute k
			ret=g_ctp_quoter->mds->regmd_period(ppinstn[i],MINUTE,1);
			LOG_DEBUG<<"regmd:"<<ppinstn[i]<<" period: 1"<<std::endl;
			assert(ret==0);
			g_ctp_quoter->mds->loadmd_period(ppinstn[i], 1, g_dmgr);
		}

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

	dt->create_tdata_table("IF1404");
	g_dmgr=new (dmgr);
	g_dmgr->regdb("tdata",dt);
	g_dmgr->regdb("sdata",ds);
	g_dmgr->regdb("kdata",dk);

	g_instmgr=new instmgr(g_dmgr);
	g_instmgr->load_inst();
	g_dmgr->pquote_io=g_quote_io;
	g_dmgr->init();

	vector<map<string,string> > rows;
	dt->exe_cmd("select name from sqlite_master where type='table'",rows);
	dt->get_product_list(g_product_list);
		for(int i=0;i<g_product_list.size();i++) {
		printf("%s\n",g_product_list[i].c_str());
	}

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
		LOG_DEBUG<<"DB_INIT"<<std::endl;
		ctp_trade_init(TRADE_DIR);
		
		while(g_instmgr->is_last()==0) {
			LOG_DEBUG<<"wait for instmgr is_last"<<std::endl;
			sleep(10);
			i++;
			if(i%3==0) {
				LOG_DEBUG<<"for debug set last"<<std::endl;
				g_instmgr->set_last(1);
			}
		}
		LOG_DEBUG<<"TRADE_FINISHED"<<std::endl;
		i=0;
		ctp_quote_init(QUOTE_DIR);
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

void printDict(PyObject* obj) {
	if (!PyDict_Check(obj))
		return;
	PyObject *k, *keys;
	keys = PyDict_Keys(obj);
	for (int i = 0; i < PyList_GET_SIZE(keys); i++) {
		k = PyList_GET_ITEM(keys, i);
		char* c_name = PyString_AsString(k);
		printf("%s/n", c_name);
	}
}

extern "C" void initsframe_agent();
int python_demo()
{

	PyObject *pName,*pModule,*pDict,*pFunc,*pArgs;
	// 载入名为pytest的脚本
	
	Py_Initialize();
	if (!Py_IsInitialized())
		return -1;
	PyRun_SimpleString("import sys");
	initsframe_agent();


	PyRun_SimpleString("import sframe_agent");
	PyRun_SimpleString("sys.path.append('./')");
	PyRun_SimpleString("print 'aaa'");
	//PyRun_SimpleString("import test");
	pName = PyString_FromString("test");
	pModule = PyImport_Import(pName);
	PyObject *pyfile = PyFile_FromString("test.py","r"); 
	FILE *f = PyFile_AsFile(pyfile); 
	PyRun_AnyFileEx(f,"test.py",0);


	//PyRun_SimpleString("help(sframe)");
	PyRun_SimpleString("print sframe");
	////PyRun_SimpleString("print sframe.put_msg(1)");



							//导入模块
							//PyObject* pModule = PyImport_ImportModule("testpy");
							//if (!pModule) {
							//printf("Cant open python file!/n");
							//return -1;
							//}
							////模块的字典列表
							//PyObject* pDict = PyModule_GetDict(pModule);
							//if (!pDict) {
							//printf("Cant find dictionary./n");
							//return -1;
							//}
							////打印出来看一下
							//printDict(pDict);
							////演示函数调用
							//PyObject* pFunHi = PyDict_GetItemString(pDict, "sayhi");
							//PyObject_CallFunction(pFunHi, "s", "lhb");
							//Py_DECREF(pFunHi);
							////演示构造一个Python对象，并调用Class的方法
							////获取Second类
							//PyObject* pClassSecond = PyDict_GetItemString(pDict, "Second");
							//if (!pClassSecond) {
							//printf("Cant find second class./n");
							//return -1;
							//}
							////获取Person类
							//PyObject* pClassPerson = PyDict_GetItemString(pDict, "Person");
							//if (!pClassPerson) {
							//printf("Cant find person class./n");
							//return -1;
							//}
							////构造Second的实例
							//PyObject* pInstanceSecond = PyInstance_New(pClassSecond, NULL, NULL);
							//if (!pInstanceSecond) {
							//printf("Cant create second instance./n");
							//return -1;
							//}
							////构造Person的实例
							//PyObject* pInstancePerson = PyInstance_New(pClassPerson, NULL, NULL);
							//if (!pInstancePerson) {
							//printf("Cant find person instance./n");
							//return -1;
							//}
							////把person实例传入second的invoke方法
							//PyObject_CallMethod(pInstanceSecond, "invoke", "O", pInstancePerson);
							////释放
							//Py_DECREF(pInstanceSecond);
							//Py_DECREF(pInstancePerson);
							//Py_DECREF(pClassSecond);
							//Py_DECREF(pClassPerson);
							//Py_DECREF(pModule);
							Py_Finalize();
							//return 0;
	return 0;
};
int main(int argc, char * argv[]){

	python_demo();
	exit(0);
	/*
	log_init();
	ctp_work();
	*/
	getchar();
	return 0;
}

/*
   tm_test();
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

