#ifndef HELP_H_
#define HELP_H_
#include "mdseries.h"
#include "boost/date_time.hpp"
using namespace boost::posix_time;
using namespace boost::gregorian;
int between(time_t start, time_t end,time_t t);
int between(time_t start, time_t end,time_t t1,time_t t2);
time_t tm_fix(tm *t,int hour,int minutes);
int tm_continue(tm *t1, tm *t2);
int is_continue(int e1,int e2, int b1, int b2);
int fix();
int date2time(string dat);
#endif
