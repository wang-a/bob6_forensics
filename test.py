#!/usr/bin/python
import whois, sys

urlf = sys.argv[1]
f=open(urlf,'r')
f2=open("jsonp.txt",'w')
line=f.readline()
domain = whois.query(line)

f2.write(str(domain.__dict__))
f2.close()
f.close()


