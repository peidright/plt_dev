
#include "dseries.h"
#include "help.h"

int get_period_slot(int sec,int msec, period_type ptype,int period){
	int factor=1;
	sec=msec>0?(sec+1):sec;
	switch(ptype){
	case MIRCO:
		factor=factor*1;
		break;
	case MINUTE:
		factor=factor*60*period;
		break;
	default:
		assert(0);
		break;
	}
	return sec / factor;
}

dseries::dseries(){
	/*
	*/
	eidx=0;
	bidx=0;
	cidx=0;
	esec=0;
	emsec=0;
	csec=0;
	cmsec=0;
	bsec=0;
	bmsec=0;
};

dseries::dseries(const dseries &){};

int dseries::dump()
{
	/*
	*/
	if(this->cidx>1) {
	LOG_DEBUG<<"price:"<<this->data[this->cidx-1]<< " time: "<<this->tsec[this->cidx-1]<<" mtime: "<<this->tmsec[this->cidx-1] <<"idx is:"<<this->cidx-1<<std::endl;
	}
	return 0;
}

int dseries::update_ms(float v, int sec, int msec){
		/*
		  1.
		  2.
		*/
	return 0;
	again:
		boost::unique_lock<boost::timed_mutex> lk(this->dmutex,boost::chrono::milliseconds(10));
		if(lk) {
			if( (sec > this->csec) || 
				(sec== this->csec && (msec >this->cmsec))
				) {
					/*update ms data, not make sure the order. if the data is older,just dropit.
					  there may has a problem
					*/
					this->tmsec[this->cidx]=msec;
					this->tsec[this->cidx]=sec;
					this->data[this->cidx]=v;
					this->cidx++;
					this->csec=sec;
					this->cmsec=msec;
					
			}else {
				/*todo warning, drop old message*/
				LOG_DEBUG<<"dseries update_ms drop old message this->csec:"<<this->csec<<" sec:"<<sec\
<<"this->cmsec: "<<this->cmsec <<" msec :"<<msec<<" idx:"<<this->cidx<<std::endl;
				return -1;
			}
			lk.unlock();
			this->dump();
		}else {
			/*warnring*/
			cerr<<"dseries update_ms lock err,again" <<std::endl;
			sleep(1);
			goto again;
		}
		return 0;
	}


int dseries::kdump(int v, int sec, int msec, int current_slot, int last_slot, int result, kdata_type type) 
{
	switch(type) {
		case HIGH:
			LOG_DEBUG<<"HIGH kdump\t"<<"\t"<<result<<v<<"\t"<<sec<<"\t"<<msec<<"\t"<<current_slot<<"\t"<<last_slot<<std::endl;
			break;
		case LOW:
			LOG_DEBUG<<"LOW kdump\t"<<"\t"<<result<<v<<"\t"<<sec<<"\t"<<msec<<"\t"<<current_slot<<"\t"<<last_slot<<std::endl;
			break;
		case OPEN:
			LOG_DEBUG<<"OPEN kdump\t"<<"\t"<<result<<v<<"\t"<<sec<<"\t"<<msec<<"\t"<<current_slot<<"\t"<<last_slot<<std::endl;
			break;
		case CLOSE:
			LOG_DEBUG<<"CLOSE kdump\t"<<"\t"<<result<<v<<"\t"<<sec<<"\t"<<msec<<"\t"<<current_slot<<"\t"<<last_slot<<std::endl;
			break;
		default:
			assert(0);
	}
	return 0;
}

int dseries::update_meh(float v, int sec, int msec,period_type ptype, int period){

	/*check if is the current bar
	 *if is:
	 	update current bar
	  else is next:
		update next bar. if current bar is not full,or changed,fix?
	  else is nnn*ext bar:
	  	if is continue, update next
		if is not continue,save space, update next
		if is the data before, igore  the data
	  */	
	int start,mstart,cidx,now,start_slot,curr_slot,bar_slot,last_bar_slot;
	float result;
	start=this->tsec[this->cidx];
	mstart=this->tmsec[this->cidx];
	cidx=this->cidx;
	now=60*(sec/60);
	start_slot = get_period_slot(start,mstart, ptype,period);
	curr_slot=get_period_slot(sec,msec,ptype,period);
	bar_slot=cidx;
	last_bar_slot=cidx;
	if(start_slot==0 && cidx==0) {
		//init, zero tick
		this->data[cidx]=v;
		this->tsec[cidx]=sec;
		this->tmsec[cidx]=msec;
		bar_slot=cidx;
		result=v;
	}else if(cidx==0 && start_slot!=0){
		//init, first tick
		if(start_slot==curr_slot) {
			/*update current bar*/
			this->data[cidx]=std::max<float>(this->data[cidx],v);
			this->tmsec[cidx]=msec;
			this->tsec[cidx]=sec;
			bar_slot=cidx;
			result = this->data[cidx];
		}else if((start_slot+1)==curr_slot){
			/*update next bar*/
			this->cidx++;
			cidx=this->cidx;
			this->tsec[cidx]=now;
			this->data[cidx]=v;
			this->tmsec[cidx]=msec;
			bar_slot=cidx+1;
			result=this->data[cidx];
		}else if( is_continue(start_slot,0, curr_slot, 0)) {
			if(curr_slot == start_slot+2) {
				/*fix one tick
				 *update next tick
				 * */	
				this->cidx++;
				cidx=this->cidx;
				this->data[cidx]=this->data[cidx-1];
				this->tmsec[cidx]=msec;
				this->tsec[cidx]=sec;

				/*
				 * */
				this->cidx++;
				cidx=this->cidx;
				this->data[cidx]=v;
				this->tmsec[cidx]=msec;
				this->tsec[cidx]=sec;

				bar_slot=cidx;
				result=v;
			} else {
				LOG_DEBUG<<"curr_slot: "<<curr_slot<<" start_slot: "<<start_slot<<std::endl;
				assert(curr_slot <= start_slot+2);
			}
		}else {
			assert(curr_slot > start_slot);
			this->cidx++;
			cidx=this->cidx;
			this->tsec[cidx]=sec;
			this->data[cidx]=v;
			this->tmsec[cidx]=msec;
			bar_slot=cidx+1;
			result=this->data[cidx];
		}
	} else if(cidx!=0 && start_slot!=0) {
		/*当cidx为非零值得时候，这个cidx必然是已经有有实际报价，
		  或者timer定时器已经发生过!
		  */
		if(start_slot==curr_slot) {
			/*is current bar*/
			this->data[cidx]=std::max<float>(this->data[cidx],v);
			this->tsec[cidx]=sec;
			this->tmsec[cidx]=msec;
			bar_slot=cidx;
			result=this->data[cidx];
		}else if((start+1)==now){
			/*is next    bar*/
			this->cidx++;
			cidx=this->cidx;
			this->tsec[cidx]=sec;
			this->data[cidx]=v;
			this->tmsec[cidx]=msec;
			bar_slot=cidx+1;
			result=this->data[cidx];
		}else if( is_continue(start_slot,0, curr_slot, 0) ) {
			if(curr_slot == start_slot+2) {
				/*fix one tick
				 *update next tick
				 * */	
				this->cidx++;
				cidx=this->cidx;
				this->data[cidx]=this->data[cidx-1];
				this->tmsec[cidx]=msec;
				this->tsec[cidx]=sec;

				/*
				 * */
				this->cidx++;
				cidx=this->cidx;
				this->data[cidx]=v;
				this->tmsec[cidx]=msec;
				this->tsec[cidx]=sec;

				bar_slot=cidx;
				result=v;
			} else {
				LOG_DEBUG<<"curr_slot: "<<curr_slot<<" start_slot: "<<start_slot<<std::endl;
				assert(curr_slot <= start_slot+2);
			}
		}else {
			this->cidx++;
			cidx=this->cidx;
			this->tsec[cidx]=sec;
			this->data[cidx]=v;
			this->tmsec[cidx]=msec;
			bar_slot=cidx+1;
			result=this->data[cidx];
		}
	} else if(cidx!=0 && start==0) {
		assert(0);
	}
	this->csec=sec;
	this->cmsec=msec;

	this->kdump(v, sec, msec, last_bar_slot, bar_slot, result, HIGH); 
	return 0;
};
	
int dseries::update_mel(float v, int sec, int msec,period_type ptype, int period){
				/*判断是否是当前这根k线
			  如果是当前分钟的，更新本k线。
		      如果是下一分钟线，更新下根k线，如果本根k线为空，是否考虑修复本根？
			  如果是是连续的，但不是下一分钟，流出空隙。但更新下一分钟。
			  如果不是连续的，紧接着更新。
			  如果是之前的数据，忽略此数据..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);
			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*如果当前是刚开始。	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start!=0){
	           /*如果是第一根k线，
			      1.是否是最新的数据
				  2.取max值。
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*是同一时间段*/) {
					/*有可能要考虑补全间隙*/

				}else {
					/*不再考虑补全间隙*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}

			} else if(cidx!=0 ) {
			   /*当cidx为非零值得时候，这个cidx必然是已经有有实际报价，
			     或者timer定时器已经发生过!
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*是同一时间段*/) {
					/*有可能要考虑补全间隙*/

				}else {
					/*不再考虑补全间隙*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}
			}
			this->csec=sec;
			this->cmsec=msec;
			return 0;
};
	
int dseries::update_meo(float v, int sec, int msec,period_type ptype, int period){
				/*判断是否是当前这根k线
			  如果是当前分钟的，更新本k线。
		      如果是下一分钟线，更新下根k线，如果本根k线为空，是否考虑修复本根？
			  如果是是连续的，但不是下一分钟，流出空隙。但更新下一分钟。
			  如果不是连续的，紧接着更新。
			  如果是之前的数据，忽略此数据..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*如果当前是刚开始。	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*如果是第一根k线，
			      1.是否是最新的数据
				  2.取max值。
			   */

			} else if(cidx!=0 && start_slot==0) {
			   /*当cidx为非零值得时候，这个cidx必然是已经有有实际报价，
			     或者timer定时器已经发生过!
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟,不是open*/
				    //this->data[cidx]=std::max<float>(this->data[cidx],v);
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*是同一时间段*/) {
					/*有可能要考虑补全间隙*/

				}else {
					/*不再考虑补全间隙*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}
			}else if (cidx!=0 && start_slot!=0) {
				//ignore
			}
			this->csec=sec;
			this->cmsec=msec;
			return 0;
};
	
int dseries::update_mec(float v, int sec, int msec,period_type ptype, int period){
				/*判断是否是当前这根k线
			  如果是当前分钟的，更新本k线。
		      如果是下一分钟线，更新下根k线，如果本根k线为空，是否考虑修复本根？
			  如果是是连续的，但不是下一分钟，流出空隙。但更新下一分钟。
			  如果不是连续的，紧接着更新。
			  如果是之前的数据，忽略此数据..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*如果当前是刚开始。	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*如果是第一根k线，
			      1.是否是最新的数据
				  2.取max值。
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*是同一时间段*/) {
					/*有可能要考虑补全间隙*/

				}else {
					/*不再考虑补全间隙*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}

			} else if(cidx!=0) {
			   /*当cidx为非零值得时候，这个cidx必然是已经有有实际报价，
			     或者timer定时器已经发生过!
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*是同一时间段*/) {
					/*有可能要考虑补全间隙*/

				}else {
					/*不再考虑补全间隙*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}
			}
			this->csec=sec;
			this->cmsec=msec;
			return 0;
};
	
int dseries::update_me(float v, int sec, int msec,kdata_type type,period_type ptype, int period){
again:
		boost::unique_lock<boost::timed_mutex> lk(this->dmutex,boost::chrono::milliseconds(1));
		if(lk) {
			switch(type) {
			case HIGH:
				this->update_meh(v,sec,msec,ptype,period);
				break;
			case LOW:
				this->update_mel(v,sec,msec,ptype,period);
				break;
			case OPEN:
				this->update_meo(v,sec,msec,ptype,period);
				break;
			case CLOSE:
				this->update_mec(v,sec,msec,ptype,period);
				break;
			default:
				break;
			}
		}else {
			/*warnring*/
			goto again;
		}
		return 0;
}

int dseries::callback(float v,int sec, int msec){
	int ret;
again:
		boost::unique_lock<boost::timed_mutex> lk(this->dmutex,boost::chrono::milliseconds(1));
		if(lk) {
		}else {
			/*warnring*/
			ret=this->cb(v,sec,msec);
			goto again;
		}
	return 0;
}

int dseries::kline_update(kdata_type ktype, int t)
{
	int start, mstart,cidx,start_slot,curr_slot;

	start=this->tsec[this->cidx];
	mstart=this->tmsec[this->cidx];
	cidx=this->cidx;
	start_slot = get_period_slot(start,mstart,MINUTE ,1);
	curr_slot=get_period_slot(t,0,MINUTE,1);

	/*sure the contract is in in trading
	assert(curr_slot < start_slot + 2);
	assert(curr_slot > start_slot - 1);
	*/
	LOG_DEBUG<<"kline update: "<<" start: "<<start<<" curr: "<<t<<std::endl;

	if(curr_slot == start_slot) {
		return -1;
	} else if(curr_slot==start_slot+1){
		switch(ktype){
			case HIGH:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case LOW:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case OPEN:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case CLOSE:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			default:
				assert(0);
		}
	} else if(curr_slot>start_slot+5){
		/**/
		switch(ktype){
			case HIGH:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case LOW:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case OPEN:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			case CLOSE:
				this->cmsec=0;
				this->csec=t;
				this->data[cidx+1]=this->data[cidx];
				this->tsec[cidx]=t;
				this->tmsec[cidx]=0;
				break;
			default:
				assert(0);
		}
	}
	return 0;
}

int dseries::update_other(float v, int sec, int msec, period_type ptype,kdata_type ktype,int period){
	/*
	1.根据不同周期，将分钟级别的行情，更新到本周期.
	2.
	*/
again:
	boost::unique_lock<boost::timed_mutex> lk(this->dmutex,boost::chrono::milliseconds(1));
	if(lk) {
		switch(ktype) {
		case HIGH:
			this->update_meh(v,sec,msec,ptype,period);
			break;
		case LOW:
			this->update_mel(v,sec,msec,ptype,period);
			break;
		case OPEN:
			this->update_meo(v,sec,msec,ptype,period);
			break;
		case CLOSE:
			this->update_mec(v,sec,msec,ptype,period);
			break;
		default:
			break;
		}
	}else {
		/*warnring*/
		goto again;
	}
	return 0;

}

