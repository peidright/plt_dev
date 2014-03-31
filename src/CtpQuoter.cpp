#include "CtpQuoter.h"
#include "trader.h"
#include <deque>
#include "help.h"
#include "quote_io.h"
CtpQuoter::CtpQuoter(Quoter *quoter,string localdir):qsem(0)
{

	this->running=1;
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
	CThostFtdcMdApi *quote_api = CThostFtdcMdApi::CreateFtdcMdApi(localdir.c_str());
	CtpQuoteSpi *quote_spi = new CtpQuoteSpi(quote_api,quoter);
	this->qupte_spi=quote_spi;
	this->quote_api=quote_api;

	quote_api->RegisterSpi((CThostFtdcMdSpi*)quote_spi);
	quote_api->RegisterFront((char*)quoter->quote_addr.c_str());
	quote_api->Init();
	cout<<"i am here"<<endl;
	getchar();
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
	this->quote_api=quote_api;
	this->quote_spi=quote_spi;
	quote_api->RegisterSpi((CThostFtdcMdSpi*)quote_spi);
			printf("3\n");
	quote_api->RegisterFront((char*)quoter->quote_addr.c_str());
			printf("4\n");
	quote_api->Init();
	
	printf("quote_api sleep 1 finished\n");
	sleep(1);
	/*
	msg_t *msg=new(msg_t);
	msg->len=sizeof(QOnFrontConnected_t);
	msg->data=new(QOnFrontConnected_t);
	msg->type=QOnFrontConnected;
	printf("OnFront Connect DEBUG\n");
	this->post_msg(msg);
	*/

	while(1){
		sleep(1);
		break;
	}	
	cout<<"i am here"<<endl;
	getchar();
}

void CtpQuoter::post_msg(msg_t *msg, string contract)
{
	/*lock
	*/
	int i=my_hash(contract);
	
again:
	boost::unique_lock<boost::timed_mutex> lk(*(this->qmutex_map[my_hash(contract)]),boost::chrono::milliseconds(1));
	if(lk) {
		this->mqueue_map[my_hash(contract)].push_back(*msg);
		this->qsem_map[my_hash(contract)]->post();
		printf("post msg\n");	
		lk.unlock();
	}else {
		/*
		   do some warnning
		*/

		goto again;
	}
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
		printf("post msg\n");	
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
	ret=this->quote_spi->api->SubscribeMarketData(ppInst, count);
	cout<<"md subscribeMarketDate cu1406!!!"<<endl;
	delete [] ppInst;
	return ret;
}
void CtpQuoter::quote_stm(msg_t &msg)
{
	/*负责从队列中取数据，进行处理*/
	msg_t *mmsg;
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
				cerr<<"sub md succed\n";
				msg.type=QSTOP;
				break;
			case QOnRspUnSubMarketData:
				break;
			case QReqUserLogin:
				#if 0
				mmsg=new(msg_t);
				mmsg->len=sizeof(QOnRspUserLogin_t);
				mmsg->data=(void*)new(QOnRspUserLogin_t);
				mmsg->type=QOnRspUserLogin;
				this->post_msg(mmsg);
				printf("fake on user Login");
				#endif


				ret= this->quote_spi->ReqUserLogin((char*)this->quoter->brokerid.c_str(),
					(char*)this->quoter->username.c_str(),
				(char*)this->quoter->password.c_str());
				if(ret==0) {
					printf("quote_stm login msg sended\n");
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
				printf("OnRspUserLogin stm\n");
				msg.type=QReqSubscribeMarketData;
				break;
			case QOnRspUserLogout:
				break;
			case QOnRtnDepthMarketData:
				/*以后可能要把行情数据单独用线程来处理
				*/
				this->DepthMarketProcess(msg);
				msg.type=QSTOP;
				break;
			default:
				break;
		}
	}
	msg.type=QSTOP;
	if(msg.type == QSTOP) {
		/*todo free message*/
		free(msg.data);
	}
	LOG_DEBUG<<"finish one Market data"<<std::endl;
}

int CtpQuoter::DepthMarketProcess(msg_t &msg)
{
	/*
		1. update market data to mem
			1.update tick data
			2.update minute data
			3.update tech data 
		2. send signal to stragte
		3. copy data to io thread to permnate

		cout<<"业务日期         ActionDay :     "<<dmd->ActionDay<<endl;
		cout<<"交易所代码       ExchangeID:     "<<dmd->ExchangeID<<endl;
		cout<<"更新时间         UpdateTime:     "<<dmd->UpdateTime<<endl;
		cout<<"最后修改毫秒 UpdateMillisec:     "<<dmd->UpdateMillisec<<endl;
		cout<<"合约ID         InstrumentID:     "<<dmd->InstrumentID<<endl;
		cout<<"交易日           TradingDay:     "<<dmd->TradingDay<<endl;
	*/
	QOnRtnDepthMarketData_t *mdata=(QOnRtnDepthMarketData_t*)msg.data;
	assert(msg.type==QOnRtnDepthMarketData);
	int msec=mdata->pDepthMarketData.UpdateMillisec;
	int  sec=date2time(string(mdata->pDepthMarketData.ActionDay)+" "+ string(mdata->pDepthMarketData.UpdateTime));
	string contract=mdata->pDepthMarketData.InstrumentID;
	float  v=(mdata->pDepthMarketData.LastPrice);
	this->mds->update(contract, v, sec, msec);
	cerr<<"Price :"<<v<<" sec: "<<sec<<" msec:" <<msec<<std::endl;
	cerr<<"Price :"<<(mdata->pDepthMarketData.LastPrice)<<" sec: "<<(mdata->pDepthMarketData.UpdateTime)<<" msec:" <<msec<<std::endl;

	//assert(0);


	/*
	cout<<"业务日期         ActionDay :     "<<dmd->ActionDay<<endl;
	cout<<"交易所代码       ExchangeID:     "<<dmd->ExchangeID<<endl;
	cout<<"更新时间         UpdateTime:     "<<dmd->UpdateTime<<endl;
	cout<<"最后修改毫秒 UpdateMillisec:     "<<dmd->UpdateMillisec<<endl;
	cout<<"合约ID         InstrumentID:     "<<dmd->InstrumentID<<endl;
	cout<<"交易日           TradingDay:     "<<dmd->TradingDay<<endl;
	cout<<"今收盘           ClosePrice:     "<<dmd->ClosePrice<<endl;
	cout<<"昨收盘        PreClosePrice:     "<<dmd->PreClosePrice<<endl;
	cout<<"今开盘            OpenPrice:     "<<dmd->OpenPrice<<endl;
	cout<<"最高价         HighestPrice:     "<<dmd->HighestPrice<<endl;
	cout<<"最低价          LowestPrice:     "<<dmd->LowestPrice<<endl;
	cout<<"本次结算价  SettlementPrice:     "<<dmd->SettlementPrice<<endl;
	cout<<"上次结算价  PreSettlementPrice:  "<<dmd->PreSettlementPrice<<endl;
	cout<<"涨停板价    UpperLimitPrice:     "<<dmd->UpperLimitPrice<<endl;
	cout<<"跌停板价    LowerLimitPrice:     "<<dmd->LowerLimitPrice<<endl;
	cout<<"昨虚实度           PreDelta:     "<<dmd->PreDelta<<endl;
	cout<<"今虚实度          CurrDelta:     "<<dmd->CurrDelta<<endl;
	cout<<"数量                 Volume:     "<<dmd->Volume<<endl;
	cout<<"成交金额           Turnover:     "<<dmd->Turnover<<endl;
	cout<<"持仓量         OpenInterest:     "<<dmd->OpenInterest<<endl;
	cout<<"最新价            LastPrice:     "<<dmd->LastPrice<<endl;
	cout<<"均价           AveragePrice:     "<<dmd->AveragePrice<<endl;
	*/
	/*
		we should not hold msg->data now.
	*/
	//mdata->pDepthMarketData->
	tdata_t *data=new(tdata_t);
	data->sec=sec;
	data->msec=msec;
	data->ask1=mdata->pDepthMarketData.AskPrice1;
	data->ask2=mdata->pDepthMarketData.AskPrice2;
	data->ask3=mdata->pDepthMarketData.AskPrice3;
	data->ask4=mdata->pDepthMarketData.AskPrice4;
	data->ask5=mdata->pDepthMarketData.AskPrice5;
	data->bid1=mdata->pDepthMarketData.BidPrice1;
	data->bid2=mdata->pDepthMarketData.BidPrice2;
	data->bid3=mdata->pDepthMarketData.BidPrice3;
	data->bid4=mdata->pDepthMarketData.BidPrice4;
	data->bid5=mdata->pDepthMarketData.BidPrice5;
	data->vol=mdata->pDepthMarketData.Volume;
	data->uprice=mdata->pDepthMarketData.UpperLimitPrice;
	data->lprice=mdata->pDepthMarketData.LowerLimitPrice;
	data->high=mdata->pDepthMarketData.HighestPrice;
	data->low=mdata->pDepthMarketData.LowestPrice;
	data->close=mdata->pDepthMarketData.OpenPrice;
	data->open=mdata->pDepthMarketData.ClosePrice;
	data->lastprice=mdata->pDepthMarketData.LastPrice;
	quote_push(contract,data);
	//data->avgprice=
	return 0;
}


void quote_loop(CtpQuoter *ctpquoter)
{
loop:
	while(ctpquoter->running) {
		ctpquoter->qsem.wait();
		boost::unique_lock<boost::timed_mutex> lk(ctpquoter->qmutex,boost::chrono::milliseconds(1));
		if (lk) {
			if(ctpquoter->mqueue.size()<=0) {
				/*bug happen*/
				cout<<"should not be zero qqueue"<<std::endl;
				lk.unlock();
			}
			msg_t msg=ctpquoter->mqueue[0];
			printf("quote_loop get this msg\n");
			ctpquoter->mqueue.pop_front();
			lk.unlock();
			//continue;
			ctpquoter->quote_stm(msg);
		} else {
			cout<<"quote main loop err"<<std::endl;
		}
	}
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
