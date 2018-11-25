'''
__cmp__ 
对 int、str 等内置数据类型排序时，Python的 sorted() 按照默认的比较函数 cmp 排序，但是，如果对一组 
Student 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()： 
'''

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
 
    def __lq__(self, s):
        if self.name < s.name:
            return -1 
        elif self.name > s.name:
            return 1
        else:
            return 0
    def __eq__(self,s):
        return self.name == s.name
        
    def __lt__(self,s):
        if self.name > s.name:
            return 1
        else:
            return 0
            
'''
 def __eq__(self, other):
        if type(other)==type(self):
            return self.value==other.value
        else:
            super(SBTNode, self).__eq__(other)
'''



'''
上述 Student 类实现了__cmp__()方法，__cmp__用实例自身self和传入的实例 s 进行比较，如果 self 应该排在
前面，就返回 -1，如果 s 应该排在前面，就返回1，如果两者相当，返回 0。 
 
Student类实现了按name进行排序： 
'''

L1 = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print (sorted(L1))

class Student(object): 
 
    def __init__(self, name, score): 
        self.name = name 
        self.score = score 
 
    def __str__(self): 
        return '(%s: %s)' % (self.name, self.score) 
 
    __repr__ = __str__
    
    def __lt__(self, s): 
        if(self.score>s.score): 
            return 1 
        elif(self.score<s.score): 
            return 0 
        else: 
            if(self.name>=s.name): 
                return 1; 
            if(self.name<s.name): 
                return 0 
            return 0 
 
L2 = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)] 
print (sorted(L2))

'''
__lt__(self, other) 
__le__(self, other) 
__eq__(self, other) 
__ne__(self, other) 
__gt__(self, other) 
__ge__(self, other) 
'''
