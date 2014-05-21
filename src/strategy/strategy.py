import sys
from ctypes import *
from libs import apiop
from libs import apistruct
from libs import sframe
class sbase(object):
    "Strategy base "
    sf=None;
    sid=None;
    def __init__(self):
        pass
    def init(self):
        self.sf=sframe.sframe(self);
    def rsp(self,msg):
        pass
    def run(self):
        self.sf.run();
#s=sbase();
#s.init();
#s.run();
