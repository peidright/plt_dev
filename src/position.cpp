#include "position.h"
position_t *update_position(CThostFtdcTradeField* trade, position_t *position)
{
    CThostFtdcInvestorPositionField  *base;
    bool need_fill=false;
    if(position) {
    }else {
        position=new (position_t);
        memcpy(position,0x0,sizeof(position_t));
        need_fill=true;
    }
    if((trade->Direction==THOST_FTDC_D_Buy && trade->OffsetFlag==THOST_FTDC_OF_Open) ||
       (trade->Direction==THOST_FTDC_D_Sell && 
        (trade->OffsetFlag==THOST_FTDC_OF_Close||trade->OffsetFlag==THOST_FTDC_OF_CloseToday))
      ){
        base=&position->bbase
        if(need_fill){
            base->PosiDirection=THOST_FTDC_PD_Long;
        }
        if(trade->OffsetFlag==THOST_FTDC_OF_Open) {
            //+
            base->Position+=trade->Volume;
        }else {
            //-
            base->Position-=trade->Volume;
        }

    }else if((trade->Direction==THOST_FTDC_D_Sell && trade->OffsetFlag==THOST_FTDC_OF_Open)||
             (trade->Direction==THOST_FTDC_D_Buy) 
            ) {
        base=&position->sbase;
        if(need_fill){
            base->PosiDirection=THOST_FTDC_PD_Short;
        }
        if(trade->OffsetFlag==Open) {
            //+
            base->Position+=trade->Volume;
        }else {
            //- todo check
            assert(base->Position>trade->Volume);
            base->Position-=trade->Volume;
        }
    }
    if(need_fill) {
        strcpy(base->BrokerID,trade->BrokerID);
        strcpy(base->InvestorID,trade->InvestorID);
        strcpy(base->InstrumentID,trade->InstrumentID);
    }
    return position;
}
