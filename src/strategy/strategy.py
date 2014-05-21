import sys
from ctypes import *
from libs import apiop
from libs import apistruct
from libs import sframe
class sbase(object):
    "Strategy base "
    sf=None;
    sid=None;
    msg2rsp={};

    def __init__(self):
        pass
    def run_init(self):
        pass
    def run_clear(self):
        pass
    def run_except(self):
        pass
    def is_running(self):
        return True;
    def init(self):
        self.sf=sframe.sframe(self);
    def rsp(self,msg):
        pass
    def rsp_default(self,msg):
        #exp,run sbase rsp
        pass
    def run(self):
        self.sf.run();
#s=sbase();
#s.init();
#s.run();
