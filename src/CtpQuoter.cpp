#include "CtpQuoter.h"
#include "trader.h"
#include <deque>
CtpQuoter::CtpQuoter(Quoter *quoter):qsem(0)
{

	this->running=1;
	/*
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(TRADE_DIR);
	this->trade_api=trade_api;
	CtpTradeSpi* trade_spi = new CtpTradeSpi(trade_api,trader);
	this->trade_spi = trade_spi;
	cout<<"begin api"<<endl;
	trade_api->RegisterSpi((CThostFtdcTraderSpi*)trade_spi);			// ע���¼���
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// ע�ṫ����
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // ע��˽����
	trade_api->RegisterFront((char*)trader->trade_addr.c_str());	// ע�ύ��ǰ�õ�ַ
	trade_api->Init();
	cout<<"end api"<<endl;
	*/
	/*
	CThostFtdcMdApi *quote_api = CThostFtdcMdApi::CreateFtdcMdApi(QUOTE_DIR);
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
	/*����Ӷ�����ȡ���ݣ����д���*/
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
				/*�Ժ����Ҫ���������ݵ������߳�������
				*/
				this->DepthMarketProcess(msg);
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
	*/
	cerr<<"in DepthMarketProcess"<<std::endl;
	QOnRtnDepthMarketData_t *mdata=(QOnRtnDepthMarketData_t*)msg.data;
	assert(msg.type==QOnRtnDepthMarketData);
	int msec=mdata->pDepthMarketData.UpdateMillisec;
	int  sec=atoi(mdata->pDepthMarketData.UpdateTime);
	string contract=mdata->pDepthMarketData.InstrumentID;
	float  v=(mdata->pDepthMarketData.LastPrice);
	this->mds->update(contract, v, sec, msec);

	/*
	cout<<"ҵ������         ActionDay :     "<<dmd->ActionDay<<endl;
	cout<<"����������       ExchangeID:     "<<dmd->ExchangeID<<endl;
	cout<<"����ʱ��         UpdateTime:     "<<dmd->UpdateTime<<endl;
	cout<<"����޸ĺ��� UpdateMillisec:     "<<dmd->UpdateMillisec<<endl;
	cout<<"��ԼID         InstrumentID:     "<<dmd->InstrumentID<<endl;
	cout<<"������           TradingDay:     "<<dmd->TradingDay<<endl;
	cout<<"������           ClosePrice:     "<<dmd->ClosePrice<<endl;
	cout<<"������        PreClosePrice:     "<<dmd->PreClosePrice<<endl;
	cout<<"����            OpenPrice:     "<<dmd->OpenPrice<<endl;
	cout<<"��߼�         HighestPrice:     "<<dmd->HighestPrice<<endl;
	cout<<"��ͼ�          LowestPrice:     "<<dmd->LowestPrice<<endl;
	cout<<"���ν����  SettlementPrice:     "<<dmd->SettlementPrice<<endl;
	cout<<"�ϴν����  PreSettlementPrice:  "<<dmd->PreSettlementPrice<<endl;
	cout<<"��ͣ���    UpperLimitPrice:     "<<dmd->UpperLimitPrice<<endl;
	cout<<"��ͣ���    LowerLimitPrice:     "<<dmd->LowerLimitPrice<<endl;
	cout<<"����ʵ��           PreDelta:     "<<dmd->PreDelta<<endl;
	cout<<"����ʵ��          CurrDelta:     "<<dmd->CurrDelta<<endl;
	cout<<"����                 Volume:     "<<dmd->Volume<<endl;
	cout<<"�ɽ����           Turnover:     "<<dmd->Turnover<<endl;
	cout<<"�ֲ���         OpenInterest:     "<<dmd->OpenInterest<<endl;
	cout<<"��1               BidPrice1:     "<<dmd->BidPrice1<<endl;
	cout<<"���¼�            LastPrice:     "<<dmd->LastPrice<<endl;
	cout<<"��2               BidPrice2:     "<<dmd->BidPrice2<<endl;
	cout<<"��3               BidPrice3:     "<<dmd->BidPrice3<<endl;
	cout<<"��4               BidPrice4:     "<<dmd->BidPrice4<<endl;
	cout<<"��5               BidPrice5:     "<<dmd->BidPrice5<<endl;
	cout<<"��1               AskPrice1:     "<<dmd->AskPrice1<<endl;
	cout<<"��2               AskPrice1:     "<<dmd->AskPrice2<<endl;
	cout<<"��3               AskPrice1:     "<<dmd->AskPrice3<<endl;
	cout<<"��4               AskPrice1:     "<<dmd->AskPrice4<<endl;
	cout<<"��5               AskPrice1:     "<<dmd->AskPrice5<<endl;
	cout<<"����           AveragePrice:     "<<dmd->AveragePrice<<endl;
	*/

	/*
		we should not hold msg->data now.
	*/
	//mdata->pDepthMarketData->
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
	Ŀǰ���и�Quote��ص���Ϣ���������ﴦ��.
	��������ص���Ϣ����������һ��״̬��������
	loop, ����Ƿ���� key, �����ڣ�sleep ��log.
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