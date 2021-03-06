#ifndef LOG_H_
#define LOG_H_

#include <iostream>  
#include <boost/log/core.hpp>  
#include <boost/log/trivial.hpp>  
#include <boost/log/expressions.hpp>  
#include <boost/log/utility/setup/file.hpp>  

namespace logging = boost::log;  
namespace sinks = boost::log::sinks;
namespace attrs = boost::log::attributes;
namespace src = boost::log::sources;
namespace expr = boost::log::expressions;
namespace keywords = boost::log::keywords;
using namespace std;  
using namespace sinks;
using namespace keywords;


#define LOG_DEBUG\
	BOOST_LOG_TRIVIAL(debug)<<"[ file:"<<__FILE__<<" ]"<<"[ line:"<<__LINE__ <<" ]"


#define LOG_INFO\
	BOOST_LOG_TRIVIAL(info)

#define LOG_ERROR\
	BOOST_LOG_TRIVIAL(error)

#define LOG_WARNING\
	BOOST_LOG_TRIVIAL(warning)

//"[ file:"<<__FILE__<<" ]"<<"[ line:"<<__LINE__ <<" ]"

#define LFATAL(fatal)\
	BOOST_LOG_TRIVIAL(fatal)



extern void log_init();
//http://blog.csdn.net/jiafu1115/article/details/20048543
#endif
