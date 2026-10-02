def check_eligibility(marks, attendance, backlog):

    if marks >= 60 and attendance >= 75 and backlog == False:
        return "Eligible"
    else:
        return "Not Eligible"


marks = int(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

backlog_input = input("Do you have a backlog? (yes/no): ")

if backlog_input.lower() == "yes":
    backlog = True
else:
    backlog = False

result = check_eligibility(marks, attendance, backlog)

print("Student is:", result)