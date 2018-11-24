

class Rational1(object): 
    def __init__(self, p, q): 
        self.p = p 
        self.q = q 
    def __add__(self, r):
        print("r:%s"%r)
        print("p:%s, q:%s"%(self.p,self.q))
        return Rational1(self.p * r.q + self.q * r.p, self.q * r.q) 
    def __str__(self): 
        return '%s/%s' % (self.p, self.q) 
    __repr__ = __str__
    

r1 = Rational1(1, 3)
r2 = Rational1(1, 2)
print(r1,r2)

print(r1 + r2)


'''
def gcd(a,b): 
    if(b==0): 
        return a 
    return gcd(b,a%b) 
class Rational2(object): 
    def __init__(self, p, q): 
        self.p = p 
        self.q = q 
 
    def __add__(self, r): 
        return Rational2(self.p * r.q + self.q * r.p, self.q * r.q) 
 
    def __sub__(self, r): 
        return Rational2(self.p * r.q - self.q * r.p, self.q * r.q)
        
    def __mul__(self, r): 
        return Rational2(self.p * r.p, self.q * r.q) 
 
    def __div__(self, r): 
        return Rational2(self.p*r.q,self.q*r.p) 
 
    def __str__(self): 
        g=gcd(self.p,self.q) 
        return '(%d/%d)' %(self.p/g,self.q/g) 
 
    __repr__ = __str__

r1 = Rational2(1, 2)
r2 = Rational2(1, 4)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)
'''