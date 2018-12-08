#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://mail.163.com")

#登陆快播私有云
driver.find_element_by_id("idInput").send_keys("sugus86")
driver.find_element_by_id("pwdInput").send_keys("sugang")
driver.find_element_by_id("loginBtn").click()
time.sleep(3)

#driver.close()
print "Login success"

