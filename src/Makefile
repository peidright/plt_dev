include ../conf.mk

objects = CSem.o account.o  CtpTrade.o CtpTrader.o boosthelp.o config.o log.o\
	main.o market.o quote_io.o datalocal.o\
	CtpQuote.o dseries.o mdseries.o StrategyFrame.o CtpQuoter.o\
        help.o msgqueue.o trader.o tm.o demo.o instmgr.o
all: $(objects) 
	g++ -o ctp_client $(objects) -L$(ROOT_DIR)/$(THIRD_LDIR) $(LUAJIT_LLIB) \
	-L$(API_LDIR) $(API_LLIB) -lpthread -lrt \
	-L$(ROOT_DIR)/$(THIRD_LDIR) $(PYTHON_LLIB) \
	$(SQLITE_LLIB) $(BOOST_LLIB) $(JSON_LLIB) 

	#todo bug,$(PYTHON_LDIR)
	cp ctp_client ../build/
	#cp -udPR  strategy ../build/


$(objects): %.o: %.cpp
	g++ -g -c -Wall    $(CFLAGS) $< -o $@ 
clean:
	rm -rf *.o
