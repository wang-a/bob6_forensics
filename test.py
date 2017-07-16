#!/usr/bin/python
import whois, sys

urlf = sys.argv[1]
f=open(urlf,'r')
f2=open("json",'w')
while True:
	line=f.readline()
	domain = whois.query(line)
	if not line : break		
	f2.write(str(domain.__dict__)+"\n")
f.close()
f2.close()
