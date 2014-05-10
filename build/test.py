from ctypes import *

import sframe

class res(Structure):
	_fields_ = [("subtype", c_int),("o", c_float),("c",c_float),("h",c_float),("l",c_float)];
if __name__=="__main__":
	d=sframe.sframe();
	res= d.put_msg("dddd");
	print res
	res= d.get_msg();
	print res

