# -*- coding: utf-8 -*-
import urllib
import urllib.request as urllib2

#test_url = "http://www.baidu.com"
#test_url = "http://esf.wuhan.fang.com"
test_url = "http://sz.lianjia.com/ershoufang/"
fd = urllib2.urlopen(test_url)
#print(fd.read())
#print(fd.read().decode('gbk'))
#print(fd.read().decode('utf'))
#print(fd.read().decode('gb2312'))
import bs4
content=fd.read()
content=bs4.BeautifulSoup(content)
print(content)