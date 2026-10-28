age = 67 #integer
height = 3.75 #float
greeting = "Hello" #float
isPythonInteresting = True #Boolean

#Data Structures - A single variable storing multiple values

cars = ["Toyota", "Audi", "BMW", "Mazda", "Ford", "Volvo"]#List - Ordered and character
fruits= ("Banana", "Orange", "Mango")# Tuple - ordered but uncharactered
countries = {"China", "France", "Italy", "Germany"}#Set - Unordered

#Dictionary
person = {
    "name": "Amina",
    "age": 28,
    "city": "Kisumu"
}

print(person["name"])      # Amina
person["age"] = 29         # update a value
person["job"] = "teacher"  # add a new key
del person["city"]         # remove a key

print(person["age"])
print(person["job"])

#Array
animals = ["monkey", "racoon" ,"rhino"]
print(animals[0])      # monkey
animals.append("bat")
print(len(animals))

print(cars)
print(height)
print(age)
print(countries)