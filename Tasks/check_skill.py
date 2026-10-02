required_skills = ["python", "Sql", "Git", "Html"]


def check_skill(skill):

    if skill in required_skills:
        return "Skill Available"
    else:
        return "Skill Not Available"


skill = input("Enter a skill: ")

result = check_skill(skill)

print(result)