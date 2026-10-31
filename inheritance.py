
#Parent Class/Super Class/Base Class
class Animal:

    isMammal = True
    age = 3

    def movement(self):
        print("Animal is moving")

#Child class
class Dog(Animal): # By adding animal in brackets, it shows that class dog has inherited the attributes of class anima
    def bark(self):
        print("Woof!! Woof!! Woof!!")

 #Child Class/Sub-Class/Derived Class
class Cat(Animal):
    def meow(self):
        print("Meow!! Meow!! Meow!!")

 dog1 = Dog()
dog1.movement()
print(dog1.movement())

cat1 = Cat()
cat1.meow()



