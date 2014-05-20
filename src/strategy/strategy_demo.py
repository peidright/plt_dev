import sys
from ctypes import *
import json
import sframe_agent as sframe_agent
import time



if __name__=="__main__":
    f=open("testt.log","a+")
    d=sframe_agent.sframe_agent();
    sid=d.init();
    req={"instn":"ag1412","period":0,"sid":sid,"type":131};
    req=json.dumps(req);
    #print>>f,req
    #print "req is",req 
    res=d.dispatchsynret(req);
    print res;
    print>>f,res;
    try:
        while True:
            res=d.get_msg();
            print>>f,res;
            print json.loads(res);
            f.flush()
    except Exception:
        print>>f,"except finished"
        f.close()
