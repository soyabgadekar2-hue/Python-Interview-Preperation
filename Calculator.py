a = int(input("Enter a number: ")) 
b = int(input("Enter another number: ")) 
Operation = input("Enter an operator (+, -, *, /,//,** ): ") 

match (Operation): 
    case "+": 
        result = a + b 
        print(f"The result of {a} + {b} is: {result}") 
    case "-": 
        result = a - b 
        print(f"The result of {a} - {b} is: {result}") 
    case "*": 
        result = a * b 
        print(f"The result of {a} * {b} is: {result}") 
    case "/": 
        if b != 0: 
            result = a / b 
            print(f"The result of {a} / {b} is: {result}") 
        else: 
            print("Error: Division by zero is not allowed.") 
    case "//": 
        if b != 0: 
            result = a // b 
            print(f"The result of {a} // {b} is: {result}") 
        else: 
            print("Error: Division by zero is not allowed.") 
    case "**": 
        result = a ** b 
        print(f"The result of {a} ** {b} is: {result}") 
    case _: 
        print("Invalid operator. Please use +, -, *, /, //, or **.")
