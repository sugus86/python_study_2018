
#单参数
#min (iterable[,key=func]) -> value 

#多参数
#min(a, b, c, ...[, key=func]) -> value

#1.自定义对象的比较
class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "a: %s, b: %s"%(self.a,self.b)

x=test(10,'x')
y=test(2,'y')
z=test(8,'z')

minTest=min(x,y,z,key=lambda t:t.a)
print(minTest)


dic={'b':3,'a':5,'c':9,'d':2}
list1 = sorted(dic)
print(list1)

# sorted with key
list2 = sorted(dic.items())
print(list2)

#sorted with value
list3 = sorted(dic.items(),key=lambda d:d[1])
print(list3)