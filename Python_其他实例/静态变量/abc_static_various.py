class A:
    a1 = 10
    def __init__(self):
        self.a2 = 5

A.a1= 30
A.a2= 15

aa=A()
ab=A()

print (aa.a1, aa.a2)
print (ab.a1, ab.a2)

aa.a1 = 45
aa.a2 = 55

print (aa.a1, aa.a2)
print (ab.a1, ab.a2)