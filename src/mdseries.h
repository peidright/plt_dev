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
	int update(float o,float c,float h, float l, int sec, int msec) {
		if(this->period==1) {
			//todo 
			return 0;
		}
		assert(this->ptype==MINUTE);
		high.update(h,sec,msec,HIGH,period);
		low.update(l,sec,msec,LOW,period);
		open.update(o,sec,msec,OPEN,period);
		close.update(c,sec,msec,CLOSE,period);
		/*todo volume*/
	}
	int kline_update();
	int flush(string instn,dmgr *pdmgr) {
		/*flush it to quote_io
		 * step:
		 * 1.lock todo
		 * 2.syn
		 * 3.iterator it to flush
		 * */
		/*
		int last_sec,last_msec;
		char sqlbuf[1024];
		snprintf(sqlbuf,1024,"select sec,msec from kdata_%s order by sec desc limit 1",instn.c_str());
		assert(high.cdix==low.cidx);
		assert(open.cidx==close.cidx);
		assert(open.cidx==high.cidx);
		vector<map<string,string> > result;
		this->pdmgr->db_map["kdata"]->exe_cmd("sqlbuf", result);
		if(result.size()==0) {
			last_sec=0;
			last_msec=0;
		} else {
			last_sec=atoi(result[0]["sec"].c_str());
			last_msec=atoi(result[0]["msec"].c_str());
		}

		/*lock
		 * */

		/*iterator
		 * */
		int iterator_idx=0;
		int open,close,high,low;
		kdata_t *pkdata;
		for(iterator_idx=0; iterator_idx<=this->open.cidx; iterator_idx++) {
			if(this->open.data[iterator_idx]==0) {
				LOG_INFO<<"debug"<<std::endl;
				continue;
			}
			if(this->close.csec <= last_sec) {
				continue;
			}
			open=this->open.data[iterator_idx];
			close=this->close.data[iterator_idx];
			high=this->high.data[iterator_idx];
			low=this->low.data[iterator_idx];

			/*syn or not?
			 * */
			pkdata=new (kdata_t);
			pkdata->close=close;
			pkdata->open=open;
			pkdata->high=high;
			pkdata->low=low;
			pdmgr->pquote_io->quote_kdata_push(instn, pkdata);
		}
		return 0;
	};
	int load(string instn,dmgr *pdmgr){
		/*flush it to quote_io
		 * */
		int sec, msec,vol;
		float open,close,high,low;
		char sqlbuf[1024];
		snprintf(sqlbuf,1024,"select * from kdata_%s order by sec asc limit 10000",instn.c_str());
		vector<map<string,string> > result;
		pdmgr->db_map["kdata"]->exe_cmd("sqlbuf", result);
		
		/**/
		for(vector<map<string,string> >::iterator it=result.begin();it!=result.end();it++) {
			open=atof((*it)["open"].c_str());
			close=atof((*it)["close"].c_str());
			high=atof((*it)["high"].c_str());
			low=atof((*it)["low"].c_str());
			sec=atoi((*it)["sec"].c_str());
			msec=atoi((*it)["msec"].c_str());
			vol=atoi((*it)["vol"].c_str());
			this->open.update(open, sec,  msec,OPEN,period);
			this->close.update(close, sec,  msec,CLOSE,period);
			this->high.update(high, sec,  msec,HIGH,period);
			this->low.update(low, sec,  msec,LOW,period);
			/*todo vol*/
		}
		return 0;
	};

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
	md() {
		this->pinst=NULL;
	}
	int update(float v, int t1, int t2);
	int update(float o,float c,float h, float l, int sec, int msec) {
		/*
		 * */
		for(map<int, mdseries*>::iterator it=this->mds.begin(); it!=this->mds.end(); it++) {
			/**/
			it->second->update(o,c,h,l,sec,msec);
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
