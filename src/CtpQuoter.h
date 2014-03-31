#ifndef CTPQUOTER1_H_
#define CTPQUOTER1_H_

#include "CtpQuote.h"
#include "CtpTrade.h"

#include <deque>
#include <map>
#include "boosthelp.h"
#include "msgqueue.h"
#include "mdseries.h"

class CtpTradeSpi;
class CtpQuoteSpi;
class dmgr;

/*
typedef struct  {
	msgtype type;
	int     len;
	void    *data;
}msg_t;
*/


class CtpQuoter{
public:
	CtpQuoteSpi *quote_spi;
	CThostFtdcMdApi *quote_api;
	dmgr *pdmgr;
	mdservice *mds;
	int running;
	std::deque<msg_t> mqueue;
	Quoter *quoter;

	boost::interprocess::interprocess_semaphore qsem;
    	boost::timed_mutex qmutex;
	
	map<int, boost::timed_mutex *> qmutex_map;
	map<int, boost::interprocess::interprocess_semaphore* > qsem_map;
	map<int, std::deque<msg_t> > mqueue_map;

	//ctpquoter->qsem_map[key].wait();
	//boost::unique_lock<boost::timed_mutex> lk(ctpquoter->qmutex_map[key],boost::chrono::milliseconds(1));
	//ctpquoter->qqueue[key].size()<=0)


	CtpQuoter(Quoter *quoter,dmgr *pdmgr, string localdir);
	CtpQuoter(const CtpQuoter &);
	int  init(mdservice *mds);
	void start();
	void post_msg(msg_t *msg);
	void post_msg(msg_t *msg, string contract);
	void quote_stm(msg_t &msg);
	int SubscribeMarketData();
	int DepthMarketProcess(msg_t &msg);

	//int ReqUserLogin(char *broker, char *username, char *password);
};

void DepthMarketProcess(CtpQuoter *ctpquoter, int key);
void quote_loop(CtpQuoter *ctpquoter);

#endif
