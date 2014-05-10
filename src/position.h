#ifndef POSITION_H_
#define POSITION_H_
#include "ThostFtdcTraderApi.h"

typedef struct {
    struct CThostFtdcInvestorPositionField base;
}position_t;

typedef struct {
    CThostFtdcOrderField base;
    int uptime;
}order_t;
typedef struct {
    CThostFtdcInputOrderField base; 
    int stime;
    int err_status;
}ordreq_t;

#endif
