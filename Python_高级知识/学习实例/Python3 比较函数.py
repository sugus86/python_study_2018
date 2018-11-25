import operator

print(operator.eq('hello','name'))
print(operator.eq('hello','hello'))

a=1
b=2

operator.lt(a, b)
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
operator.__lt__(a, b)
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)


'''
lt(a,b) 相当于 a<b     从第一个数字或字母（ASCII）比大小  
le(a,b)相当于a<=b 
eq(a,b)相当于a==b     字母完全一样，返回True, 
ne(a,b)相当于a!=b 
gt(a,b)相当于a>b 
ge(a,b)相当于 a>=b 
函数的返回值是布尔哦
'''