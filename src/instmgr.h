#ifndef INSTMGR_H_
#define INSTMGR_H_
#include <string>

#include "ThostFtdcTraderApi.h"
#include "ThostFtdcMdApi.h"

#include "log.h"



class inst {
	public:
		CThostFtdcInstrumentField  base;
		int inst_status;
		int is_trading(){
			return base.IsTrading;
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
	public:
	map<string, int   > statusmap;  
	map<string, inst *> instmap;
	int is_trading(string instn){
		if(instmap.find(instn)!=instmap.end()) {
			return instmap[instn]->is_trading() ;
			if(statusmap[instn] ==  THOST_FTDC_IS_Continous &&
			   instmap[instn]->is_trading()
			  ) {
				return 1;
			} else {
				/*todo*/
				LOG_INFO<<"not trading tradestatus: "<<statusmap[instn]<<" is_trading: "<<instmap[instn]->is_trading()<<std::endl;
			}
		}else {
			/*todo*/
			LOG_DEBUG<<"can not find status in instmap :"<<instn<<std::endl;
			return  THOST_FTDC_IS_NoTrading;
		}	
		return 0;
	};
	int update_inst_status(string product, int status) {
		/*
		 * */
		if(statusmap.find(product)==statusmap.end()) {
			LOG_INFO<<"can not find product: "<<product<<std::endl;
		}
		statusmap[product]=status;
		return 0;
	}

	int get_inst_status(string instn) {
		if(statusmap.find(instn)!=statusmap.end()) {
			return statusmap[instn];
		}else {
			LOG_DEBUG<<"can not find status, inst: "<<instn<<std::endl;
			return THOST_FTDC_IS_NoTrading;
		}
	}
	int update_inst(string instn, inst *pinst) {
		/*todo lock
		 * */
		if(instmap.find(instn)==instmap.end()) {
			instmap[instn]=pinst;
		}else {
			free(instmap[instn]);
			instmap[instn]=pinst;
			return 0;
		}	
		if(statusmap.find(pinst->base.ProductID)==statusmap.end()) {
			statusmap[pinst->base.ProductID]=THOST_FTDC_IS_NoTrading;
		}
		return 0;
	}
};


#endif
