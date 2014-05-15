
#include "mdseries.h"
#include "help.h"
#include "boost/date_time.hpp"
#include "log.h"
#include "tm.h"
#include "StrategyFrame.h"
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

	int mdseries::flush(string instn,dmgr *pdmgr) {
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
		int open,close,high,low,mnum;
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
            mnum=this->close.mnum[iterator_idx];

			/*syn or not?
			 * */
			pkdata=new (kdata_t);
			pkdata->close=close;
			pkdata->open=open;
			pkdata->high=high;
			pkdata->low=low;
            pkdata->mnum=mnum;
            pkdata->period=period;
			pdmgr->pquote_io->quote_kdata_push(instn, pkdata);
		}
		return 0;
	};
	int mdseries::load(string instn,dmgr *pdmgr){
		/*flush it to quote_io
		 * */
		int sec, msec,vol,mnum;
		float open,close,high,low;
		char sqlbuf[1024];
		snprintf(sqlbuf,1024,"select * from kdata_1_%s order by sec asc limit 10000",instn.c_str());
		vector<map<string,string> > result;
		pdmgr->db_map["kdata"]->exe_cmd(sqlbuf, result);
        LOG_DEBUG<<instn<<" md load size:"<<result.size()<<std::endl;
		
		/**/
		for(vector<map<string,string> >::iterator it=result.begin();it!=result.end();it++) {
			open=atof((*it)["open"].c_str());
			close=atof((*it)["close"].c_str());
			high=atof((*it)["high"].c_str());
			low=atof((*it)["low"].c_str());
			sec=atoi((*it)["sec"].c_str());
			msec=atoi((*it)["msec"].c_str());
			vol=atoi((*it)["vol"].c_str());
            mnum=atoi((*it)["mnum"].c_str());
			this->open.update(open, sec,  msec,OPEN,period,1);
			this->close.update(close, sec,  msec,CLOSE,period,1);
			this->high.update(high, sec,  msec,HIGH,period,1);
			this->low.update(low, sec,  msec,LOW,period,1);
			/*todo vol*/
		}
		return 0;
	};

	int mdseries::update(float o,float c,float h, float l, int sec, int msec,int is_new) {
		if(this->period==1) {
			//todo 
			return 0;
		}
		assert(this->ptype==MINUTE);

		high.update(h,sec,msec,HIGH,period,is_new);
		low.update(l,sec,msec,LOW,period,is_new);
		open.update(o,sec,msec,OPEN,period,is_new);
		close.update(c,sec,msec,CLOSE,period,is_new);
		/*todo volume*/
        return 0;
	}


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

int md::reg_strategy(int sid, int period)
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
    LOG_DEBUG<<"reg_strategy : sid="<<sid<<" period:"<<period<<std::endl;
    return ret;
};
	
int md::update(float v, int t1, int t2) {
		/*1.更新 ds
		  2.更新 分钟线。
		  3.更新 x周期线。
		  每次更新，都反馈是否要更新下次线的四个值。
		*/
		int status=this->ds.update_ms(v,t1,t2);
        int idx_prev;
        int idx_next;
        float o,c,h,l;
        int sec,msec;


		if(status <0) {
			/**/
			assert(0);
		}else {
#if 0
			cerr<<"update ms finished, return first"<<std::endl;
			return 0;
#endif
            for(map<int,bool>::iterator it=this->tsregmap.begin();it!=this->tsregmap.end();it++) {
                /*todo*/
                LOG_DEBUG<<"quote_tchange v:"<<v<<" sid:"<<it->first<<std::endl;
                sframe_quote_tchange(v, t1, t2,0,it->first);
            }


			if(this->mds.find(1)!=this->mds.end()) {
				if( (t1 > this->mds[1]->last_sec) || 
						(t1== this->mds[1]->last_sec && (t2 >this->mds[1]->last_msec)) ) { 
                        /*
                        cout<<"idx_o:"<<this->mds[1]->open.cidx<<std::endl;
                        cout<<"idx_h:"<<this->mds[1]->high.cidx<<std::endl;
                        cout<<"idx_l:"<<this->mds[1]->low.cidx<<std::endl;
                        cout<<"idx_c:"<<this->mds[1]->close.cidx<<std::endl;
                        */

                        assert(this->mds[1]->open.cidx==this->mds[1]->close.cidx);
                        assert(this->mds[1]->high.cidx==this->mds[1]->close.cidx);
                        assert(this->mds[1]->low.cidx==this->mds[1]->close.cidx);
                        idx_prev=this->mds[1]->close.cidx;
						this->mds[1]->open.update_me(v,t1,t2,OPEN,MINUTE,1);
						this->mds[1]->close.update_me(v,t1,t2,CLOSE,MINUTE,1);
						this->mds[1]->high.update_me(v,t1,t2,HIGH,MINUTE,1);
						this->mds[1]->low.update_me(v,t1,t2,LOW,MINUTE,1);
						this->mds[1]->last_msec=t2;
						this->mds[1]->last_sec=t1;

                        /*
                        cout<<"idx_o:"<<this->mds[1]->open.cidx<<std::endl;
                        cout<<"idx_h:"<<this->mds[1]->high.cidx<<std::endl;
                        cout<<"idx_l:"<<this->mds[1]->low.cidx<<std::endl;
                        cout<<"idx_c:"<<this->mds[1]->close.cidx<<std::endl;
                        */
                        assert(this->mds[1]->open.cidx==this->mds[1]->close.cidx);
                        assert(this->mds[1]->high.cidx==this->mds[1]->close.cidx);
                        assert(this->mds[1]->low.cidx==this->mds[1]->close.cidx);
                        idx_next=this->mds[1]->close.cidx;

						//todo lock bug
						//todo update v
						/*	
						 for(vector<int>::iterator it=perids.begin();it!=perids.end();it++) 
						 */
                        assert(idx_next<=idx_prev+1);
                        o=this->mds[1]->open.data[idx_next];
                        c=this->mds[1]->close.data[idx_next];
                        h=this->mds[1]->high.data[idx_next];
                        l=this->mds[1]->low.data[idx_next];
                        sec=t1;
                        msec=t2;

                        for(map<int, mdseries*>::iterator it=this->mds.begin();it!=this->mds.end();it++) {
                            if(it->first!=1) {
                                //this->update(o,c,h,l,sec,msec,idx_next-idx_prev);
                            }
                        	for(map<int,bool>::iterator subit=this->mds[it->first]->ksregmap.begin();subit!=this->mds[it->first]->ksregmap.end();subit++) {
                                sframe_quote_kchange(o,c,h,l,sec,msec,idx_next-idx_prev, subit->first);
                            }
                        }
                        if(idx_next !=idx_prev) {
                            o=this->mds[1]->open.data[idx_prev];
                            c=this->mds[1]->close.data[idx_prev];
                            h=this->mds[1]->high.data[idx_prev];
                            l=this->mds[1]->low.data[idx_prev];
                            sec=this->mds[1]->close.tsec[idx_prev];
                            msec=this->mds[1]->close.tmsec[idx_prev];;
                            LOG_DEBUG<<"candle data"<<" open:"<<o<<" close:"<<c<<" high:"<<h<<" low:"<<l<<" sec:"<<sec<<" msec:"<<msec<<std::endl;
                        }
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
	/*
    not load any data
    */

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

int mdservice::regmd_strategy(string instn, int sid, int period){
    if(mds.find(instn)==mds.end()) {
        return -1;
    }
    return mds[instn]->reg_strategy(sid, period);
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
