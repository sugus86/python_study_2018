

import ConfigParser

#读取配置文件：
conf = ConfigParser.ConfigParser()
conf.read('dbconf.ini')              # 文件路径
name = conf.get("section1", "name")  # 获取指定section 的option值
print name
sex = conf.get("section1", "sex")    # 获取section1 的sex值
print age

#写入配置文件：
conf = ConfigParser.ConfigParser()
conf.read('dbconf.ini')

conf.set("section1", "name", "jhao104")       # 修改指定section 的option
conf.set("section1", "age", "21")             # 增加指定section 的option
conf.add_section("section3")                  # 增加section
conf.set("section3", "site", "oschina.net")   # 给新增的section 写入option
conf.write(open('dbconf.ini', 'w'))