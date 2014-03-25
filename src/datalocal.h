#ifndef DATALOCAL_H_
#define DATALOCAL_H_
#include "sqlite3.h"
#include <string>
#include <map>
#include <vector>
#include "quote_io.h"
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
	int update_tdata(string contract, deque<struct tdata_s*> &tdataq);
	int update_kdata(string contract, deque<struct kdata_s*> &kdataq);
	sqlite3 *db;
};
#endif
