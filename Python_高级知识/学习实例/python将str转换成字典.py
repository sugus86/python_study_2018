

#典型的应用场景：Json数据的解析

user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
b=eval(user)
print(b)

exec("c="+user)
print(c)