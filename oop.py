# Class is a blueprint of an object.
# Object is an instance of a class

class Employee:

    def __init__(self, name, gender, position,age):
      self.name = name
      self.gender = gender
      self.position = position
      self.age = age

    def drive(self):
        print("Employee is driving")

    def eat(self):
        print("Employee is eating")



employee1 = Employee(name:"Mark",gender:"Male", position:"CEO", age:67) #Creating an object
print(employee1.name, employee1.gender. employee1.position)
employee1.drive()

employee2 = Employee(name:"Jane", gender:"Female",position:"Admin", age:25)
print(employee2.name, employee2.gender. employee2.position)
employee2.drive()
employee2.eat()

employee3 = Employee(name:"Anita", gender:"Female", position:"HR", age:43)

