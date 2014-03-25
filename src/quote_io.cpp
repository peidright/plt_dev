#include "quote_io.h"

quote_io g_quote_io;
void quote_io::quote_kdata_push(string contract, kdata_t *data)
{
	if(this->kdata_map.find(contract)==this->kdata_map.end()) {
		/*error process
		 to fix there has a mutex bug
		*/
		this->kdata_map[contract]=new (kdata_io_t);
		//return ;
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
		to fix there has a mutex bug
		*/
		this->tdata_map[contract]=new (tdata_io_t);
		//return ;
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
	/*
	*/
	time_t t=time(NULL);
	map<string, kdata_io_t *> kdata_map;
	map<string, tdata_io_t *> tdata_map;
	deque<tdata_t*> tdataq;
	for(map<string, tdata_io_t *>::iterator it=this->tdata_map.begin();it!=this->tdata_map.end();it++) {
		/**/
		tdataq.clear();
		if(it->second->tdataq.size()>10 || ((int)t -it->second->lsec )>10) {
			/*
				lockit, copy it out , flush it to db
				todo assert it->first exit in db_map
			*/
			boost::unique_lock<boost::timed_mutex> lk(it->second->qmutex,boost::chrono::milliseconds(100));
			tdataq.swap(it->second->tdataq);
			this->db_map[it->first]->update_tdata(it->first, tdataq);
		/*
	data->sec=sec;
	data->msec=msec;
	data->ask1=mdata->pDepthMarketData.AskPrice1;
	data->ask2=mdata->pDepthMarketData.AskPrice2;
	data->ask3=mdata->pDepthMarketData.AskPrice3;
	data->ask4=mdata->pDepthMarketData.AskPrice4;
	data->ask5=mdata->pDepthMarketData.AskPrice5;
	data->bid1=mdata->pDepthMarketData.BidPrice1;
	data->bid2=mdata->pDepthMarketData.BidPrice2;
	data->bid3=mdata->pDepthMarketData.BidPrice3;
	data->bid4=mdata->pDepthMarketData.BidPrice4;
	data->bid5=mdata->pDepthMarketData.BidPrice5;
	data->vol=mdata->pDepthMarketData.Volume;
	data->uprice=mdata->pDepthMarketData.UpperLimitPrice;
	data->lprice=mdata->pDepthMarketData.LowerLimitPrice;
	data->high=mdata->pDepthMarketData.HighestPrice;
	data->low=mdata->pDepthMarketData.LowestPrice;
	data->close=mdata->pDepthMarketData.OpenPrice;
	data->open=mdata->pDepthMarketData.ClosePrice;
	data->lastprice=mdata->pDepthMarketData.LastPrice;
	quote_push(contract,data);
		*/

			/*push it into db*/
	
		}
	}
}
void quote_io::quote_io_work()
{
	/*
	*/
	this->quote_kdata_work();
	this->quote_tdata_work();
}

void quote_push(string contract ,tdata_t *data){
	g_quote_io.quote_tdata_push(contract, data);
}

void quote_io_work() 
{
	g_quote_io.quote_io_work();
}
