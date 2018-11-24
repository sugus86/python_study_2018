

#创建set二种方式
#1、第一种
s1=set()   #创建一个空的set，看下面就知道为什么要这么创建一个空的集合
#2、第二种
s2={11,22,33,44} #不仔细看有点想字典，如果s2={} 这个就是一个空的字典类型

print(s1,s2)

#增加集合add
s1.add(11)
print(s1)

#清空集合内容
s.clear()

a={11,22,33}
b={22,33,44}


a.difference(b) #查找A比B多的
b.difference(a) #查找B比A多的

#更新集合(B保留A集合中没有的值)
a={11,22,33}
b={33, 44, 22}
b.difference_update(a)
print(b)


a={11,22,33}
a.discard(11)
a.remove(33)

a=b.pop()

