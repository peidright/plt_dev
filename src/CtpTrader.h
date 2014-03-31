#ifndef CTPTRADER_H_
#define CTPTRADER_H_
#include "CtpQuote.h"
#include "CtpTrade.h"
#include "account.h"
#include <deque>
#include <map>
#include "boosthelp.h"
#include "msgqueue.h"
#include "mdseries.h"
class dmgr;
class CtpTradeSpi;
class CtpTrader{
public:
	Trader *trader;
	CtpTradeSpi * trade_spi;
	CThostFtdcTraderApi* trade_api;
	dmgr *pdmgr;

	CtpTrader(Trader *trader,dmgr *pdmgr);
	void trade_stm(msg_t &msg);
	void post_msg(msg_t *msg);


	int init();
	int start();
	Account account; 
	int running;
	std::deque<msg_t> mqueue;
	boost::interprocess::interprocess_semaphore qsem;
    	boost::timed_mutex qmutex;
	//map<int, boost::timed_mutex *> qmutex_map;
	//map<int, boost::interprocess::interprocess_semaphore* > qsem_map;
	//map<int, std::deque<msg_t> > mqueue_map;
};
void trader_loop(CtpTrader *ctptrader, int key);

#endif
