
def f1(a,b,c,*d, e,f):
    localvar = 1
    x = '123'

print('co_argcount:' ,f1.__code__.co_argcount)                  #位置参数个数(a,b,c)
print('co_kwonlyargcount:',f1.__code__.co_kwonlyargcount)      #关键字参数个数(e,f)
print('all_local:',f1.__code__.co_nlocals)                          #函数中局部参数(位置参数+关键字+可变参数(*d) + 本地变量)
print('consts:',f1.__code__.co_consts)                          #函数内部的常量
print('filename:',f1.__code__.co_filename)                      #函数所属的文件
print('name:',f1.__code__.co_name)                              #函数名
print('函数在第几行:',f1.__code__.co_firstlineno)


'''
--------------------- 
作者：dashoumeixi 
来源：CSDN 
原文：https://blog.csdn.net/dashoumeixi/article/details/80765610 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''