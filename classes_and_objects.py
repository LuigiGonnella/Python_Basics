#creating a class
class Person:
    def __init__(self, first_name, last_name, age): #if we put an equality, like first_name = 'Luigi' we would insert a default value
        self.first_name = first_name #attach parameter to class object
        self.last_name = last_name
        self.age = age
    def print(self): #ovverrides standard print function
        print(f'My full name is {self.first_name} {self.last_name}')
    def person_info(self):
        print(f'{self.first_name} {self.last_name} info:\n First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}')

p =  Person('Luigi', 'Gonnella', 23)
p.print()# --> My full name is Luigi Gonnella
p.person_info()

#INHERITANCE
#we can inherit all methods of a class in a son-class. In this son-class we can override the parent methods or ADD exclusive methods

class Student(Person): #Student inherits Person, Student is more specifiyng
    def __init__(self, first_name, last_name, age):
        self.marks = dict() # and add infos --> override of method
        super().__init__(first_name, last_name, age) #inherit method
        
    def add_mark(self, subject, mark): #add new method
        self.marks[subject] = mark
    def get_marks(self):
        return self.marks
    
    #the other methods are the same for both person anad student


s1 = Student('Luigi', 'Gonnella', 23)
s1.add_mark('Informatics', 30)
s1.add_mark('Software Engineering', 30)
s1.add_mark('Formal Languages', 29)

s1.person_info()
s1.print()
print(s1.get_marks())