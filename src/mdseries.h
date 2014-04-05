#ifndef MDSERIES_H_
#define MDSERIES_H_
#include "dseries.h"
#include "log.h"

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
	int kline_update();
};

class md {
public:
	int reg_period(period_type ptype, int period);
	int drivemd();
	map<int, mdseries*> mds;
	vector<int>         perids;
	dseries             ds;  /*base misc service*/
	int update(float v, int t1, int t2);
	int update_timer();
	int kline_update();

};

class mdservice {
public:
	/*每个md一个线程*/
	map<string, md*> mds;
	/*todo 读写锁*/
	int mmd(string contract,int period, int bar);
	int regmd_period(string contract,period_type ptype, int period);
	int regmd(string contract);
	int update(string contract, float v, int t1, int t2);
	int update_timer();
};





#endif
