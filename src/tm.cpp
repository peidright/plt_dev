#include "tm.h"

using namespace std;
boost::asio::io_service io;
boost::asio::deadline_timer t(io, boost::posix_time::seconds(5)); 
boost::asio::deadline_timer t1(io, boost::posix_time::seconds(3)); 

void tm_cancel(const boost::system::error_code &)
{
	cerr<<"err"<<std::endl;
}

void tm_work(const boost::system::error_code &, 
	     boost::asio::deadline_timer *t, int *count)
{
	cerr<<"work"<<std::endl;
	t->expires_at(t->expires_at()+boost::posix_time::seconds(1));
	t->async_wait(boost::bind(tm_work,boost::asio::placeholders::error,t,count));
	//t.async_wait(boost::bind(print,boost::asio::placeholders::error,t,&count));
}

void tm_test() 
{
	int count=0;
	t.async_wait(boost::bind(tm_work,boost::asio::placeholders::error,&t,&count));
	//t.async_wait(boost::bind(print,boost::asio::placeholders::error,&t,&count));



	t1.async_wait(tm_cancel);
	io.run();
	sleep(10);
	cout<<"run finished"<<std::endl;
	sleep(10);
	cout<<"sleep 10 finished"<<std::endl;
	exit(0);
}

int get_time()
{
	return (int)(time(NULL));
}

