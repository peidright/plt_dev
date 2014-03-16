#ifndef DATALOCAL_H_
#define DATALOCAL_H_
#include "sqlite3.h"
#include <string>
#include <map>
#include <vector>
using namespace std;
class datalocal {
public:
	datalocal();
	~datalocal();
	void get_product_list(vector<string> &product_list);
	void store_instant_info(string product);
	void init_product_list(vector<string> product_list);
    void init_product(string product);
	void exe_cmd(string cmd, vector<map<string,string>> &rows);
	void exe_cmd(string cmd);
	sqlite3 *db;
};
#endif