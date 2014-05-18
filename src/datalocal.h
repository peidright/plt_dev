#ifndef DATALOCAL_H_
#define DATALOCAL_H_
#include <sqlite/sqlite3.h>
#include <string>
#include <map>
#include <vector>
#include "quote_io.h"
#include "instrument.h"

#include "log.h"

using namespace std;
struct kdata_s;
struct tdata_s;
class  quote_io;
class datalocal {
public:
	string dbn;
	datalocal(string dir,string dbname);
	~datalocal();
	void get_product_list(vector<string> &product_list);
	void store_instant_info(string product);
	void init_product_list(vector<string> product_list);
    void init_product(string product);
	void exe_cmd(string cmd, vector<map<string,string> > &rows);
	void exe_cmd(string cmd);
	int create_tdata_table(string contract);
	int create_kdata_table(string contract);
	int create_inst_kdata(string instn);
#if 0
	int create_inst_tdata(string instn);
	int create_inst_sdata(string instn);
	int load_inst_sdata( map<string, inst_t * > &instmap );
	int insert_inst_sdata(inst_t *pinst);
#endif

	int update_tdata(string contract, deque<struct tdata_s*> &tdataq);
	int update_kdata(string contract, deque<struct kdata_s*> &kdataq);
	sqlite3 *db;
};

class dmgr {
	public:
		map<string , datalocal * > db_map;
		map<string ,  inst_t *> instmap;
		map<string ,  inst_t *> qinstmap;
		quote_io *pquote_io;
		map<string,string> filter_inst;
		map<string,string> need_inst;

		map<string ,  inst_t *> new_instmap;
		int cstatus;
		int inst_sync;
		dmgr();
		int regdb(string dbname, datalocal *dl);
		int init();
		int load_inst();
};
#endif
