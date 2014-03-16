include ../conf.mk

objects = CSem.o account.o  CtpTrade.o CtpTrader.o boosthelp.o config.o \
	main.o Quote.o CtpTraderSpi.o Quote.o market.o quote_io.o datalocal.o\
	mdseries.o CtpQuote.o dseries.o mdseries.o StrategyFrame.o CtpQuoter.o\
        help.o msgqueue.o trader.o
all: $(objects) 
	g++ -o ctp_client $(objects) -L$(BOOST_LDIR) $(BOOST_LLIB) -L$(LUAJIT_LDIR) $(LUAJIT_LLIB) \
	-L$(API_LDIR) $(API_LLIB) -lpthread -lrt -L$(SQLITE_LDIR) $(SQLITE_LLIB)
	echo $(SQLITE_LDIR)


$(objects): %.o: %.cpp
	g++ -c $(CFLAGS) $< -o $@ 
clean:
	rm -rf *.o
