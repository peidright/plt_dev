import sys
import json
import time
from strategy import strategy


class strategy1(sbase):
    def rsp(self,msg):
        print "rsp";
        pass
    def config(self):
        print "config";
        pass
if __name__=="__main__":
    s=strategy1();
    s.config();
    s.init();
    s.run();
