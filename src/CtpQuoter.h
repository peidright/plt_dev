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

/*
typedef struct  {
	msgtype type;
	int     len;
	void    *data;
}msg_t;
*/


class CtpQuoter{
public:
	//CtpTradeSpi * trade_spi;
	//CThostFtdcTraderApi* trade_api
	CtpQuoteSpi *quote_spi;
	CThostFtdcMdApi *quote_api;
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


	CtpQuoter(Quoter *quoter);
	CtpQuoter(const CtpQuoter &);
	int  init(mdservice *mds);
	void start();
	void post_msg(msg_t *msg);
	void quote_stm(msg_t &msg);
	int SubscribeMarketData();
	int DepthMarketProcess(msg_t &msg);

	//int ReqUserLogin(char *broker, char *username, char *password);
};

void DepthMarketProcess(CtpQuoter *ctpquoter, int key);

#endif