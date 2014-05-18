#ifndef TM_H_
#define TM_H_

#include <iostream>
#include <boost/bind.hpp>
#include <boost/asio.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>


extern boost::asio::io_service io;

void tm_cancel(const boost::system::error_code &);
void tm_work(const boost::system::error_code &);
void tm_test();
int get_time();
#endif
