#ifndef QUOTE_IO_H_
#define QUOTE_IO_H_
#include <map>
#include <deque>
#include <string>

#include "boosthelp.h"
#include "datalocal.h"
using namespace boost;
class datalocal;
class dmgr;

using namespace std;
typedef struct tdata_s {
	/*为避免库耦合，暂时直接写出字段。以后为了效率，再考虑耦合
	this->exe_cmd("create table instrument(day integer, seconds integer, \
				  closeprice integer,openprice  interger,uprice integer,lprice integer,\
				  highprice integer,lowprice integer,lastprice integer,\
				  avgprice integer,vol integer,bid1 integer,ask1 integer",rows);
    */
	int sec;
	int msec;
	int close;
	int open;
	int uprice;
	int lprice;
	int high;
	int low;
	int lastprice;
	int avgprice;
	int vol;
	int bid1;
	int ask1;
	int bid2;
	int ask2;
	int bid3;
	int ask3;
	int bid4;
	int ask4;
	int bid5;
	int ask5;
}tdata_t;

typedef struct tdata_io_s {
	int lsec;
	int lmsec;
	deque<tdata_t*> tdataq;
	timed_mutex     qmutex;
}tdata_io_t;

typedef struct kdata_s {
	/*为避免库耦合，暂时直接写出字段。以后为了效率，再考虑耦合*/
	int sec;
	int msec;
	int close;
	int open;
	int uprice;
	int lprice;
	int highprice;
	int lowprice;
	int lastprice;
	int avgprice;
	int vol;
}kdata_t;
typedef struct kdata_io_s {
	int lsec;
	int lmsec;
	deque<kdata_t*> kdataq;
	timed_mutex     qmutex;
}kdata_io_t;

class quote_io {
	/*string 命名规则：
	  cu401    表铜的1401合约
	  cu4015.  表示铜的1401 的5分钟合约.
	*/
public:
	map<string, kdata_io_t *> kdata_map;
	map<string, tdata_io_t *> tdata_map;
	map<string, datalocal  *> db_map;
	dmgr *pdmgr;
	void reg_dmgr(dmgr *mgr){this->pdmgr=mgr;};
	void quote_kdata_push(string contract, kdata_t *data);
	void quote_tdata_push(string contract, tdata_t *data);
	void quote_kdata_work();
	void quote_tdata_work();
	void quote_io_work();
};
extern quote_io g_quote_io;

void quote_push(string contract ,tdata_t *data);
void quote_io_work();
#endif
