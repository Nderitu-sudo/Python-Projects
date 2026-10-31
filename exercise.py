# 1.using the built-in max() function
numbers = [12 ,53,76, 23,98, 45]
print(max(numbers))

# 2. using a loop
numbers = [12 ,53,76, 23,98, 45]

largest = numbers[0]  # assume the first is the largest no.

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is: ", largest)


#finding the smallest no.
numbers = [12 ,53,76, 23,98, 45]

smallest = numbers[4]  # assume the first is the largest no.

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is: ", smallest)

def number():
    num1 = float(input("Enter first number: "))
    num2 = float(input( "Enter second number: "))
    num3 = float(input("Enter third number: "))

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print("Largest number is:", largest)


number()


