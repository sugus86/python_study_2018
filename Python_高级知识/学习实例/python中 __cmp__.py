

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dispc(self):
        return ('(' + str(self.x) + ',' + str(self.y) + ')')
    ...
    def __lt__(self, other):
        return ((self.x < other.x) and (self.y < other.y))
        
    def __eq__(self,other):
        return self.x == other.x
        
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 < p2)
print()

'''
请修改 Student 的__cmp__方法，让它按照分数从高到底排序，分数相同的按名字排序。 
?不会了怎么办 
1.sorted()函数会在程序运行时自动调用cmp()方法，当检测到有__cmp__()方法时则调用__cmp__()方法 
2.print sorted(L)相当于print sorted(L).__cmp__python 调用sorted函数时会自动调用该方法
--------------------- 
作者：周小董 
来源：CSDN 
原文：https://blog.csdn.net/xc_zhou/article/details/80823817 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

class Student(object):  

    def __init__(self, name, score):  
        self.name = name  
        self.score = score  

    def __str__(self):  
        return '(%s: %s)' % (self.name, self.score)  

    __repr__ = __str__  

    def __cmp__(self, s):  
        if self.score>s.score:  
            return -1  
        elif self.score<s.score:  
            return  1  
        else :  
             if self.name<s.name:  
                 return -1  
             elif self.name>s.name:  
                 return 1  
             else:  
                 return 0  


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]  
print (sorted(L))


'''
--------------------- 
作者：周小董 
来源：CSDN 
原文：https://blog.csdn.net/xc_zhou/article/details/80823817 
版权声明：本文为博主原创文章，转载请附上博文链接！

In Python3 the six rich comparison operators

__lt__(self, other) 
__le__(self, other) 
__eq__(self, other) 
__ne__(self, other) 
__gt__(self, other) 
__ge__(self, other) 
must be provided individually. This can be abbreviated by using functools.total_ordering.

This however turns out rather unreadable and unpractical most of the time. Still you have to put similar code pieces in 2 funcs - or use a further helper func.

So mostly I prefer to use the mixin class PY3__cmp__ shown below. This reestablishes the single __cmp__ method framework, which was and is quite clear and practical in most cases. One can still override selected rich comparisons.

Your example would just become:

 class point(PY3__cmp__):
      ... 
      # unchanged code
The PY3__cmp__ mixin class:
PY3 = sys.version_info[0] >= 3
if PY3:
    def cmp(a, b):
        return (a > b) - (a < b)
    # mixin class for Python3 supporting __cmp__
    class PY3__cmp__:   
        def __eq__(self, other):
            return self.__cmp__(other) == 0
        def __ne__(self, other):
            return self.__cmp__(other) != 0
        def __gt__(self, other):
            return self.__cmp__(other) > 0
        def __lt__(self, other):
            return self.__cmp__(other) < 0
        def __ge__(self, other):
            return self.__cmp__(other) >= 0
        def __le__(self, other):
            return self.__cmp__(other) <= 0
else:
    class PY3__cmp__:
        pass
'''        