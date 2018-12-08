class MyProperty(object) :
        def __init__(self, method) :
                self.method = method
                self.method_dict = self.method()
 
        def __get__(self, obj, type=None) :
                return self.method_dict['fget'](obj)
 
        def __set__(self, obj, val) :
                self.method_dict['fset'](obj, val)
 
class Test(object) :
        def __init__(self, x) :
                self.__x = x
 
        @MyProperty
        def x() :
                def fget(self) :
                        return self.__x
 
                def fset(self, val) :
                        assert isinstance(val, int), 'val must be an integer!'
                        self.__x = val
 
                return locals()
 
t = Test(5)
print t.x
t.x = 10
print t.x
 
# 5
# 10
 