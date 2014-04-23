include ../conf.mk

objects = CSem.o account.o  CtpTrade.o CtpTrader.o boosthelp.o config.o log.o\
	main.o Quote.o  Quote.o market.o quote_io.o datalocal.o\
	CtpQuote.o dseries.o mdseries.o StrategyFrame.o CtpQuoter.o\
        help.o msgqueue.o trader.o tm.o
all: $(objects) 
	g++ -o ctp_client $(objects) -L$(LUAJIT_LDIR) $(LUAJIT_LLIB) \
	-L$(API_LDIR) $(API_LLIB) -lpthread -lrt -L$(SQLITE_LDIR) $(SQLITE_LLIB) $(PYTHON_LLIB)  \
	-L$(BOOST_LDIR) $(BOOST_LLIB) \
	-L$(JSON_LDIR)  $(JSON_LLIB)

	#todo bug,$(PYTHON_LDIR)
	echo $(SQLITE_LDIR)
	cp ctp_client ../build/


$(objects): %.o: %.cpp
	g++ -g -c -Wall   $(CFLAGS) $< -o $@ 
clean:
	rm -rf *.o
