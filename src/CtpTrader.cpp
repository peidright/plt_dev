#include "CtpTrader.h"
#include "trader.h"
#include <deque>
#include "help.h"


CtpTrader::CtpTrader(Trader *trader):qsem(0)
{
	this->trader=trader;
	this->running=1;
}
int CtpTrader::init()
{
	CThostFtdcTraderApi* trade_api = CThostFtdcTraderApi::CreateFtdcTraderApi(TRADE_DIR);
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
				break;
			case TOnHeartBeatWarning:
				/*todo err process
				*/
				break;
			case TOnRspError:
				/*todo err process
				*/
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
				if(   !this->trade_spi->IsErrorRspInfo(&(((TOnRspSettlementInfoConfirm_t*)msg.data)->pRspInfo))) {
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
				/**/
				msg.type=TSTOP;
				//CThostFtdcInstrumentField pInstrument;
				//TOnRspQryInstrument_t;
				if(!this->trade_spi->IsErrorRspInfo(&((( TOnRspQryInstrument_t*)msg.data)->pRspInfo))) {
					LOG_DEBUG<<"OnRspInstrument inst:"<<(( TOnRspQryInstrument_t*)msg.data)->pInstrument.InstrumentID<<std::endl;
				} else {
					LOG_DEBUG<<"OnRspInstrument err"<<std::endl;
				}
				msg.type=TSTOP;
				break;
			case TReqQryTradingAccount:
				break;
			case TOnRspQryTradingAccount:
				break;
			case TReqQryInvestorPosition:
				break;
			case TOnRspQryInvestorPosition:
				break;
			case TReqOrderInsert:
				break;
			case TOnRspOrderInsert:
				break;
			case TReqOrderAction:
				break;
			case TOnRspOrderAction:
				break;
			case TOnRtnOrder:
				break;
			default:
				break;
		}
	}
	msg.type=TSTOP;
	if(msg.type == TSTOP) {
		/*todo free message*/
		free(msg.data);
	}
	LOG_DEBUG<<"finish one Trade data"<<std::endl;
}

void trader_loop(CtpTrader *ctptrader, int key)
{
loop:
	while(ctptrader->running) {
		ctptrader->qsem.wait();
		boost::unique_lock<boost::timed_mutex> lk(ctptrader->qmutex,boost::chrono::milliseconds(3));
		if (lk) {
			if(ctptrader->mqueue.size()<=0) {
				/*bug happen*/
				cout<<"should not be zero qqueue"<<std::endl;
				lk.unlock();
			}
			msg_t msg=ctptrader->mqueue[0];
			printf("trader_loop get this msg\n");
			ctptrader->mqueue.pop_front();
			lk.unlock();
			//continue;
			ctptrader->trade_stm(msg);
		} else {
			cout<<"quote main loop err"<<std::endl;
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
		printf("post msg\n");	
		//?lk.unlock();
	}else {
		/*
		   do some warnning
		*/

		goto again;
	}
}

