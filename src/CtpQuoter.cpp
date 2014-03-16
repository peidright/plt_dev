#include "CtpQuoter.h"
#include "Trader.h"
#include <deque>
CtpQuoter::CtpQuoter(Quoter *quoter):qsem(0)
{
	/*
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(TRADE_DIR);
	this->trade_api=trade_api;
	CtpTradeSpi* trade_spi = new CtpTradeSpi(trade_api,trader);
	this->trade_spi = trade_spi;
	cout<<"begin api"<<endl;
	trade_api->RegisterSpi((CThostFtdcTraderSpi*)trade_spi);			// 注册事件类
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// 注册公有流
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // 注册私有流
	trade_api->RegisterFront((char*)trader->trade_addr.c_str());	// 注册交易前置地址
	trade_api->Init();
	cout<<"end api"<<endl;
	*/
	/*
	CThostFtdcMdApi *quote_api = CThostFtdcMdApi::CreateFtdcMdApi(QUOTE_DIR);
	CtpQuoteSpi *quote_spi = new CtpQuoteSpi(quote_api,quoter);
	quote_api->RegisterSpi((CThostFtdcMdSpi*)quote_spi);
	quote_api->RegisterFront((char*)quoter->quote_addr.c_str());
	quote_api->Init();
	cout<<"i am here"<<endl;
	getchar();
	*/

	/*
	md->Init();
	cout<<"market init"<<endl;
	pUserApi->Init();
	//todo
	pUserApi->Join();
	*/
	this->quoter=quoter;
}

	CtpQuoter::CtpQuoter(const CtpQuoter &):qsem(0){
		
	};
int  CtpQuoter::init(mdservice *mds)
{
	this->mds=mds;

	map<int, boost::timed_mutex *> qmutex_map;
	map<int, boost::interprocess::interprocess_semaphore* > qsem_map;
	map<int, std::deque<msg_t> > mqueue_map;
	
	for (int i=0;i<CTP_WORK_THREAD_NUM;i++){
		this->qmutex_map[i]=new boost::timed_mutex;
		this->qsem_map[i]=new boost::interprocess::interprocess_semaphore(0);
		this->mqueue_map[i]=*(new std::deque<msg_t>);
	}
	return 0;
}
void CtpQuoter::start()
{
	CThostFtdcMdApi *quote_api = CThostFtdcMdApi::CreateFtdcMdApi(QUOTE_DIR);
		printf("1\n");
	CtpQuoteSpi *quote_spi = new CtpQuoteSpi(quote_api,this);
		printf("2\n");
	quote_api->RegisterSpi((CThostFtdcMdSpi*)quote_spi);
			printf("3\n");
	quote_api->RegisterFront((char*)quoter->quote_addr.c_str());
			printf("4\n");
	quote_api->Init();
		printf("5\n");


	
	cout<<"i am here"<<endl;
	getchar();
}

void CtpQuoter::post_msg(msg_t *msg)
{
	/*lock
	*/
	
again:
	boost::unique_lock<boost::timed_mutex> lk(this->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
		this->mqueue.push_back(*msg);
		this->qsem.post();
		
		lk.unlock();
	}else {
		/*
		   do some warnning
		*/

		goto again;
	}
}

int CtpQuoter::SubscribeMarketData()
{
	int count,ret;
	count=g_product_list.size();
	char ** ppInst = (char**)new char *[MAX_INSTS];
	//char insts[MAX_INSTS][32];
	//ppInst=(char**)insts;
	//memset(insts,0x0, sizeof(insts));
	cerr<<"md login sucess: "<<count<<endl;
	//g_product_list
	assert(count <MAX_INSTS);
	for(int i=0;i<MAX_INSTS;i++) {
		ppInst[i]=(char*)0;
	}
	for(int i=0;i<count;i++) {
		    ppInst[i]=new char[32];
			strcpy(ppInst[i], g_product_list[i].c_str());
			printf("insts is %s\n",ppInst[i]);
	}
	//return;
	//char inst[32];
	//strcpy(inst, "cu1401");
	//char*ppInst[1];

	//ppInst[0] = inst;
	ret=this->quote_api->SubscribeMarketData(ppInst, count);
	cout<<"md subscribeMarketDate cu1401"<<endl;
	delete [] ppInst;
	return ret;
}
void CtpQuoter::quote_stm(msg_t &msg)
{
	/*负责从队列中取数据，进行处理*/
	int ret;
	while(msg.type!=QSTOP) {
		switch(msg.type) {
			/*        */
			case QSTART:
				this->start();
				msg.type=QSTOP;
				break;
			case QOnFrontConnected:
				cerr <<"md connected stm"<<endl;
				getchar();
				msg.type=QReqUserLogin;
				break;
			case QOnFrontDisconnected:
				break;
			case QOnHeartBeatWarning:
				/*todo err process
				*/
				break;
			case QOnRspError:
				/*todo err process
				*/
				break;
			case QReqSubscribeMarketData:
				this->SubscribeMarketData();
				msg.type=QSTOP;
				/*!!!!*/
				break;
			case QOnRspSubMarketData:
				/**/
				break;
			case QOnRspUnSubMarketData:
				break;
			case QReqUserLogin:
				ret= this->quote_spi->ReqUserLogin((char*)this->quoter->brokerid.c_str(),
					(char*)this->quoter->username.c_str(),
				(char*)this->quoter->password.c_str()
				);
				if(ret==0) {
					msg.type=QSTOP;
				}else {
					/*err process
					
					
					*/
				}
				break;
			case QOnRspUserLogin:
				/*err process
				  else subscribe
				*/
				msg.type=QReqSubscribeMarketData;
				break;
			case QOnRspUserLogout:
				break;
			case QOnRtnDepthMarketData:
				/*以后可能要把行情数据单独用线程来处理
				*/
				this->DepthMarketProcess(msg);
				break;
			default:
				break;
		}
	}
	if(msg.type == QSTOP) {
		/*todo free message*/
	}
}

int CtpQuoter::DepthMarketProcess(msg_t &msg)
{
	/*
	    这里只处理报价信息。
	    内存拥有策略所需要的全部数据，更新ma
		发信号量给策略
		
		?把数据拷贝到io线程等待入库.(暂时io直接入库)
	*/
	QOnRtnDepthMarketData_t *mdata=(QOnRtnDepthMarketData_t*)msg.data;
	assert(msg.type==QOnRtnDepthMarketData);

	
    


	/*
	   上面处理完后，不应该再有其他地方持有msg.data的指针。将 msg丢到io_queue，待入库。
	*/
	//mdata->pDepthMarketData->
	return 0;
}

void DepthMarketProcess(CtpQuoter *ctpquoter, int key)
{
	/*
	目前所有跟Quote相关的消息，都走这里处理.
	跟交易相关的信息，都另外用一个状态机处理。
	loop, 检测是否存在 key, 不存在，sleep ，log.
	*/
loop:
	if (ctpquoter->qsem_map.find(key)==ctpquoter->qsem_map.end()) {
		/*log it */
		printf("can not find this slot %d, thread sleep 3 and loop null\n",key);
		boost::chrono::milliseconds(10000);
		goto loop;
	}

	while(ctpquoter->running) {
		ctpquoter->qsem_map[key]->wait();
		boost::unique_lock<boost::timed_mutex> lk(*ctpquoter->qmutex_map[key],boost::chrono::milliseconds(1));
		if (lk) {
			if(ctpquoter->mqueue_map[key].size()<=0) {
				/*bug happen*/
				cout<<"should not be zero qqueue"<<std::endl;
				lk.unlock();
			}
			msg_t msg=ctpquoter->mqueue_map[key][0];
			ctpquoter->mqueue_map[key].pop_front();
			lk.unlock();
			ctpquoter->quote_stm(msg);
		} else {
			cout<<"depth market process lk err,thread id: "<<key<<std::endl;
		}
	}
}

/*	
boost::thread_group tg;
tg.add_thread(new boost::thread(worker,"dddd"));
*/