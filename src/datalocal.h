#ifndef DATALOCAL_H_
#define DATALOCAL_H_
#include "sqlite3.h"
#include <string>
#include <map>
#include <vector>
#include "quote_io.h"
#include "instrument.h"
using namespace std;
struct kdata_s;
struct tdata_s;
class datalocal {
public:
	string dbn;
	datalocal(string dbname);
	~datalocal();
	void get_product_list(vector<string> &product_list);
	void store_instant_info(string product);
	void init_product_list(vector<string> product_list);
    void init_product(string product);
	void exe_cmd(string cmd, vector<map<string,string> > &rows);
	void exe_cmd(string cmd);
	int create_tdata_table(string contract);
	int create_kdata_table(string contract);
	int create_inst_tdata(string instn);
	int create_inst_sdata(string instn);
	int create_inst_kdata(string instn);

	int load_inst_sdata( map<string, inst_t * > &instmap );
	int insert_inst_sdata(inst_t *pinst);

	int update_tdata(string contract, deque<struct tdata_s*> &tdataq);
	int update_kdata(string contract, deque<struct kdata_s*> &kdataq);
	sqlite3 *db;
};

class dmgr {
	public:
		map<string , datalocal * > db_map;
		map<string ,  inst_t *> instmap;
		map<string ,  inst_t *> new_instmap;
		int cstatus;
		int inst_sync;
		dmgr(){
			this->cstatus=0;
			this->inst_sync=0;
		}
		int regdb(string dbname, datalocal *dl){/*err process*/ this->db_map[dbname]=dl;};
		int init(){};
		int sync_inst(){
			for(map<string, inst_t *>::iterator it=new_instmap.begin();it!=new_instmap.end();it++) {
				/*
				 * */
				this->add_inst(it->first,it->second, 1);
			}	
			this->inst_sync=1;	
		};
		int load_inst(){
			return 0;
		};
		int add_inst(string instn, inst_t *pinst, int syn) {
			if(this->instmap.find(instn)==this->instmap.end()) {
				/*
				 * */
				this->new_instmap[instn]=pinst;
			}
			if(syn) {
				/*flush it into db;
				 * */
				this->db_map["tdata"]->create_inst_tdata(instn);
				this->db_map["sdata"]->create_inst_sdata(instn);
			}
			return 0;
		};
		int get_inst(string instn, inst_t **pinst) {
			if(this->instmap.find(instn)==this->instmap.end()) {
				/*
				 * */
				(*pinst)=this->new_instmap[instn];
				/*insert it into table
				 * */
			} else {
				(*pinst)=NULL;
			}
			return 0;
		};
};
#endif
