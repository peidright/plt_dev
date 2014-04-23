ROOT_DIR=/home/dev/plt_dev/
BOOST_DIR=third/boost/boost155
SQLITE_DIR=third/sqlite/sqlite308/
LUAJIT_DIR=third/luajit/luajit202/src
PYTHON_DIR=third/python/python276
JSON_DIR=third/json/jsoncpp060

BOOST_LDIR=$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/regex/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/thread/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/datetime/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/chrono/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/signals/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/log/build/gcc-4.7/release/link-static/log-api-unix/threading-multi\
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/system/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/filesystem/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/date_time/build/gcc-4.7/release/link-static/threading-multi/  \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/python/build/gcc-4.7/release/link-static/threading-multi/ 




BOOST_LLIB= -lboost_regex -lboost_thread -lboost_chrono -lboost_signals -lboost_log_setup -lboost_log -lboost_system -lboost_filesystem -lboost_date_time -lboost_python

LUAJIT_LDIR=$(ROOT_DIR)/third/luajit/luajit202/src
LUAJIT_LLIB=-lluajit

PYTHON_LDIR=$(ROOT_DIR)/$(PYTHON_DIR)/
PYTHON_LLIB=-lpython2.7

JSON_LDIR=$(ROOT_DIR)/$(JSON_DIR)/libs/linux-gcc-4.7/
JSON_LLIB=-ljson_linux-gcc-4.7_libmt -ldl -lutil

API_DIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LDIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LLIB=-lthostmduserapi -lthosttraderapi


SQLITE_LDIR=$(ROOT_DIR)/third/sqlite/sqlite308/.libs/
SQLITE_LLIB=-lsqlite3

GCC=gcc
CFLAGS= -I$(API_DIR) -I$(ROOT_DIR)/third/boost/boost155/ \
 -I$(ROOT_DIR)/$(SQLITE_DIR) -I$(ROOT_DIR)/$(LUAJIT_DIR)\
 -I$(ROOT_DIR)/$(PYTHON_DIR)/Include -I$(ROOT_DIR)/$(JSON_DIR)/include 

