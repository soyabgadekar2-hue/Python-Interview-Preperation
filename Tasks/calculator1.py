def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    elif operator == "//":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a // b

    elif operator == "%":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a % b

    elif operator == "**":
        return a ** b

    else:
        return "Invalid operator"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")

result = calculator(a, b, operator)

print("Result:", result)