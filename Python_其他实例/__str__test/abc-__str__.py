'''
class a:
    def __init__(self):
        self.b = "b"

    def __str__(self):
        c = "c"
        return c
      

aa = a()
print aa
'''

class Friend():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Friend : %s" % self.name

    def show(self):
        print str(self)
        
'''
if __name__ == '__main__':
    friend = Friend('Li')
    print friend
'''

