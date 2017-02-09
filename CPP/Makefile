CXXFLAGS= -g -Iinclude -std=c++11
LDFLAGS=

all : bin/app

tmp/Cheese.o : src/Cheese.cpp include/Cheese.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<
	
tmp/PastaDish.o : src/PastaDish.cpp include/PastaDish.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Spagetti.o : src/Spagetti.cpp include/Spagetti.h include/PastaDish.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<
	
tmp/Alfredo.o : src/Alfredo.cpp include/Alfredo.h include/PastaDish.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Cheesable.o : src/Cheesable.cpp include/Cheesable.h include/Cheese.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/main.o : src/main.cpp include/Spagetti.h include/Alfredo.h include/PastaDish.h include/Cheese.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

bin/app : tmp/main.o tmp/PastaDish.o tmp/Spagetti.o tmp/Alfredo.o tmp/Cheese.o tmp/Cheesable.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)
