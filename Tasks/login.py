def login(username, password):

    if username == "admin" and password == "Python123":
        return "Valid User"
    else:
        return "Invalid User"


username = input("Enter username: ")
password = input("Enter password: ")

result = login(username, password)

print(result)