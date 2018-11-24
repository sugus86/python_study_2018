
1.getattr（）：python自省函数，用于查看某对象是否具有某种属性并返回属性值或者末字符串，参数格式（一
个对象， 属性名称字符串， 不存在时输出的字符串），举个例子：
1 class A: 
2     def __init__(self): 
3         self.name = 'hahahaha' 
4 a = A() 
5 print getattr(a, 'name', 'nonono')   
6 #如果有name属性打印name值，如果没有打印nonono

2.globals（）：python自省函数，以字典形式列出所有的全局变量，对应的函数是locals（）-作用是以字典形式
列出函数内所有的局部变量
3.hex（）：参数格式为数字，作用是将数字转换为十六进制，返回值带十六进制标识0x，格式为字符串
4.id（）：Cpython中对象的内存地址
5.int（）：可以将字符串转换为整数，同时可设置以何种进制转换，默认是十进制，举个例子：
int ('13')  #以十进制输出13 
int ('13', base=5)  #输出5进制13的值，即为8 
int ('ff', base=16)  #输出16进制的ff的值，即为255
6.issubclass(A, B)：判断A是不是B的子类，实际上是指同一个模块下的类，而不是不同模块下的类。
7.filter(A, B)把传入的函数A依次作用于B中的每个元素，然后根据返回值是True还是False决定保留还是丢弃该元
素。
1 def is_odd(n): 
2     #只返回奇数 
3     return n % 2 == 1 
4   
5 filter(is_odd, [1, 2, 4, 5, 6, 9]) 
6 # 结果: [1, 5, 9]
8.map（A， B）把传入的函数A依次作用于B中的每个元素，将结果输出，看一个例子分别map和filter：
1 def ixii(x): 
2     return x != 10 
3 list1 = [1, 2, 4, 10, 20] 
4 print filter(ixii, list1) 
5 # 输出为[1, 2, 4, 20] 
6 print map(ixii, list1) 
7 # 输出为[True, True, True, False, True]
由此可知，map返回值为return的值，而filter会根据返回的布尔值去除false所对应的项，输出为处理后的列表
9.reduce（）：他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数
func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函
数运算，最后得到一个结果。这么说有点绕口，看以下俩个例子就可以明白了：
1 a = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
2 # 该操作等价于下方表达式 
3 a = ((((1+2)+3)+4)+5)
1 a = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5],6) 
2 # 等价于： 
3 a = (((((6+1)+2)+3)+4)+5)