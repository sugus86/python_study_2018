import datetime,time

#��datetimeת���ַ���
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#���ַ���ת��datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")

#���ַ���ת��ʱ�����ʽ
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#��ʱ���ת���ַ�����ʽ
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", tiem.localtime(stamp))

#��datetime����ת��ʱ�����ʽ
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())
    


#1. �����������ʱ��֮���ʱ���
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
#2. ��ȡn��ǰ��ʱ��
cur_time = dt.now()
# previous n days
pre_time = dt.timedelta(days=n)
#3. ��������ʱ�侫ȷ�������������λ
cur_time = dt.now()
# get day of current time
cur_day = cur_time.replace(hour=0, minute=0, second=0, mircrosecond=0)
#4. ��ȡһ������ʱ�����У�����list��
cur_time = dt.datetime.today()
datelist = [cur_time - dt.timedelta(days=x) for x in range(0, 100)]
#����

import pandas as pd
datelist =  pd.date_range(pd.datetime.today(), periods=100).tolist()
#5. ��ʱ���ַ���ת��Ϊdatetime����
date_formate = "%Y-%m-%d" # year-month-day
time = dt.strptime('2016-06-22', date_format)
#6. ��ʱ������ת��Ϊ�ַ�������
time_str = dt.strftime("%Y-%m-%d", dt.now()) # return like "2016-06-22"
