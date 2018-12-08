#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs
  
class douyu(unittest.TestCase):
  
    #初始化方法
    def setUp(self):
     self.option = webdriver.ChromeOptions()
     self.option.add_argument("test-type")
     self.driver = webdriver.Chrome(options=self.option)
     self.driver=webdriver.Chrome()
     self.num=0
    # 测试方法必须有test开头
  
    def testDouyu(self):
           self.driver.get("https://www.douyu.com/directory/all")
           while True:
              soup= bs(self.driver.page_source,"lxml")
              names=soup.find_all("h3",{"class":"ellipsis"})
              numbers=soup.find_all("span",{"class":"dy-num fr"})
            #zip(names,numbers)将这两个列表合并为一个元组
              for name,number in zip(names,numbers):
                print("观众人数:%s"%number.get_text().strip(),"\t房间名:%s"%name.get_text().strip())
                self.num =1
              if  self.driver.page_source.find("shark-pager-disable-next")!=-1:
                 break
              self.driver.find_element_by_class_name("shark-pager-next").click()
  
    #测试结束后执行的方式
    def tearDown(self):
        print("当前直播人数: %d"%self.num)
        self.driver.quit()
if __name__=="__main__":
    #启动测试模块
    unittest.main()
