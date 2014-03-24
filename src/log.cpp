#include "log.h"
/*
void SetFilter1() {  
  logging::core::get()->set_filter(logging::trivial::severity >= logging::trivial::info);  
}  
void SetFilter2() {  
  logging::core::get()->set_filter(logging::trivial::severity >= logging::trivial::debug);  
}  
int main () {  
  cout << "hello, world" << endl;  
  logging::add_file_log("sample.log");  
  SetFilter1();  
  BOOST_LOG_TRIVIAL(trace) << "A trace severity message";  
  BOOST_LOG_TRIVIAL(debug) << "A debug severity message";  
  BOOST_LOG_TRIVIAL(info) << "An informational severity message";  
  BOOST_LOG_TRIVIAL(warning) << "A warning severity message";  
  BOOST_LOG_TRIVIAL(error) << "An error severity message";  
  BOOST_LOG_TRIVIAL(fatal) << "A fatal severity message";  
   
  BOOST_LOG_TRIVIAL(info) << "--------------------" << endl;  
  SetFilter2();  
  BOOST_LOG_TRIVIAL(trace) << "A trace severity message";  
  BOOST_LOG_TRIVIAL(debug) << "A debug severity message";  
  BOOST_LOG_TRIVIAL(info) << "An informational severity message";  
  BOOST_LOG_TRIVIAL(warning) << "A warning severity message";  
  BOOST_LOG_TRIVIAL(error) << "An error severity message";  
  BOOST_LOG_TRIVIAL(fatal) << "A fatal severity message";  
} 

*/

void log_init()
{
	boost::shared_ptr<sinks::synchronous_sink<sinks::text_file_backend> > fsink=logging::add_file_log
        (
        keywords::file_name="sample1.log",      //文件名
        keywords::rotation_size=10*1024*1024,       //单个文件限制大小
        keywords::time_based_rotation=sinks::file::rotation_at_time_point(0,0,0)    //每天重建
        );

	fsink->locked_backend()->auto_flush(true);
	logging::core::get()->add_sink(fsink);

	//logging::add_file_log("sample.log"); 
        //keywords::file_name="%Y-%m-%d_%N.log"


}
