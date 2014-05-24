//#include <python/Python.h>
#include <boost/python.hpp>
#include "StrategyFrame.h"


using namespace boost::python;
class sframe g_sframe;
static map<string,int> type2valmap;
static map<int,string> val2typemap;


extern int sframe_agent_loop(strategy_config_t &config);
int type2val(string t);
string val2type(int val);


sframe::sframe(){
    this->base_key=1;
};


int sframe::put_msg(msg_t *msg,int key) {
again:
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
		pipemap[key]->msgqueue.push_back(*msg);
		pipemap[key]->qsem.post();
	}else {
        /*todo*/
        LOG_DEBUG<<"lockerr put_msg again"<<std::endl;
        goto again;
	}
    return 0;
};

msg_t sframe::get_msg(int key) {
	msg_t msg;
    memset(&msg,0x0,sizeof(msg_t));
again:
    //while(this->pipemap[key]->msgqueue.size() == 0){usleep(100);};
    pipemap[key]->qsem.wait();
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
        if(pipemap[key]->msgqueue.size()>0){

            //pipemap[key]->qsem.wait();
            msg=pipemap[key]->msgqueue[0];
            pipemap[key]->msgqueue.pop_front();
            LOG_DEBUG<<"sframe get_msg"<<std::endl;
        }else {
            LOG_DEBUG<<"sframe get_msg null, repost? todo"<<std::endl;
            //pipemap[key]->qsem.post();
        }
	}else {
        /*todo*/
        LOG_DEBUG<<"sframe get_msg lockerr"<<std::endl;
        goto again;
	}
	return msg;
};
int sframe::reg_agent_key() {
	int key=0;
again:
	boost::unique_lock<boost::timed_mutex> lk(this->smutex,boost::chrono::milliseconds(1));
	if (lk) {
		key=this->base_key++;
		pipemap[key]=new (msgpipe_t);
	} else {
		/*todo */
		goto again;
	}
	return key;
};
int sframe::dispatch(){
    return 0;
};

int sframe::init(CtpQuoter *ctpquoter, CtpTrader *ctptrader)
{
    this->ctpquoter=ctpquoter;
    this->ctptrader=ctptrader;
    return 0;
};

msg_t sframe::dispatchsynret(msg_t msg)
{
    int ret;
    SRegMdInst_t *pSRegMdInst;
    SRegMdPeriod_t *pSRegMdPeriod;
    SRegMdStrategy_t *pSRegMdStrategy;
    //SRegRspCommon_t  *pSRegRspCommon;

    TReqQryInstrument_t *req_inst=NULL;
    TReqQryTradingAccount_t *req_account=NULL;
    TReqQryInvestorPosition_t *req_position=NULL;
    TReqOrderInsert_t *req_order=NULL;
    TReqOrderAction_t  *req_action=NULL;

    msg_t msg1;
    memset(&msg1,0x0,sizeof(msg_t));
    cout<<"msg.type"<<msg.type<<std::endl;

    switch(msg.type) {
        case SRegMdInst:
            pSRegMdInst=(SRegMdInst_t*)msg.data;
            assert(0);
            break;
        case SRegMdPeriod:
            pSRegMdPeriod=(SRegMdPeriod_t*)msg.data;
            ret=this->ctpquoter->mds->regmd_period(pSRegMdPeriod->instn,(pSRegMdPeriod->period==0?MIRCO:MINUTE),pSRegMdPeriod->period);
            goto retcommon;
            break;
        case SRegMdStrategy:
            pSRegMdStrategy=(SRegMdStrategy_t*)msg.data;
            ret=this->ctpquoter->mds->regmd_strategy(pSRegMdStrategy->instn,pSRegMdStrategy->sid,pSRegMdStrategy->period);
            goto retcommon;
            break;
        case TReqQryInstrument:
            req_inst=(TReqQryInstrument_t*)msg.data;
            ret=this->ctptrader->trade_spi->ReqQryInstrument(req_inst->instn,req_inst->sid);
            goto retcommon;
            break;
        case TReqQryTradingAccount:
            req_account=(TReqQryTradingAccount_t*)msg.data;
            ret=this->ctptrader->trade_spi->ReqQryTradingAccount(req_account->sid);
            goto retcommon;
            break;
        case TReqQryInvestorPosition:
            req_position=(TReqQryInvestorPosition_t*)msg.data;
            ret=this->ctptrader->trade_spi->ReqQryInvestorPosition(req_position->instn, req_position->sid);
            goto retcommon;
            break;
        case TReqOrderInsert:
            req_order=(TReqOrderInsert_t*)msg.data;
            ret=this->ctptrader->trade_spi->ReqOrderInsert(req_order->instn,req_order->dir,req_order->kpp,
					req_order->price,req_order->vol,req_order->sid);
            goto retcommon;
            break;
        case TReqOrderAction:
            req_action=(TReqOrderAction_t*)msg.data;
            ret=this->ctptrader->trade_spi->ReqOrderAction(req_action->exchangeid,req_action->ordersysid,
                                                           req_action->sid);
            goto retcommon;
            break;
        default:
            assert(0);
            break;
    }
    return msg1;
retcommon:
    /*todo free msg?*/
    msg1.type=SRegRspCommon;
    msg1.data=new(SRegRspCommon_t);
    ((SRegRspCommon_t*)msg1.data)->ret=ret;
    return msg1;
}
int sframe::dispatchsyn(msg_t msg){
    int ret=-1;
    SRegMdInst_t *pSRegMdInst;
    SRegMdPeriod_t *pSRegMdPeriod;
    SRegMdStrategy_t *pSRegMdStrategy;
    SRegRspCommon_t  *pSRegRspCommon;

    switch(msg.type) {
        case SRegMdInst:
            pSRegMdInst=(SRegMdInst_t*)msg.data;
            assert(0);
            break;
        case SRegMdPeriod:
            pSRegMdPeriod=(SRegMdPeriod_t*)msg.data;
            ret=this->ctpquoter->mds->regmd_period(pSRegMdPeriod->instn,(pSRegMdPeriod->period==0?MIRCO:MINUTE),pSRegMdPeriod->period);
            break;
        case SRegMdStrategy:
            pSRegMdStrategy=(SRegMdStrategy_t*)msg.data;
            ret=this->ctpquoter->mds->regmd_strategy(pSRegMdStrategy->instn,pSRegMdStrategy->sid,pSRegMdStrategy->period);
            break;
        default:
            assert(0);
            break;
    }
    return ret;
}

int sframe::test(int key){
	msg_t *msg=new(msg_t);
	msg->data=NULL;
	TChange_t *tchange=NULL;
	tchange=new (TChange_t);
	tchange->subtype=TChange;
	tchange->v=1.01;
	msg->type=TChange;
	msg->data=(void*)tchange;

	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if (lk) {
		pipemap[key]->msgqueue.push_back(*msg);
		pipemap[key]->qsem.post();
	} else {
		assert(0);
	}
	return 0;
};

int sframe::run(strategy_config_t &config) {
	cout<<"run sframe"<<std::endl;
	this->stg.add_thread(new boost::thread(sframe_agent_loop,config));
	return 0;
}

int sframe_agent::put_msg(string msg) {
	return 0;
};
string sframe_agent::get_msg() {
	//cout<<"get_msg1"<<std::endl;
	//this->psframe->test(agent_key);
	//cout<<"get_msg2"<<std::endl;
	msg_t msg=this->psframe->get_msg(agent_key);
	//cout<<"get_msg3"<<std::endl;
	return this->msg2pystr(msg);
};

int sframe_agent::init(){
	this->psframe=&g_sframe;
	this->agent_key=this->psframe->reg_agent_key();
    return this->agent_key;
};

msg_t sframe_agent::pystr2msg(string str) {
	/*
	 * */
	Json::Reader reader;
	Json::Value root;

    string instn;
	msg_t msg;
    memset(&msg,0x0,sizeof(msg_t));
	KChange_t *kchange=NULL;
	TChange_t *tchange=NULL;
    TReqQryInstrument_t *req_inst=NULL;
    TReqQryTradingAccount_t *req_account;
    TReqQryInvestorPosition_t *req_position;
    TReqOrderInsert_t *req_order;
    TReqOrderAction_t  *req_action;


    SRegMdStrategy_t *pSRegMdStrategy;
    cout<<"str is:"<<str<<std::endl;
	if (reader.parse(str, root))  
	{
		int type=type2val(root["type"].asString());    
        cout<<"type:"<<root["type"].asString()<<" val:"<<type<<std::endl;
		/*
		   int type = root["type"].asString();  
		   int code = root["code"].asInt();    
		   */
		switch(type) {
            case TReqQryInstrument:
                req_inst=new(TReqQryInstrument_t);
                msg.data=req_inst;
                msg.len=sizeof(TReqQryInstrument_t);
                msg.type=TReqQryInstrument;
                strcpy(req_inst->instn,root["instn"].asString().c_str());
                LOG_DEBUG<<"instn is:"<<req_inst->instn<<std::endl;
                req_inst->sid=root["sid"].asInt();
                break;
            case TReqQryTradingAccount:
                req_account=new(TReqQryTradingAccount_t);
                msg.data=req_account;
                msg.len=sizeof(TReqQryTradingAccount_t);
                msg.type=TReqQryTradingAccount;
                req_account->sid=root["sid"].asInt();
                break;
            case TReqQryInvestorPosition:
                req_position=new(TReqQryInvestorPosition_t);
                msg.data=req_position;
                msg.len=sizeof(TReqQryInvestorPosition_t);
                msg.type=TReqQryInvestorPosition;
                req_position->sid=root["sid"].asInt();
                strcpy(req_position->instn,root["instn"].asString().c_str());
                break;
            case TReqOrderInsert:
                req_order=new(TReqOrderInsert_t);
                msg.data=req_order;
                msg.len=sizeof(TReqOrderInsert_t);
                msg.type=TReqOrderInsert;
                strcpy(req_order->instn,root["instn"].asString().c_str());
                req_order->dir=root["instn"].asInt();
                req_order->price=root["price"].asFloat();
                req_order->vol=root["vol"].asInt();
                req_order->sid=root["sid"].asInt();
                req_order->kpp=root["kpp"].asInt();
                break;
            case TReqOrderAction:
                req_action=new(TReqOrderAction_t);
                req_action->exchangeid=root["exchangeid"].asString();
                req_action->ordersysid=root["ordersysid"].asString();
                req_action->sid=root["sid"].asInt();
                msg.data=req_action;
                msg.len=sizeof(TReqOrderAction_t);
                msg.type=TReqOrderAction;
                break;
            case SRegMdStrategy:
                cout<<"SRegMdStrategy"<<std::endl;
                pSRegMdStrategy=new (SRegMdStrategy_t);
                msg.data=pSRegMdStrategy;
                msg.type=SRegMdStrategy;
                pSRegMdStrategy->instn=root["instn"].asString();
                pSRegMdStrategy->period=root["period"].asInt();
                pSRegMdStrategy->sid=root["sid"].asInt();
                break;
			default:
				break;
		}
        return msg;
	} else {
        /*todo msg free*/
        LOG_DEBUG<<"parse error:"<<str<<std::endl;
	}
	return msg;
};

int sframe_agent::dispatchsyn(string msg){
    /*if complicate result, we must return json*/
    int ret;
    msg_t msg1=this->pystr2msg(msg);
    ret=this->psframe->dispatchsyn(msg1);
    free(msg1.data);
    return ret;
}


string sframe_agent::dispatchsynret(string msg){
    string ret;
    msg_t msg1=this->pystr2msg(msg);
    msg_t msg2=this->psframe->dispatchsynret(msg1);
    free(msg1.data);
    ret=this->msg2pystr(msg2);
    //free(msg2.data);
    return ret;
}


string sframe_agent::msg2pystr(msg_t msg) {

	Json::Reader reader;
	Json::Value root;
	KChange_t *kchange=NULL;
	TChange_t *tchange=NULL;
    SRegRspCommon_t *pSRegRspCommon;
    TOnRspQryInstrument_t *rsp_inst;
    TOnRspQryTradingAccount_t *rsp_account;
    TOnRspQryInvestorPosition_t *rsp_position;
    TOnRspOrderInsert_t *rsp_insert;
    TOnRspOrderAction_t *rsp_action;
    TOnRtnOrder_t *rtn_order;
    TOnRtnTrade_t *rtn_trade;

    LOG_DEBUG<<"msg2pystr ,msg.type is:"<<msg.type<<std::endl;
	string strmsg="";
	/*
	std::string out = root.toStyledString();
	Json::FastWriter writer;
	std::string out2 = writer.write(root);
	*/
    if(msg.type==MSG_NULL){
        if(msg.data)
            free(msg.data);
        return root.toStyledString();
    }

	switch(msg.type) {
		case TChange:
			tchange=(TChange_t*)msg.data;
			root["type"]=val2type(TChange);
			root["subtype"]=tchange->subtype;
			root["v"]=tchange->v;
            LOG_DEBUG<<"root v:"<<root["v"]<<"tchange->v"<<tchange->v<<std::endl;
			strmsg=root.toStyledString();
            LOG_DEBUG<<"TChange"<<std::endl;
			break;
		case KChange:
            LOG_DEBUG<<"KChange"<<std::endl;
			kchange=(KChange_t*)msg.data;
			root["type"]=val2type(KChange);
			root["subtype"]=kchange->subtype;
			root["o"]=kchange->o;
			root["c"]=kchange->c;
			root["h"]=kchange->h;
			root["l"]=kchange->l;
			strmsg=root.toStyledString();
			break; 
        case SRegRspCommon:
            LOG_DEBUG<<"RspCommon"<<std::endl;
            pSRegRspCommon=(SRegRspCommon_t*)msg.data;
            root["ret"]=pSRegRspCommon->ret;
            root["type"]=val2type(msg.type);
        	strmsg=root.toStyledString();
            break;
        case TOnRspQryInstrument:
            LOG_DEBUG<<"msg2pystr RspQryInst"<<std::endl;
            /*todo rspinfo, and string*/
            rsp_inst=(TOnRspQryInstrument_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rsp_inst->nRequestID;
            root["bIsLast"]=rsp_inst->bIsLast;
            root["CreateDate"] = rsp_inst->pInstrument.CreateDate;
            root["DeliveryMonth"]=rsp_inst->pInstrument.DeliveryMonth;
            root["DeliveryYear"]=rsp_inst->pInstrument.DeliveryYear;
            root["EndDelivDate"]=rsp_inst->pInstrument.EndDelivDate;
            root["ExchangeID"]=rsp_inst->pInstrument.ExchangeID;
            root["ExchangeInstID"]=rsp_inst->pInstrument.ExchangeInstID;
            root["ExpireDate"]=rsp_inst->pInstrument.ExpireDate;
            root["InstLifePhase"]=rsp_inst->pInstrument.InstLifePhase;
            root["InstrumentID"]=rsp_inst->pInstrument.InstrumentID;
            root["InstrumentName"]=rsp_inst->pInstrument.InstrumentName;
            root["IsTrading"]=rsp_inst->pInstrument.IsTrading;
            root["LongMarginRatio"]=rsp_inst->pInstrument.LongMarginRatio;
            root["MaxLimitOrderVolume"]=rsp_inst->pInstrument.MaxLimitOrderVolume;
            root["MaxMarginSideAlgorithm"]=rsp_inst->pInstrument.MaxMarginSideAlgorithm;
            root["MaxMarketOrderVolume"]=rsp_inst->pInstrument.MaxMarketOrderVolume;
            root["MinLimitOrderVolume"]=rsp_inst->pInstrument.MinLimitOrderVolume;
            root["MinMarketOrderVolume"]=rsp_inst->pInstrument.MinMarketOrderVolume;
            root["OpenDate"]=rsp_inst->pInstrument.OpenDate;
            root["PositionDateType"]=rsp_inst->pInstrument.PositionDateType;
            root["PositionType"]=rsp_inst->pInstrument.PositionType;
            root["PriceTick"]=rsp_inst->pInstrument.PriceTick;
            root["ProductClass"]=rsp_inst->pInstrument.ProductClass;
            root["ProductID"]=rsp_inst->pInstrument.ProductID;
            root["ShortMarginRatio"]=rsp_inst->pInstrument.ShortMarginRatio;
            root["StartDelivDate"]=rsp_inst->pInstrument.StartDelivDate;
            root["VolumeMultiple"]=rsp_inst->pInstrument.VolumeMultiple;
            strmsg=root.toStyledString();
            break;
        case TOnRspQryTradingAccount:
            LOG_DEBUG<<"RspQryTrad"<<std::endl;
            rsp_account=(TOnRspQryTradingAccount_t*)msg.data;
            root["bIsLast"]=rsp_account->bIsLast;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rsp_account->nRequestID;
            root["AccountID"]=rsp_account->pTradingAccount.AccountID;
            root["Available"]=rsp_account->pTradingAccount.Available;
            root["Balance"]=rsp_account->pTradingAccount.Balance;
            root["BrokerID"]=rsp_account->pTradingAccount.BrokerID;
            root["CashIn"]=rsp_account->pTradingAccount.CashIn;
            root["CloseProfit"]=rsp_account->pTradingAccount.CloseProfit;
            root["Commission"]=rsp_account->pTradingAccount.Commission;
            root["Credit"]=rsp_account->pTradingAccount.Credit;
            root["CurrMargin"]=rsp_account->pTradingAccount.CurrMargin;
            root["DeliveryMargin"]=rsp_account->pTradingAccount.DeliveryMargin;
            root["Deposit"]=rsp_account->pTradingAccount.Deposit;
            root["ExchangeDeliveryMargin"]=rsp_account->pTradingAccount.ExchangeDeliveryMargin;
            root["ExChangeMargin"]=rsp_account->pTradingAccount.ExchangeMargin;
            root["FrozenCash"]=rsp_account->pTradingAccount.FrozenCash;
            root["FrozenCommission"]=rsp_account->pTradingAccount.FrozenCommission;
            root["FrozenMargin"]=rsp_account->pTradingAccount.FrozenMargin;
            root["Interest"]=rsp_account->pTradingAccount.Interest;
            root["InterestBase"]=rsp_account->pTradingAccount.InterestBase;
            root["Mortgage"]=rsp_account->pTradingAccount.Mortgage;
            root["PositionProfit"]=rsp_account->pTradingAccount.PositionProfit;
            root["PreBalance"]=rsp_account->pTradingAccount.PreBalance;
            root["PreCredit"]=rsp_account->pTradingAccount.PreCredit;
            root["PreDeposit"]=rsp_account->pTradingAccount.PreDeposit;
            root["PreMargin"]=rsp_account->pTradingAccount.PreMargin;
            root["PreMortgage"]=rsp_account->pTradingAccount.PreMortgage;
            root["Reserve"]=rsp_account->pTradingAccount.Reserve;
            root["ReserveBalance"]=rsp_account->pTradingAccount.ReserveBalance;
            root["SettlementID"]=rsp_account->pTradingAccount.SettlementID;
            root["TradingDay"]=rsp_account->pTradingAccount.TradingDay;
            root["Withdraw"]=rsp_account->pTradingAccount.Withdraw;
            root["WithDrawQuota"]=rsp_account->pTradingAccount.WithdrawQuota;
            strmsg=root.toStyledString();
            break;
        case TOnRspQryInvestorPosition:
            LOG_DEBUG<<"RspQryInvest"<<std::endl;
            rsp_position=(TOnRspQryInvestorPosition_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rsp_position->nRequestID;
            root["bIsLast"]=rsp_position->bIsLast;
            root["BrokerID"]=rsp_position->pInvestorPosition.BrokerID;
            root["CashIn"]=rsp_position->pInvestorPosition.CashIn;
            root["CloseAmount"]=rsp_position->pInvestorPosition.CloseAmount;
            root["CloseProfit"]=rsp_position->pInvestorPosition.CloseProfit;
            root["CloseProfitByDate"]=rsp_position->pInvestorPosition.CloseProfitByDate;
            root["CloseProfitByTrade"]=rsp_position->pInvestorPosition.CloseProfitByTrade;
            root["CloseVolume"]=rsp_position->pInvestorPosition.CloseVolume;
            root["CombLongFrozen"]=rsp_position->pInvestorPosition.CombLongFrozen;
            root["CombPosition"]=rsp_position->pInvestorPosition.CombPosition;
            root["CombShortFrozen"]=rsp_position->pInvestorPosition.CombShortFrozen;
            root["Commission"]=rsp_position->pInvestorPosition.Commission;
            root["ExchangeMargin"]=rsp_position->pInvestorPosition.ExchangeMargin;
            root["FrozenCash"]=rsp_position->pInvestorPosition.FrozenCash;
            root["FrozenCommission"]=rsp_position->pInvestorPosition.FrozenCommission;
            root["FrozenMargin"]=rsp_position->pInvestorPosition.FrozenMargin;
            root["HedgeFlag"]=rsp_position->pInvestorPosition.HedgeFlag;
            root["InstrumentID"]=rsp_position->pInvestorPosition.InstrumentID;
            root["InvestorID"]=rsp_position->pInvestorPosition.InvestorID;
            root["LongFrozen"]=rsp_position->pInvestorPosition.LongFrozen;
            root["LongFrozenAmount"]=rsp_position->pInvestorPosition.LongFrozenAmount;
            root["MarginRateByMoney"]=rsp_position->pInvestorPosition.MarginRateByMoney;
            root["MarginRateByVolume"]=rsp_position->pInvestorPosition.MarginRateByVolume;
            root["OpenAmount"]=rsp_position->pInvestorPosition.OpenAmount;
            root["OpenCost"]=rsp_position->pInvestorPosition.OpenCost;
            root["OpenVolume"]=rsp_position->pInvestorPosition.OpenVolume;
            root["PosiDirection"]=rsp_position->pInvestorPosition.PosiDirection;
            root["Position"]=rsp_position->pInvestorPosition.Position;
            root["PositionCost"]=rsp_position->pInvestorPosition.PositionCost;
            root["PositionDate"]=rsp_position->pInvestorPosition.PositionDate;
            root["PositionProfit"]=rsp_position->pInvestorPosition.PositionProfit;
            root["PreMargin"]=rsp_position->pInvestorPosition.PreMargin;
            root["PreSettlementPrice"]=rsp_position->pInvestorPosition.PreSettlementPrice;
            root["SettlementID"]=rsp_position->pInvestorPosition.SettlementID;
            root["SettlementPrice"]=rsp_position->pInvestorPosition.SettlementPrice;
            root["ShortFozen"]=rsp_position->pInvestorPosition.ShortFrozen;
            root["ShortFrozenAmount"]=rsp_position->pInvestorPosition.ShortFrozenAmount;
            root["TodayPosition"]=rsp_position->pInvestorPosition.TodayPosition;
            root["TradingDay"]=rsp_position->pInvestorPosition.TradingDay;
            root["UseMargin"]=rsp_position->pInvestorPosition.UseMargin;
            root["YdPosition"]=rsp_position->pInvestorPosition.YdPosition;
            strmsg=root.toStyledString();
            break;
        case TOnRspOrderInsert:
            LOG_DEBUG<<"RspOrderInsert"<<std::endl;
            rsp_insert=(TOnRspOrderInsert_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rsp_insert->nRequestID;
            root["bIsLast"]=rsp_insert->bIsLast;
            root["BrokerID"]=rsp_insert->pInputOrder.BrokerID;
            root["BusinessUnit"]=rsp_insert->pInputOrder.BusinessUnit;
            root["CombHedgeFlag"]=rsp_insert->pInputOrder.CombHedgeFlag;
            root["CombOffsetFlag"]=rsp_insert->pInputOrder.CombOffsetFlag;
            root["ContingentCondition"]=rsp_insert->pInputOrder.ContingentCondition;
            root["Direction"]=rsp_insert->pInputOrder.Direction;
            root["ForceCloseReason"]=rsp_insert->pInputOrder.ForceCloseReason;
            root["GTDDate"]=rsp_insert->pInputOrder.GTDDate;
            root["InstrumentID"]=rsp_insert->pInputOrder.InstrumentID;
            root["InvestorID"]=rsp_insert->pInputOrder.InvestorID;
            root["IsAutoSuspend"]=rsp_insert->pInputOrder.IsAutoSuspend;
            root["IsSwapOrder"]=rsp_insert->pInputOrder.IsSwapOrder;
            root["LimitPrice"]=rsp_insert->pInputOrder.LimitPrice;
            root["MinVolume"]=rsp_insert->pInputOrder.MinVolume;
            root["OrderPriceType"]=rsp_insert->pInputOrder.OrderPriceType;
            root["OrderRef"]=rsp_insert->pInputOrder.OrderRef;
            root["RequestID"]=rsp_insert->pInputOrder.RequestID;
            root["StopPrice"]=rsp_insert->pInputOrder.StopPrice;
            root["TimeCondition"]=rsp_insert->pInputOrder.TimeCondition;
            root["UserForceClose"]=rsp_insert->pInputOrder.UserForceClose;
            root["UserID"]=rsp_insert->pInputOrder.UserID;
            root["VolumeCondition"]=rsp_insert->pInputOrder.VolumeCondition;
            root["VolumeTotalOriginal"]=rsp_insert->pInputOrder.VolumeTotalOriginal;
            strmsg=root.toStyledString();
            break;
        case TOnRspOrderAction:
            LOG_DEBUG<<"RspOrderAction"<<std::endl;
            rsp_action=(TOnRspOrderAction_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rsp_action->nRequestID;
            root["bIsLast"]=rsp_action->bIsLast;
            root["ActionFlag"]=rsp_action->pInputOrderAction.ActionFlag;
            root["BrokerID"]=rsp_action->pInputOrderAction.BrokerID;
            root["ExchangeID"]=rsp_action->pInputOrderAction.ExchangeID;
            root["FrontID"]=rsp_action->pInputOrderAction.FrontID;
            root["InstrumentID"]=rsp_action->pInputOrderAction.InstrumentID;
            root["InvestorID"]=rsp_action->pInputOrderAction.InvestorID;
            root["LimitPrice"]=rsp_action->pInputOrderAction.LimitPrice;
            root["OrderActionRef"]=rsp_action->pInputOrderAction.OrderActionRef;
            root["OrderRef"]=rsp_action->pInputOrderAction.OrderRef;
            root["OrderSysID"]=rsp_action->pInputOrderAction.OrderSysID;
            root["RequestID"]=rsp_action->pInputOrderAction.RequestID;
            root["SessionID"]=rsp_action->pInputOrderAction.SessionID;
            root["UserID"]=rsp_action->pInputOrderAction.UserID;
            root["VolumeChange"]=rsp_action->pInputOrderAction.VolumeChange;
            strmsg=root.toStyledString();
            break;
        case TOnRtnOrder:
            LOG_DEBUG<<"RspRtnOrder"<<std::endl;
            rtn_order=(TOnRtnOrder_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            root["reqid"]=rtn_order->pOrder.RequestID;
            root["ActiveTime"]=rtn_order->pOrder.ActiveTime;
            root["ActiveTraderID"]=rtn_order->pOrder.ActiveTraderID;
            root["ActiveUserID"]=rtn_order->pOrder.ActiveUserID;
            root["BrokerID"]=rtn_order->pOrder.BrokerID;
            root["BrokerOrderSeq"]=rtn_order->pOrder.BrokerOrderSeq;
            root["BusinessUnit"]=rtn_order->pOrder.BusinessUnit;
            root["CancelTime"]=rtn_order->pOrder.CancelTime;
            root["ClearingPartID"]=rtn_order->pOrder.ClearingPartID;
            root["ClientID"]=rtn_order->pOrder.ClientID;
            root["CombHedgeFlag"]=rtn_order->pOrder.CombHedgeFlag;
            root["CombOffsetFlag"]=rtn_order->pOrder.CombOffsetFlag;
            root["ContingentCondition"]=rtn_order->pOrder.ContingentCondition;
            root["Direction"]=rtn_order->pOrder.Direction;
            root["ExchangeID"]=rtn_order->pOrder.ExchangeID;
            root["ExchangeInstID"]=rtn_order->pOrder.ExchangeInstID;
            root["ForceCloseReason"]=rtn_order->pOrder.ForceCloseReason;
            root["FrontID"]=rtn_order->pOrder.FrontID;
            root["GTDDate"]=rtn_order->pOrder.GTDDate;
            root["InsertDate"]=rtn_order->pOrder.InsertDate;
            root["InsertTime"]=rtn_order->pOrder.InsertTime;
            root["InstallID"]=rtn_order->pOrder.InstallID;
            root["InstrumentID"]=rtn_order->pOrder.InstrumentID;
            root["InvestorID"]=rtn_order->pOrder.InvestorID;
            root["IsAutoSuspend"]=rtn_order->pOrder.IsAutoSuspend;
            root["IsSwapOrder"]=rtn_order->pOrder.IsSwapOrder;
            root["LimitPrice"]=rtn_order->pOrder.LimitPrice;
            root["MinVolume"]=rtn_order->pOrder.MinVolume;
            root["NotifySequence"]=rtn_order->pOrder.NotifySequence;
            root["OrderLocalID"]=rtn_order->pOrder.OrderLocalID;
            root["OrderPriceType"]=rtn_order->pOrder.OrderPriceType;
            root["OrderRef"]=rtn_order->pOrder.OrderRef;
            root["OrderSource"]=rtn_order->pOrder.OrderSource;
            root["OrderStatus"]=rtn_order->pOrder.OrderStatus;
            root["OrderSubmitStatus"]=rtn_order->pOrder.OrderSubmitStatus;
            root["OrderSysID"]=rtn_order->pOrder.OrderSysID;
            root["OrderType"]=rtn_order->pOrder.OrderType;
            root["ParticipantID"]=rtn_order->pOrder.ParticipantID;
            root["RelativeOrderSysID"]=rtn_order->pOrder.RelativeOrderSysID;
            root["RequestID"]=rtn_order->pOrder.RequestID;
            root["SequenceNo"]=rtn_order->pOrder.SequenceNo;
            root["SessionID"]=rtn_order->pOrder.SessionID;
            root["SettlementID"]=rtn_order->pOrder.SettlementID;
            root["StatusMsg"]=rtn_order->pOrder.StatusMsg;
            root["StopPrice"]=rtn_order->pOrder.StopPrice;
            root["SuspendTime"]=rtn_order->pOrder.SuspendTime;
            root["TimeCondition"]=rtn_order->pOrder.TimeCondition;
            root["TraderID"]=rtn_order->pOrder.TraderID;
            root["TradingDay"]=rtn_order->pOrder.TradingDay;
            root["UpdateTime"]=rtn_order->pOrder.UpdateTime;
            root["UserForceClose"]=rtn_order->pOrder.UserForceClose;
            root["UserID"]=rtn_order->pOrder.UserID;
            root["UserProductInfo"]=rtn_order->pOrder.UserProductInfo;
            root["VolumeCondition"]=rtn_order->pOrder.VolumeCondition;
            root["VolumeTotal"]=rtn_order->pOrder.VolumeTotal;
            root["VolumeTotalOriginal"]=rtn_order->pOrder.VolumeTotalOriginal;
            root["VolumeTraded"]=rtn_order->pOrder.VolumeTraded;
            root["ZCETotalTradedVolume"]=rtn_order->pOrder.ZCETotalTradedVolume;
            strmsg=root.toStyledString();
            break;
        case TOnRtnTrade:
            LOG_DEBUG<<"RspRtnTrade"<<std::endl;
            rtn_trade=(TOnRtnTrade_t*)msg.data;
            root["type"]=val2type(msg.type);
            root["subtype"]=0;
            //root["reqid"]=0;
            root["BrokerID"]=rtn_trade->pTrade.BrokerID;
            root["BrokerOrderSeq"]=rtn_trade->pTrade.BrokerOrderSeq;
            root["BusinessUnit"]=rtn_trade->pTrade.BusinessUnit;
            root["ClearingPartID"]=rtn_trade->pTrade.ClearingPartID;
            root["ClientID"]=rtn_trade->pTrade.ClientID;
            root["Direction"]=rtn_trade->pTrade.Direction;
            root["ExchangeID"]=rtn_trade->pTrade.ExchangeID;
            root["ExchangeInstID"]=rtn_trade->pTrade.ExchangeInstID;
            root["HedgeFlag"]=rtn_trade->pTrade.HedgeFlag;
            root["InstrumentID"]=rtn_trade->pTrade.InstrumentID;
            root["InvestorID"]=rtn_trade->pTrade.InvestorID;
            root["OffsetFlag"]=rtn_trade->pTrade.OffsetFlag;
            root["OrderLocalID"]=rtn_trade->pTrade.OrderLocalID;
            root["OrderRef"]=rtn_trade->pTrade.OrderRef;
            root["OrderSysID"]=rtn_trade->pTrade.OrderSysID;
            root["ParticipantID"]=rtn_trade->pTrade.ParticipantID;
            root["Price"]=rtn_trade->pTrade.Price;
            root["PriceSource"]=rtn_trade->pTrade.PriceSource;
            root["SequenceNo"]=rtn_trade->pTrade.SequenceNo;
            root["SettlementID"]=rtn_trade->pTrade.SettlementID;
            root["TradeDate"]=rtn_trade->pTrade.TradeDate;
            root["TradeID"]=rtn_trade->pTrade.TradeID;
            root["TradeSource"]=rtn_trade->pTrade.TradeSource;
            root["TradeTime"]=rtn_trade->pTrade.TradeTime;
            root["TradeType"]=rtn_trade->pTrade.TradeType;
            root["TraderID"]=rtn_trade->pTrade.TraderID;
            root["TradingDay"]=rtn_trade->pTrade.TradingDay;
            root["TradingRole"]=rtn_trade->pTrade.TradingRole;
            root["UserID"]=rtn_trade->pTrade.UserID;
            root["Volume"]=rtn_trade->pTrade.Volume;
            strmsg=root.toStyledString();
            break;
		default:
			/*todo*/
            LOG_DEBUG<<"default"<<std::endl;
			break;
	}
    if(msg.data){
        LOG_DEBUG<<"free msg.data,point:"<<msg.data<<std::endl;
        free(msg.data);
        msg.data=NULL;
    }
    LOG_DEBUG<<"strmsg is :"<<strmsg<<std::endl;
	return strmsg;
};

BOOST_PYTHON_MODULE(sframe_agent)
{
	class_<sframe_agent>("sframe_agent")
		.def("get_msg", &sframe_agent::get_msg)
		.def("put_msg", &sframe_agent::put_msg)
		.def("init",    &sframe_agent::init)
        .def("dispatchsyn",&sframe_agent::dispatchsyn)
        .def("dispatchsynret",&sframe_agent::dispatchsynret)
	;
};


int sframe_agent_loop(strategy_config_t &config) {
	cout<<"sframe_agent loop"<<std::endl;
	//PyObject *pName,*pModule,*pDict,*pFunc,*pArgs;
	Py_Initialize();
	if (!Py_IsInitialized()){
		return -1;
	}
	PyRun_SimpleString("import sys");
	initsframe_agent();
	PyRun_SimpleString("import sframe_agent");
	PyRun_SimpleString("sys.path.append('./')");
	//pName = PyString_FromString("test");
	//pModule = PyImport_Import(pName);
	PyObject *pyfile = PyFile_FromString((char*)config.scrip_name.c_str(),"r"); 
	FILE *f = PyFile_AsFile(pyfile); 
	PyRun_AnyFileEx(f,config.scrip_name.c_str(),0);
    return 0;
}

int sframe_put_msg(msg_t *msg, int key)
{
    int ret=g_sframe.put_msg(msg, key);
    return ret;
}

int sframe_quote_kchange(float o,float c, float h, float l, int sec,int msec,int subtype, int key)
{
    int ret;
    msg_t *msg=new(msg_t);
    msg->data=new (KChange_t);
    msg->type=KChange;
    ((KChange_t*)msg->data)->o=o;
    ((KChange_t*)msg->data)->c=c;
    ((KChange_t*)msg->data)->h=h;
    ((KChange_t*)msg->data)->l=l;
    subtype=(subtype==0?OLD:NEW);
    ((KChange_t*)msg->data)->subtype=subtype;
    ret=sframe_put_msg(msg,key);
    return ret;
}

int sframe_quote_tchange(float v, int sec, int msec,int subtype, int key)
{
    LOG_DEBUG<<"sframe quote tchange"<<std::endl;
    int ret;
    msg_t *msg=new(msg_t);
    msg->type=TChange;
    msg->data=new (TChange_t);
    ((TChange_t*)msg->data)->subtype=NEW;
    ((TChange_t*)msg->data)->v=v;
    LOG_DEBUG<<"sframe_quote_tchange: v="<<((TChange_t*)msg->data)->v<<std::endl;
    ret=sframe_put_msg(msg, key);
    return ret;
}


void typeval_init()
{
    type2valmap["MSG_NULL"]=0;
    val2typemap[0]="MSG_NULL";

    type2valmap["TChange"]=6;
    val2typemap[6]="TChange";

    type2valmap["KChange"]=7;
    val2typemap[7]="KChange";

    type2valmap["TMessage"]=8;
    val2typemap[8]="TMessage";

    type2valmap["TSTOP"]=9;
    val2typemap[9]="TSTOP";

    type2valmap["TSTART"]=10;
    val2typemap[10]="TSTART";

    type2valmap["TOnFrontConnected"]=11;
    val2typemap[11]="TOnFrontConnected";

    type2valmap["TReqUserLogin"]=12;
    val2typemap[12]="TReqUserLogin";
    type2valmap["TOnRspUserLogin"]=13;
    val2typemap[13]="TOnRspUserLogin";
    type2valmap["TReqSettlementInfoConfirm"]=14;
    val2typemap[14]="TReqSettlementInfoConfirm";
    type2valmap["TOnRspSettlementInfoConfirm"]=15;
    val2typemap[15]="TOnRspSettlementInfoConfirm";
    type2valmap["TReqQryInstrument"]=16;
    val2typemap[16]="TReqQryInstrument";
    type2valmap["TOnRspQryInstrument"]=17;
    val2typemap[17]="TOnRspQryInstrument";
    type2valmap["TReqQryTradingAccount"]=18;
    val2typemap[18]="TReqQryTradingAccount";
    type2valmap["TOnRspQryTradingAccount"]=19;
    val2typemap[19]="TOnRspQryTradingAccount";
    type2valmap["TReqQryInvestorPosition"]=20;
    val2typemap[20]="TReqQryInvestorPosition";
    type2valmap["TOnRspQryInvestorPosition"]=21;
    val2typemap[21]="TOnRspQryInvestorPosition";
    type2valmap["TReqOrderInsert"]=22;
    val2typemap[22]="TReqOrderInsert";
    type2valmap["TOnRspOrderInsert"]=23;
    val2typemap[23]="TOnRspOrderInsert";
    type2valmap["TReqOrderAction"]=24;
    val2typemap[24]="TReqOrderAction";
    type2valmap["TOnRspOrderAction"]=25;
    val2typemap[25]="TOnRspOrderAction";;
    type2valmap["TOnRtnInstrumentStatus"]=26;
    val2typemap[26]="TOnRtnInstrumentStatus";;
    type2valmap["TOnRtnOrder"]=27;
    val2typemap[27]="TOnRtnOrder";

    type2valmap["TOnRtnTrade"]=28;
    val2typemap[28]="TOnRtnTrade";

    type2valmap["TOnFrontDisconnected"]=29;
    val2typemap[29]="TOnFrontDisconnected";;
    type2valmap["TOnHeartBeatWarning"]=30;
    val2typemap[30]="TOnHeartBeatWarning";
    type2valmap["TOnRspError"]=31;
    val2typemap[31]="TOnRspError";
    type2valmap["TRADE_QUOTE"]=64;
    val2typemap[64]="TRADE_QUOTE";
    type2valmap["QSTOP"]=65;
    val2typemap[65]="QSTOP";
    type2valmap["QSTART"]=66;
    val2typemap[66]="QSTART";
    type2valmap["OnFrontConnected"]=67;
    val2typemap[67]="OnFrontConnected";

    type2valmap["QOnFrontDisconnected"]=68;
    val2typemap[68]="QOnFrontDisconnected";
    type2valmap["QOnHeartBeatWarning"]=69;
    val2typemap[69]="QOnHeartBeatWarning";
    type2valmap["QOnRspError"]=70;
    val2typemap[70]="QOnRspError";
    type2valmap["QReqSubScribeMarketData"]=71;
    val2typemap[71]="QReqSubScribeMarketData";
    type2valmap["QOnRspSubMarketData"]=72;
    val2typemap[72]="QOnRspSubMarketData";
    type2valmap["QOnRspUnSubMarketData"]=73;
    val2typemap[73]="QOnRspUnSubMarketData";
    type2valmap["QReqUserLogin"]=74;
    val2typemap[74]="QReqUserLogin";
    type2valmap["QOnRspUserLogin"]=75;
    val2typemap[75]="QOnRspUserLogin";
    type2valmap["QOnRspUserLogout"]=76;
    val2typemap[76]="QOnRspUserLogout";
    type2valmap["QOnRtnDepthMarketData"]=77;
    val2typemap[77]="QOnRtnDepthMarketData";
    type2valmap["TRADE_STRATEGY"]=128;
    val2typemap[128]="TRADE_STRATEGY";
    type2valmap["SRegMdInst"]=129;
    val2typemap[129]="SRegMdInst";
    type2valmap["SRegMdPeriod"]=130;
    val2typemap[130]="SRegMdPeriod";
    type2valmap["SRegMdStrategy"]=131;
    val2typemap[131]="SRegMdStratgy";
    type2valmap["SRegRspCommon"]=196;
    val2typemap[196]="SRegRspCommon";
}

int type2val(string t)
{
    if(type2valmap.find(t)!=type2valmap.end()){
        return type2valmap[t];
    }else {
        return -1;
    }
}
string val2type(int val)
{
    if(val2typemap.find(val)!=val2typemap.end()) {
        return val2typemap[val];
    }else {
        return "error";
    }
}
