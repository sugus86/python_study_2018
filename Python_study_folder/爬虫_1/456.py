# -*- coding: utf-8 -*-
import urllib
import urllib.request as urllib2
import http.cookiejar as cookielib
import re
import string


class FangSpider(object):
    def __init__(self):
        self.testUrl = 'http://esf.wuhan.fang.com/'
        self.cookieJar = cookielib.CookieJar()
        self.postdata = urllib.parse.urlencode({'stuid': '201100300428', 'pwd': '921030'})
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
        self.s = []
        self.t = []

    def fang_init(self):
        myRequest = urllib2.Request(url=self.testUrl)
        result = self.opener.open(myRequest)
        # print(result.read().decode('gbk'))
        # self.deal_data(result.read().decode('GB2312'))
        print(result.read().decode('gb2312'))
        # self.deal_data(result.read())
        # print(self.s,self.t)

    def deal_data(self, myPage):
        myItem1 = re.findall('<a target="_blank" href=.*? title=.*?><span>.*?</span></a>', myPage, re.S)
        for item in myItem1:
            # self.s.append(item[0].encode('gbk'))
            # self.t.append(item[1].encode('gbk'))
            print(item)


mySpider = FangSpider()
mySpider.fang_init()
