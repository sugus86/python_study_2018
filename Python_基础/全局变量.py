


a = 1

def test():
    global a
    a=3
    print("in test: ",a)

test()
print("out test: ",a)
