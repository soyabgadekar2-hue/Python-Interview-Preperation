def check_access(age, has_id, is_employee):

    if (age >= 18 and has_id == True) or is_employee == True:
        return "Access Granted"
    else:
        return "Access Denied"


age = int(input("Enter age: "))

has_id_input = input("Do you have ID? (yes/no): ")
is_employee_input = input("Are you an employee? (yes/no): ")

has_id = has_id_input.lower() == "yes"
is_employee = is_employee_input.lower() == "yes"

result = check_access(age, has_id, is_employee)

print(result)