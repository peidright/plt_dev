#include "instmgr.h"

inst::inst(){
    /*-1 old, 1,new 0 all*/
    ignore=-1;
}
void inst::copy(inst *pinst) {
    this->inst_status=pinst->inst_status;
    this->ignore=pinst->ignore;
    memcpy(&this->base,&pinst->base,sizeof(CThostFtdcInstrumentField));
}
int inst::is_trading(){
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

instmgr::instmgr(dmgr *pdmgr) {
    this->pdmgr=pdmgr;
    this->need_inst["IF1406"]="IF1406";
    //this->need_inst["cu1407"]="cu1407";
    this->need_inst["ag1412"]="ag1412";
    last=0;
}


int instmgr::create_inst_kdata(string instn, int period) {
    char sqlbuf[1024];
    sprintf(sqlbuf, "create table kdata_%d_%s(open float, close float, high float, low float, vol int,mnum int,sec int,msec int)",period,instn.c_str());

    //sprintf(sqlbuf,"create table sdata_inst(InstrumentID char(32),ExchangeID char(32),InstrumentName char(32),ExchangeInstID char(32),ProductID char(32),ProductClass char(1),DeliveryYear int,DeliveryMonth int,MaxMarketOrderVolume int,MinMarketOrderVolume int,MaxLimitOrderVolume int,MinLimitOrderVolume int,VolumeMultiple int,PriceTick float,CreateDate char(32),OpenDate char(32),ExpirDate char(32),StartDelivDate char(32),EndDelivDate char(32),InstLifePhase char(1),IsTrading int,PositionType char(1) ,PositionDateType char(1),LongMarginRatio float,ShortMarginRatio float,MaxMarginSideAlgorithm char(1))");[2014-04-25 15:01:24.961142 0x00007f6dec97b700 debug ] [ file:datalocal.cpp ][ line:323 ]sqlstr :create table kdata_1_SP jm1405&jm1409(open float, close float, high float, low float, vol int,sec int,msec int); exe err: near "jm1405": syntax error
    this->pdmgr->db_map["kdata"]->exe_cmd(sqlbuf);
    return 0;
}
int instmgr::create_inst_sdata() {
    char sqlbuf[1024];
    sprintf(sqlbuf,"create table sdata_inst(InstrumentID char(32),ExchangeID char(32),InstrumentName char(32),ExchangeInstID char(32),ProductID char(32),ProductClass char(1),DeliveryYear int,DeliveryMonth int,MaxMarketOrderVolume int,MinMarketOrderVolume int,MaxLimitOrderVolume int,MinLimitOrderVolume int,VolumeMultiple int,PriceTick float,CreateDate char(32),OpenDate char(32),ExpirDate char(32),StartDelivDate char(32),EndDelivDate char(32),InstLifePhase char(1),IsTrading int,PositionType char(1) ,PositionDateType char(1),LongMarginRatio float,ShortMarginRatio float,MaxMarginSideAlgorithm char(1))");
    this->pdmgr->db_map["sdata"]->exe_cmd(sqlbuf);
    return 0;
}
int instmgr::create_inst_tdata(string instn) {
    /*todo err process
     * */
    char sqlbuf[256];
    sprintf(sqlbuf,"create table tdata_%s(open real,close real,high real,low real,uprice real,lprice real,bid1 real,bid2 real,bid3 real, bid4 real, bid5 real,ask1 real,ask2 real,ask3 real,ask4 real,ask5 real,lastprice real,sec integer,msec integer,vol integer)",instn.c_str());
    this->pdmgr->db_map["tdata"]->exe_cmd(sqlbuf);
    return 0;
}
int instmgr::insert_inst(inst *pinst) {
    /*todo may duplicate insert
     * */
    char sqlbuf[2048];
    sprintf(sqlbuf,"insert into sdata_inst values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%d\',\'%f\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%d\',\'%d\', \'%d\',\'%d\', \'%f\',\'%f\',\'%d\')",pinst->base.InstrumentID,pinst->base.ExchangeID,pinst->base.InstrumentName,pinst->base.ExchangeInstID,pinst->base.ProductID,pinst->base.ProductClass,pinst->base.DeliveryYear,pinst->base.DeliveryMonth,pinst->base.MaxMarketOrderVolume,pinst->base.MinMarketOrderVolume,pinst->base.MaxLimitOrderVolume,pinst->base.MinLimitOrderVolume,pinst->base.VolumeMultiple,pinst->base.PriceTick,pinst->base.CreateDate,pinst->base.OpenDate,pinst->base.ExpireDate,pinst->base.StartDelivDate,pinst->base.EndDelivDate,pinst->base.InstLifePhase,pinst->base.IsTrading,pinst->base.PositionType,pinst->base.PositionDateType,pinst->base.LongMarginRatio,pinst->base.ShortMarginRatio,pinst->base.MaxMarginSideAlgorithm);
    this->pdmgr->db_map["sdata"]->exe_cmd(sqlbuf);
    return 0;
}
int instmgr::load_inst() {
    /*todo may be we should use a old_instmap*/
    int ret=0;
    vector<map<string,string> > rows;
    this->pdmgr->db_map["sdata"]->exe_cmd("select * from sdata_inst", rows);
    assert(ret==0);
    inst *pinst;
    LOG_DEBUG<< "instmgr load_inst total: "<<instmap.size()<<std::endl;
    for (vector<map<string,string> >::iterator it=rows.begin();it!=rows.end();it++) {
        pinst=new(inst);
        if(instmap.find((*it)["InstrumentID"]) !=instmap.end()) {
            /*todo fix some error
             * */
            LOG_DEBUG<<"find duplicate inst: "<<(*it)["InstrumentID"]<<std::endl;
        }

        instmap[(*it)["InstrumentID"]]=pinst;
        sprintf(pinst->base.InstrumentID,(*it)["InstrumentID"].c_str());
        sprintf(pinst->base.ExchangeID,(*it)["ExchangeID"].c_str());
        sprintf(pinst->base.InstrumentName,(*it)["InstrumentName"].c_str());
        sprintf(pinst->base.ExchangeInstID,(*it)["ExchangeInstID"].c_str());
        sprintf(pinst->base.ProductID,(*it)["ProductID"].c_str());
        pinst->base.IsTrading=atoi((*it)["IsTrading"].c_str());
        pinst->base.LongMarginRatio=atof((*it)["LongMarginRatio"].c_str());
        pinst->base.ShortMarginRatio=atof((*it)["ShortMarginRatio"].c_str());

        /*to do there has a bug*/
        pinst->base.ProductClass=atoi((*it)["ProductClass"].c_str());
        pinst->base.InstLifePhase=atoi((*it)["InstLifePhase"].c_str());
        pinst->base.PositionType=atoi((*it)["PositionType"].c_str());
        pinst->base.PositionDateType=atoi((*it)["PositionDateType"].c_str());
        pinst->base.MaxMarginSideAlgorithm=atoi((*it)["MaxMarginSideAlgorithm"].c_str());

        pinst->base.DeliveryYear=atoi((*it)["DeliveryYear"].c_str());
        pinst->base.DeliveryMonth=atoi((*it)["DeliveryMonth"].c_str());
        pinst->base.MaxMarketOrderVolume=atoi((*it)["MaxMarketOrderVolume"].c_str());
        pinst->base.MinMarketOrderVolume=atoi((*it)["MinMarketOrderVolume"].c_str());
        pinst->base.MaxLimitOrderVolume=atoi((*it)["MinLimitOrderVolume"].c_str());
        pinst->base.VolumeMultiple=atoi((*it)["VolumeMultiple"].c_str());
        pinst->base.PriceTick=atof((*it)["PriceTick"].c_str());

        sprintf(pinst->base.CreateDate,(*it)["CreateDate"].c_str());
        sprintf(pinst->base.OpenDate,(*it)["OpenDate"].c_str());
        sprintf(pinst->base.ExpireDate,(*it)["ExpireDate"].c_str());
        sprintf(pinst->base.StartDelivDate,(*it)["StarDelivDate"].c_str());
        sprintf(pinst->base.EndDelivDate,(*it)["EndDelivDate"].c_str());

        /*set status
         * */
        statusmap[pinst->base.ProductID]=THOST_FTDC_IS_NoTrading;
    }
    LOG_DEBUG<< "instmgr load_inst total: "<<instmap.size()<<std::endl;
    return 0;
}

int instmgr::get_inst_list(char ***pppinst, int *count, int ignore) {
    int i=0;
    int c=this->instmap.size();
    (*pppinst)= (char**)new char *[c];
    for(map<string ,  inst *>::iterator it=this->instmap.begin();it!=this->instmap.end();it++) {
        /**/
        if((this->need_inst.size()!=0 && this->need_inst.find(it->first)==this->need_inst.end())
                ||(this->filter_inst.size()!=0 && this->filter_inst.find(it->first)!=this->filter_inst.end())			
          ) {
            continue;
        }

        if(it->second->ignore==ignore) {
            continue;
        }

        (*pppinst)[i]= new char [(it->first.size()+1)];
        strcpy((*pppinst)[i], it->first.c_str());
        i=i+1;
    }
    (*count)=i;
    return 0;
}

int instmgr::is_trading(string instn){
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
int instmgr::update_inst_status(string product, int status) {
    /*
     * */
    if(statusmap.find(product)==statusmap.end()) {
        LOG_INFO<<"can not find product: "<<product<<std::endl;
        statusmap[product]=status;
    } else {
        if(statusmap[product]==THOST_FTDC_IS_Continous &&
                status==THOST_FTDC_IS_NoTrading) {
            /*close*/
        } else if(statusmap[product]==THOST_FTDC_IS_NoTrading &&
                status==THOST_FTDC_IS_Continous) {
            /*open*/
        }
        statusmap[product]=status;
    }
    return 0;
}

int instmgr::get_inst_status(string instn) {
    if(statusmap.find(instn)!=statusmap.end()) {
        return statusmap[instn];
    }else {
        LOG_DEBUG<<"can not find status, inst: "<<instn<<std::endl;
        return THOST_FTDC_IS_NoTrading;
    }
}

int instmgr::is_last() {
    return this->last;
}
int instmgr::set_last(int last) {
    this->last=last;
}

int instmgr::update_inst(string instn, inst *pinst) {
    /*todo lock
     * */
    if(pinst->base.ProductClass!= THOST_FTDC_PC_Futures) {
        /*
#define THOST_FTDC_PC_Futures '1'
#define THOST_FTDC_PC_Options '2'
#define THOST_FTDC_PC_Combination '3'
#define THOST_FTDC_PC_Spot '4'
#define THOST_FTDC_PC_EFP '5'
        */
        LOG_DEBUG<<"not Futures :"<<instn<<std::endl;
        return 0;
    }

    if(instmap.find(instn)==instmap.end()) {
        instmap[instn]=pinst;
        /*syn it into db
         * */
        this->insert_inst(pinst);
        this->create_inst_tdata(instn);
        this->create_inst_kdata(instn, 1);
    }else {
        /*todo need refreash?, read==write？check, copy?
          free(instmap[instn]);
          instmap[instn]=pinst;
          */
        instmap[instn]->copy(pinst);
        return 0;
    }	
    if(statusmap.find(pinst->base.ProductID)==statusmap.end()) {
        LOG_INFO<<"can not find product: "<<instn<<std::endl;
        statusmap[pinst->base.ProductID]=THOST_FTDC_IS_NoTrading;
    }
    return 0;
}
