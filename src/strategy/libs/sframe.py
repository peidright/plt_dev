import json
import sframe_agent
import apiop
import apistruct
import thread
import time

op2req={
        "ReqAuthenticate":{},
        "ReqUserLogin":{},
        "ReqUserLogout":{},
        "ReqUserLogout":{},
        "ReqQryInstrument":{"instn":"","sid":-1,"type":"TReqQryInstrument"},
        "ReqQryTradingAccount":{"sid":-1,"type":"TReqQryTradingAccount"},
        "ReqQryInvestorPosition":{"instn":"","sid":-1,"type":"TReqQryInvestorPosition"},
        "ReqOrderInsert":{"instn":"","dir":-1,"price":0,"vol":0,"sid":-1,"type":"TReqOrderInsert"},
        "ReqOrderAction":{"exchangeid":-1,"ordersysid":-1,"sid":-1,"type":"TReqOrderAction"},
        "RegMdStrategy":{"type":"SRegMdStrategy"},
}

def sframe_callback(arg):
    while True:
        print "dddd";
        time.sleep(1);
    pass

class sframe:
    agent=None;
    sid  =None;
    def __init__(self,strategy):
        self.op_vec=[];
        self.op_map={};
        self.msg=[]
        self.agent=sframe_agent.sframe_agent();
        self.sid=self.agent.init();
        self.strategy=strategy;
        self.lfile="strategy_"+str(self.sid)+".log";
    def log(self,msg):
        fh=open(self.lfile,"a+");
        fh.write(msg+"\n");
        fh.close();
        pass
    def req(self, t, req):
        _req=op2reg.get(t,{});
        _req["type"]=type2valmap.get(t,-1);
        return self.agent.dispatchsynret(_req);
    def test(self):
        thread.start_new_thread(sframe_callback,arg);
        pass
    def wait(self):
        print "in wait";
        msg=self.agent.get_msg();
        msg=json.loads(msg);
        return msg;
    def run(self):
        print "in run";
        self.strategy.run_init();
        try:
            while self.strategy.is_running():
                msg=self.wait();
                self.strategy.rsp(msg);
                #break;
                pass
            self.strategy.run_clear();
        except Exception,e:
            print "exp happen",e;
            self.strategy.run_except();
            pass
    def buy(self,instn,price,lots,off):
        ret=self.ReqOrderInsert(instn, 'B', price, lots):
        return {"retmsg":"not implement"};
        pass
    def sell(self,instn,price,lots,off):
        ret=self.ReqOrderInsert(instn, 'C', price, lots):
        return {"retmsg":"not implement"};
        pass
    def req(self,msg):
        pass

    def ReqQryInstrument(self, instn):
        #req=op2req.get
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["instn"]=instn;
        req["sid"]=self.sid;
        pass
    def ReqQryTradingAccount(self):
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["sid"]=self.sid;
        pass
    def ReqQryInvestorPosition(self, instn):
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["instn"]=instn;
        req["sid"]=self.sid;

        pass
    def ReqOrderInsert(self, instn, dir, price, vol):
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["instn"]=instn;
        req["dir"]=ord(dir);
        #str(unichr(97))
        req["price"]=price;
        req["vol"]=vol;
        req["sid"]=self.sid;

        pass
    def ReqOrderAction(self, exchangeid, ordersysid):
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["exchangeid"]=exchangeid;
        req["ordersysid"]=ordersysid;
        req["sid"]=self.sid;

        pass
    def RegMdStrategy(self, instn, period):
        func_name=sys._getframe().f_code.co_name
        req=op2req.get(func_name,{});
        req["instn"]=instn;
        req["period"]=period;
        req["sid"]=self.sid;
        pass

