num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operator"

print("Result:", result)


print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice = input("Enter your choice (1, 2, 3, 4): ")
if choice in ["1", "2", "3", "4"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print("The result is", result)

    if choice == '2':
        result = num1 - num2
        print("The result is", result)

    if choice == '3':
        result = num1 * num2
        print("The result is", result)

    if choice == '4':
        result = num1 / num2
        print("The result is", result)

