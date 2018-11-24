
#在Python 2.2以前
#代码段1：
class A: 
    def __init__(self): 
        print ("enter A")
        print ("leave A")
 
class B(A): 
    def __init__(self): 
        print ("enter B")
        A.__init__(self) 
        print ("leave B")

b = B()

代码段2：
class B(C):    # A --> C 
  def __init__(self): 
   print "enter B"
 C.__init__(self) # A --> C 
   print "leave B"
   

'''
    因此，自Python 2.2开始，Python添加了一
个关键字super，来解决这个问题。下面是Python
2.3的官方文档说明：
 super(type[, object-or-type])
  Return the superclass of type. If the
second argument is omitted the super object
  returned is unbound. If the second
argument is an object, isinstance(obj, type)  
  must be true. If the second argument is a
type, issubclass(type2, type) must be  
  true. super() only works for new-style
classes.
  A typical use for calling a cooperative
superclass method is:
   class C(B): 
       def meth(self, arg): 
           super(C, self).meth(arg)
  New in version 2.2.
    
'''
#代码段3：
class A(object):    # A must be new-
style class 
  def __init__(self): 
   print "enter A" 
   print "leave A" 
 
class B(C):     # A --> C 
  def __init__(self): 
   print "enter B" 
   super(B, self).__init__() 
   print "leave B"

'''
    在我们的印象中，对于super(B,
self).__init__()是这样理解的：super(B, self)首
先找到B的父类（就是类A），然后把类B的对象
self转换为类A的对象（通过某种方式，一直没有考
究是什么方式，惭愧），然后“被转换”的类A对象调
用自己的__init__函数。考虑到super中只有指明
子类的机制，因此，在多继承的类定义中，通常我
们保留使用类似代码段1的方法。
'''
#代码段4：
class A(object): 
  def __init__(self): 
   print "enter A" 
   print "leave A" 
 
 class B(object): 
  def __init__(self): 
   print "enter B" 
   print "leave B" 
 
 class C(A): 
  def __init__(self): 
   print "enter C" 
   super(C, self).__init__() 
   print "leave C" 
 class D(A): 
  def __init__(self): 
   print "enter D" 
   super(D, self).__init__() 
   print "leave D" 
 class E(B, C): 
  def __init__(self): 
   print "enter E" 
   B.__init__(self) 
   C.__init__(self) 
   print "leave E" 
 class F(E, D): 
  def __init__(self): 
   print "enter F" 
   E.__init__(self) 
   D.__init__(self) 
   print "leave F"

 f = F()
 '''
    明显地，类A和类D的初始化函数被重复调用了
2次，这并不是我们所期望的结果！我们所期望的结
果是最多只有类A的初始化函数被调用2次——其实
这是多继承的类体系必须面对的问题。我们把代码
段4的类体系画出来，如下图：
    object 
   |       \ 
   |        A 
   |      / | 
   B  C  D 
    \   /   | 
      E    | 
        \   | 
          F

    按我们对super的理解，从图中可以看出，在
调用类C的初始化函数时，应该是调用类A的初始化
函数，但事实上却调用了类D的初始化函数。好一
个诡异的问题！
    也就是说，mro中记录了一个类的所有基类的
类类型序列。查看mro的记录，发觉包含7个元素，
7个类名分别为：
 F E B C D A object
    从而说明了为什么在C.__init__中使用
super(C, self).__init__()会调用类D的初始化函
数了。 ???
    我们把代码段4改写为：


'''

#代码段9：
class A(object): 
  def __init__(self): 
   print "enter A" 
   super(A, self).__init__()  # new 
   print "leave A" 
 
 class B(object): 
  def __init__(self): 
   print "enter B" 
   super(B, self).__init__()  # new 
   print "leave B" 
 
 class C(A): 
  def __init__(self): 
   print "enter C" 
   super(C, self).__init__() 
   print "leave C" 
 class D(A): 
  def __init__(self): 
   print "enter D" 
   super(D, self).__init__() 
   print "leave D" 
 class E(B, C): 
  def __init__(self): 
   print "enter E" 
   super(E, self).__init__()  # change 
   print "leave E" 
 class F(E, D): 
  def __init__(self): 
   print "enter F" 
   super(F, self).__init__()  # change 
   print "leave F"
f = F()

'''
    明显地，F的初始化不仅完成了所有的父类的调
用，而且保证了每一个父类的初始化函数只调用一
次。
    再看类结构：
    object 
     /   \ 
    /      A 
   |     /   \ 
  B-1  C-2   D-2 
    \   /    / 
     E-1    / 
        \  / 
          F

E-1,D-2是F的父类，其中表示E类在前，即F（E，
D）。
所以初始化顺序可以从类结构图来看出 ： F－>E-
>B -->C --> D --> A
由于C，D有同一个父类，因此会先初始化D再是
A。          

四、小结
    1. super并不是一个函数，是一个类名，形如
super(B, self)事实上调用了super类的初始化函
数， 
       产生了一个super对象； 
    2. super类的初始化函数并没有做什么特殊的
操作，只是简单记录了类类型和具体实例； 
    3. super(B, self).func的调用并不是用于调
用当前类的父类的func函数； 
    4. Python的多继承类是通过mro的方式来保
证各个父类的函数被逐一调用，而且保证每个父类
函数 
       只调用一次（如果每个类都使用super）； 
    5. 混用super类和非绑定的函数是一个危险行
为，这可能导致应该调用的父类函数没有调用或者
一个父类函数被调用多次。
'''