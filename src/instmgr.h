#ifndef INSTMGR_H_
#define INSTMGR_H_
#include <string>
#include "ThostFtdcTraderApi.h"
#include "ThostFtdcMdApi.h"



class inst {
	public:
		CThostFtdcInstrumentField  base;
		int inst_status;
		int is_trading(){
			switch(inst_status){
				case THOST_FTDC_IS_BeforeTrading:
					break;
				case THOST_FTDC_IS_NoTrading:
					break;
				case THOST_FTDC_IS_Continous:
					return 1;
					break;
				case THOST_FTDC_IS_AuctionOrdering:
					break;
				case THOST_FTDC_IS_AuctionBalance:
					break;
				case THOST_FTDC_IS_AuctionMatch:
					break;
				case THOST_FTDC_IS_Closed:
					break;
			}
			return 0;
		};
/*
THOST_FTDC_IS_BeforeTrading '0'
THOST_FTDC_IS_NoTrading '1'
THOST_FTDC_IS_Continous '2'
THOST_FTDC_IS_AuctionOrdering '3'
THOST_FTDC_IS_AuctionBalance '4'
THOST_FTDC_IS_AuctionMatch '5'
THOST_FTDC_IS_Closed '6'
*/
};
class instmgr {
	map<string instn, inst *pinst> instmap;
};



#endif
