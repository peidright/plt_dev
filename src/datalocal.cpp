#include "datalocal.h"
#include "sqlite3.h"
#include "config.h"
#include "assert.h"
#include <map>
#include <vector>
string g_db_name="local.sdb";

int callback(void *,int count, char **row,char **titles)
{
	for(int i=0;i<count;i++){
		cout<<"title= "<<titles[i]<<"value= "<<row[i]<<endl;
	}
	return 0;
}
datalocal::datalocal()
{
	int ret;
	char                  *error = 0;
	//
	ret= sqlite3_config(SQLITE_CONFIG_URI) ;
	ret=sqlite3_config(SQLITE_CONFIG_MULTITHREAD);
	// assert(ret==SQLITE_OK);
	//ret = sqlite3_open("file:memdb1?mode=memory&cache=shared", &this->db); 
	ret = sqlite3_open(g_db_name.c_str(), &this->db); 
	if(ret==-1) {
		cout<<"localdb create error"<<endl; 
	} else {
		cout<<"localdb init ok"<<endl;
	}

	ret = sqlite3_exec(this->db, "drop  table trader", 0,0, &error );
	ret = sqlite3_exec(this->db, "create table trader(username char(32), password char(32))", 0,0, &error );
	assert(ret==SQLITE_OK);
	if(ret!=SQLITE_OK) {
		printf("%s\n",error);
	}

	ret=sqlite3_exec(this->db,"insert into trader values ('aaa','bbb')",callback,NULL,&error);
	ret=sqlite3_exec(this->db,"select * from trader",callback,NULL,&error);
	assert(ret== SQLITE_OK);

	ret=sqlite3_exec(this->db, "drop table instrument",0,0,&error);
	ret=sqlite3_exec(this->db,"create table instrument(name char(32), product char(32), status  interger ,ctime integer)",0,0,&error);
	if(ret!=SQLITE_OK) {
		printf("%s\n",error);
	}

	/*create schema */
	ret=sqlite3_exec(this->db, "drop table contractschema",0,0,&error);
	ret=sqlite3_exec(this->db,"create table contractschema(contract char(32),ctype char(32))",callback,NULL,&error);
	assert(ret== SQLITE_OK);
	ret=sqlite3_exec(this->db,"insert into contractschema values('rm1401','rm')",callback,NULL,&error);
	assert(ret== SQLITE_OK);

	vector<map<string,string> > result;
	this->exe_cmd("select contract,ctype from contractschema", result);

	/*create all table*/
	for (vector<map<string,string> >::iterator it=result.begin();it!=result.end();it++) {
		char sqlbuf[256];
		memset(sqlbuf,0x0,256);
		cout<<"sql1:begin"<<endl;
		sprintf(sqlbuf,"create table contract_%s(cprice real,oprice real,hprice real,lprice real,aprice real,bidprice real,askprice real,lastprice real,udtime integer,volume integer,turnover integer)",(*it)["contract"].c_str());
		cout<<"sql1£º"<<sqlbuf<<endl;
		this->exe_cmd(sqlbuf);
		cout<<"sql1:end"<<endl;
	}
	cout<<"sql2:end"<<endl;
	ret=sqlite3_exec(this->db, "insert into instrument values('au1406','au',1,1380629713)",0,0,&error);
	//ret=sqlite3_exec(this->db,"drop table ",0,0,&error);
	//sqlite3_close(this->db);
}

int get_product_callback(void *arg,int count, char **row,char **titles)
{
	for(int i=0;i<count;i++){
		cout<<"title= "<<titles[i]<<"value= "<<row[i]<<endl;
	}
	return 0;
}
int general_callback(void *arg, int count, char **row, char **titles)
{
	vector< map<string,string> > *v=(vector< map<string,string> > *)arg;
	map<string,string> m;

	for(int i=0;i<count;i++){
		cout<<"title= "<<titles[i]<<" "<<"value= "<<row[i]<<endl;
		m[titles[i]]=row[i];
	}
	v->push_back(m);
	return 0;
}

void datalocal:: get_product_list(vector<string> &product_list)
{
	//int ret;
	char                  *error = 0;
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
    /*product_day (day, openprice,closeprice,highprice,lowprice,
	  product_instant (day,seconds,openprice, closeprice, lastprice,lowprice,highprice,avgprice,vol,bid1,ask1,uprice,lprice,tvol,tavgprice)
	  product_xxxxxxx  (???)
	*/	
	
}

void datalocal::exe_cmd(string cmd, vector<map<string,string> > &rows)
{
	int ret;
	char                  *error = 0;
	//vector< map<string,string> > rows;
	vector< map<string,string> >::iterator rows_it;
	map<string,string>::iterator rows_map_it;
	//cout<<"!!!!!!!!!!!!!!!!!"<<endl;
	ret=sqlite3_exec(this->db,cmd.c_str(),general_callback,&rows,&error);
	if (ret!=SQLITE_OK) {
		cout<<"sqlite exe err: "<<error<<endl;
	}
	for(rows_it=rows.begin();rows_it!=rows.end();rows_it++) {
		for(rows_map_it=rows_it->begin();rows_map_it!=rows_it->end();rows_map_it++) {
			cout<<rows_map_it->first<<"=="<<rows_map_it->second<<endl;
		}
	}
	//cout<<"!!!!!!!!!!!!!!!!!"<<endl;
}

void datalocal::exe_cmd(string cmd)
{
	int ret;
	char                  *error = 0;
	//vector< map<string,string> > rows;
	//cout<<"!!!!!!!!!!!!!!!!!"<<endl;
	ret=sqlite3_exec(this->db,cmd.c_str(),NULL,NULL,&error);
	if (ret!=SQLITE_OK) {
		cout<<"sqlite exe err: "<<error<<endl;
	}
	//cout<<"!!!!!!!!!!!!!!!!!"<<endl;
}

void datalocal::store_instant_info(string product)
{

}

datalocal::~datalocal()
{
	sqlite3_close(this->db);
	this->db=NULL;
}


