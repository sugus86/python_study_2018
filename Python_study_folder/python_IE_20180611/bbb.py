# -*- coding: cp936 -*-

from selenium import webdriver
from time import sleep


'''
driver = webdriver.Firefox()

driver.get('http://radar.kuaibo.com')

print driver.title

sleep(5)

driver.quit()
'''


#����xxxx��վ
driver = webdriver.Firefox()
driver.get("http://mail.163.com")
#���û�������д�������cookie
driver.add_cookie({'name':'username', 'value':'sugus86'})
driver.add_cookie({'name':'password', 'value':'xxxx'})
#�ٴη���xxxx��վ�������Զ���¼
sleep(0.5)
driver.quit()

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
sleep(5)

driver.quit()
