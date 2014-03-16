#include "boosthelp.h"
#include <boost/interprocess/sync/interprocess_semaphore.hpp>
#include <boost/signal.hpp>
#include <time.h>
#include <stdio.h>
boost::interprocess::interprocess_semaphore g_iosem(0);

template<typename funT, typename paramT>
struct adapter {
	adapter(funT f,paramT& p):f_(f),p_(&p){}
	void operator()() {f_(*p_);}
private:
	funT f_;
	paramT *p_;
};

void worker(const std::string& s) 
{
	g_iosem.wait();
	std::cout<<s<<std::endl;
}
typedef void(*workfunc)(const std::string& s);
void test()
{
	std::string *s1=new std::string("thread1");
	boost::thread thr1(adapter<workfunc,std::string>(worker,*s1));

}

void helloworld() {
	boost::this_thread::sleep(boost::get_system_time()+boost::posix_time::seconds(5));
	std::cout<<"hellow"<<std::endl;
}
boost::signal<void ()>sig;

void test1()
{
	//g_iosem.post();
	test();
	

	//sig.connect(&helloworld);
	//sig();
	//std::cout<<"test1 end"<<std::endl;


	//thread_group
	boost::thread_group tg;
	tg.add_thread(new boost::thread(worker,"dddd"));
	//tg.add_thread(boost::thread(adapter<workfunc,std::string>(worker,"dddd")));
}
