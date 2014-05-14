#include "StrategyFrame.h"
#include "Python.h"

class sframe g_sframe;

extern int sframe_agent_loop(strategy_config_t &config);



int sframe::put_msg(msg_t *msg,int key) {
again:
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
		pipemap[key]->msgqueue.push_back(msg);
		pipemap[key]->qsem.post();
	}else {
        /*todo*/
        goto again;
	}
};

msg_t* sframe::get_msg(int key) {
	msg_t *msg=NULL;
again:
	boost::unique_lock<boost::timed_mutex> lk(this->pipemap[key]->qmutex,boost::chrono::milliseconds(1));
	if(lk) {
		pipemap[key]->qsem.wait();
		msg=pipemap[key]->msgqueue[0];
		pipemap[key]->msgqueue.pop_front();
	}else {
        /*todo*/
        goto again;
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

int sframe::init(CtpQuoter *ctpquoter, CtpTrader *ctptrader)
{
    this->ctpquoter=ctpquoter;
    this->ctptrader=ctptrader;
    return 0;
};
msg_t *sframe::dispatchsynret(msg_t *msg)
{
    int ret;
    SRegMdInst_t *pSRegMdInst;
    SRegMdPeriod_t *pSRegMdPeriod;
    SRegMdStrategy_t *pSRegMdStrategy;
    SRegRspCommon_t  *pSRegRspCommon;
    msg_t *pmsg=NULL;

    switch(msg->type) {
        case SRegMdInst:
            pSRegMdInst=(SRegMdInst_t*)msg->data;
            assert(0);
            break;
        case SRegMdPeriod:
            pSRegMdPeriod=(SRegMdPeriod_t*)msg->data;
            pmsg=new(msg_t);
            ret=this->ctpquoter->mds->regmd_period(pSRegMdPeriod->instn,(pSRegMdPeriod->period==0?MIRCO:MINUTE),pSRegMdPeriod->period);
            pSRegRspCommon=new(SRegRspCommon_t);
            pmsg->data=pSRegRspCommon;
            pmsg->type=SRegRspCommon;
            pSRegRspCommon->ret=ret;
            break;
        case SRegMdStrategy:
            pSRegMdStrategy=(SRegMdStrategy_t*)msg->data;
            ret=this->ctpquoter->mds->regmd_strategy(pSRegMdStrategy->instn,pSRegMdStrategy->sid,pSRegMdStrategy->period);
            pmsg=new(msg_t);
            pSRegRspCommon=new(SRegRspCommon_t);
            pmsg->data=pSRegRspCommon;
            pmsg->type=SRegRspCommon;
            pSRegRspCommon->ret=ret;
            break;
        default:
            assert(0);
            break;
    }
    return pmsg;
}
int sframe::dispatchsyn(msg_t *msg){
    int ret=-1;
    SRegMdInst_t *pSRegMdInst;
    SRegMdPeriod_t *pSRegMdPeriod;
    SRegMdStrategy_t *pSRegMdStrategy;
    SRegRspCommon_t  *pSRegRspCommon;

    switch(msg->type) {
        case SRegMdInst:
            pSRegMdInst=(SRegMdInst_t*)msg->data;
            assert(0);
            break;
        case SRegMdPeriod:
            pSRegMdPeriod=(SRegMdPeriod_t*)msg->data;
            ret=this->ctpquoter->mds->regmd_period(pSRegMdPeriod->instn,(pSRegMdPeriod->period==0?MIRCO:MINUTE),pSRegMdPeriod->period);
            break;
        case SRegMdStrategy:
            pSRegMdStrategy=(SRegMdStrategy_t*)msg->data;
            ret=this->ctpquoter->mds->regmd_strategy(pSRegMdStrategy->instn,pSRegMdStrategy->sid,pSRegMdStrategy->period);
            break;
        default:
            assert(0);
            break;
    }
    return ret;
}

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
	//cout<<"get_msg1"<<std::endl;
	this->psframe->test(agent_key);
	//cout<<"get_msg2"<<std::endl;
	msg_t *msg=this->psframe->get_msg(agent_key);
	//cout<<"get_msg3"<<std::endl;
	return this->msg2pystr(msg);
};

int sframe_agent::init(){
	this->psframe=&g_sframe;
	this->agent_key=this->psframe->reg_agent_key();
    return this->agent_key;
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
    SRegMdStrategy_t *pSRegMdStrategy;
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

            case SRegMdStrategy:
                pSRegMdStrategy=new (SRegMdStrategy_t);
                msg->data=pSRegMdStrategy;
                msg->type=SRegMdStrategy;
                pSRegMdStrategy->instn=root["instn"].asString();
                pSRegMdStrategy->period=root["period"].asInt();
                pSRegMdStrategy->sid=root["sid"].asInt();
			default:
				break;
		}
        return msg;
	} else {
        /*todo msg free*/
	}
	return NULL;
};

int sframe_agent::dispatchsyn(string msg){
    /*if complicate result, we must return json*/
    int ret;
    msg_t *msg1=this->pystr2msg(msg);
    ret=this->psframe->dispatchsyn(msg1);
    free(msg1->data);
    free(msg1);
    return ret;
}


string sframe_agent::dispatchsynret(string msg){
    string ret;
    msg_t *msg1=this->pystr2msg(msg);
    msg_t *msg2=this->psframe->dispatchsynret(msg1);
    free(msg1->data);
    free(msg1);
    ret=this->msg2pystr(msg2);
    free(msg2->data);
    free(msg2);
    return ret;
}


string sframe_agent::msg2pystr(msg_t *msg) {

	Json::Reader reader;
	Json::Value root;
	KChange_t *kchange=NULL;
	TChange_t *tchange=NULL;
    SRegRspCommon_t *pSRegRspCommon;
	string strmsg="";
	
	/*
	std::string out = root.toStyledString();
	Json::FastWriter writer;
	std::string out2 = writer.write(root);
	*/
    if(msg==NULL)
        return root.toStyledString();

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
        case SRegRspCommon:
            pSRegRspCommon=(SRegRspCommon_t*)msg->data;
            root["ret"]=pSRegRspCommon->ret;
            root["type"]=msg->type;
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
        .def("dispatchsyn",&sframe_agent::dispatchsyn)
        .def("dispatchsynret",&sframe_agent::dispatchsynret)
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

int sframe_put_msg(msg_t *msg, int key)
{
    int ret=g_sframe.put_msg(msg, key);
    return ret;
}

int sframe_quote_kchange(float o,float c, float h, float l, int sec,int msec,int subtype, int key)
{
    int ret;
    msg_t *msg=new(msg_t);
    msg->data=new (KChange_t);
    ((KChange_t*)msg->data)->o=o;
    ((KChange_t*)msg->data)->c=c;
    ((KChange_t*)msg->data)->h=h;
    ((KChange_t*)msg->data)->l=l;
    subtype=(subtype==0?OLD:NEW);
    ((KChange_t*)msg->data)->subtype=subtype;
    ret=sframe_put_msg(msg,key);
    return ret;
}

int sframe_quote_tchange(float v, int sec, int msec,int subtype, int key)
{
    int ret;
    msg_t *msg=new(msg_t);
    msg->data=new (TChange_t);
    ((TChange_t*)msg->data)->subtype=NEW;
    ((TChange_t*)msg->data)->v=v;
    ret=sframe_put_msg(msg, key);
    return ret;
}



