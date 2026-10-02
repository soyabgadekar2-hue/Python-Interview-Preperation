def check_number(number):

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    if number % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not divisible by 3")

    if number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")


number = int(input("Enter a number: "))

check_number(number)