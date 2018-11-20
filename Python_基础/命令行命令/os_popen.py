import os

#print(os.popen("ps -C ntpd | grep -v CMD |awk '{ print $1 }'").readlines())
#print(os.popen("tasklist").readlines())



#!/usr/bin/python
import os

p=os.popen('ipconfig')
x=p.read()
print(x)
p.close()
