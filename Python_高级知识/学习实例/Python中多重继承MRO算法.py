import inspect

class A:   # 是没有继承任何父类的
    def __init__(self):
        print ("这是经典类")
        
print(inspect.getmro(A))


class D:
    pass
 
class C(D):
    pass
 
class B(D):
    pass
 
class A(B,C):
    pass
 
if __name__ == '__main__':
    print (inspect.getmro(A))

class A1(object):   # 继承于object
    def __init__(self):
        print("这是新式类")
        
print(A1.__mro__)

class D(object):
    pass
 
class E(object):
    pass
 
class F(object):
    pass
 
class C(D, F):
    pass
 
class B(E, D):
    pass
 
class A2(B, C):
    pass
 
if __name__ == '__main__':
    print("#"*80)
    print (A2.__mro__)