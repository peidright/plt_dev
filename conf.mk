ROOT_DIR=/home/dev/plt_dev/
BOOST_DIR=third/boost/boost155
SQLITE_DIR=third/sqlite/sqlite308/
LUAJIT_DIR=third/luajit/luajit202/src

BOOST_LDIR=$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/regex/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/thread/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/datetime/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/chrono/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/signals/build/gcc-4.7/release/link-static/threading-multi/ \
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/log/build/gcc-4.7/release/link-static/log-api-unix/threading-multi\
	-L$(ROOT_DIR)/$(BOOST_DIR)/bin.v2/libs/system/build/gcc-4.7/release/link-static/threading-multi/ 

BOOST_LLIB= -lboost_regex -lboost_thread -lboost_chrono -lboost_signals -lboost_log_setup -lboost_log -lboost_system

LUAJIT_LDIR=$(ROOT_DIR)/third/luajit/luajit202/src
LUAJIT_LLIB=-lluajit

API_DIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LDIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LLIB=-lthostmduserapi -lthosttraderapi


SQLITE_LDIR=$(ROOT_DIR)/third/sqlite/sqlite308/.libs/
SQLITE_LLIB=-lsqlite3

GCC=gcc
CFLAGS= -I$(API_DIR) -I$(ROOT_DIR)/third/boost/boost155/ \
 -I$(ROOT_DIR)/$(SQLITE_DIR) -I$(ROOT_DIR)/$(LUAJIT_DIR)

