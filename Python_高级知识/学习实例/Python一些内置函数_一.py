

1.divmod（a，b）：取a除以b的商和余数，功效等价于（a//b, a%b）;
2.dir()：参数为函数名，类名。它会告诉我们对应函数包含有什么参数
3.enumerate：遍历列表时同时生成了序号,举个例子：
1 a = [1, 2, 3] 
2 for index,item in enumerate(a): 
3     print index 
4     print item
4.complex：处理python中的复数，比如complex（2, 3）-->2+3j；complex（2+3j）-->2+3j注意这个地方括号里
的表达式是不能有空格的！！
5.cmp(x,y)： 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
6.chr(i)：返回整数i对应的ASCII字符。与ord()作用相反。
7.isinstance（a,obj）:用于判断某一对象类型，意思大约是a是否是obj类型；在这里要注意type函数，它俩最重
要的一个区别为:type只能对类型作直接判断，而isinstance功能    比type更强，可以对子类

8. any和all：any与all()函数的区别，any是任意，而all是全部。any---->如果iterable的任何元素不为0、''、
False,all(iterable)返回True。如果iterable为空，返回False。函数等价于：
def any(iterable):  
    for element in iterable: 
        if  element: 
            return False 
    return True
 
 
然而all---->如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；函
数等价于：

1 def all(iterable): 
2     for element in iterable: 
3         if not element: 
4             return False 
5     return True
9.__doc__：python函数描述文档字符串，print（function.__doc__），输出的是function函数中使用三引号括起
来的描述。
10.eval：将字符串str当成有效的表达式来求值并返回计算结果。还可以执行字符串代码
11：exec，execfile，exec语句用来执行储存在字符串或文件中的Python语句；execfile(filename [,globals
[,locals ]])函数可以用来执行一个文件。
12：format----->python格式化内置函数，网上找到的用法:

1 age = 25   
2 name = 'Caroline'   
3 def test:       
4     print '{0} is {1} years old. '.format(name, age) # 输出参数   
5     print '{0} is a girl. '.format(name) 
6     print '{0:.3} is a decimal. '.format(1/3) # 小数点后三位   
7     print '{0:_^11} is a 11 length. '.format(name)  # 使用_补齐空位   
8     # 别名替换   
9     print '{first} is as {second}. '.format(first=name, second='Wendy') 
10     print 'My name is {0.name}'.format(open('out.txt', 'w')) # 调用方法   
11     print 'My name is {0:8}.'.format('Fred') # 指定宽度  