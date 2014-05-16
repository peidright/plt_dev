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
#include "instmgr.h"
#include "position.h"
#include "StrategyFrame.h"
class dmgr;
class instmgr;
class CtpTradeSpi;
class CtpTrader{
public:
	Trader *trader;
	CtpTradeSpi * trade_spi;
	CThostFtdcTraderApi* trade_api;
	dmgr *pdmgr;
	instmgr *pinstmgr;
	string localdir;
    map<string, position_t*> position;
    map<string, string> reqid2orderid;
    map<string, string> orderid2reqid;
    map<string, ordreq_t*> reqid2req;
    map<string, order_t*> orderid2order;

    map<string, int> orderid2sid;
    /*for 
     * */
    map<string, int> reqid2sid;
    //map<string, int> reqid2strategyid;
    
	CtpTrader(Trader *trader,dmgr *pdmgr,instmgr *pinstmgr, string localdir);
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
