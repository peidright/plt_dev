#ifndef STRATEGY_FRAME_H_
#define STRATEGY_FRAME_H_
#include "json/json.h"
#include "boosthelp.h"
#include "msgqueue.h"
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


typedef struct msgpipe_s {
	boost::interprocess::interprocess_semaphore qsem;
	deque<symsg_t> msgqueue;
}msgpipe_t;	

class sframe {
	public:
	map<int,msgpipe_t * > pipemap;
	int key;
	string msg;
	int put_msg(string msg) {
		this->msg=msg+":ddd";
		cout<<"msg: "<<std::endl;
		return 0;
	};
	string get_msg() {
		return msg;
	};
	int dispatch(){
	};
};
extern class g_sframe;

class sframe_agent{
	public:
	int key;
	string msg;
	int put_msg(string msg) {
		this->msg=msg+":ddd";
		cout<<"msg: "<<std::endl;
		this->pystr2msg(msg);
		return 0;
	};
	string get_msg() {
		return msg;
	};
	int    register() {
		this->psframe=&g_sframe;
	}
	private:
	class sframe  *psframe;
	msg_t *pystr2msg(string str);
	string msg2pystr(msg_t *msg);
};

#endif
