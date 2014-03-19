
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

dseries::dseries(){
	/*
	static const int MAX_DSERIES_SIZE=10000;
	float data[MAX_DSERIES_SIZE];
	int   tsec[MAX_DSERIES_SIZE];
	int   tmsec[MAX_DSERIES_SIZE];
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
	LOG_DEBUG<<"price¿"<<this->data[this->cidx]<< "time: "<<this->tsec[this->cidx]<<std::endl;
	return 0;
}
int dseries::update_ms(float v, int sec, int msec){
		/*
		  1.
		  2.
		*/
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
				cerr<<"dseries update_ms drop old message"<<std::endl;
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

int dseries::update_meh(float v, int sec, int msec,period_type ptype, int period){
			/*ÅÐ¶ÏÊÇ·ñÊÇµ±Ç°Õâ¸ùkÏß
			  Èç¹ûÊÇµ±Ç°·ÖÖÓµÄ£¬¸üÐÂ±¾kÏß¡£
		      Èç¹ûÊÇÏÂÒ»·ÖÖÓÏß£¬¸üÐÂÏÂ¸ùkÏß£¬Èç¹û±¾¸ùkÏßÎª¿Õ£¬ÊÇ·ñ¿¼ÂÇÐÞ¸´±¾¸ù£¿
			  Èç¹ûÊÇÊÇÁ¬ÐøµÄ£¬µ«²»ÊÇÏÂÒ»·ÖÖÓ£¬Á÷³ö¿ÕÏ¶¡£µ«¸üÐÂÏÂÒ»·ÖÖÓ¡£
			  Èç¹û²»ÊÇÁ¬ÐøµÄ£¬½ô½Ó×Å¸üÐÂ¡£
			  Èç¹ûÊÇÖ®Ç°µÄÊý¾Ý£¬ºöÂÔ´ËÊý¾Ý..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);
			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*Èç¹ûµ±Ç°ÊÇ¸Õ¿ªÊ¼¡£	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*Èç¹ûÊÇµÚÒ»¸ùkÏß£¬
			      1.ÊÇ·ñÊÇ×îÐÂµÄÊý¾Ý
				  2.È¡maxÖµ¡£
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tmsec[cidx]=msec;
					this->tsec[cidx]=sec;
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=now;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}

			} else if(cidx!=0 && start_slot!=0) {
			   /*µ±cidxÎª·ÇÁãÖµµÃÊ±ºò£¬Õâ¸öcidx±ØÈ»ÊÇÒÑ¾­ÓÐÓÐÊµ¼Ê±¨¼Û£¬
			     »òÕßtimer¶¨Ê±Æ÷ÒÑ¾­·¢Éú¹ý!
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start+1)==now){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
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
				/*ÅÐ¶ÏÊÇ·ñÊÇµ±Ç°Õâ¸ùkÏß
			  Èç¹ûÊÇµ±Ç°·ÖÖÓµÄ£¬¸üÐÂ±¾kÏß¡£
		      Èç¹ûÊÇÏÂÒ»·ÖÖÓÏß£¬¸üÐÂÏÂ¸ùkÏß£¬Èç¹û±¾¸ùkÏßÎª¿Õ£¬ÊÇ·ñ¿¼ÂÇÐÞ¸´±¾¸ù£¿
			  Èç¹ûÊÇÊÇÁ¬ÐøµÄ£¬µ«²»ÊÇÏÂÒ»·ÖÖÓ£¬Á÷³ö¿ÕÏ¶¡£µ«¸üÐÂÏÂÒ»·ÖÖÓ¡£
			  Èç¹û²»ÊÇÁ¬ÐøµÄ£¬½ô½Ó×Å¸üÐÂ¡£
			  Èç¹ûÊÇÖ®Ç°µÄÊý¾Ý£¬ºöÂÔ´ËÊý¾Ý..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);
			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*Èç¹ûµ±Ç°ÊÇ¸Õ¿ªÊ¼¡£	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start!=0){
	           /*Èç¹ûÊÇµÚÒ»¸ùkÏß£¬
			      1.ÊÇ·ñÊÇ×îÐÂµÄÊý¾Ý
				  2.È¡maxÖµ¡£
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}

			} else if(cidx!=0 ) {
			   /*µ±cidxÎª·ÇÁãÖµµÃÊ±ºò£¬Õâ¸öcidx±ØÈ»ÊÇÒÑ¾­ÓÐÓÐÊµ¼Ê±¨¼Û£¬
			     »òÕßtimer¶¨Ê±Æ÷ÒÑ¾­·¢Éú¹ý!
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
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
				/*ÅÐ¶ÏÊÇ·ñÊÇµ±Ç°Õâ¸ùkÏß
			  Èç¹ûÊÇµ±Ç°·ÖÖÓµÄ£¬¸üÐÂ±¾kÏß¡£
		      Èç¹ûÊÇÏÂÒ»·ÖÖÓÏß£¬¸üÐÂÏÂ¸ùkÏß£¬Èç¹û±¾¸ùkÏßÎª¿Õ£¬ÊÇ·ñ¿¼ÂÇÐÞ¸´±¾¸ù£¿
			  Èç¹ûÊÇÊÇÁ¬ÐøµÄ£¬µ«²»ÊÇÏÂÒ»·ÖÖÓ£¬Á÷³ö¿ÕÏ¶¡£µ«¸üÐÂÏÂÒ»·ÖÖÓ¡£
			  Èç¹û²»ÊÇÁ¬ÐøµÄ£¬½ô½Ó×Å¸üÐÂ¡£
			  Èç¹ûÊÇÖ®Ç°µÄÊý¾Ý£¬ºöÂÔ´ËÊý¾Ý..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*Èç¹ûµ±Ç°ÊÇ¸Õ¿ªÊ¼¡£	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*Èç¹ûÊÇµÚÒ»¸ùkÏß£¬
			      1.ÊÇ·ñÊÇ×îÐÂµÄÊý¾Ý
				  2.È¡maxÖµ¡£
			   */

			} else if(cidx!=0 && start_slot==0) {
			   /*µ±cidxÎª·ÇÁãÖµµÃÊ±ºò£¬Õâ¸öcidx±ØÈ»ÊÇÒÑ¾­ÓÐÓÐÊµ¼Ê±¨¼Û£¬
			     »òÕßtimer¶¨Ê±Æ÷ÒÑ¾­·¢Éú¹ý!
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ,²»ÊÇopen*/
				    //this->data[cidx]=std::max<float>(this->data[cidx],v);
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
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
				/*ÅÐ¶ÏÊÇ·ñÊÇµ±Ç°Õâ¸ùkÏß
			  Èç¹ûÊÇµ±Ç°·ÖÖÓµÄ£¬¸üÐÂ±¾kÏß¡£
		      Èç¹ûÊÇÏÂÒ»·ÖÖÓÏß£¬¸üÐÂÏÂ¸ùkÏß£¬Èç¹û±¾¸ùkÏßÎª¿Õ£¬ÊÇ·ñ¿¼ÂÇÐÞ¸´±¾¸ù£¿
			  Èç¹ûÊÇÊÇÁ¬ÐøµÄ£¬µ«²»ÊÇÏÂÒ»·ÖÖÓ£¬Á÷³ö¿ÕÏ¶¡£µ«¸üÐÂÏÂÒ»·ÖÖÓ¡£
			  Èç¹û²»ÊÇÁ¬ÐøµÄ£¬½ô½Ó×Å¸üÐÂ¡£
			  Èç¹ûÊÇÖ®Ç°µÄÊý¾Ý£¬ºöÂÔ´ËÊý¾Ý..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*Èç¹ûµ±Ç°ÊÇ¸Õ¿ªÊ¼¡£	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*Èç¹ûÊÇµÚÒ»¸ùkÏß£¬
			      1.ÊÇ·ñÊÇ×îÐÂµÄÊý¾Ý
				  2.È¡maxÖµ¡£
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}

			} else if(cidx!=0) {
			   /*µ±cidxÎª·ÇÁãÖµµÃÊ±ºò£¬Õâ¸öcidx±ØÈ»ÊÇÒÑ¾­ÓÐÓÐÊµ¼Ê±¨¼Û£¬
			     »òÕßtimer¶¨Ê±Æ÷ÒÑ¾­·¢Éú¹ý!
			   */
				if(start_slot==curr_slot) {
					/*Èç¹ûÊÇÍ¬Ò»·ÖÖÓ*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*Èç¹ûÊÇÐÂµÄÒ»·ÖÖÓ*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*ÊÇÍ¬Ò»Ê±¼ä¶Î*/) {
					/*ÓÐ¿ÉÄÜÒª¿¼ÂÇ²¹È«¼äÏ¶*/

				}else {
					/*²»ÔÙ¿¼ÂÇ²¹È«¼äÏ¶*/
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
	1.¸ù¾Ý²»Í¬ÖÜÆÚ£¬½«·ÖÖÓ¼¶±ðµÄÐÐÇé£¬¸üÐÂµ½±¾ÖÜÆÚ.
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

