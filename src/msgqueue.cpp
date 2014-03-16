#include "msgqueue.h"
#include <deque>
std::deque<msg_t> control_msg;
//deque<msg_t> g_quote_msg;
std::deque<msg_t> priority_msg;
std::deque<msg_t> g_quote_queue;

boost::interprocess::interprocess_semaphore g_quote_sem(0);
boost::timed_mutex g_quote_mutex;
void strategy_stm()
{
	/* post */

}
void quote_stm()
{
	/*fix mem status,tecical indi, send msg to strategy,quote_io*/
	//msg_t quote;
	while(1) {

	}
}

void trade_stm(msg_t &msg)
{
	while(msg.type!=QSTOP) {
	switch(msg.type) {
		/**/
	    case TOnFrontConnected:
			/*login and QSTOP*/
			break;
		case TReqUserLogin:
			break;
		case TOnRspUserLogin:
			break;
		case TReqSettlementInfoConfirm:
			break;
		case TOnRspSettlementInfoConfirm:
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
		case TOnFrontDisconnected:
			break;
		case TOnHeartBeatWarning:
			break;
		case TOnRspError:
			break;
		case TRADE_QUOTE:
			break;
		default:
			break;
	}
	}
}

void quote_stm(msg_t &msg)
{
	switch(msg.type) {
		/**/
		case TRADE_QUOTE:
			break;

        /**/
		case QOnFrontConnected:
			break;
		case QOnFrontDisconnected:
			break;
		case QOnHeartBeatWarning:
			break;
		case QOnRspError:
			break;
		case QOnRspSubMarketData:
			break;
		case QOnRspUnSubMarketData:
			break;
		case QReqUserLogin:
			break;
		case QOnRspUserLogin:
			break;
		case QOnRspUserLogout:
			break;
		case QOnRtnDepthMarketData:
			break;
		default:
			break;
	}
}

void trade_process()
{

}
void quote_process()
{
	/*每个合约,hash到一个key.每个线程，只负责等待这个合约的信号*/
	while(1) {
		g_quote_sem.wait();
		if(g_quote_queue.size() > 0)  {
			boost::unique_lock<boost::timed_mutex> lk(g_quote_mutex,boost::chrono::milliseconds(1));
			if(lk) {
				std::deque<msg_t> quote_queue;
				quote_queue.swap(g_quote_queue);
				lk.unlock();

				for(std::deque<msg_t>::iterator it=quote_queue.begin();it!=quote_queue.end();it++) {
					quote_stm(*it);
				}
				quote_queue.clear();
			}else {
				std::cout<<"dead locked ??"<<std::endl;
			}
		}else {
			std::cout<<"size zero"<<std::endl;
		}
	}
}



