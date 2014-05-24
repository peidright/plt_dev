#include "CtpTrader.h"
#include "datalocal.h"
#include "trader.h"
#include <deque>
#include "help.h"

#include "instmgr.h"

CtpTrader::CtpTrader(Trader *trader,dmgr *pdmgr,instmgr *pinstmgr, string localdir):qsem(0)
{
	this->trader=trader;
	this->pdmgr=pdmgr;
	this->running=1;
	this->pinstmgr=pinstmgr;
	this->localdir=localdir;
}

int CtpTrader::init()
{
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(this->localdir.c_str());
	this->trade_api=trade_api;
	CtpTradeSpi* trade_spi = new CtpTradeSpi(trade_api,this);
	this->trade_spi = trade_spi;
	return 0;
}

int CtpTrader::start()
{
	trade_api->RegisterSpi((CThostFtdcTraderSpi*)this->trade_spi);			// 注册事件类
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// 注册公有流
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // 注册私有流
	trade_api->RegisterFront((char*)this->trader->trade_addr.c_str());	// 注册交易前置地址
	trade_api->Init();
    LOG_DEBUG<<"CtpTrader init()"<<std::endl;
	return 0;
}


void CtpTrader::trade_stm(msg_t &msg)
{
	//msg_t *mmsg;
	//inst_t *pinst;
	inst   *ppinst;
	TThostFtdcInstrumentIDType instId;
	int ret;
	char reqid[64];
	char orderid[64];
	TOnRtnOrder_t *OnRtnOrder;
	TOnRtnTrade_t *OnRtnTrade;
	position_t *pposition;
	struct CThostFtdcInvestorPositionField  *pposition_field;
	TOnRspOrderAction_t  *OnRspOrderAction;
	TOnRspOrderInsert_t *OnRspOrderInsert;
	TOnRspQryTradingAccount_t *OnRspQryTradingAccount;



	int orderref;
	int requestid;


	while(msg.type!=TSTOP) {
		switch(msg.type) {
			/*        */
			case TSTART:
				this->start();
				msg.type=TSTOP;
				break;
			case TOnFrontConnected:
				LOG_DEBUG <<"trade connected stm"<<std::endl;
				msg.type=TReqUserLogin;
				break;
			case TOnFrontDisconnected:
				msg.type=TSTOP;
				break;
			case TOnHeartBeatWarning:
				/*todo err process
				 */
				msg.type=TSTOP;
				break;
			case TOnRspError:
				/*todo err process
				 */
				msg.type=TSTOP;
				break;
			case TReqSettlementInfoConfirm:
				/**/
				LOG_DEBUG<<"trade req settle stm"<<std::endl;
				this->trade_spi->ReqSettlementInfoConfirm(this->trader->brokerid.c_str(), 
						this->trader->username.c_str(),0
						);
				msg.type=TSTOP;
				break;
			case TOnRspSettlementInfoConfirm:
				/**/
				if(   !this->trade_spi->IsErrorRspInfo((((TOnRspSettlementInfoConfirm_t*)msg.data)->pRspInfo))) {
					LOG_DEBUG<<"OnRspSettlement investor :"<<((TOnRspSettlementInfoConfirm_t*)msg.data)->pSettlementInfoConfirm.ConfirmDate<<std::endl;
				} else {
					LOG_DEBUG<<"fail Onrsp settlement confirm"<<std::endl;
				}
				msg.type=TReqQryInstrument;
				break;
			case TReqUserLogin:
				/**/
				LOG_DEBUG<<"trade login stm"<<std::endl;
				ret= this->trade_spi->ReqUserLogin((char*)this->trader->brokerid.c_str(),
						(char*)this->trader->username.c_str(),
						(char*)this->trader->password.c_str(),0);
				if(ret==0) {
					//LOG_DEBUG<<"trade_stm login msg sended\n" <<std::endl;
					msg.type=TSTOP;
				}else {
					LOG_DEBUG<<"trade_stm login msg sended fail\n" <<std::endl;
					/*err process					
					 */
				}
				msg.type=TSTOP;
				break;
			case TOnRspUserLogin:
				LOG_DEBUG<<"trade rsplogin stm"<<std::endl;
				msg.type=TReqSettlementInfoConfirm;		
				/*fix*/
				msg.data=NULL;
				break;
			case TReqQryInstrument:
				/*two case, if msg.data==NULL, query all the Instrument
				 *else 
				 * */
				LOG_DEBUG<<"trade qryInstrument stm"<<std::endl;
				memset(&instId,0x0,sizeof(TThostFtdcInstrumentIDType));
				this->trade_spi->ReqQryInstrument(instId,-1);
				msg.type=TSTOP;
				break;
			case TOnRspQryInstrument:
				/*1.update it into dmgr
				 *2.if is last,..
				 * */
				LOG_DEBUG<<"trade rsp_qryInstrument stm"<<std::endl;
				//CThostFtdcInstrumentField pInstrument;
				//TOnRspQryInstrument_t;
				if(!this->trade_spi->IsErrorRspInfo(((( TOnRspQryInstrument_t*)msg.data)->pRspInfo))) {
					//LOG_DEBUG<<"OnRspInstrument inst:"<<(( TOnRspQryInstrument_t*)msg.data)->pInstrument.InstrumentID<<std::endl;

					/*update it into pinstmgr
					 *todo merge pinstmgr to pdmgr
					 * */
					if((( TOnRspQryInstrument_t*)msg.data)->pInstrument.ProductClass==THOST_FTDC_PC_Futures){

						ppinst=new inst();
						ppinst->ignore=1;
						memcpy(&ppinst->base,&(( TOnRspQryInstrument_t*)msg.data)->pInstrument,sizeof( CThostFtdcInstrumentField ));
						this->pinstmgr->update_inst(ppinst->base.InstrumentID, ppinst);

						if((( TOnRspQryInstrument_t*)msg.data)->bIsLast) {
							LOG_DEBUG<<"OnRspInstrument isLast"<<std::endl;
							this->pinstmgr->set_last(1);
						}
					}else {
						LOG_DEBUG<<"Not Futures:"<<(( TOnRspQryInstrument_t*)msg.data)->pInstrument.InstrumentID<<std::endl;
					}
				} else {
					LOG_DEBUG<<"OnRspInstrument err"<<std::endl;
				}

                char reqid[64];
                //char orderid[64];
                //char id_buf[64];
                snprintf(reqid,64,"%d",((TOnRspQryInstrument_t*)msg.data)->nRequestID);
                if( this->reqid2sid.find(reqid)!=this->reqid2sid.end()) {

				    LOG_DEBUG<<"trade rsp_qryInstrument stm requestid:"<<((TOnRspQryInstrument_t*)msg.data)->nRequestID <<std::endl;
                    sframe_put_msg(&msg, this->reqid2sid[reqid]);
                    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryInstrument can not find requestid"<<((TOnRspQryInstrument_t*)msg.data)->nRequestID <<std::endl;
                }
				msg.type=TSTOP;
				break;
			case TOnRtnInstrumentStatus:
				//(TOnRtnInstrumentStatus_t);
				LOG_DEBUG<<"trade rtn_Instrument stm"<<std::endl;
				/*
				   LOG_DEBUG<<"OnRtnInstrumentStatus enter "<<
				   " time: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.EnterTime<<
				   " inst: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentID<<
				   " reason: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.EnterReason<<
				   " status: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentStatus<<std::endl;
				 */
				this->pinstmgr->update_inst_status(((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentID,  
						((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentStatus);
				msg.type=TSTOP;
				break;
			case TReqQryTradingAccount:
				//TReqQryTradingAccount_t
				msg.type=TSTOP;
				break;
			case TOnRspQryTradingAccount:
				/*todo ok?*/
				OnRspQryTradingAccount=(TOnRspQryTradingAccount_t*)msg.data;
				snprintf(reqid,sizeof(reqid),"%d",OnRspQryTradingAccount->nRequestID);
				LOG_DEBUG<<"CurrMargin:"<<((TOnRspQryTradingAccount_t*)msg.data)->pTradingAccount.CurrMargin<<
					" Available:"<<((TOnRspQryTradingAccount_t*)msg.data)->pTradingAccount.Available<<std::endl;
                if( this->reqid2sid.find(reqid)!=this->reqid2sid.end()) {

				    LOG_DEBUG<<"trade rsp_qryTradingAccount stm requestid:"<<((TOnRspQryTradingAccount_t*)msg.data)->nRequestID<<std::endl;
                    sframe_put_msg(&msg, this->reqid2sid[reqid]);
                    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryTradingAccount can not find requestid"<<((TOnRspQryTradingAccount_t*)msg.data)->nRequestID <<std::endl;
                }
				msg.data=NULL;
				msg.type=TSTOP;
				break;
			case TReqQryInvestorPosition:
				msg.type=TSTOP;
				break;
			case TOnRspQryInvestorPosition:
				if(this->position.find(((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.InstrumentID)
						==this->position.end()) {
					pposition=new (position_t);

					if(((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.PosiDirection==THOST_FTDC_PD_Long) {
						pposition_field=&pposition->bbase;
					}else if(((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.PosiDirection==THOST_FTDC_PD_Short){
						pposition_field=&pposition->sbase;
					}else {
						assert(0);
					}
					memcpy(pposition_field, &((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition, 
							sizeof(struct CThostFtdcInvestorPositionField));
					position[((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.InstrumentID]=pposition;
				}else {
					if(((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.PosiDirection==THOST_FTDC_PD_Long) {
						pposition_field=&position[((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.InstrumentID]->bbase;
					}else if(((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.PosiDirection==THOST_FTDC_PD_Short){
						pposition_field=&position[((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.InstrumentID]->sbase;
					}else {
						assert(0);
					}
					memcpy(&pposition_field, &((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition, 
							sizeof(struct CThostFtdcInvestorPositionField));
				}
				LOG_DEBUG<<"Inst position:"<<((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.InstrumentID<<" yp:"<<
					((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.YdPosition<<" p:"<<
					((TOnRspQryInvestorPosition_t*)msg.data)->pInvestorPosition.Position<<std::endl;

				snprintf(reqid,sizeof(reqid),"%d",((TOnRspQryInvestorPosition_t*)msg.data)->nRequestID);
                if( this->reqid2sid.find(reqid)!=this->reqid2sid.end()) {

				    LOG_DEBUG<<"trade rsp_qryInvestorPosition stm requestid:"<<reqid<<std::endl;
                    sframe_put_msg(&msg, this->reqid2sid[reqid]);
                    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryInvestorPosition can not find requestid"<<reqid <<std::endl;
                }
				msg.type=TSTOP;
				break;
			case TReqOrderInsert:
				//CThostFtdcInputOrderField *pInputOrder, 
				msg.type=TSTOP;
				break;
			case TOnRspOrderInsert:
				/*reqid2req map, status
				 * */
				OnRspOrderInsert=(TOnRspOrderInsert_t*)msg.data;
				snprintf(reqid,sizeof(reqid),"%d_%s",OnRspOrderInsert->pInputOrder.RequestID,
						OnRspOrderInsert->pInputOrder.OrderRef);
                if(this->reqid2sid.find(reqid)!=this->reqid2sid.end()){
                    LOG_DEBUG<<"trade rsp_qryOrderInsert stm requestid:"<<reqid <<std::endl;
				    sframe_put_msg(&msg, this->reqid2sid[reqid]);
                    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryOrderInsert can not find requestid"<<reqid <<std::endl;
                }
				msg.type=TSTOP;
				break;
			case TReqOrderAction:
				/*
				 * */
				msg.type=TSTOP;
				break;
			case TOnRspOrderAction:
				/*fix status,todo use req_id, or ordid
				 * */
				OnRspOrderAction=(TOnRspOrderAction_t*)msg.data;;
				snprintf(reqid,sizeof(reqid),"%d_%s",OnRspOrderAction->pInputOrderAction.RequestID,
						OnRspOrderAction->pInputOrderAction.OrderRef);
                if(this->reqid2sid.find(reqid)!=this->reqid2sid.end()){
                    LOG_DEBUG<<"trade rsp_qryOrderInsert stm requestid:"<<reqid <<std::endl;
				    sframe_put_msg(&msg, this->reqid2sid[reqid]);
				    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryOrderInsert can not find requestid"<<reqid <<std::endl;
                }
				msg.type=TSTOP;
				break;
			case TOnRtnOrder:
				//TOnRtnOrder_t;
				OnRtnOrder=(TOnRtnOrder_t*)msg.data;
				orderref=atoi(OnRtnOrder->pOrder.OrderRef);
				requestid=OnRtnOrder->pOrder.RequestID;
				snprintf(reqid,sizeof(reqid),"%d_%d",requestid,orderref);
				snprintf(orderid,sizeof(orderid),"%s_%s",OnRtnOrder->pOrder.ExchangeID, OnRtnOrder->pOrder.OrderSysID);

				if(this->orderid2order.find(orderid)!=this->orderid2order.end()) {
					memcpy(&this->orderid2order[orderid]->base, &OnRtnOrder->pOrder, sizeof(CThostFtdcOrderField));
					this->orderid2order[orderid]->uptime=time(NULL);
				} else {
					this->orderid2order[orderid]=new (order_t);
					memcpy(&this->orderid2order[orderid]->base, &OnRtnOrder->pOrder, sizeof(CThostFtdcOrderField));
					this->orderid2order[orderid]->uptime=time(NULL);
					//assert(0);
				}
				/*todo err check*/
				this->orderid2reqid[orderid]=reqid;
				this->reqid2orderid[reqid]=orderid;
				/*if reqid not existed*/
                if( this->reqid2sid.find(reqid)!=this->reqid2sid.end()) {
                    LOG_DEBUG<<"trade rsp_qryRtnOrder stm  requestid:"<<reqid<<std::endl;
				    sframe_put_msg(&msg, this->reqid2sid[reqid]);
				    msg.data=NULL;
                }else {
                    cout<<"not find reqid:"<<reqid<<std::endl;
                    LOG_DEBUG<<"trade rsp_qryRtnOrder stm requestid"<<reqid<<std::endl;
                }
				msg.type=TSTOP;
				break;
			case TOnRtnTrade:
				//TOnRtnTrade_t;
				//update req
				//update Order
				//update position
				//append Trade to position for recheck
				OnRtnTrade=(TOnRtnTrade_t*)msg.data;
				snprintf(orderid,sizeof(orderid),"%s_%s",OnRtnTrade->pTrade.ExchangeID,OnRtnTrade->pTrade.OrderSysID);
				if(this->orderid2reqid.find(orderid)!=this->orderid2reqid.end()) {
					if(this->reqid2req.find(this->orderid2reqid[orderid])!=this->reqid2req.end()) {
						//this->reqid2req[this->orderid2reqid[orderid]]->base.
					}else {
					}
				}else {
					//todo some check
				}
				if(this->orderid2order.find(orderid)!=this->orderid2order.end()) {
					//this->orderid2order[orderid]->
				}else {
				}
				if(this->position.find(OnRtnTrade->pTrade.InstrumentID)!=this->position.end()){
					/*
					 * todo if existed in vector
					 * */
					//position_t *position;
					//CThostFtdcInvestorPositionField base;
					//OnRtnTrade->pTrade.

				}else {
					this->position[OnRtnTrade->pTrade.InstrumentID]=new (position_t);
				}
                if(this->orderid2sid.find(orderid)!=this->orderid2sid.end()){
                    LOG_DEBUG<<"trade rsp_qryRtnTrade stm  orderid:"<<orderid <<std::endl;
				    sframe_put_msg(&msg, this->orderid2sid[orderid]);
				    msg.data=NULL;
                }else {
                    LOG_DEBUG<<"trade rsp_qryRtnTrade can not find orderid"<<orderid <<std::endl;
                }
				msg.type=TSTOP;
				break;
			default:
				msg.type=TSTOP;
				break;
		}
	}
	msg.type=TSTOP;
	if(msg.type == TSTOP) {
		/*todo free message,bug fix*/
		if(msg.data)
			free(msg.data);
	}
	//LOG_DEBUG<<"finish one Trade data"<<std::endl;
}

void trader_loop(CtpTrader *ctptrader, int key)
{
	int i=0;
    LOG_DEBUG<<"CtpTrader trader_loop working"<<std::endl;
	while(ctptrader->running) {
		i=i+1;
		if(i%100==0) {
			i=0;
			LOG_INFO<<"trader_loop living"<<std::endl;
		}
		ctptrader->qsem.wait();
		boost::unique_lock<boost::timed_mutex> lk(ctptrader->qmutex,boost::chrono::milliseconds(3));
		if (lk) {
			if(ctptrader->mqueue.size()<=0) {
				/*bug happen*/
				LOG_INFO<<"trader_loop should not be zero qqueue"<<std::endl;
				lk.unlock();
				continue;
			}
			msg_t msg=ctptrader->mqueue[0];
			ctptrader->mqueue.pop_front();
			lk.unlock();
			ctptrader->trade_stm(msg);
		} else {
			LOG_INFO<<"trader_loop quote main loop err"<<std::endl;
		}
	}
}

void CtpTrader::post_msg(msg_t *msg)
{
	/*lock
	*/
	
again:
	boost::unique_lock<boost::timed_mutex> lk(this->qmutex,boost::chrono::milliseconds(3));
	if(lk) {
		this->mqueue.push_back(*msg);
		this->qsem.post();
		//?lk.unlock();
	}else {
		/*
		   do some warnning
		*/
        lk.unlock();
		LOG_DEBUG<<"ctptrader post_msg again"<<std::endl;
		goto again;
	}
}
