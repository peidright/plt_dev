#include "StrategyFrame.h"
#include "Python.h"

class sframe g_sframe;

extern int sframe_agent_loop(strategy_config_t &config);



int sframe::put_msg(string msg) {
	this->msg=msg+":ddd";
	cout<<"msg: "<<std::endl;
	return 0;
};
msg_t* sframe::get_msg(int key) {
	msg_t *msg=NULL;
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
		pipemap[key]->qsem.wait();
		msg=pipemap[key]->msgqueue[0];
		pipemap[key]->msgqueue.pop_front();
	}else {
	}
	return msg;
};
int sframe::reg_agent_key() {
	int key=0;
again:
	boost::unique_lock<boost::timed_mutex> lk(this->smutex,boost::chrono::milliseconds(1));
	if (lk) {
		key=this->base_key++;
		pipemap[key]=new (msgpipe_t);
	} else {
		/*todo */
		goto again;
	}
	return key;
};
int sframe::dispatch(){
};
int sframe::test(int key){
	msg_t *msg=new(msg_t);
	msg->data=NULL;
	TChange_t *tchange=NULL;
	tchange=new (TChange_t);
	tchange->subtype=TChange;
	tchange->v=1.01;
	msg->type=TChange;
	msg->data=(void*)tchange;

	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if (lk) {
		pipemap[key]->msgqueue.push_back(msg);
		pipemap[key]->qsem.post();
	} else {
		assert(0);
	}
	return 0;
};

int sframe::run(strategy_config_t &config) {
	cout<<"run sframe"<<std::endl;
	this->stg.add_thread(new boost::thread(sframe_agent_loop,config));
	return 0;
}

int sframe_agent::put_msg(string msg) {
	return 0;
};
string sframe_agent::get_msg() {
	cout<<"get_msg1"<<std::endl;
	this->psframe->test(agent_key);
	cout<<"get_msg2"<<std::endl;
	msg_t *msg=this->psframe->get_msg(agent_key);
	cout<<"get_msg3"<<std::endl;
	return this->msg2pystr(msg);
};

int sframe_agent::init(){
	this->psframe=&g_sframe;
	this->agent_key=this->psframe->reg_agent_key();
};

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
				msg->data=kchange;
				msg->len=sizeof(KChange_t);
				msg->type=KChange;
				kchange->subtype=root["subtype"].asInt();
				kchange->o=root["o"].asFloat();
				kchange->c=root["c"].asFloat();
				kchange->h=root["h"].asFloat();
				kchange->l=root["l"].asFloat();
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
		.def("get_msg", &sframe_agent::get_msg)
		.def("put_msg", &sframe_agent::put_msg)
		.def("init",    &sframe_agent::init)
	;
};


int sframe_agent_loop(strategy_config_t &config) {
	cout<<"sframe_agent loop"<<std::endl;
	PyObject *pName,*pModule,*pDict,*pFunc,*pArgs;
	
	Py_Initialize();
	if (!Py_IsInitialized()){
		cout<<"-1...."<<std::endl;
		return -1;
	}
	PyRun_SimpleString("import sys");
	initsframe_agent();
	cout<<"step2...."<<std::endl;

	PyRun_SimpleString("import sframe_agent");
	PyRun_SimpleString("sys.path.append('./')");
	PyRun_SimpleString("print 'aaa'");
	//PyRun_SimpleString("import test");
	//pName = PyString_FromString("test");
	//pModule = PyImport_Import(pName);
	PyObject *pyfile = PyFile_FromString((char*)config.scrip_name.c_str(),"r"); 
	FILE *f = PyFile_AsFile(pyfile); 
	PyRun_AnyFileEx(f,"test.py",0);
	cout<<"step3...."<<std::endl;
}

