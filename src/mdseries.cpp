
#include "mdseries.h"
#include "help.h"
#include "boost/date_time.hpp"
using namespace boost::posix_time;
using namespace boost::gregorian;



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
			  1.计算...
			  如果是当前这根K线上的。就更新当前这根k线。如果不是。
			  对于分钟线，逻辑如下：
			  如果是当前分钟的，更新本K线。
			  如果是下一分钟的，更新下跟k线。
			  如果是是连续，但是不是下一分钟的。留出空隙。但是更新下一分钟。
			  如果不是连续的。紧接着更新。
			  如果是之前的数据。忽略此数据。
			*/
		    return  0;
	};




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
		int status=this->ds.update_ms(v,t1,t2);
		if(status <0) {
			/**/
		}else {
			/*
			*/
			float o,c,h,l;int e1,e2;
			/*更新分钟线*/
			c=ds[0];
			e1=ds.csec;
			e2=ds.cmsec;
			//status=mds[1].update50(c,e1,e2);
			status=mds[1]->updateme(c,e1,e2);


			/*更新其他周期*/
			o=mds[1]->open[0];
			c=mds[1]->close[0];
			h=mds[1]->high[0];
			l=mds[1]->low[0];
			e1=mds[1]->close.csec;
			e2=mds[1]->close.cmsec;

			for(vector<int>::iterator it=perids.begin();it!=perids.end();it++) {
				int temp=0;
				if(status & OPEN_FLAG) {
					temp=temp | mds[*it]->open.update_me(o,e1,e2,OPEN,MIRCO,1);
				}
				if(status & CLOSE_FLAG) {
					temp=temp | mds[*it]->close.update_me(c,e1,e2,CLOSE,MIRCO,1);
				}
				if(status & HIGH_FLAG) {
					temp=temp | mds[*it]->high.update_me(h,e1,e2,HIGH,MIRCO,1);
				}
				if(status & LOW_FLAG) {
					temp=temp | mds[*it]->low.update_me(l,e1,e2,LOW,MIRCO,1);
				}
				if(status & VOLUME_FLAG) {
					//vol how to process
					//temp=temp | mds[*it].open.update(v,e1,e2);
				}
				status=temp;
			}
		}
		return 0;
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


int mdservice::md(string contract,int period, int bar){

	return 0;
};
int mdservice::update(string contract, float v, int t1, int t2){
	int ret;
	if(this->mds.find(contract)==this->mds.end()) {
		/*!!!!*/
		return -1;
	}
	ret= this->mds[contract]->update(v,t1,t2);
	
	return ret;
};

int mdservice::regmd(string contract){

	/*
		1.check 合约合法性
		2.check 合约是否已经存在
	*/
	if(this->mds.find(contract)!=this->mds.end()){
		/*log it, the contract has existed*/
		return -1;
	}

	class md *pmd= new class md();
	this->mds[contract]=pmd;
	return 0;
};
int mdservice::regmd_period(string contract,period_type ptype, int period){
	/*1.check 合法性
	*/
	if(this->mds.find(contract)==this->mds.end()){
		/*log it, the contract has not existed*/
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
	/*定时器，负责定时更新各个合约的各个周期线
	  回报，只负责更新其自身对应的那个分钟线。分钟线定时更新上面各个周期的线。
	*/