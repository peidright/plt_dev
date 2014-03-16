#ifndef ACCOUNT_H_
#define ACCOUNT_H_
#include <string>
#include <map>

using namespace std;


typedef struct cp {
	int blots;
	int slots;
	int baprice;
	int saprice;
	int bprofit;
	int sprofit;
	int bdepos;
	int sdepos;
	char cname[32];
	int time;
}cp_t;
	
typedef struct captial {
	int total;
	int used;
	int left;
	int profit;
}captial_t;

class Account{
public:
	map<std::string,map<string, cp_t> > contract_positon;
	captial_t captial;
};

#endif