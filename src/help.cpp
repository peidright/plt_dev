#include "mdseries.h"
#include "boost/date_time.hpp"
using namespace boost::posix_time;
using namespace boost::gregorian;
	

int between(time_t start, time_t end,time_t t)
	{
		int _start=(int)start;
		int _end=(int)end;
		int _t = (int)t;
		if((t>_start-300) && (t<_end+300))
			return 1;
		else
			return 0;
	}
	int between(time_t start, time_t end,time_t t1,time_t t2)
	{
		int _start = (int)start;
		int _end = (int)end;
		int _t1  = (int)t1;
		int _t2  = (int)t2;
		if((_t1>_start-300) && (_t1<_end+300) &&
		   (_t2>_start-300) && (_t2<_end+300)
			)
			return 1;
		else
			return 0;
	}
	time_t tm_fix(tm *t,int hour,int minutes){
		t->tm_hour=hour;
		t->tm_sec=minutes;
		return mktime(t);
	}
	int tm_continue(tm *t1, tm *t2) {
			int ret=0;
		    tm begin;
			tm end;
			time_t tt1,tt2,tbegin,tend;
			tm *pbegin,*pend;
			//tm *pend=gmtime((time_t*)&e1);
		    //tm *pbegin=gmtime((time_t*)&b1);
			pbegin=&begin;
			pend=&end;
			tt1=mktime(t1);
			tt2=mktime(t2);
			if(tt1<=tt2) {
				memcpy(&begin,t1,sizeof(tm));
				memcpy(&end, t2,sizeof(tm));
			}else {
				memcpy(&begin,t2,sizeof(tm));
				memcpy(&end, t1,sizeof(tm));
			}
			if(t1->tm_mday==t2->tm_mday) {
				/*如果是同一天
				*/
				tbegin=tm_fix(&begin,9,0);
				tend=tm_fix(&end,10,15);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}
				tbegin=tm_fix(&begin,10,15);
				tend=tm_fix(&end,11,30);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}

				tbegin=tm_fix(&begin,13,30);
				tend=tm_fix(&end,15,0);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}

				tbegin=tm_fix(&begin,21,0);
				tend=tm_fix(&end,2,30);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}
			}else {
				/*如果不是同一天
				*/	
				tbegin=tm_fix(&begin,9,0);
				tend=tm_fix(&end,10,15);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}

				tbegin=tm_fix(&begin,10,15);
				tend=tm_fix(&end,11,30);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}

				tbegin=tm_fix(&begin,13,30);
				tend=tm_fix(&end,15,0);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}

				tbegin=tm_fix(&begin,21,0);
				tend=tm_fix(&end,2,30);
				if(between(tbegin,tend,tt1,tt2)) {
					ret=1;
					goto out;
				}
			}
			return ret;
out:
			return ret;
	}
	int is_continue(int e1,int e2, int b1, int b2){
	    /*9点到-10:15,10:30-11:30,1:30-3:00,21:00-2:30
		  0 =is_continue;
		  1 =biger than xxx
		  -1=smaller than xxx
		*/

		/*
		tm *t;
		ptime d(ptime_from_tm(*t));
		time_t td=time(NULL);
		t=gmtime(&td);
		*/
		
		tm *end=gmtime((time_t*)&e1);
		tm *begin=gmtime((time_t*)&b1);
		if(e1+ 28800<b1) {
			/*时间差8小时
			*/
			return 0;
		}else if(e1 > b1+28800){
			/*时间差8小时
			*/
			return 0;
		}else {

			return 1;
		}
		assert(0);
		return 0;
	};
	
	int fix(){
		/*如果报单延时，则更新最高最低价。量不动。*/
		return 0;
	};
	/*need a mutex*/


int date2time(string dat)
{
	//11:03:18
	ptime pt(time_from_string(dat)); 
	tm tm1 = to_tm(pt);
 	time_t tt = mktime(&tm1);
	cerr<<"str: " <<dat<<" time"<<to_simple_string(pt) <<std::endl;
	return (int)tt;
}

