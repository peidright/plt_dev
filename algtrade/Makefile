include ../conf.mk

test_objs =  main.o fea.o ga_fea.o
gene_objs =  gene.o genome.o population.o gene_main.o gene_chaos.o gene_chaos_tick1.o gene_chaos_tick2.o gene_chaos_tick3.o global.o gene_cell.o
all: $(test_objs) $(gene_objs) 
	g++ -o test_main $(test_objs) -L$(ROOT_DIR)/$(THIRD_LDIR) $(GA_LLIB)
	g++ -o gene_main $(gene_objs) -L$(ROOT_DIR)/$(THIRD_LDIR) $(GA_LLIB)


	#$(LUAJIT_LLIB) \
	#-L$(ROOT_DIR)/$(THIRD_LDIR) $(PYTHON_LLIB) \
	#-L$(API_LDIR) $(API_LLIB) -lpthread -lrt \
	#$(SQLITE_LLIB) $(BOOST_LLIB) $(JSON_LLIB) $(GA_LLIB)

	#todo bug,$(PYTHON_LDIR)
	cp test_main ../build/
	cp gene_main ../build/
	#cp -udPR  strategy ../build/

$(test_objs) $(gen_objs): %.o: %.cpp
	g++ -g -c -Wall    $(CFLAGS) $< -o $@ 
clean:
	rm -rf *.o
