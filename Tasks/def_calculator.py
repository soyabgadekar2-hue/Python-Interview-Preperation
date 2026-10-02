def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Remainder:", a % b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:
    calculator(a, b)
else:
    print("Division by zero is not allowed.")