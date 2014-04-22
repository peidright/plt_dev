
#include "mdseries.h"
#include "help.h"
#include "boost/date_time.hpp"
#include "log.h"
#include "tm.h"
using namespace boost::posix_time;
using namespace boost::gregorian;

class dmgr;



update_status mdseries::get_update_status(int b1,int b2,int e1,int e2,int n1,int n2,period_type ptype) {
		/*
		b1 当前bar的开始.
		e1 当前bar的结束.
		n1 当前行情的时间。
		需要判断当前的行情，是否是当前的bar的数据.
		*/
		if(n1+n2<=e1+e2)
			return PREV_BAR;
		switch(ptype){
		case MIRCO:
			if(is_continue(e1,e2,n1,n2)) {
				/*如果是连续*/
				if(e1==n1 && e2==0 && n2==500) {
					return NEXT_BAR;
				}else {
					return NNEXT_BAR;
				}
			}else {
				return NNNEXT_BAR;
			}
			break;		
		case MINUTE:
			if(is_continue(e1,e2,n1,n2)) {
				/*
				  case 1:当前bar.
				  case 2:下根bar.
				  case 3:下下根BAR
				*/
			}else {
				/*
				  case 1:
				  case 2:
				  case 3:
				*/
			}
			break;
		case HOUR:
			break;
		case DAY:
			assert(0);
			break;
		case WEEK:
			assert(0);
			break;
		case YEAR:
			assert(0);
			break;
		default:
			assert(0);
			cout<<"err"<<endl;
			break;
	}
	//	
	return DEFAULT_BAR;
}
	int mdseries::updatems(float v, int b1, int b2) {
			/*todo lock 
			  1.计算...
			  如果是当前这根K线上的。就更新当前这根k线。如果不是。
			  对于分钟线，逻辑如下：
			  如果是当前分钟的，更新本K线。
			  如果是下一分钟的，更新下跟k线。
			  如果是是连续，但是不是下一分钟的。留出空隙。但是更新下一分钟。
			  如果不是连续的。紧接着更新。
			  如果是之前的数据。忽略此数据。
			*/	    
		return 0;
	};

	mdseries::mdseries(period_type ptype, int period){
		this->ptype=ptype;
		this->period=period;
	};

	int mdseries::updateme(float v, int b1, int b2) {
			/*todo lock 
			 *1.if on this bar,update it.
			  2.if not, for minit k,the logic is below:
			    1.if is for current bar, update it.
			    2.if is the next bar, update next.
			    3.if is coninue time, but not next bar, live the space. update next.
			    4.if it is not the coninue, update it next
			    5.if is k before, ignore it.
			*/

		    return  0;
	};
	/*
	int mdseries::flush(string instn, dmgr *pdmgr)
		flush it to quote_io
		return 0;
	};
	int mdseries::load(string instn, dmgr *pdmgr){
		flush it to quote_io
		return 0;
	};
	*/
	int mdseries::kline_update() {
		/*md_uptime,kd_uptime,
		 *every time md updated, update md_uptime, 
		 *if now kd_uptime > 1minute of md_uptime.
		 *    update next bar
		 *else
		 *    ignore
		 * */

		int t=get_time();

		/*
		if(this->md_uptime!=0) {
			if(this->kd_uptime==0 || this->lmd_uptime==0) {
				assert(0);
			} else {
				if(t>=this->kd_uptime+60) {
					if(t+this->lmd_uptime>this->kd_uptime+this->md_uptime+60){
						this->lmd_uptime=this->lmd_uptime+60;
						this->md_uptime=this->md_uptime+60;
						this->kd_uptime=this->kd_uptime+60;
					} else {
						this->kd_uptime=this->kd_uptime+60;
					}
				} else {
				}
			}
		} else {
		}
		*/
		return 0;
	}




#define OPEN_FLAG 0x01
#define CLOSE_FLAG 0x02
#define HIGH_FLAG  0x04
#define LOW_FLAG   0x08
#define VOLUME_FLAG 0x10


int md::reg_period(period_type ptype, int period) {
		/*注册一个周期
		 check 是否存在
		*/
		if (this->mds.find(period)!=this->mds.end()){
			//log it
			return -1;
		}
	    	mdseries *pmds= new mdseries(ptype,period);
		this->perids.push_back(period);
		this->mds[period]=pmds;
		return 0;
	};
int md::drivemd() {
		/*行情驱动,更新各个周期*/
	return 0;
};
	
int md::update(float v, int t1, int t2) {
		/*1.更新 ds
		  2.更新 分钟线。
		  3.更新 x周期线。
		  每次更新，都反馈是否要更新下次线的四个值。
		*/
		cerr<<"ds update ms"<<std::endl;

		int status=this->ds.update_ms(v,t1,t2);
		if(status <0) {
			/**/
			assert(0);
		}else {
#if 1
			cerr<<"update ms finished, return first"<<std::endl;
			return 0;
#endif
			if(this->mds.find(1)!=this->mds.end()) {
				if( (t1 > this->mds[1]->last_sec) || 
						(t1== this->mds[1]->last_sec && (t2 >this->mds[1]->last_msec)) ) { 


						this->mds[1]->open.update_me(v,t1,t2,OPEN,MIRCO,1);
						this->mds[1]->close.update_me(v,t1,t2,CLOSE,MIRCO,1);
						this->mds[1]->high.update_me(v,t1,t2,HIGH,MIRCO,1);
						this->mds[1]->low.update_me(v,t1,t2,LOW,MIRCO,1);
						this->mds[1]->last_msec=t2;
						this->mds[1]->last_sec=t1;
						//todo lock bug
						//todo update v
						/*	
							for(vector<int>::iterator it=perids.begin();it!=perids.end();it++) 
							*/
					}
				else {
					/*todo check*/
					LOG_DEBUG<<"update kdata: ignore and drop the old data"<<std::endl;
				}
			}
			else {
				/*other process
				 * */
			}

		}
		return 0;
	}

int md::flush(string instn, dmgr *pdmgr)
{
	/*copy msg to quote_io
	 *update dserice
	 * */


	return 0;
}


int md::load(string instn, dmgr *pdmgr)
{
	/**/

	return 0;
}


int md::kline_update()
{
	if(this->mds.find(1)==this->mds.end()) {
		this->mds[1]->kline_update();
	}else {
		assert(0);
	}

}
int md::update_timer()
{
		/*
			每1秒运行一次。
			如果当前是xx周期的开始，并且当前周期没有行情，就默认填充行情。
			只考虑分钟及分钟以上级别周期.
		*/
	return 0;
};


int mdservice::mmd(string contract,int period, int bar){

	return 0;
};
int mdservice::update(string contract, float v, int t1, int t2){
	int ret;
	if(this->mds.find(contract)==this->mds.end()) {
		/*!!!!*/
		LOG_DEBUG<<"find not contract: "<<contract<<std::endl;
		return -1;
	}

	if (this->mds[contract]->pinst==NULL ||
		!this->mds[contract]->pinst->is_trading()
	   ) {
		/*bad struct. put it into md->update*/
		LOG_INFO<<"not ready:"<<contract<<std::endl;
		return -1;
	}
	
	ret= this->mds[contract]->update(v,t1,t2);
	assert(ret==0);
	return ret;
};

int mdservice::regmd(string contract, inst *pinst){

	/*
		1.check 合约合法性
		2.check 合约是否已经存在
	*/
	if(this->mds.find(contract)!=this->mds.end()){
		/*log it, the contract has existed*/
		return -1;
	}
	LOG_INFO<<"reg md :"<<contract<<std::endl;
	//assert(0);

	class md *pmd= new class md();
	pmd->pinst=pinst;
	this->mds[contract]=pmd;
	return 0;
};
int mdservice::regmd_period(string contract,period_type ptype, int period){
	/*1.check 合法性
	*/
	if(this->mds.find(contract)==this->mds.end()){
		/*log it, the contract has not existed*/
		LOG_DEBUG<<"regmd ,not find the mdservice"<<std::endl;
		assert(0);
		return -1;
	}
	this->mds[contract]->reg_period(ptype,period);
	return 0;
}

int mdservice::update_timer() {
		/*
			每1秒运行一次。
			如果当前是xx周期的开始，填补默认行情。
		*/
	return 0;
}
int mdservice::flush(string instn, dmgr *pdmgr)
{
	/*copy msg to quote_io
	 *update dserice
	 * */
	return 0;
}


int mdservice::load(string instn,dmgr *pdmgr)
{
	return 0;
}
