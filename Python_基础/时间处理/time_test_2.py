

from datetime import datetime, timedelta
import time

#�ַ���תdatetime
string = '2017-04-25 11:59:58'
time1 = datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
print (time1)
print (type(time1))
#datetimeת�ַ���
time1_str = datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
print(time1_str)
print(type(time1_str))
#ʱ���תʱ�����,�����õ���timeģ���ǵ���import time
new_time = time.time()
print (new_time)
now_time =datetime.fromtimestamp(new_time)
print (now_time)

#ԭ�ģ�https://blog.csdn.net/qq_25611295/article/details/78489290
'''
2017-04-25 11:59:58 
type ��datetime.datetime��

2017-04-25 11:59:58 
type ��str��

1510150491.54 
2017-11-08 22:14:51.539000
'''

from datetime import datetime, timedelta

now_time = datetime.now()
print (now_time)
#��ȷ�����ʱ��
new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
print (new_time)
#��׼ʱ��
aa = now_time.strftime('%c')
print (aa)
#��ʾ����
yesterday = now_time + timedelta(days=-1)
print (yesterday)
#��ȷ���������
y = yesterday.strftime('%Y-%m-%d %H:%M:%S')
print (y)
#��ʾ����
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
���ߣ��������� 
��Դ��CSDN 
ԭ�ģ�https://blog.csdn.net/qq_25611295/article/details/78489290 
��Ȩ����������Ϊ����ԭ�����£�ת���븽�ϲ������ӣ�
'''
