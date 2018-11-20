
str1 = "abc"
num = 123

#格式化输出
a="%s%d" % (str1,num)
print(a)


a="%5s%d" % (str1,num)
print(a)


a="%-5s%d" % (str1,num)
print(a)


#用+进行字符串的合并：

str1="hello"
str2="world"
result=str1+str2

#通过切片截取字符串：

word="world"
print(word[0:3])
