def check_result(marks):

    if marks >= 75:
        return "Distinction"
    elif marks >= 35:
        return "Pass"
    else:
        return "Fail"


marks = int(input("Enter marks: "))

result = check_result(marks)

print("Result:", result)