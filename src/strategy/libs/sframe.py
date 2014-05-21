import json
import sframe_agent
import apiop
import apistruct
import thread
import time

op2req={
        "TReqAuthenticate":{},
        "TReqUserLogin":{},
        "TReqUserLogout":{},
        "TReqUserLogout":{},
        "TReqQryInstrument":{"instn":"","sid":-1},
        "TReqQryTradingAccount":{"sid":-1},
        "TReqQryInvestorPosition":{"instn":"","sid":-1},
        "TReqOrderInsert":{"instn":"","dir":-1,"price":0,"vol":0,"sid":-1},
        "TReqOrderAction":{"exchangeid":-1,"ordersysid":-1,"sid":-1},
        "SRegMdStrategy":{},
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
        try:
            while True:
                msg=self.wait();
                self.strategy.rsp(msg);
                #break;
                pass
        except Exception,e:
            print "exp happen",e;
            pass
