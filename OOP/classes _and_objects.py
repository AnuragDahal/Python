''' Class:- Class is a blueprint or a template for creating objects
providing initial values for state(member variables or attributes) and implementation of behaviour
(member functions or methods).'''

# Creating a class

class Student():
    name=""#name,age and address are properties of class Student
    age=""#default value can also be assigned to attrributes in class
    Address=""
    def info(self):#Assigning Method to class
        print(f'{self.name} is of {self.age} and is from {self.Address}')

'''Object:- Object is an instance used to access the properties of class'''
#Creating an object 

a=Student()
a.name="Anurag Dahal"
a.age=20
a.Address="Birtamode"
a.info()

# other name and datas can also be assigned to same class

b=Student()
b.name="Swikriti Sigdel"
b.age=19
b.address="Jhapa"
b.info()
a.info()