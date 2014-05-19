from ctypes import *
import json
import sframe_agent

if __name__=="__main__":
	d=sframe_agent.sframe_agent();
	d.init();
	res= d.get_msg();
	print json.loads(res)
