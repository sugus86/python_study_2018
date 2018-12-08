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


#访问xxxx网站
driver = webdriver.Firefox()
driver.get("http://mail.163.com")
#将用户名密码写入浏览器cookie
driver.add_cookie({'name':'username', 'value':'sugus86'})
driver.add_cookie({'name':'password', 'value':'xxxx'})
#再次访问xxxx网站，将会自动登录
sleep(0.5)
driver.quit()

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
sleep(5)

driver.quit()
