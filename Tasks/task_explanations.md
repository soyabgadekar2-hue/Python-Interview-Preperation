# Python Functions and Operators — 10 Practice Tasks

These 10 tasks practice:

* Functions
* Parameters and arguments
* `return`
* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Membership operators
* `if`, `elif`, `else`
* Boolean values
* Multiple return values

---

# Task 1 — Calculator

## Requirement

Create a calculator that performs:

* Addition
* Subtraction
* Multiplication
* Division
* Floor Division
* Remainder

## Operators Used

```text
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Remainder
```

## Code

```python
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
```

## Explanation

### Step 1 — Create the function

```python
def calculator(a, b):
```

`def` is used to create a function.

`calculator` is the function name.

`a` and `b` are parameters.

The function needs two numbers to perform calculations.

---

### Step 2 — Addition

```python
a + b
```

The `+` operator adds two numbers.

Example:

```text
10 + 5 = 15
```

---

### Step 3 — Subtraction

```python
a - b
```

The `-` operator subtracts the second number from the first.

```text
10 - 5 = 5
```

---

### Step 4 — Multiplication

```python
a * b
```

The `*` operator multiplies two numbers.

```text
10 * 5 = 50
```

---

### Step 5 — Division

```python
a / b
```

The `/` operator performs normal division.

```text
10 / 5 = 2.0
```

Python normally returns a floating-point value for `/`.

---

### Step 6 — Floor Division

```python
a // b
```

`//` performs floor division.

Example:

```text
10 // 3 = 3
```

Normal division:

```text
10 / 3 = 3.333...
```

Floor division gives:

```text
3
```

---

### Step 7 — Remainder

```python
a % b
```

`%` returns the remainder after division.

Example:

```text
10 % 3 = 1
```

Because:

```text
3 × 3 = 9
10 - 9 = 1
```

---

### Step 8 — Division by zero

```python
if b != 0:
```

`!=` means "not equal to".

We check that `b` is not zero before performing division.

This prevents:

```text
10 / 0
```

which causes an error.

---

# Task 2 — Check Even/Odd and Divisibility

## Requirement

Create a function that accepts an integer and determines:

* Whether the number is even or odd
* Whether it is divisible by 3
* Whether it is divisible by 5

## Code

```python
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
```

## Explanation

The important operator in this task is:

```python
%
```

It is called the **modulus/remainder operator**.

### Checking even number

```python
number % 2 == 0
```

If the remainder after dividing by 2 is zero, the number is even.

Example:

```text
10 % 2 = 0
```

Therefore:

```text
10 is even
```

But:

```text
11 % 2 = 1
```

Therefore:

```text
11 is odd
```

---

### Checking divisibility by 3

```python
number % 3 == 0
```

If the remainder is zero, the number is divisible by 3.

Example:

```text
15 % 3 = 0
```

Therefore:

```text
15 is divisible by 3
```

---

### Checking divisibility by 5

```python
number % 5 == 0
```

Example:

```text
20 % 5 = 0
```

Therefore:

```text
20 is divisible by 5
```

---

# Task 3 — Student Marks

## Requirement

Create a function that accepts student marks and returns:

* `Distinction` if marks are `>= 75`
* `Pass` if marks are `>= 35`
* `Fail` otherwise

## Code

```python
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
```

## Explanation

### Why check `75` first?

Consider:

```text
marks = 80
```

80 satisfies:

```python
marks >= 35
```

but it should be classified as:

```text
Distinction
```

Therefore we check the higher condition first:

```python
if marks >= 75:
```

Then:

```python
elif marks >= 35:
```

Finally:

```python
else:
```

handles everything below 35.

### Decision flow

```text
Marks
  |
  |-- >= 75 --> Distinction
  |
  |-- >= 35 --> Pass
  |
  |-- otherwise --> Fail
```

### Example

```text
Marks = 85
Result = Distinction

Marks = 60
Result = Pass

Marks = 20
Result = Fail
```

---

# Task 4 — Student Eligibility

## Requirement

A student is eligible only when:

```text
Marks >= 60
Attendance >= 75
Backlog == False
```

All three conditions must be true.

## Code

```python
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
```

## Explanation

This task introduces the logical operator:

```python
and
```

`and` means **all conditions must be true**.

The main condition is:

```python
marks >= 60 and attendance >= 75 and backlog == False
```

Think of it as three questions:

```text
Are marks >= 60?
       AND
Is attendance >= 75?
       AND
Is backlog False?
```

Only if all answers are `True` does the student become eligible.

### Example 1

```text
Marks = 70
Attendance = 80
Backlog = False
```

All conditions are true.

```text
Eligible
```

### Example 2

```text
Marks = 70
Attendance = 60
Backlog = False
```

Attendance is below 75.

```text
Not Eligible
```

### Example 3

```text
Marks = 70
Attendance = 80
Backlog = True
```

Student has a backlog.

```text
Not Eligible
```

---

# Task 5 — Username and Password

## Requirement

A user is valid only when:

```text
username == "admin"
AND
password == "Pyhton123"
```

## Code

```python
def login(username, password):

    if username == "admin" and password == "Pyhton123":
        return "Valid User"
    else:
        return "Invalid User"


username = input("Enter username: ")
password = input("Enter password: ")

result = login(username, password)

print(result)
```

## Explanation

The function accepts two parameters:

```python
username
password
```

The condition is:

```python
username == "admin" and password == "Pyhton123"
```

`==` means **equal to**.

`and` means **both conditions must be true**.

### Valid login

```text
username = admin
password = Pyhton123
```

Both match.

```text
Valid User
```

### Invalid login

```text
username = admin
password = abc123
```

The password doesn't match.

```text
Invalid User
```

### Important

`=` and `==` are different.

```python
=
```

means assignment.

```python
==
```

means comparison.

Example:

```python
username = "admin"
```

assigns a value.

```python
username == "admin"
```

checks whether the value is equal.

---

# Task 6 — Purchase Discount

## Requirement

Apply discounts according to purchase amount:

| Purchase Amount | Discount |
| --------------- | -------: |
| ₹5000 or more   |      20% |
| ₹300 to ₹4999   |      10% |
| Below ₹300      |       5% |

Return:

* Discount amount
* Final payable amount

## Code

```python
def calculate_discount(amount):

    if amount >= 5000:
        discount_percentage = 20

    elif amount >= 300:
        discount_percentage = 10

    else:
        discount_percentage = 5


    discount_amount = amount * discount_percentage / 100

    final_amount = amount - discount_amount

    return discount_amount, final_amount


amount = float(input("Enter purchase amount: "))

discount, final_amount = calculate_discount(amount)

print("Discount amount:", discount)
print("Final payable amount:", final_amount)
```

## Explanation

### Step 1 — Check purchase amount

```python
if amount >= 5000:
    discount_percentage = 20
```

If amount is ₹5000 or more, discount is 20%.

---

### Step 2 — Check ₹300 to ₹4999

```python
elif amount >= 300:
    discount_percentage = 10
```

This condition is checked only if the first condition was false.

So the amount is between ₹300 and ₹4999.

---

### Step 3 — Below ₹300

```python
else:
    discount_percentage = 5
```

Anything below ₹300 gets 5%.

---

### Step 4 — Calculate discount

```python
discount_amount = amount * discount_percentage / 100
```

Example:

```text
Amount = 6000
Discount = 20%
```

Calculation:

```text
6000 × 20 / 100
= 1200
```

Discount amount:

```text
₹1200
```

---

### Step 5 — Calculate final amount

```python
final_amount = amount - discount_amount
```

```text
6000 - 1200 = 4800
```

Final payable amount:

```text
₹4800
```

---

### Step 6 — Multiple return values

The function returns:

```python
return discount_amount, final_amount
```

So two values are returned.

They are received here:

```python
discount, final_amount = calculate_discount(amount)
```

The first returned value goes into `discount`.

The second returned value goes into `final_amount`.

---

# Task 7 — Access Control

## Requirement

Access should be granted when:

```text
Age >= 18 AND has_id == True
```

OR:

```text
is_employee == True
```

## Code

```python
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
```

## Explanation

This task uses both:

```python
and
or
```

The condition is:

```python
(age >= 18 and has_id == True) or is_employee == True
```

### `and`

Both conditions on its side must be true:

```python
age >= 18 and has_id == True
```

### `or`

At least one side must be true:

```python
(condition1) or condition2
```

### Example 1

```text
Age = 20
Has ID = True
Employee = False
```

First part is true:

```text
20 >= 18 → True
has_id → True
```

Therefore access is granted.

---

### Example 2

```text
Age = 16
Has ID = False
Employee = True
```

The first part is false.

But:

```text
is_employee == True
```

is true.

Because `or` needs only one side to be true:

```text
Access Granted
```

---

### Why use parentheses?

```python
(age >= 18 and has_id == True) or is_employee == True
```

The parentheses make it easier to understand that:

```text
age + ID
```

form one group, which is then combined with the employee condition.

---

# Task 8 — Membership Operator

## Requirement

Create a list:

```python
["python", "Sql", "Git", "Html"]
```

Create a function that accepts a skill and checks whether it exists in the list.

## Code

```python
required_skills = ["python", "Sql", "Git", "Html"]


def check_skill(skill):

    if skill in required_skills:
        return "Skill Available"
    else:
        return "Skill Not Available"


skill = input("Enter a skill: ")

result = check_skill(skill)

print(result)
```

## Explanation

The list contains:

```python
required_skills = ["python", "Sql", "Git", "Html"]
```

The operator:

```python
in
```

is a **membership operator**.

It checks whether a value exists inside a collection.

Example:

```python
"python" in required_skills
```

Result:

```text
True
```

But:

```python
"Java" in required_skills
```

Result:

```text
False
```

### `not in`

Python also has:

```python
not in
```

Example:

```python
"Java" not in required_skills
```

This returns:

```text
True
```

because Java is not in the list.

### Important

Membership checking is generally case-sensitive.

For example:

```python
"python" in required_skills
```

is `True`.

But:

```python
"Python" in required_skills
```

is `False` because `"python"` and `"Python"` are different strings.

---

# Task 9 — Calculator With Operator Selection

## Requirement

Create a function that accepts:

```text
a
b
operator
```

The function should support:

```text
+
-
*
/
//
//%
**
```

It should also:

* Handle invalid operators
* Handle division by zero

## Code

```python
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
```

## Explanation

The function receives three values:

```python
def calculator(a, b, operator):
```

For example:

```python
calculator(10, 5, "+")
```

means:

```text
a = 10
b = 5
operator = "+"
```

The program then checks which operator was entered.

---

### Addition

```python
if operator == "+":
    return a + b
```

If the operator is `+`, addition is performed.

---

### Subtraction

```python
elif operator == "-":
    return a - b
```

---

### Multiplication

```python
elif operator == "*":
    return a * b
```

---

### Division

```python
elif operator == "/":
```

Before dividing, we check:

```python
if b == 0:
```

If `b` is zero, return an error message.

Otherwise:

```python
return a / b
```

---

### Floor Division

```python
return a // b
```

Example:

```text
10 // 3 = 3
```

---

### Remainder

```python
return a % b
```

Example:

```text
10 % 3 = 1
```

---

### Power

```python
return a ** b
```

Example:

```text
2 ** 3 = 8
```

---

### Invalid operator

The final:

```python
else:
    return "Invalid operator"
```

handles anything that wasn't supported.

For example:

```text
@
&
$
```

would produce:

```text
Invalid operator
```

---

# Task 10 — Placement Eligibility

## Requirement

A candidate is placement eligible when:

```text
Marks >= 60
AND
Attendance >= 75
AND
No backlog
```

Then determine candidate category based on experience:

```text
0 years       → Fresher
1–2 years     → Junior
More than 2   → Experienced
```

Finally display:

```text
Placement Eligible: Yes/No
Candidate Category: Fresher/Junior/Experienced
```

## Code

```python
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
```

## Explanation

### Step 1 — Function parameters

```python
def placement_eligibility(age, marks, attendance, experience, has_backlog):
```

The function accepts five parameters:

```text
age
marks
attendance
experience
has_backlog
```

In the current requirements, `age` is accepted but **not used in the eligibility condition** because no age requirement was specified.

---

### Step 2 — Check placement eligibility

```python
if marks >= 60 and attendance >= 75 and has_backlog == False:
```

There are three conditions.

#### Condition 1

```python
marks >= 60
```

Marks must be at least 60.

#### Condition 2

```python
attendance >= 75
```

Attendance must be at least 75%.

#### Condition 3

```python
has_backlog == False
```

The candidate must not have a backlog.

Because `and` is used, all three conditions must be true.

---

### Step 3 — Store eligibility

If all conditions are true:

```python
eligible = "Yes"
```

Otherwise:

```python
eligible = "No"
```

---

### Step 4 — Determine experience category

If experience is exactly zero:

```python
if experience == 0:
    category = "Fresher"
```

If experience is 1 or 2:

```python
elif experience <= 2:
    category = "Junior"
```

Otherwise:

```python
else:
    category = "Experienced"
```

### Decision flow

```text
Experience
    |
    |-- 0 ------> Fresher
    |
    |-- 1–2 ----> Junior
    |
    |-- >2 -----> Experienced
```

---

### Step 5 — Return two values

```python
return eligible, category
```

The function returns two values.

For example:

```text
("Yes", "Junior")
```

They are received using:

```python
eligible, category = placement_eligibility(...)
```

So:

```text
eligible → "Yes"
category → "Junior"
```

---

# Important Concepts Used Across All 10 Tasks

## 1. `def`

Used to define a function.

```python
def add(a, b):
```

---

## 2. Parameters

Variables inside the function definition.

```python
def add(a, b):
```

Here `a` and `b` are parameters.

---

## 3. Arguments

Actual values passed to a function.

```python
add(10, 20)
```

Here `10` and `20` are arguments.

---

## 4. `return`

Sends a result back from the function.

```python
def add(a, b):
    return a + b
```

---

## 5. `if`

Checks a condition.

```python
if marks >= 60:
```

---

## 6. `elif`

Checks another condition if the previous `if` condition was false.

```python
if marks >= 75:
    ...
elif marks >= 35:
    ...
```

---

## 7. `else`

Runs when all previous conditions are false.

```python
if marks >= 35:
    ...
else:
    ...
```

---

## 8. Comparison Operators

Used to compare values.

```text
==    Equal
!=    Not equal
>     Greater than
<     Less than
>=    Greater than or equal
<=    Less than or equal
```

Example:

```python
marks >= 60
```

---

## 9. Logical Operators

### `and`

All conditions must be true.

```python
marks >= 60 and attendance >= 75
```

### `or`

At least one condition must be true.

```python
age >= 18 or is_employee == True
```

### `not`

Reverses a Boolean value.

```python
not is_logged_in
```

---

## 10. Arithmetic Operators

```text
+     Addition
-     Subtraction
*     Multiplication
/     Division
//    Floor Division
%     Remainder
**    Power
```

---

## 11. Membership Operators

```python
in
not in
```

Example:

```python
"Python" in skills
```

Checks whether `"Python"` exists in the collection.

---

## 12. Boolean Values

Python has two Boolean values:

```python
True
False
```

Example:

```python
has_backlog = False
```

Then:

```python
has_backlog == False
```

checks whether the variable contains `False`.

---

# Overall Pattern

Most of these tasks follow the same programming structure:

```text
Take Input
    ↓
Call Function
    ↓
Function receives Parameters
    ↓
Use Operators
    ↓
Check Conditions
    ↓
Calculate / Decide
    ↓
Return Result
    ↓
Print Result
```

For example:

```python
def add(a, b):
    return a + b
```

The complete flow is:

```text
10, 20
  ↓
a = 10, b = 20
  ↓
a + b
  ↓
30
  ↓
return 30
  ↓
result = 30
```

# Main Things to Remember

1. **Function** → reusable block of code.
2. **Parameter** → variable received by a function.
3. **Argument** → actual value passed to a function.
4. **`return`** → sends a result back.
5. **`if`** → checks a condition.
6. **`elif`** → checks another condition.
7. **`else`** → handles the remaining cases.
8. **`and`** → all conditions must be true.
9. **`or`** → at least one condition must be true.
10. **`%`** → gives the remainder.
11. **`in`** → checks membership.
12. **`==`** → compares values.
13. **`=`** → assigns a value.
14. **Multiple return values** can be received using multiple variables.

These 10 tasks are essentially exercises for learning how to combine **functions, operators, conditions, inputs, and return values** to solve small real-world programming problems.
