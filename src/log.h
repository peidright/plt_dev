#ifndef LOG_H_
#define LOG_H_

#include <iostream>  
#include <boost/log/core.hpp>  
#include <boost/log/trivial.hpp>  
#include <boost/log/expressions.hpp>  
#include <boost/log/utility/setup/file.hpp>  
namespace logging = boost::log;  
using namespace std;  


#define LOG_DEBUG\  
	BOOST_LOG_TRIVIAL(debug) 
#define LOG_INFO\  
	BOOST_LOG_TRIVIAL(info) 
#define LOG_ERROR\  
	BOOST_LOG_TRIVIAL(error) 
#define LOG_WARNING\  
	BOOST_LOG_TRIVIAL(warning) 
#define LOG_FATAL(fatal)\
	BOOST_LOG_TRIVIAL(fatal) 
extern void log_init();
#endif
