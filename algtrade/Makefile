include ../conf.mk

objects = 	main.o fea.o ga_fea.o
all: $(objects) 
	g++ -o ga_fea $(objects) -L$(ROOT_DIR)/$(THIRD_LDIR) $(GA_LLIB)

	#$(LUAJIT_LLIB) \
	#-L$(ROOT_DIR)/$(THIRD_LDIR) $(PYTHON_LLIB) \
	#-L$(API_LDIR) $(API_LLIB) -lpthread -lrt \
	#$(SQLITE_LLIB) $(BOOST_LLIB) $(JSON_LLIB) $(GA_LLIB)

	#todo bug,$(PYTHON_LDIR)
	cp ga_fea ../build/
	#cp -udPR  strategy ../build/

$(objects): %.o: %.cpp
	g++ -g -c -Wall    $(CFLAGS) $< -o $@ 
clean:
	rm -rf *.o
