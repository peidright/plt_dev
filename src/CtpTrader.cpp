#include "CtpTrader.h"
#include "trader.h"
#include <deque>
#include "help.h"


CtpTrader::CtpTrader(Trader *trader):qsem(0)
{
	this->trader=trader;
	this->running=1;
}
int CtpTrader::init()
{
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(TRADE_DIR);
	this->trade_api=trade_api;
	CtpTradeSpi* trade_spi = new CtpTradeSpi(trade_api,this);
	this->trade_spi = trade_spi;
	cout<<"begin api"<<endl;

	return 0;
}

int CtpTrader::start()
{
	trade_api->RegisterSpi((CThostFtdcTraderSpi*)this->trade_spi);			// 注册事件类
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// 注册公有流
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // 注册私有流
	trade_api->RegisterFront((char*)this->trader->trade_addr.c_str());	// 注册交易前置地址
	trade_api->Init();
	cout<<"start trade api"<<endl;
	return 0;
}


void CtpTrader::trade_stm(msg_t &msg)
{
	msg_t *mmsg;
	int ret;

	while(msg.type!=TSTOP) {
		switch(msg.type) {
			/*        */
			case TSTART:
				this->start();
				msg.type=TSTOP;
				break;
			case TOnFrontConnected:
				cerr <<"md connected stm"<<endl;
				msg.type=QReqUserLogin;
				break;
			case TOnFrontDisconnected:
				break;
			case TOnHeartBeatWarning:
				/*todo err process
				*/
				break;
			case TOnRspError:
				/*todo err process
				*/
				break;
			case TReqSettlementInfoConfirm:
				break;
			case TOnRspSettlementInfoConfirm:
				/**/
				msg.type=QSTOP;
				break;
			case TReqUserLogin:
				break;
			case TOnRspUserLogin:
				break;
			case TReqQryInstrument:
				break;
			case TOnRspQryInstrument:
				break;
			case TReqQryTradingAccount:
				break;
			case TOnRspQryTradingAccount:
				break;
			case TReqQryInvestorPosition:
				break;
			case TOnRspQryInvestorPosition:
				break;
			case TReqOrderInsert:
				break;
			case TOnRspOrderInsert:
				break;
			case TReqOrderAction:
				break;
			case TOnRspOrderAction:
				break;
			case TOnRtnOrder:
				break;
			default:
				break;
		}
	}
	msg.type=TSTOP;
	if(msg.type == TSTOP) {
		/*todo free message*/
		free(msg.data);
	}
	LOG_DEBUG<<"finish one Trade data"<<std::endl;
}

void trader_loop(CtpTrader *ctptrader, int key)
{
loop:
	while(ctptrader->running) {
		ctptrader->qsem.wait();
		boost::unique_lock<boost::timed_mutex> lk(ctptrader->qmutex,boost::chrono::milliseconds(1));
		if (lk) {
			if(ctptrader->mqueue.size()<=0) {
				/*bug happen*/
				cout<<"should not be zero qqueue"<<std::endl;
				lk.unlock();
			}
			msg_t msg=ctptrader->mqueue[0];
			printf("trader_loop get this msg\n");
			ctptrader->mqueue.pop_front();
			lk.unlock();
			//continue;
			ctptrader->trade_stm(msg);
		} else {
			cout<<"quote main loop err"<<std::endl;
		}
	}
}

void CtpTrader::post_msg(msg_t *msg)
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

