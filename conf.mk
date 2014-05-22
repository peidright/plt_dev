ROOT_DIR=/home/dev/plt_dev/
THIRD_LDIR=third/lib
THIRD_IDIR=third/include

BOOST_LLIB= -lboost_regex -lboost_thread -lboost_chrono -lboost_signals -lboost_system -lboost_filesystem -lboost_date_time -lboost_python -lboost_log_setup -lboost_log 

LUAJIT_LLIB=-lluajit-5.1

PYTHON_LLIB=-lpython2.7

GA_LLIB=-lga

JSON_LLIB=-ljson_linux-gcc-4.7_libmt -ldl -lutil

API_DIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LDIR=$(ROOT_DIR)/api/linux/ctp131204/ 
API_LLIB=-lthostmduserapi -lthosttraderapi

SQLITE_LLIB=-lsqlite3

GCC=gcc
CFLAGS= -I$(API_DIR) -I$(ROOT_DIR)/$(THIRD_IDIR) -I$(ROOT_DIR)/$(THIRD_IDIR)/python -DBOOST_LOG_DYN_LINK


