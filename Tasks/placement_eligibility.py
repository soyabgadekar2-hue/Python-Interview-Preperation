def placement_eligibility(age, marks, attendance, experience, has_backlog):

    if marks >= 60 and attendance >= 75 and has_backlog == False:
        eligible = "Yes"
    else:
        eligible = "No"

    if experience == 0:
        category = "Fresher"
    elif experience <= 2:
        category = "Junior"
    else:
        category = "Experienced"

    return eligible, category


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = int(input("Enter years of experience: "))

backlog_input = input("Do you have backlog? (yes/no): ")
has_backlog = backlog_input.lower() == "yes"

eligible, category = placement_eligibility(
    age,
    marks,
    attendance,
    experience,
    has_backlog
)

print("Placement Eligible:", eligible)
print("Candidate Category:", category)