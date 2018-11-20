import time
import datetime

print("\n"+"#"*80+"\n")

print(time.time())

print("\n"+"#"*80+"\n")

a = 1478244598.0
b = time.localtime(a)
time.strftime("%Y-%m-%d %H:%M:%S", b)
print(time.localtime())

print("\n"+"#"*80+"\n")

print(time.gmtime(time.time()))

print("\n"+"#"*80+"\n")

print(time.mktime(time.localtime()))

print("\n"+"#"*80+"\n")

print(time.strftime("%Y%m%d", time.localtime()))

print("\n"+"#"*80+"\n")

print(time.strptime('20130810', "%Y%m%d"))

print("\n"+"#"*80+"\n")

print(datetime.datetime.now())

print("\n"+"#"*80+"\n")

print(datetime.datetime.now().strftime("%Y%m%d"))

print("\n"+"#"*80+"\n")

print(datetime.datetime.strptime("20130810", "%Y%m%d"))

print("\n"+"#"*80+"\n")

print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime(2013, 8, 10, 11, 14, 50, 842812))

print("\n"+"#"*80+"\n")

time1 = datetime.datetime.now()
time.sleep(3)
time2 = datetime.datetime.now()
print(time2-time1)
print(time2>time1)
print(datetime.datetime.now() - datetime.timedelta(days = 7))
