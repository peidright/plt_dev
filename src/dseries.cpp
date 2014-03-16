
#include "dseries.h"

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

dseries::dseries(){cidx=0;};

dseries::dseries(const dseries &){};

int dseries::update_ms(float v, int sec, int msec){
		/*
		  1.
		  2.
		*/
	again:
		boost::unique_lock<boost::timed_mutex> lk(this->dmutex,boost::chrono::milliseconds(1));
		if(lk) {
			if( (sec > this->csec) || 
				(sec== this->csec && (msec >this->cmsec))
				) {
			        /*需要更新,这里不确认是否保证先后顺序.暂时按顺序的处理。忽略不按顺序的包丢弃.
				   */
					this->tmsec[this->cidx]=msec;
					this->tsec[this->cidx]=sec;
					this->data[this->cidx]=v;
					this->cidx++;
					this->csec=sec;
					this->cmsec=msec;
			}else {
				/*todo warning, drop old message*/
			}
		}else {
			/*warnring*/
			goto again;
		}
		return 0;
	}

int dseries::update_meh(float v, int sec, int msec,period_type ptype, int period){
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
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tmsec[cidx]=msec;
					this->tsec[cidx]=sec;
				}else if((start_slot+1)==curr_slot){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=now;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
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

			} else if(cidx!=0 && start_slot!=0) {
			   /*当cidx为非零值得时候，这个cidx必然是已经有有实际报价，
			     或者timer定时器已经发生过!
			   */
				if(start_slot==curr_slot) {
					/*如果是同一分钟*/
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start+1)==now){
					/*如果是新的一分钟*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
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
			} else if(cidx!=0 && start==0) {
					assert(0);
			}
			this->csec=sec;
			this->cmsec=msec;
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

