import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import time
import types
from strategy.strategy import sbase

class strategy1(sbase):
    def rsp(self,msg):
        t=msg.get("type","default");
        func_name=self.msg2rsp.get(t,"rsp_default");
        func_inst=getattr(self,func_name);
        if isinstance(func_inst, types.FunctionType):
            #todo err
            pass
        else:
            func_inst(msg);
            pass
    def is_running(self):
        return True;
    def run_init(self):
        #ret=self.sf.RegMdStrategy("ag1412", 0);
        #ret=self.sf.RegMdStrategy("IF1406", 0);
        #self.sf.log("RspRegMdStrategy: "+json.dumps(ret));
        ret=self.sf.ReqQryInstrument("ag1412")
        self.sf.log("RspReqQryInstrument: "+json.dumps(ret));
        #time.sleep(10);
        #ret=self.sf.ReqQryTradingAccount();
        #self.sf.log("RspQryTradingAccount: "+json.dumps(ret));
        #ReqQryInstrument(self, instn)
        #ReqQryTradingAccount(self)
        #ReqQryInvestorPosition(self, instn)
        #ReqOrderInsert(self, instn, dir,kpp, price, vol)
        #ReqOrderAction(self, exchangeid, ordersysid)
        #RegMdStrategy(self, instn, period)
    def run_clear(self):
        pass
    def config(self):
        print "config";
        self.msg2rsp={
                "TChange":"rsp_quote",
                "KChange":"rsp_quote",
                "SRegRspCommon":"rsp_default",
                "TOnRspQryInstrument":"rsp_default",
                "TOnRspQryTradingAccount":"rsp_trade",
                "TOnRspQryInvestorPosition":"rsp_trade",
                "TOnRspOrderInsert":"rsp_trade",
                "TOnRspOrderAction":"rsp_trade",
                "TOnRtnOrder":"rsp_trade",
                "TOnRtnTrade":"rsp_trade",
                "default":"rsp_default",
        };
        print sys._getframe().f_code.co_name,"ssss"
        pass
    def rsp_trade(self,msg):
        pass
    def rsp_quote(self,msg):
        pass
    def rsp_default(self,msg):
        pass
if __name__=="__main__":
    s=strategy1();
    s.config();
    #sys.exit(0);
    s.init();
    s.run();
#(isinstance(getattr(Test, 'foo'), types.FunctionType))
#(isinstance(getattr(Test, 'bar'), types.FunctionType))
#True, False
#You can also use the inspect module:
#    >>> inspect.isfunction(Test.foo)
#    True
#    >>> inspect.isfunction(Test.bar)
#    False
