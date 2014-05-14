from ctypes import *
import json
import sframe_agent
import time

if __name__=="__main__":
	d=sframe_agent.sframe_agent();
	sid=d.init();
    //dispatchsynret",&sframe_agent::dispatchsynret)
    req={"instn":"cu1407","period":0,"sid":sid,"type":131};
    req=str(req);
    res=d.dispatchsynret(req);
    print res;
    time.sleep(4);
    while(True) {
            res=d.get_msg();
	        print json.loads(res)
    }
