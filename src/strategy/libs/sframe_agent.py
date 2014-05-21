import json
class sframe_agent(object):
    def __init__(self):
        self.ret={"ret":0,"msg":"hook agent"};
        pass
    def init(self):
        return 1;
        pass
    def dispatchsynret(self,req):
        return json.dumps(self.ret);
        pass
    def get_msg(self):
        return json.dumps(self.ret);
        pass
