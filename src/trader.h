#ifndef TRADER_H_
#define TRADER_H_
#include <string>
using namespace std;
class Trader {
public:
	string username;
	string password;
	string brokerid;
	string trade_addr;
	string quote_addr;
	Trader(string username,string password,string brokerid,string trade_addr);
};

class Quoter {
public:
	string username;
	string password;
	string brokerid;
	string quote_addr;
	Quoter(string username,string password,string brokerid,string quote_addr);
};

#endif