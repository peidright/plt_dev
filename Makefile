include conf.mk
all: ctp test 
	echo "finished"
ctp: ctp.o
	echo "ctp build"
test:
	echo "test finished"

ctp.o:
	make -C src
	echo $(BOOST_DIR)
