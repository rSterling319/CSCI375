CXXFLAGS =-g -Iinclude -std=c++11
LDFLAGS=

all : bin/app

tmp/Owned.o : src/Owned.cpp include/Owned.h include/Own.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Own.o : src/Own.cpp include/Own.h include/Owned.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Powered.o : src/Powered.cpp include/Powered.h include/Owned.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Type.o : src/Type.cpp include/Type.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Instrument.o : src/Instrument.cpp include/Instrument.h include/Owned.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Guitar.o : src/Guitar.cpp include/Guitar.h include/Instrument.h include/Powered.h include/Owned.h include/Type.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Toaster.o : src/Toaster.cpp include/Toaster.h include/Powered.h include/Owned.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/Piano.o : src/Piano.cpp include/Piano.h include/Instrument.h include/Owned.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

tmp/main.o : src/main.cpp include/Guitar.h include/Toaster.h include/Piano.h include/Instrument.h include/Powered.h include/Type.h include/Owned.h 
	$(CXX) $(CXXFLAGS) -c -o $@ $<

bin/app : tmp/main.o tmp/Guitar.o tmp/Piano.o tmp/Toaster.o tmp/Instrument.o tmp/Type.o tmp/Powered.o tmp/Own.o tmp/Owned.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)