all: evil.so example

evil.so: 
	gcc -shared -fPIC -g -ldl evil.c -o $@

example:
	gcc -Wl,--no-as-needed -ldl example.c -o $@

clean:
	rm evil.so example
