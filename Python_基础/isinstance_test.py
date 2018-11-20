
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score

class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.cource = course
        
p = Person("Tim","Male")
s = Student("Bob","Male",88)
t = Teacher("Alice","Female","English")
print("#"*80)
print(isinstance(p,Person))
print(isinstance(p,Student))
print(isinstance(p,Teacher))
print("#"*80)
print(isinstance(s, Person))
print(isinstance(s, Student))
print(isinstance(s, Teacher))
print("#"*80)
print(isinstance(t, Person))
print(isinstance(t, Student))
print(isinstance(t, Teacher))
print(isinstance(t, object))   
print("#"*80)
