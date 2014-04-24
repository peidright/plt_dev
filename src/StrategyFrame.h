#ifndef STRATEGY_FRAME_H_
#define STRATEGY_FRAME_H_
#include "json/json.h"
#include "boosthelp.h"
#include "msgqueue.h"
#include "strategy_config.h"
#include <boost/python.hpp>
using namespace boost::python;
using namespace std;


#include <map>
#include <deque>
#include <string>


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
	deque<msg_t*> msgqueue;
};	

class sframe {
	public:
	map<int,msgpipe_t * > pipemap;
	boost::timed_mutex  smutex;
	int base_key;
	string msg;
	int put_msg(string msg);
	msg_t* get_msg(int key);
	int reg_agent_key();
	int dispatch();
	int test(int key);
	boost::thread_group stg;
	int run(strategy_config_t &config);
};

extern sframe g_sframe;

class sframe_agent{
	public:
	int agent_key;
	int put_msg(string msg);
	string get_msg();
	int    init();
	private:
	class sframe  *psframe;
	msg_t *pystr2msg(string str);
	string msg2pystr(msg_t *msg);
};

extern "C" void initsframe_agent();
#endif
