import sys
import threading
from libs import sframe


def backtest_callback(bt):
    running=True;
    self.lock.acquire(1):  
    bt.thread_living=bt.thread_living+1;
    self.lock.release();
    stgy=None; 
    old_stgy=None;
    while running:
        self.lock.acquire(1); 
            if bt.strategy_list.size() > 0:
                if stgy!=None:
                    old_stgy=stgy;
                bt.strategy_list.pop(stgy);

                #reg to map
                self.lock.release();

                #stgy.sf.regbt();
            else: 
                if stgy!=None:
                    old_stgy=stgy;
                pass
        self.lock.release()
        if old_stgy!=None:
            #report
        pass
    pass
def ctpdemo_callback(bt):
    while bt.running:
        bt.slock.acquire(1);
        for (sid,item) in self.stgy_queue.items():
            if item["trademsg"].size()>0:
                #process trademsg
            if item["squote_idx"]==item["rquote_idx"]:
                #send next quote
            pass
        bt.lock.release();
        pass
    pass

class backtest():
    strategy=None;
    lock=None;
    slock=None;
    strategy_list=[];
    running_strategy=[]
    thread_num=10;
    thread_living=0;
    has_start=0;
    curr_idx=0;
    running=True;
    self.stgy_queue={"id":{"squote_idx":0,"rquote_idx":0,"reqtrade_idx":0,"rsptrade_idx":0, "trademsg":[],"stgy":None}};
    def __init__(self,strategy):
        self.strategy=strategy;
        self.strategy_list=strategy.expand();
        self.lock=threading.Lock();
        self.slock=threading.Lock();
        #self.lock.acquire(1):  
        #self.lock.release()
        pass
    def ctpdemo(self):
        #send msg,
        #check if all thread has process this msg
        #set all the trade msg
        #send next msg, check trade
        #next loop
        pass
    def send_quote(self):
        pass
    def judge_trade(self):
        pass
    def run(self):
        for idx in range(0,thread_num):
            thread.start_new_thread(backtest_callback, self);
        thread.start_new_thread(ctpdemo_callback, self);
        while True:
            #
            pass
        pass
