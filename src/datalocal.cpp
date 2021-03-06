#include "datalocal.h"
#include <sqlite/sqlite3.h>
#include "config.h"
#include "assert.h"
#include <map>
#include <vector>
#include "quote_io.h"

#include <limits>

//...
//
//std::numeric_limits<float>::max();
//std::numeric_limits<float>::min();
//std::numeric_limits<float>::infinity();

int callback(void *,int count, char **row,char **titles)
{
	for(int i=0;i<count;i++){
		//cout<<"title= "<<titles[i]<<"value= "<<row[i]<<endl;
	}
	return 0;
}
datalocal::datalocal(string dir,string dbname)
{
	int ret;
	char                  *error = 0;
	//
	string path = dir + "/" + dbname;
	ret= sqlite3_config(SQLITE_CONFIG_URI) ;
	ret=sqlite3_config(SQLITE_CONFIG_MULTITHREAD);
	// assert(ret==SQLITE_OK);
	//ret = sqlite3_open("file:memdb1?mode=memory&cache=shared", &this->db); 
	ret = sqlite3_open(path.c_str(), &this->db); 
	if(ret==-1) {
		LOG_DEBUG<<"localdb create error"<<endl; 
	} else {
	}

	ret = sqlite3_exec(this->db, "drop  table trader", 0,0, &error );
	ret = sqlite3_exec(this->db, "create table trader(username char(32), password char(32))", 0,0, &error );
	assert(ret==SQLITE_OK);
	if(ret!=SQLITE_OK) {
		printf("%s\n",error);
        LOG_DEBUG<<"sql create table trade err:"<<error<<std::endl;
	}

	ret=sqlite3_exec(this->db,"insert into trader values ('aaa','bbb')",callback,NULL,&error);
	ret=sqlite3_exec(this->db,"select * from trader",callback,NULL,&error);
	assert(ret== SQLITE_OK);

	ret=sqlite3_exec(this->db, "drop table instrument",0,0,&error);
	ret=sqlite3_exec(this->db,"create table instrument(name char(32), product char(32), status  interger ,ctime integer)",0,0,&error);
	if(ret!=SQLITE_OK) {
        LOG_DEBUG<<"sql create table trade instrument err:"<<error<<std::endl;
	}

	/*create schema */
	ret=sqlite3_exec(this->db, "drop table contractschema",0,0,&error);
	ret=sqlite3_exec(this->db,"create table contractschema(contract char(32),ctype char(32))",callback,NULL,&error);
	assert(ret== SQLITE_OK);
	ret=sqlite3_exec(this->db,"insert into contractschema values('IF1404','m')",callback,NULL,&error);
	assert(ret== SQLITE_OK);

    /*todo
	vector<map<string,string> > result;
	this->exe_cmd("select contract,ctype from contractschema", result);
	for (vector<map<string,string> >::iterator it=result.begin();it!=result.end();it++) {
		char sqlbuf[256];
		memset(sqlbuf,0x0,256);
		sprintf(sqlbuf,"create table contract_%s(cprice real,oprice real,hprice real,lprice real,aprice real,bidprice real,askprice real,lastprice real,udtime integer,volume integer,turnover integer)",(*it)["contract"].c_str());
		this->exe_cmd(sqlbuf);
	}*/

	ret=sqlite3_exec(this->db, "insert into instrument values('IF1404','m',1,1380629713)",0,0,&error);
	//ret=sqlite3_exec(this->db,"drop table ",0,0,&error);
	//sqlite3_close(this->db);
}

int datalocal::create_tdata_table(string contract)
{
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
	*/
	char sqlbuf[256];
	sprintf(sqlbuf,"create table tdata_%s(open real,close real,high real,low real,uprice real,lprice real,bid1 real,bid2 real,bid3 real, bid4 real, bid5 real,ask1 real,ask2 real,ask3 real,ask4 real,ask5 real,lastprice real,sec integer,msec integer,vol integer)",contract.c_str());
	this->exe_cmd(sqlbuf);
	return 0;
}
#if 0
int datalocal::create_inst_tdata(string instn){
	assert(0);
	char sqlbuf[256];
	sprintf(sqlbuf,"create table tdata_%s(open real,close real,high real,low real,uprice real,lprice real,bid1 real,bid2 real,bid3 real, bid4 real, bid5 real,ask1 real,ask2 real,ask3 real,ask4 real,ask5 real,lastprice real,sec integer,msec integer,vol integer)",instn.c_str());
	this->exe_cmd(sqlbuf);
	return 0;
}

int datalocal::create_inst_sdata(string instn){
	char sqlbuf[1024];
	sprintf(sqlbuf,"create table sdata_inst(InstrumentID char(32),ExchangeID char(32),InstrumentName char(32),ExchangeInstID char(32),ProductID char(32),ProductClass char(1),DeliveryYear int,DeliveryMonth int,MaxMarketOrderVolume int,MinMarketOrderVolume int,MaxLimitOrderVolume int,MinLimitOrderVolume int,VolumeMultiple int,PriceTick float,CreateDate char(32),OpenDate char(32),ExpirDate char(32),StartDelivDate char(32),EndDelivDate char(32),InstLifePhase char(1),IsTrading int,PositionType char(1) ,PositionDateType char(1),LongMarginRatio float,ShortMarginRatio float,MaxMarginSideAlgorithm char(1))");
	this->exe_cmd(sqlbuf);
	return 0;
}

int datalocal::load_inst_sdata( map<string , inst_t * > &instmap )
{
	int ret=0;
	vector<map<string,string> > rows;
	datalocal::exe_cmd("select * from sdata_inst", rows);
	assert(ret==0);
	inst_t *pinst;
	for (vector<map<string,string> >::iterator it=rows.begin();it!=rows.end();it++) {
		pinst=new(inst_t);
		instmap[(*it)["InstrumentID"]]=pinst;
		sprintf(pinst->base.InstrumentID,(*it)["InstrumentID"].c_str());
		sprintf(pinst->base.ExchangeID,(*it)["ExchangeID"].c_str());
		sprintf(pinst->base.InstrumentName,(*it)["InstrumentName"].c_str());
		sprintf(pinst->base.ExchangeInstID,(*it)["ExchangeInstID"].c_str());
		sprintf(pinst->base.ProductID,(*it)["ProductID"].c_str());
		pinst->base.IsTrading=atoi((*it)["IsTrading"].c_str());
		pinst->base.LongMarginRatio=atof((*it)["LongMarginRatio"].c_str());
		pinst->base.ShortMarginRatio=atof((*it)["ShortMarginRatio"].c_str());


		/*to do there has a bug*/
		pinst->base.ProductClass=atoi((*it)["ProductClass"].c_str());
		pinst->base.InstLifePhase=atoi((*it)["InstLifePhase"].c_str());
		pinst->base.PositionType=atoi((*it)["PositionType"].c_str());
		pinst->base.PositionDateType=atoi((*it)["PositionDateType"].c_str());
		pinst->base.MaxMarginSideAlgorithm=atoi((*it)["MaxMarginSideAlgorithm"].c_str());

		pinst->base.DeliveryYear=atoi((*it)["DeliveryYear"].c_str());
		pinst->base.DeliveryMonth=atoi((*it)["DeliveryMonth"].c_str());
		pinst->base.MaxMarketOrderVolume=atoi((*it)["MaxMarketOrderVolume"].c_str());
		pinst->base.MinMarketOrderVolume=atoi((*it)["MinMarketOrderVolume"].c_str());
		pinst->base.MaxLimitOrderVolume=atoi((*it)["MinLimitOrderVolume"].c_str());
		pinst->base.VolumeMultiple=atoi((*it)["VolumeMultiple"].c_str());
		pinst->base.PriceTick=atof((*it)["PriceTick"].c_str());

		sprintf(pinst->base.CreateDate,(*it)["CreateDate"].c_str());
		sprintf(pinst->base.OpenDate,(*it)["OpenDate"].c_str());
		sprintf(pinst->base.ExpireDate,(*it)["ExpireDate"].c_str());
		sprintf(pinst->base.StartDelivDate,(*it)["StarDelivDate"].c_str());
		sprintf(pinst->base.EndDelivDate,(*it)["EndDelivDate"].c_str());
	}
}

int datalocal::insert_inst_sdata(inst_t *pinst)
{
	char sqlbuf[2048];
	sprintf(sqlbuf,"insert into sdata_inst values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%f\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%d\',\'%d\', \'%d\',\'%d\', \'%f\',\'%f\',\'%d\')",pinst->base.InstrumentID,pinst->base.ExchangeID,pinst->base.InstrumentName,pinst->base.ExchangeInstID,pinst->base.ProductID,pinst->base.ProductClass,pinst->base.DeliveryYear,pinst->base.DeliveryMonth,pinst->base.MaxMarketOrderVolume,pinst->base.MinMarketOrderVolume,pinst->base.MaxLimitOrderVolume,pinst->base.MinLimitOrderVolume,pinst->base.VolumeMultiple,pinst->base.PriceTick,pinst->base.CreateDate,pinst->base.OpenDate,pinst->base.ExpireDate,pinst->base.StartDelivDate,pinst->base.EndDelivDate,pinst->base.InstLifePhase,pinst->base.IsTrading,pinst->base.PositionType,pinst->base.PositionDateType,pinst->base.LongMarginRatio,pinst->base.ShortMarginRatio,pinst->base.MaxMarginSideAlgorithm);
	LOG_DEBUG<<"strlen:"<<strlen(sqlbuf)<<std::endl;
	this->exe_cmd(sqlbuf);
	return 0;
}
#endif

int datalocal::create_inst_kdata(string instn){
	/*todo err process
	 * */
	return 0;
}



int datalocal::update_tdata(string contract, deque<struct tdata_s*> &tdataq)
{
	int ret=0;
	//char *errmsg;
	int size=tdataq.size();
	char sqlbuf[2048];

	/*todo err check, sure the table existed!
	 * NLL
	*/

	if(size > 10){
		this->exe_cmd("BEGIN;");
		//this->exe_cmd("VACUUM;");
	}

	for(deque<struct tdata_s*>::iterator it=tdataq.begin();it!=tdataq.end();it++) {
		/**/
		memset(sqlbuf,0x0,sizeof(sqlbuf));
		sprintf(sqlbuf,"insert into tdata_%s values ('%f','%f','%f','%f','%f','%f', '%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%d','%d','%d')",contract.c_str(),(*it)->open,(*it)->close,(*it)->high,(*it)->low,(*it)->uprice,(*it)->lprice,(*it)->bid1,(*it)->bid2,(*it)->bid3,(*it)->bid4,(*it)->bid5,(*it)->ask1,(*it)->ask2,(*it)->ask3,(*it)->ask4,(*it)->ask5,(*it)->lastprice,(*it)->sec,(*it)->msec,(*it)->vol);

		this->exe_cmd(sqlbuf);
		if((*it)->bid4==std::numeric_limits<float>::infinity()) {
			//LOG_DEBUG<<"MAX FLOAT equal"<<std::endl;
		} else {
			//LOG_DEBUG<<"MAX FLOAT not equal"<<(*it)->bid4<<"  "<<  std::numeric_limits<float>::infinity() <<std::endl;
		}
	}

	if(size > 10) {
		this->exe_cmd("COMMIT;");
	}
	return ret;
}
int datalocal::update_kdata(string contract,deque<struct kdata_s*> &kdataq)
{
	int ret;
	char *errmsg;
    char sqlbuf[2048];
	int size=kdataq.size();
	if(size > 10){
		ret = sqlite3_exec(this->db, "BEGIN;", 0, 0, &errmsg);
		assert(ret==0);
	}

	for(deque<struct kdata_s*>::iterator it=kdataq.begin();it!=kdataq.end();it++) {
		/**/
        sprintf(sqlbuf,"insert table kdata_%d_%s('%f','%f','%f','%f','%d','%d','%d','%d')",(*it)->period,contract.c_str(), (*it)->open,(*it)->close,
                (*it)->high,(*it)->low,(*it)->vol,(*it)->mnum,(*it)->sec,(*it)->msec);
        this->exe_cmd(sqlbuf);
	}
	if(size > 10) {
		ret = sqlite3_exec(this->db, "COMMIT;", 0, 0, &errmsg);
		assert(ret==0);
	}
	return 0;
}



int datalocal::create_kdata_table(string contract)
{
	return 0;
}


int get_product_callback(void *arg,int count, char **row,char **titles)
{
	for(int i=0;i<count;i++){
		//cout<<"title= "<<titles[i]<<"value= "<<row[i]<<endl;
	}
	return 0;
}
int general_callback(void *arg, int count, char **row, char **titles)
{
	vector< map<string,string> > *v=(vector< map<string,string> > *)arg;
	map<string,string> m;

	for(int i=0;i<count;i++){
		//cout<<"title= "<<titles[i]<<" "<<"value= "<<row[i]<<endl;
		m[titles[i]]=row[i];
	}
	v->push_back(m);
	return 0;
}

void datalocal:: get_product_list(vector<string> &product_list)
{
	//int ret;
	//char                  *error = 0;
	vector< map<string,string> > rows;
	vector< map<string,string> >::iterator rows_it;
	//ret=sqlite3_exec(this->db,"select name, product, status,ctime from instrument",general_callback,&rows,&error);
	this->exe_cmd("select name, product, status,ctime from instrument", rows);
	for(rows_it=rows.begin();rows_it!=rows.end();rows_it++) {
		(*rows_it)["name"];
		product_list.push_back((*rows_it)["name"]);
	}
}

void datalocal::init_product_list(vector<string> product_list)
{
	//*check if exist product_list,if not exist,delete*//
	vector<map<string,string> > rows;
	this->exe_cmd("select name from sqlite_master where type='table'",rows);
}

void datalocal::init_product(string product)
{
	vector<map<string,string> > rows;
	this->exe_cmd("select name from sqlite_master where type='table'",rows);
	this->exe_cmd("create table instrument(day integer, seconds integer, \
		           closeprice integer,openprice  interger,uprice integer,lprice integer,\
				   highprice integer,lowprice integer,lastprice integer,\
				   avgprice integer,vol integer,bid1 integer,ask1 integer",rows);
}

void datalocal::exe_cmd(string cmd, vector<map<string,string> > &rows)
{
	int ret;
	char                  *error = 0;
	//vector< map<string,string> > rows;
	vector< map<string,string> >::iterator rows_it;
	map<string,string>::iterator rows_map_it;
	ret=sqlite3_exec(this->db,cmd.c_str(),general_callback,&rows,&error);
	if (ret!=SQLITE_OK) {
		LOG_DEBUG<<"sqlstr :"<<cmd.c_str()<<" exe err: "<<error<<endl;
	}
	for(rows_it=rows.begin();rows_it!=rows.end();rows_it++) {
		for(rows_map_it=rows_it->begin();rows_map_it!=rows_it->end();rows_map_it++) {
			//LOG_DEBUG<<" ; "<<rows_map_it->first<<"=="<<rows_map_it->second;
		}
		//LOG_DEBUG<<std::endl;
	}
}

void datalocal::exe_cmd(string cmd)
{
	int ret;
	char                  *error = 0;
	//vector< map<string,string> > rows;
	ret=sqlite3_exec(this->db,cmd.c_str(),NULL,NULL,&error);
	if (ret!=SQLITE_OK) {
		LOG_DEBUG<<"sqlstr :"<<cmd.c_str()<<" exe err: "<<error<<endl;
	}
}

void datalocal::store_instant_info(string product)
{

}

datalocal::~datalocal()
{
	sqlite3_close(this->db);
	this->db=NULL;
}


dmgr::dmgr(){
    this->cstatus=0;
    this->inst_sync=0;

    /*todo for debug
     * */
    this->need_inst["IF1404"]="IF1404";
    this->need_inst["ag1412"]="ag1412";
}
int dmgr::regdb(string dbname, datalocal *dl){
    /*err process*/ 
    this->db_map[dbname]=dl;
    return 0;
};
int dmgr::init(){
    return 0;
};
int dmgr::load_inst(){
    return 0;
};
