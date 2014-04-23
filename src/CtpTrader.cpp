#include "CtpTrader.h"
#include "datalocal.h"
#include "trader.h"
#include <deque>
#include "help.h"

#include "instmgr.h";

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
	cout<<"begin api"<<endl;

	return 0;
}

int CtpTrader::start()
{
	trade_api->RegisterSpi((CThostFtdcTraderSpi*)this->trade_spi);			// 注册事件类
	trade_api->SubscribePublicTopic(THOST_TERT_RESTART);					// 注册公有流
	trade_api->SubscribePrivateTopic(THOST_TERT_RESTART);			  // 注册私有流
	trade_api->RegisterFront((char*)this->trader->trade_addr.c_str());	// 注册交易前置地址
	trade_api->Init();
	cout<<"start trade api"<<endl;
	return 0;
}


void CtpTrader::trade_stm(msg_t &msg)
{
	msg_t *mmsg;
	inst_t *pinst;
	inst   *ppinst;
	TThostFtdcInstrumentIDType instId;
	int ret;

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
						this->trader->username.c_str()
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
				 this->trade_spi->ReqUserLogin((char*)this->trader->brokerid.c_str(),
					(char*)this->trader->username.c_str(),
				(char*)this->trader->password.c_str());
				if(ret==0) {
					LOG_DEBUG<<"trade_stm login msg sended\n" <<std::endl;
					msg.type=TSTOP;
				}else {
					LOG_DEBUG<<"trade_stm login msg sended fail\n" <<std::endl;
					/*err process					
					*/
				}
				msg.type=TSTOP;
				break;
			case TOnRspUserLogin:
				LOG_DEBUG<<"TOnRspUserLogin stm"<<std::endl;;
				msg.type=TReqSettlementInfoConfirm;		
				/*fix*/
				msg.data=NULL;
				break;
			case TReqQryInstrument:
				/*two case, if msg.data==NULL, query all the Instrument
				 *else 
				 * */
				LOG_DEBUG<<"send TReqQryInstrument"<<std::endl;
				memset(&instId,0x0,sizeof(TThostFtdcInstrumentIDType));
				this->trade_spi->ReqQryInstrument(instId);
				msg.type=TSTOP;
				break;
			case TOnRspQryInstrument:
				/*1.update it into dmgr
				 *2.if is last,..
				 * */
				msg.type=TSTOP;
				//CThostFtdcInstrumentField pInstrument;
				//TOnRspQryInstrument_t;
				if(!this->trade_spi->IsErrorRspInfo(((( TOnRspQryInstrument_t*)msg.data)->pRspInfo))) {
					//LOG_DEBUG<<"OnRspInstrument inst:"<<(( TOnRspQryInstrument_t*)msg.data)->pInstrument.InstrumentID<<std::endl;


					/*
					pinst=new (inst_t);
					memset(pinst,0x0, sizeof(inst_t));
					memcpy(&pinst->base,&(( TOnRspQryInstrument_t*)msg.data)->pInstrument,sizeof( CThostFtdcInstrumentField ));
					this->pdmgr->add_inst(pinst->base.InstrumentID,pinst,0);
					if((( TOnRspQryInstrument_t*)msg.data)->bIsLast) {
						LOG_DEBUG<<"OnRspInstrument isLast"<<std::endl;
						this->pdmgr->sync_inst();
					}*/


					/*update it into pinstmgr
					 *todo merge pinstmgr to pdmgr
					 * */
					ppinst=new inst();
					ppinst->ignore=1;
					memcpy(&ppinst->base,&(( TOnRspQryInstrument_t*)msg.data)->pInstrument,sizeof( CThostFtdcInstrumentField ));
					this->pinstmgr->update_inst(ppinst->base.InstrumentID, ppinst);
					
					if((( TOnRspQryInstrument_t*)msg.data)->bIsLast) {
						LOG_DEBUG<<"OnRspInstrument isLast"<<std::endl;
						this->pinstmgr->set_last(1);
					}
				} else {
					LOG_DEBUG<<"OnRspInstrument err"<<std::endl;
				}
				msg.type=TSTOP;
				break;
			case TOnRtnInstrumentStatus:
				//(TOnRtnInstrumentStatus_t);
				LOG_DEBUG<<"OnRtnInstrumentStatus enter "<<
				" time: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.EnterTime<<
				" inst: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentID<<
				" reason: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.EnterReason<<
				" status: "<<((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentStatus<<std::endl;

				this->pinstmgr->update_inst_status(((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentID,  
						                   ((TOnRtnInstrumentStatus_t*)msg.data)->pInstrumentStatus.InstrumentStatus);
				msg.type=TSTOP;
				break;
			case TReqQryTradingAccount:
				msg.type=TSTOP;
				break;
			case TOnRspQryTradingAccount:
				msg.type=TSTOP;
				break;
			case TReqQryInvestorPosition:
				msg.type=TSTOP;
				break;
			case TOnRspQryInvestorPosition:
				msg.type=TSTOP;
				break;
			case TReqOrderInsert:
				msg.type=TSTOP;
				break;
			case TOnRspOrderInsert:
				msg.type=TSTOP;
				break;
			case TReqOrderAction:
				msg.type=TSTOP;
				break;
			case TOnRspOrderAction:
				msg.type=TSTOP;
				break;
			case TOnRtnOrder:
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
	LOG_DEBUG<<"finish one Trade data"<<std::endl;
}

void trader_loop(CtpTrader *ctptrader, int key)
{
	int i=0;
loop:
	while(ctptrader->running) {
		i=i+1;
		if(i%50==0) {
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
			printf("trader_loop get this msg\n");
			ctptrader->mqueue.pop_front();
			lk.unlock();
			//continue;
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
		LOG_DEBUG<<"post_msg func"<<std::endl;
		//?lk.unlock();
	}else {
		/*
		   do some warnning
		*/
		LOG_DEBUG<<"post_msg again"<<std::endl;
		goto again;
	}
}
