CXX = gcc
CXXFLAGS = -shared -fPIC -g
EXE = evil.so

all: $(EXE)

$(EXE): 
	$(CXX) $(CXXFLAGS) evil.c -o $@

clean:
	rm $(EXE)
