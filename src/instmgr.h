#ifndef INSTMGR_H_
#define INSTMGR_H_
#include <string>
#include "datalocal.h"

#include "ThostFtdcTraderApi.h"
#include "ThostFtdcMdApi.h"

#include "log.h"



class inst {
	public:
		CThostFtdcInstrumentField  base;
		int inst_status;

		/*ignore,running status*/
		inst();
		void copy(inst *pinst);
		int ignore;
		int is_trading();
};
class instmgr {
	public:
	map<string, int   > statusmap;  
	map<string, inst *> instmap;
	map<string,string> filter_inst;
	map<string,string> need_inst;

	dmgr *pdmgr;
	int last;
	instmgr(dmgr *pdmgr);
	int create_inst_kdata(string instn,int period);
	int create_inst_sdata();
	int create_inst_tdata(string instn);
	int insert_inst(inst *pinst);
	int load_inst();
	int get_inst_list(char ***pppinst, int *count, int ignore);
	int is_trading(string instn);
	int update_inst_status(string product, int status);
	int get_inst_status(string instn);
	int is_last();
	int set_last(int last);
	int update_inst(string instn, inst *pinst);
};


#endif
