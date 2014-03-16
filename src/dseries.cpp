
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
			        /*��Ҫ����,���ﲻȷ���Ƿ�֤�Ⱥ�˳��.��ʱ��˳��Ĵ������Բ���˳��İ�����.
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
			/*�ж��Ƿ��ǵ�ǰ���k��
			  ����ǵ�ǰ���ӵģ����±�k�ߡ�
		      �������һ�����ߣ������¸�k�ߣ��������k��Ϊ�գ��Ƿ����޸�������
			  ������������ģ���������һ���ӣ�������϶����������һ���ӡ�
			  ������������ģ������Ÿ��¡�
			  �����֮ǰ�����ݣ����Դ�����..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);
			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*�����ǰ�Ǹտ�ʼ��	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*����ǵ�һ��k�ߣ�
			      1.�Ƿ������µ�����
				  2.ȡmaxֵ��
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tmsec[cidx]=msec;
					this->tsec[cidx]=sec;
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=now;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}

			} else if(cidx!=0 && start_slot!=0) {
			   /*��cidxΪ����ֵ��ʱ�����cidx��Ȼ���Ѿ�����ʵ�ʱ��ۣ�
			     ����timer��ʱ���Ѿ�������!
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=std::max<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start+1)==now){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
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
				/*�ж��Ƿ��ǵ�ǰ���k��
			  ����ǵ�ǰ���ӵģ����±�k�ߡ�
		      �������һ�����ߣ������¸�k�ߣ��������k��Ϊ�գ��Ƿ����޸�������
			  ������������ģ���������һ���ӣ�������϶����������һ���ӡ�
			  ������������ģ������Ÿ��¡�
			  �����֮ǰ�����ݣ����Դ�����..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);
			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*�����ǰ�Ǹտ�ʼ��	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start!=0){
	           /*����ǵ�һ��k�ߣ�
			      1.�Ƿ������µ�����
				  2.ȡmaxֵ��
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->data[cidx]=v;
					this->tmsec[cidx]=msec;
				}

			} else if(cidx!=0 ) {
			   /*��cidxΪ����ֵ��ʱ�����cidx��Ȼ���Ѿ�����ʵ�ʱ��ۣ�
			     ����timer��ʱ���Ѿ�������!
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=std::min<float>(this->data[cidx],v);
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
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
				/*�ж��Ƿ��ǵ�ǰ���k��
			  ����ǵ�ǰ���ӵģ����±�k�ߡ�
		      �������һ�����ߣ������¸�k�ߣ��������k��Ϊ�գ��Ƿ����޸�������
			  ������������ģ���������һ���ӣ�������϶����������һ���ӡ�
			  ������������ģ������Ÿ��¡�
			  �����֮ǰ�����ݣ����Դ�����..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*�����ǰ�Ǹտ�ʼ��	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*����ǵ�һ��k�ߣ�
			      1.�Ƿ������µ�����
				  2.ȡmaxֵ��
			   */

			} else if(cidx!=0 && start_slot==0) {
			   /*��cidxΪ����ֵ��ʱ�����cidx��Ȼ���Ѿ�����ʵ�ʱ��ۣ�
			     ����timer��ʱ���Ѿ�������!
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����,����open*/
				    //this->data[cidx]=std::max<float>(this->data[cidx],v);
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
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
				/*�ж��Ƿ��ǵ�ǰ���k��
			  ����ǵ�ǰ���ӵģ����±�k�ߡ�
		      �������һ�����ߣ������¸�k�ߣ��������k��Ϊ�գ��Ƿ����޸�������
			  ������������ģ���������һ���ӣ�������϶����������һ���ӡ�
			  ������������ģ������Ÿ��¡�
			  �����֮ǰ�����ݣ����Դ�����..
			*/	
		    int start,mstart,cidx,now,start_slot,curr_slot;
			start=this->tsec[this->cidx];
			mstart=this->tmsec[this->cidx];
			cidx=this->cidx;
			now=60*(sec/60);

			start_slot = get_period_slot(start,mstart, ptype,period);
			curr_slot=get_period_slot(sec,msec,ptype,period);
			if(start_slot==0 && cidx==0) {
				/*�����ǰ�Ǹտ�ʼ��	  
				*/
				this->data[cidx]=v;
				this->tsec[cidx]=sec;
				this->tmsec[cidx]=msec;
			}else if(cidx==0 && start_slot!=0){
	           /*����ǵ�һ��k�ߣ�
			      1.�Ƿ������µ�����
				  2.ȡmaxֵ��
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}

			} else if(cidx!=0) {
			   /*��cidxΪ����ֵ��ʱ�����cidx��Ȼ���Ѿ�����ʵ�ʱ��ۣ�
			     ����timer��ʱ���Ѿ�������!
			   */
				if(start_slot==curr_slot) {
					/*�����ͬһ����*/
				    this->data[cidx]=v;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
				}else if((start_slot+1)==curr_slot){
					/*������µ�һ����*/
					this->cidx++;
					cidx=this->cidx;
					this->tsec[cidx]=sec;
					this->tmsec[cidx]=msec;
					this->data[cidx]=v;
				}else if(1/*��ͬһʱ���*/) {
					/*�п���Ҫ���ǲ�ȫ��϶*/

				}else {
					/*���ٿ��ǲ�ȫ��϶*/
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
	1.���ݲ�ͬ���ڣ������Ӽ�������飬���µ�������.
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

