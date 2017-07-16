#!/usr/bin/python
import whois, sys

urlf = sys.argv[1]
f=open(urlf,'r')

while True:
	line=f.readline()
	domain = whois.query(line)
	if not line : break
	f2=open(line.replace("\n","") + ".json", 'w')
	f2.write(str(domain.__dict__))
f.close()
f2.close()
