import datetime,time

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", tiem.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())
    


#1. 计算给出两个时间之间的时间差
import datetime as dt
# current time
cur_time = dt.datetime.today()
# one day
pre_time = dt.date(2016, 5, 20) # eg: 2016.5.20
delta = cur_time - pre_time
# if you want to get discrepancy in days
print (delta.days)
# if you want to get discrepancy in hours
print (delta.hours)
# and so on
#2. 获取n天前的时间
cur_time = dt.now()
# previous n days
pre_time = dt.timedelta(days=n)
#3. 将给定的时间精确到天或者其他单位
cur_time = dt.now()
# get day of current time
cur_day = cur_time.replace(hour=0, minute=0, second=0, mircrosecond=0)
#4. 获取一连串的时间序列（返回list）
cur_time = dt.datetime.today()
datelist = [cur_time - dt.timedelta(days=x) for x in range(0, 100)]
#或者

import pandas as pd
datelist =  pd.date_range(pd.datetime.today(), periods=100).tolist()
#5. 将时间字符串转化为datetime类型
date_formate = "%Y-%m-%d" # year-month-day
time = dt.strptime('2016-06-22', date_format)
#6. 将时间类型转化为字符串类型
time_str = dt.strftime("%Y-%m-%d", dt.now()) # return like "2016-06-22"
