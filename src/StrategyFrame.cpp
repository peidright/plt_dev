#include "StrategyFrame.h"
class sframe g_sframe;

msg_t *sframe_agent::pystr2msg(string str) {
	/*
	 * */
	Json::Reader reader;
	Json::Value root;

	msg_t *msg=new(msg_t);
	msg->data=NULL;
	KChange_t *kchange=NULL;
	TChange_t *tchange=NULL;
	if (reader.parse(str, root))  
	{
		int type=root["type"].asInt();    
		/*
		   int type = root["type"].asString();  
		   int code = root["code"].asInt();    
		   */
		switch(type) {
			case TChange:
				tchange=new (TChange_t);
				msg->data=tchange;
				msg->len=sizeof(TChange_t);
				msg->type=TChange;
				tchange->subtype=root["subtype"].asInt();
				tchange->v=root["v"].asFloat();
				break;
			case KChange:
				kchange=new (KChange_t);
				msg->data=KChange;
				msg->len=sizeof(KChange_t);
				msg->type=KChange;
				kchange->subtype=root["subtype"].asInt();
				kchange->v=root["v"].asFloat();
				break; 
			default:
				break;
		}
	} else {
	}
	return NULL;
};

string sframe_agent::msg2pystr(msg_t *msg) {

	Json::Reader reader;
	Json::Value root;
	KChange_t *kchange=NULL;
	TChange_t *tchange=NULL;
	string strmsg="";
	
	/*
	std::string out = root.toStyledString();
	Json::FastWriter writer;
	std::string out2 = writer.write(root);
	*/
	switch(msg->type) {
		case TChange:
			tchange=(TChange_t*)msg->data;
			root["type"]=TChange;
			root["subtype"]=tchange->subtype;
			root["v"]=tchange->v;
			strmsg=root.toStyledString();
			break;
		case KChange:
			kchange=(KChange_t*)msg->data;
			root["type"]=KChange;
			root["subtype"]=kchange->subtype;
			root["o"]=kchange->o;
			root["c"]=kchange->c;
			root["h"]=kchange->h;
			root["l"]=kchange->l;
			strmsg=root.toStyledString();
			break; 
		default:
			/*todo*/
			break;
	}
	return strmsg;
};

BOOST_PYTHON_MODULE(sframe_agent)
{
	class_<sframe_agent>("sframe_agent")
		.def("get_msg", &sframe_agent::get_msg
				)
		.def("put_msg", &sframe_agent::put_msg)
	;
};



