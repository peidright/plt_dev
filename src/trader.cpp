#include "trader.h"
#include <string.h>
#include <stdio.h>
 Trader::Trader(string username, string password,string brokerid,string trade_addr)
{
	this->password=password;
	this->username=username;
	this->brokerid=brokerid;
	this->trade_addr=trade_addr;
}

Quoter::Quoter(string username, string password,string brokerid,string quote_addr)
{
	this->password=password;
	this->username=username;
	this->brokerid=brokerid;
	this->quote_addr=quote_addr;
}
