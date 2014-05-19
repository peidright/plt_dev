#ifndef POSITION_H_
#define POSITION_H_
#include <vector>
#include "ThostFtdcTraderApi.h"

typedef struct {
    struct CThostFtdcInvestorPositionField bbase;
    struct CThostFtdcInvestorPositionField sbase;
    int syned;
}position_t;

typedef struct {
    CThostFtdcOrderField base;
    vector<struct CThostFtdcTradeField*> ordtrdq;
    int uptime;
}order_t;

typedef struct {
    CThostFtdcInputOrderField base; 
    int stime;
    int err_status;
}ordreq_t;

position_t *update_position(CThostFtdcTradeField* trade, position_t *position);
#endif
