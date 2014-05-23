#include "log.h"
#include <boost/log/sources/logger.hpp>  
#include <boost/log/sources/record_ostream.hpp>  
#include <boost/log/sources/global_logger_storage.hpp>  
#include <boost/log/utility/setup/file.hpp>  
#include <boost/log/utility/setup/common_attributes.hpp>  
#include <boost/log/sinks/text_ostream_backend.hpp>  
#include <boost/log/attributes/named_scope.hpp>  
#include <boost/log/expressions.hpp>  
#include <boost/log/support/date_time.hpp>  
#include <boost/log/detail/format.hpp>  
#include <boost/log/detail/thread_id.hpp>  

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
        keywords::file_name="ctp.%Y-%m-%d_%N.log",
        keywords::rotation_size=10*1024*1024,
        keywords::time_based_rotation=sinks::file::rotation_at_time_point(0,0,0),
	keywords::format =  
	(  
	 expr::stream
	 << "[" <<expr::format_date_time< boost::posix_time::ptime >("TimeStamp", "%Y-%m-%d %H:%M:%S.%f")
	 << " " << expr::attr< boost::log::aux::thread::id >("ThreadID")
	 << " " << logging::trivial::severity
	 << " ] " << expr::smessage
	)
        );

	fsink->locked_backend()->auto_flush(true);

	logging::core::get()->add_sink(fsink);
	logging::add_common_attributes(); 

	//logging::add_file_log("sample.log"); 
        //keywords::file_name="%Y-%m-%d_%N.log"
}
