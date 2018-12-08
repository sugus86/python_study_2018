'''
class b:
    def __init__(self):
        print 'b'
        
class a(b):
    def __init__(self):
        super(type(a), self).__init__()
        print 'a'
'''


class A(object):    # A must be new-style class, without object failed
  def __init__(self):
   print "enter A"
   print "leave A"

class B(A):     # A --> C
  def __init__(self):
   print "enter B"
   super(B, self).__init__()
   print "leave B"

