#ifndef STRATEGY_FRAME_H_
#define STRATEGY_FRAME_H_
#include <json/json.h>
#include "boosthelp.h"
#include "msgqueue.h"
#include "strategy_config.h"
#include "CtpTrader.h"
#include "CtpQuoter.h"

using namespace std;


#include <map>
#include <deque>
#include <string>

class CtpTrader;
class CtpQuoter;


enum symsg_type {
	TCHANGE,
	KCHANGE,
	TMSSAGE,
};

enum symsg_subtype {
	OLD,
	NEW,
};

typedef struct symsg_tchange_s {
	symsg_subtype subtype;
	float v;
}symsg_tchange_t;

typedef struct symsg_kchange_s {
	symsg_subtype subtype;
	float o;
	float c;
	float h;
	float l;
}symsg_kchange_t;


typedef struct  symsg_s{
	symsg_type type;
	int     len;
	void    *data;
}symsg_t;


class msgpipe_t {
	public:
	msgpipe_t():qsem(0){
	};
	boost::interprocess::interprocess_semaphore qsem;
	boost::timed_mutex  qmutex;
	deque<msg_t> msgqueue;
};	

class sframe {
	public:
	map<int,msgpipe_t * > pipemap;
	boost::timed_mutex  smutex;
	int base_key;
	string msg;
	int put_msg(msg_t *msg,int key);
	msg_t  get_msg(int key);
	int reg_agent_key();
	int dispatch();
    int dispatchsyn(msg_t msg);
    sframe();
    msg_t dispatchsynret(msg_t msg);

	int test(int key);
    int init(CtpQuoter *ctpquoter, CtpTrader *ctptrader);
	boost::thread_group stg;

    class CtpQuoter *ctpquoter;
    class CtpTrader *ctptrader;
	int run(strategy_config_t &config);
};

extern sframe g_sframe;

class sframe_agent{
	public:
	int agent_key;
	int put_msg(string msg);
	string get_msg();
    int dispatchsyn(string msg);
    string dispatchsynret(string msg);
	int    init();
	private:
	class sframe  *psframe;
	msg_t pystr2msg(string str);
	string msg2pystr(msg_t msg);
};

int sframe_put_msg(msg_t *msg, int key);
int sframe_quote_kchange(float o,float c, float h, float l, int sec,int msec,int subtype, int key);
int sframe_quote_tchange(float v, int sec, int msec, int subtype, int key);
extern void typeval_init();
extern "C" void initsframe_agent();

#endif
