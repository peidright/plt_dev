#include "quote_io.h"


void quote_io::quote_kdata_push(string contract, kdata_t *data)
{
	if(this->kdata_map.find(contract)==this->kdata_map.end()) {
		/*error process
		*/
		return ;
	}
again:
	boost::unique_lock<boost::timed_mutex> lk(this->kdata_map[contract]->qmutex,boost::chrono::milliseconds(1));
	if (lk){
		this->kdata_map[contract]->kdataq.push_back(data);
		this->kdata_map[contract]->lmsec=data->msec;
		this->kdata_map[contract]->lsec=data->sec;
	}else {
		goto again;
	}
	return;
}

void quote_io::quote_tdata_push(string contract, tdata_t *data)
{
	if(this->tdata_map.find(contract)==this->tdata_map.end()) {
		/*error process
		*/
		return ;
	}
again:
	boost::unique_lock<boost::timed_mutex> lk(this->tdata_map[contract]->qmutex,boost::chrono::milliseconds(1));
	if (lk){
		this->tdata_map[contract]->tdataq.push_back(data);
		this->tdata_map[contract]->lmsec=data->msec;
		this->tdata_map[contract]->lsec=data->sec;
	}else {
		goto again;
	}
	return;
}

void quote_io::quote_kdata_work()
{
	/*将数据入库*/
	int now=(int)time(NULL);

}

void quote_io::quote_tdata_work()
{
}
void quote_io::quote_io_work()
{
	/*
	*/
	this->quote_kdata_work();
	this->quote_tdata_work();
}