#include "StrategyFrame.h"
#include "Python.h"

class sframe g_sframe;

extern int sframe_agent_loop(strategy_config_t &config);



int sframe::put_msg(msg_t *msg,int key) {
again:
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
        LOG_DEBUG<<"real sframe put_msg"<<((TChange_t*)msg->data)->v<<std::endl;
		pipemap[key]->msgqueue.push_back(*msg);
		pipemap[key]->qsem.post();
	}else {
        /*todo*/
        LOG_DEBUG<<"lockerr put_msg again"<<std::endl;
        goto again;
	}
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
    SRegRspCommon_t  *pSRegRspCommon;

    TReqQryInstrument_t *req_inst=NULL;
    TReqQryTradingAccount_t *req_account=NULL;
    TReqQryInvestorPosition_t *req_position=NULL;
    TReqOrderInsert_t *req_order=NULL;
    TReqOrderAction_t  *req_action=NULL;

    msg_t msg1;
    memset(&msg1,0x0,sizeof(msg_t));

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
    int sid;
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
		int type=root["type"].asInt();    
		/*
		   int type = root["type"].asString();  
		   int code = root["code"].asInt();    
		   */
		switch(type) {
			case TChange:
				tchange=new (TChange_t);
				msg.data=tchange;
				msg.len=sizeof(TChange_t);
				msg.type=TChange;
				tchange->subtype=root["subtype"].asInt();
				tchange->v=root["v"].asFloat();
				break;
			case KChange:
				kchange=new (KChange_t);
				msg.data=kchange;
				msg.len=sizeof(KChange_t);
				msg.type=KChange;
				kchange->subtype=root["subtype"].asInt();
				kchange->o=root["o"].asFloat();
				kchange->c=root["c"].asFloat();
				kchange->h=root["h"].asFloat();
				kchange->l=root["l"].asFloat();
				break; 
            case TReqQryInstrument:
                req_inst=new(TReqQryInstrument_t);
                msg.data=req_inst;
                msg.len=sizeof(TReqQryInstrument_t);
                msg.type=TReqQryInstrument;
                strcpy(req_inst->instn,root["instn"].asString().c_str());
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
                msg.data=new(TReqQryInvestorPosition_t);
                msg.len=sizeof(TReqQryInvestorPosition_t);
                msg.type=TReqQryInvestorPosition;
                req_position->sid=root["sid"].asInt();
                strcpy(req_inst->instn,root["instn"].asString().c_str());
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
                break;
            case TReqOrderAction:
                req_action=new(TReqOrderAction_t);
                req_action->exchangeid=root["exchangeid"].asString();
                req_action->ordersysid=root["ordersysid"].asString();
                req_action->sid=root["sid"].asInt();
                msg.data=req_order;
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
    free(msg2.data);
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

	string strmsg="";
	/*
	std::string out = root.toStyledString();
	Json::FastWriter writer;
	std::string out2 = writer.write(root);
	*/
    if(msg.type==MSG_NULL)
        return root.toStyledString();

	switch(msg.type) {
		case TChange:
			tchange=(TChange_t*)msg.data;
			root["type"]=TChange;
			root["subtype"]=tchange->subtype;
			root["v"]=tchange->v;
            LOG_DEBUG<<"root v:"<<root["v"]<<"tchange->v"<<tchange->v<<std::endl;
			strmsg=root.toStyledString();
			break;
		case KChange:
			kchange=(KChange_t*)msg.data;
			root["type"]=KChange;
			root["subtype"]=kchange->subtype;
			root["o"]=kchange->o;
			root["c"]=kchange->c;
			root["h"]=kchange->h;
			root["l"]=kchange->l;
			strmsg=root.toStyledString();
			break; 
        case SRegRspCommon:
            pSRegRspCommon=(SRegRspCommon_t*)msg.data;
            root["ret"]=pSRegRspCommon->ret;
            root["type"]=msg.type;
        	strmsg=root.toStyledString();
            break;
        case TOnRspQryInstrument:
            /*todo rspinfo, and string*/
            rsp_inst=(TOnRspQryInstrument_t*)msg.data;
            root["type"]=msg.type;
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
            rsp_account=(TOnRspQryTradingAccount_t*)msg.data;
            root["bIsLast"]=rsp_account->bIsLast;
            root["type"]=msg.type;
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
            rsp_position=(TOnRspQryInvestorPosition_t*)msg.data;
            root["type"]=msg.type;
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
            rsp_insert=(TOnRspOrderInsert_t*)msg.data;
            root["type"]=msg.type;
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
            rsp_action=(TOnRspOrderAction_t*)msg.data;
            root["type"]=msg.type;
            root["subtype"]=0;
            root["reqid"]=rsp_insert->nRequestID;
            root["bIsLast"]=rsp_insert->bIsLast;
            
            break;
        case TOnRtnOrder:
            break;
        case TOnRtnTrade:
            break;
		default:
			/*todo*/
			break;
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
		cout<<"-1...."<<std::endl;
		return -1;
	}
	PyRun_SimpleString("import sys");
	initsframe_agent();
	cout<<"step2...."<<std::endl;

	PyRun_SimpleString("import sframe_agent");
	PyRun_SimpleString("sys.path.append('./')");
	PyRun_SimpleString("print 'aaa'");
	//PyRun_SimpleString("import test");
	//pName = PyString_FromString("test");
	//pModule = PyImport_Import(pName);
	PyObject *pyfile = PyFile_FromString((char*)config.scrip_name.c_str(),"r"); 
	FILE *f = PyFile_AsFile(pyfile); 
	PyRun_AnyFileEx(f,"test.py",0);
	cout<<"step3...."<<std::endl;
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



