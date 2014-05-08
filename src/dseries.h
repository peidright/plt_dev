#ifndef DSERIES_H_
#define DSERIES_H_
#include "log.h"
#include "boosthelp.h"
using namespace std;
using namespace boost;
enum period_type {
	MIRCO,
	MINUTE=60,
	HOUR,
	DAY,
	WEEK,
	YEAR,
};

enum kdata_type {
	HIGH,
	LOW,
	OPEN,
	CLOSE,
};

class dseries {
public:
	static const int MAX_DSERIES_SIZE=10000;
	float data[MAX_DSERIES_SIZE];
	int   tsec[MAX_DSERIES_SIZE];
	int   tmsec[MAX_DSERIES_SIZE];
	int   mnum[MAX_DSERIES_SIZE];
	timed_mutex dmutex;
	typedef int (*updatecb)(float ,int,int);
	updatecb cb;
	int eidx;
	int bidx;
	int cidx;
	int esec,emsec;
    	int csec,cmsec;
	int bsec,bmsec;
	period_type ptype;
	dseries();
	dseries(updatecb cb) {this->cb = cb;};
	dseries(const dseries &);

	int update_ms(float v, int sec, int msec);
	int update_meh(float v, int sec, int msec,period_type ptype, int period);
	int update_mel(float v, int sec, int msec,period_type ptype, int period);
	int update_meo(float v, int sec, int msec,period_type ptype, int period);
	int update_mec(float v, int sec, int msec,period_type ptype, int period);
	int update_me(float v, int sec, int msec,kdata_type type,period_type ptype, int period);
	int update_other(float v, int sec, int msec, period_type ptype,kdata_type ktype,int period);
	int kline_update(kdata_type ktype, int t);
	int update(float v,int sec, int msec,kdata_type ktype,int period, int is_new);
	int dump();
	int kdump(int v, int sec, int msec, int current_slot, int last_slot, int result, kdata_type type);

	float operator[](int i){
		/*fault tolerent*/
		return this->data[cidx-i];
	}
	int callback(float v,int sec, int msec);

};
#endif
