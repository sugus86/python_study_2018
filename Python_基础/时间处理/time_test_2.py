

from datetime import datetime, timedelta
import time

#字符串转datetime
string = '2017-04-25 11:59:58'
time1 = datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
print (time1)
print (type(time1))
#datetime转字符串
time1_str = datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
print(time1_str)
print(type(time1_str))
#时间戳转时间对象,这里用到的time模块是单独import time
new_time = time.time()
print (new_time)
now_time =datetime.fromtimestamp(new_time)
print (now_time)

#原文：https://blog.csdn.net/qq_25611295/article/details/78489290
'''
2017-04-25 11:59:58 
type ‘datetime.datetime’

2017-04-25 11:59:58 
type ‘str’

1510150491.54 
2017-11-08 22:14:51.539000
'''

from datetime import datetime, timedelta

now_time = datetime.now()
print (now_time)
#精确到秒的时间
new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
print (new_time)
#标准时间
aa = now_time.strftime('%c')
print (aa)
#表示昨天
yesterday = now_time + timedelta(days=-1)
print (yesterday)
#精确到昨天的秒
y = yesterday.strftime('%Y-%m-%d %H:%M:%S')
print (y)
#表示明天
tommorow = now_time + timedelta(days=+1)
print (tommorow)

'''
2017-11-09 14:20:03.955000 
2017-11-09 14:20:03 
11/09/17 14:20:03

2017-11-08 14:20:03.955000 
2017-11-08 14:20:03 
2017-11-10 14:20:03.955000
--------------------- 
作者：超级大饭粒 
来源：CSDN 
原文：https://blog.csdn.net/qq_25611295/article/details/78489290 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
