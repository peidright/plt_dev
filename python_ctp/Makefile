
CC=g++ -g
CXXFLAGS = -fPIC -I ../inc -I /usr/include/python2.7
LDFLAGS  = -L ../lib -lthostmduserapiSSE -lthostmduserapiSSE
all: _ctp_Md.so _ctp_Trader.so

_ctp_Md.so: _ctp_Md.o wrapper_Md.o struct.o
	$(CC) $(CXXFLAGS) -shared $^  -o $@ $(LDFLAGS)

_ctp_Trader.so: _ctp_Trader.o wrapper_Trader.o struct.o
	$(CC) $(CXXFLAGS) -shared $^  -o $@ $(LDFLAGS)


_ctp_Md.cpp wrapper_Md.cpp struct.cpp _ctp_Trader.cpp wrapper_Trader.cpp: generate_wrapper.py
	python generate_wrapper.py
	python generate_struct.py

clean:
	rm -rf *.o *.con wrapper* struct.* _ctp_* UserApiStruct* MdApi.py TraderApi.py *.pyc
