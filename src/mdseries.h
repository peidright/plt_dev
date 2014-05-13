#ifndef MDSERIES_H_
#define MDSERIES_H_
#include "dseries.h"
#include "log.h"
#include "instmgr.h"
#include "quote_io.h"

class inst;
class dmgr;

#include <map>
using namespace std;

/*500毫秒线，实时启动分钟线。分钟线换线，才驱动高级别线*/
typedef enum update_status {
	CURRENT_BAR,
	NEXT_BAR,
	NNEXT_BAR,
	NNNEXT_BAR,
	PREV_BAR,
	DEFAULT_BAR,
}update_status;

class mdseries {
public:
	int period;/*周期*/    
	int kd_uptime;
	int md_uptime;
	int lmd_uptime;
	int last_sec;
	int last_msec;
	period_type ptype;/*周期类型*/
	dseries  high;
	dseries  low;
	dseries open;
	dseries close;
	dseries volume;
	update_status get_update_status(int b1,int b2,int e1,int e2,int n1,int n2,period_type ptype);
	mdseries(period_type ptype, int period);
	int updatems(float v, int b1, int b2);
	int updateme(float v, int b1, int b2);
	map<int,bool> ksregmap;//stragtepy map

	int update(float o,float c,float h, float l, int sec, int msec,int is_new);
	int kline_update();
	int flush(string instn,dmgr *pdmgr);
	int load(string instn,dmgr *pdmgr);
};

class md {
public:
	int load_period(string instn, int period, dmgr *pdmgr) {
		if(mds.find(period)==mds.end()) {
			/*todo*/
			return -1;
		}
		mds[period]->load(instn,pdmgr);
		return 0;
	}
	int reg_period(period_type ptype, int period);
	int drivemd();
	map<int, mdseries*> mds;
	vector<int>         perids;
	dseries             ds;  /*base misc service*/
	inst                *pinst;
	map<int,bool> tsregmap;//stragtepy map
	md() {
		this->pinst=NULL;
	}
    int reg_strategy(int sid, int period)
    {
        int ret=0;
        /*0==tick
         * */
        if(period==0) {
            tsregmap[sid]=true;
        }else {
            /**/
            if(mds.find(period)!=mds.end()) {
                mds[period]->ksregmap[sid]=true;
            }else {
                ret=-1;
            }
        }
        return ret;
    };
	int update(float v, int t1, int t2);

	//int mdseries::update(float o,float c,float h, float l, int sec, int msec,int is_new) {
	int update(float o,float c,float h, float l, int sec, int msec,int is_new) {
		/*
		 * */
		for(map<int, mdseries*>::iterator it=this->mds.begin(); it!=this->mds.end(); it++) {
			/**/
			it->second->update(o,c,h,l,sec,msec,is_new);
		}
	}
	int update_timer();
	int kline_update();
	int flush(string instn,dmgr *pdmgr);
	int load(string instn, dmgr *pdmgr);
};

class mdservice {
public:
	/*每个md一个线程*/
	map<string, md*> mds;
	/*todo 读写锁*/
	int mmd(string contract,int period, int bar);
	int regmd_period(string contract,period_type ptype, int period);
	int loadmd_period(string instn, int period, dmgr *pdmgr) {
		/*todo err*/
		if(mds.find(instn)==mds.end()){
			return -1;
		}
		mds[instn]->load_period(instn, period, pdmgr);
		return 0;
	};

	int regmd(string contract, inst *pinst);
	int update(string contract, float v, int t1, int t2);
	int update_timer();
	int flush(string instn,dmgr *pdmgr);
	int load(string instn,dmgr *pdmgr);
};





#endif
