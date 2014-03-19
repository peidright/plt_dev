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
	logging::add_file_log("sample.log"); 
}
