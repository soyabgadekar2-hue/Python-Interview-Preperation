# 07_Python_Practice_Tasks.md

# Python Practice Tasks — Beginner to Interview

This file contains practical Python problems to apply the concepts learned in the previous files.

The tasks progress from:

```text
Beginner
   ↓
Basic Logic
   ↓
Functions
   ↓
Operators
   ↓
Control Flow
   ↓
Intermediate Practice
   ↓
Interview Challenge
```

---

# 1. How to Practice

For every problem, follow this process:

```text
1. Understand the problem
2. Identify the input
3. Identify the expected output
4. Decide which Python concept is required
5. Write the logic
6. Write the code
7. Test with different inputs
8. Explain your solution in your own words
```

Do not immediately look at the solution.

Try solving each task yourself first.

---

# 2. Basic Calculator

## Task

Write a program that accepts two numbers and displays:

* Addition
* Subtraction
* Multiplication
* Division
* Floor division
* Modulus
* Exponentiation

### Example

```text
Input:
10
3

Output:
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

### Concepts

```text
Input
Variables
Arithmetic operators
Output
```

---

# 3. Number Properties

## Task

Accept an integer and determine whether it is:

* Positive
* Negative
* Zero
* Even
* Odd

### Example

```text
Input: 10

Output:
Positive
Even
```

### Concepts

```text
if
elif
else
%
```

---

# 4. Marks and Grade

## Task

Accept marks and display the grade:

```text
90 or above → A+
75–89       → A
60–74       → B
40–59       → C
Below 40    → F
```

Also reject marks outside the valid range:

```text
0–100
```

### Example

```text
Input: 82
Output: Grade A
```

### Concepts

```text
if
elif
else
comparison operators
```

---

# 5. Login Validation

## Task

Create a simple login program.

Use:

```python
username = "soyab"
password = "python123"
```

Ask the user for their username and password.

Display:

```text
Login successful
```

or:

```text
Invalid username or password
```

### Concepts

```text
input()
==
and
if-else
```

---

# 6. Discount Calculator

## Task

Create a program that calculates a discount based on purchase amount.

Use:

```text
5000 or more → 20%
2000–4999    → 10%
Below 2000   → 0%
```

Display:

* Original amount
* Discount percentage
* Discount amount
* Final amount

### Example

```text
Input:
2500

Output:
Discount: 10%
```

### Concepts

```text
if-elif-else
arithmetic operators
variables
```

---

# 7. Access Control

## Task

A person can access a system only if:

```text
Age >= 18
AND
Has valid ID
```

Create a program that checks both conditions.

### Example

```text
Age: 21
Has ID: yes

Output:
Access allowed
```

### Concepts

```text
and
if-else
Boolean values
```

---

# 8. Check Required Skill

## Task

Given:

```python
skills = ["Python", "HTML", "CSS", "JavaScript"]
```

Check whether the user has Python.

### Expected output

```text
Python skill found
```

### Concepts

```text
list
in
if-else
```

---

# 9. Placement Eligibility

## Task

A student is eligible for placement if:

```text
Percentage >= 60
AND
No backlog
```

Ask the user for:

* Percentage
* Backlog status

Display the result.

### Example

```text
Percentage: 72
Backlog: no

Output:
Eligible for placement
```

---

# 10. Electricity Bill

## Task

Create a simple electricity bill calculator.

Use these practice rates:

```text
First 100 units → ₹2 per unit
Next 100 units  → ₹3 per unit
Above 200       → ₹5 per unit
```

### Example

```text
Input:
120

Output:
Bill: ₹260
```

This is a programming exercise; actual electricity tariffs can use different slabs and rules.

---

# 11. Operation-Choice Calculator

## Task

Create a calculator where the user chooses an operation.

Example:

```text
1. Addition
2. Subtraction
3. Multiplication
4. Division
```

Input:

```text
Enter first number: 10
Enter second number: 5
Enter choice: 1
```

Output:

```text
Result: 15
```

### Concepts

```text
input
if-elif-else
arithmetic operators
```

---

# 12. Print Even Numbers

## Task

Print all even numbers from 1 to 20.

Expected:

```text
2
4
6
8
10
12
14
16
18
20
```

### Concepts

```text
for
range()
%
```

---

# 13. Sum of Numbers

## Task

Find the sum of numbers from 1 to 100.

Expected:

```text
5050
```

### Concepts

```text
for
range()
accumulator variable
+=
```

---

# 14. Find the Largest Number

## Task

Given:

```python
numbers = [10, 25, 7, 42, 18]
```

Find the largest number without using:

```python
max()
```

Expected:

```text
42
```

### Concepts

```text
list
for
if
comparison
```

---

# 15. Factorial Using a Loop

## Task

Calculate the factorial of a number using a loop.

Example:

```text
Input: 5
Output: 120
```

Because:

```text
5 × 4 × 3 × 2 × 1 = 120
```

### Concepts

```text
for
range()
multiplication
```

---

# 16. Factorial Using Recursion

## Task

Create a function that calculates factorial using recursion.

Example:

```text
Input: 5
Output: 120
```

### Concepts

```text
function
recursion
base case
return
```

---

# 17. Positive, Negative, Zero, Even, Odd

## Task

Create a function that accepts an integer and determines:

1. Whether it is positive, negative, or zero.
2. If it is not zero, whether it is even or odd.

### Example

```text
Input: -8

Output:
Negative
Even
```

---

# 18. Student Eligibility Function

## Task

Create a function:

```python
check_eligibility(percentage, has_backlog)
```

The student is eligible if:

```text
percentage >= 60
AND
has_backlog is False
```

Return:

```text
"Eligible"
```

or:

```text
"Not Eligible"
```

---

# 19. Nested Condition Practice

## Task

Create an entry system.

Rules:

```text
Age must be >= 18
Then ID must be available
```

Possible outputs:

```text
Access allowed
ID required
Age restriction
```

Try solving this using nested `if`.

---

# 20. Membership Practice

## Task

Given:

```python
sports = ["Cricket", "Football", "Basketball", "Volleyball"]
```

Check whether:

```text
Cricket
Tennis
```

are present.

Expected:

```text
Cricket → Found
Tennis → Not Found
```

---

# 21. Identity Practice

## Task

Consider:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
```

Check:

```python
a == b
a == c

a is b
a is c
```

Explain why the results are different.

### Important

Your explanation should distinguish:

```text
Equality
Identity
```

---

# 22. `*args` Practice

## Task

Create a function:

```python
calculate_sum(*numbers)
```

It should accept any number of positional arguments and return their sum.

Example:

```python
calculate_sum(10, 20, 30)
```

Output:

```text
60
```

Try:

```python
calculate_sum(1, 2)
calculate_sum(1, 2, 3, 4, 5)
```

---

# 23. `**kwargs` Practice

## Task

Create a function that accepts any number of keyword arguments and prints them.

Example:

```python
display_student(
    name="Soyab",
    age=21,
    course="BCA"
)
```

Expected output:

```text
name: Soyab
age: 21
course: BCA
```

---

# 24. Lambda Practice

## Task

Create a lambda function that accepts a number and returns its square.

Example:

```text
Input: 5
Output: 25
```

Expected concept:

```python
square = lambda x: x * x
```

---

# 25. `map()` Practice

## Task

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Use `map()` to create the squares:

```text
[1, 4, 9, 16, 25]
```

Remember that in Python 3, `map()` returns an iterator, so convert it to a list when you want to display the resulting values as a list.

---

# 26. `filter()` Practice

## Task

Given:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Use `filter()` to get only even numbers.

Expected:

```text
[2, 4, 6, 8, 10]
```

---

# 27. While Countdown

## Task

Use a `while` loop to print:

```text
10
9
8
7
6
5
4
3
2
1
```

### Requirement

Do not use a `for` loop.

---

# 28. `break` Practice

## Task

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Search for `30`.

Stop the loop immediately after finding it.

### Requirement

Use:

```python
break
```

---

# 29. `continue` Practice

## Task

Print numbers from 1 to 20 but skip all numbers divisible by 3.

Expected:

```text
1
2
4
5
7
8
10
11
13
14
16
17
19
20
```

### Requirement

Use:

```python
continue
```

---

# 30. Simple Menu Program

## Task

Create a simple menu:

```text
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

The user selects an option.

Perform the selected operation.

If the user chooses `5`, display:

```text
Program ended
```

### Concepts

```text
while
if-elif-else
break
input
functions
arithmetic operators
```

---

# 31. Mini Interview Challenge

Create a small student management program.

The program should:

1. Accept a student's name.
2. Accept marks.
3. Calculate the grade.
4. Check pass/fail.
5. Check placement eligibility.
6. Display the final information.

Example:

```text
Student Name: Soyab
Marks: 82

Grade: A
Result: Pass
Placement: Eligible
```

### Suggested concepts

```text
Variables
input()
type conversion
functions
if-elif-else
comparison operators
logical operators
return
```

---

# 32. Mini Calculator Function

Create separate functions:

```python
add()
subtract()
multiply()
divide()
```

Then create a menu that calls the correct function.

Example:

```python
add(10, 5)
```

should return:

```text
15
```

### Goal

Practice separating logic into functions instead of putting everything into one large block.

---

# 33. Number Analysis Function

Create:

```python
analyze_number(number)
```

The function should display:

```text
Positive / Negative / Zero
Even / Odd
```

For example:

```text
Input: 12

Output:
Positive
Even
```

---

# 34. Find Common Elements

Given:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
```

Find the common values.

Expected:

```text
4
5
```

Try solving it using:

```python
in
```

before using sets.

---

# 35. Count Vowels

## Task

Accept a string and count the number of vowels.

Example:

```text
Input:
Python Programming

Output:
4
```

Consider:

```text
a
e
i
o
u
```

### Concepts

```text
for
in
if
string
counter
```

---

# 36. Reverse a String

## Task

Accept a string and reverse it.

Example:

```text
Input:
Python

Output:
nohtyP
```

Try solving it using slicing:

```python
text[::-1]
```

Then try another approach using a loop.

---

# 37. Count Words

## Task

Accept a sentence and count the number of words.

Example:

```text
Input:
Python is easy to learn

Output:
5
```

Hint:

```python
split()
```

---

# 38. Find Duplicate Values

Given:

```python
numbers = [1, 2, 3, 2, 4, 5, 1]
```

Find values that appear more than once.

Expected values:

```text
1
2
```

Try solving the problem without immediately converting the entire list into a set.

---

# 39. Student Marks Using a Function

Create a function:

```python
calculate_grade(marks)
```

It should return the appropriate grade.

Then use:

```python
marks = [85, 72, 91, 64, 38]
```

to calculate the grade for every student.

### Concepts

```text
function
return
for
list
if-elif-else
```

---

# 40. Login with Three Attempts

Create a login program that gives the user a maximum of three attempts.

Example:

```text
Attempt 1 → Incorrect
Attempt 2 → Incorrect
Attempt 3 → Correct

Login successful
```

Stop immediately when the correct password is entered.

### Concepts

```text
while
if
break
counter
comparison
```

---

# 41. Search a Student

Given:

```python
students = ["Soyab", "Ashish", "Siddiq", "Rahul"]
```

Ask the user for a name.

Display:

```text
Student found
```

or:

```text
Student not found
```

---

# 42. Student Dictionary

Create:

```python
student = {
    "name": "Soyab",
    "age": 21,
    "course": "BCA",
    "percentage": 72
}
```

Write a program that:

1. Displays the student's name.
2. Displays the course.
3. Checks whether `"percentage"` exists as a key.
4. Checks whether `"BCA"` exists as a value.

---

# 43. Simple Shopping Cart

Create:

```python
cart = [100, 250, 500, 150]
```

Calculate:

```text
Total amount
```

Then apply:

```text
10% discount if total >= 1000
```

Display:

```text
Total
Discount
Final amount
```

---

# 44. Multiplication Tables

Create a program that prints multiplication tables from 1 to 5.

Example:

```text
1 x 1 = 1
1 x 2 = 2
...

5 x 10 = 50
```

### Concepts

```text
nested loops
range()
arithmetic
```

---

# 45. Pattern Practice

Print:

```text
*
**
***
****
*****
```

Then print:

```text
*****
****
***
**
*
```

### Concepts

```text
nested loops
range()
string repetition
```

---

# 46. Prime Number Check

## Task

Determine whether a number is prime.

Example:

```text
Input: 7
Output: Prime
```

Example:

```text
Input: 10
Output: Not Prime
```

Try solving it first using a loop.

### Concepts

```text
for
range()
%
break
```

---

# 47. Fibonacci Sequence

## Task

Print the first `n` Fibonacci numbers.

Example:

```text
Input: 7

Output:
0 1 1 2 3 5 8
```

### Concepts

```text
variables
loop
multiple assignment
```

---

# 48. Find the Second Largest Number

Given:

```python
numbers = [10, 25, 7, 42, 18]
```

Find the second largest number.

Expected:

```text
25
```

Try solving it without directly using:

```python
sorted()
```

or:

```python
sort()
```

---

# 49. Function with Default Parameter

Create:

```python
def greet(name="Guest"):
    ...
```

If the user provides a name:

```python
greet("Soyab")
```

Output:

```text
Hello Soyab
```

If no name is provided:

```python
greet()
```

Output:

```text
Hello Guest
```

---

# 50. Function Returning Multiple Values

Create a function:

```python
calculate(a, b)
```

It should return:

```text
sum
difference
product
```

Example:

```python
result = calculate(10, 5)
```

Then unpack the returned values.

---

# 51. Function Accepting `*args`

Create:

```python
def find_largest(*numbers):
    ...
```

The function should accept any number of numbers and return the largest.

Example:

```python
find_largest(10, 50, 20, 40)
```

Expected:

```text
50
```

---

# 52. Function Accepting `**kwargs`

Create:

```python
def create_profile(**details):
    ...
```

Call:

```python
create_profile(
    name="Soyab",
    course="BCA",
    city="Athani"
)
```

Display all the profile information.

---

# 53. Lambda with Sorting

Given:

```python
students = [
    ("Soyab", 72),
    ("Ashish", 85),
    ("Siddiq", 65)
]
```

Sort the students according to their marks using:

```python
lambda
```

---

# 54. Map and Filter Together

Given:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Create a program that:

1. Selects even numbers.
2. Squares them.

Expected:

```text
[4, 16, 36]
```

---

# 55. Interview Challenge — Explain the Output

Predict the output before running the code:

```python
x = 10

if x > 5:
    print("A")

if x > 8:
    print("B")
else:
    print("C")
```

Then explain why both `A` and `B` are printed.

---

# 56. Interview Challenge — `break`

Predict:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

Expected:

```text
1
2
```

Explain why `3`, `4`, and `5` are not printed.

---

# 57. Interview Challenge — `continue`

Predict:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Expected:

```text
1
2
4
5
```

---

# 58. Interview Challenge — `and`

Predict:

```python
print("Hello" and "Python")
```

Expected:

```text
Python
```

Explain that `and` returns an operand according to its short-circuit rules rather than necessarily returning a Boolean.

---

# 59. Interview Challenge — `or`

Predict:

```python
print("" or "Guest")
```

Expected:

```text
Guest
```

Explain why the empty string is skipped because it is falsy.

---

# 60. Interview Challenge — Identity

Predict:

```python
a = [1, 2]
b = a
c = [1, 2]

print(a == b)
print(a == c)
print(a is b)
print(a is c)
```

Expected:

```text
True
True
True
False
```

---

# 61. Interview Challenge — Mutable Default Argument

What happens here?

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
```

Expected:

```text
['A']
['A', 'B']
```

### Why?

The default list is created once when the function is defined, not every time the function is called.

A safer pattern is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

# 62. Interview Challenge — Assignment and Objects

Predict:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

### Why?

`a` and `b` refer to the same list object.

---

# 63. Interview Challenge — Copy

Predict:

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Here `b` is a separate list object.

---

# 64. Mini Project — Student Result System

Build a small command-line program.

## Requirements

Accept:

```text
Student name
Student marks
```

Calculate:

```text
Total
Percentage
Grade
Pass/Fail
Placement eligibility
```

Use functions such as:

```python
calculate_grade()
check_result()
check_placement()
```

### Goal

Practice combining multiple Python concepts instead of solving isolated questions.

---

# 65. Mini Project — Simple Banking System

Create a basic command-line banking program.

Start with:

```text
Balance = 10000
```

Menu:

```text
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

Rules:

* Deposit should increase balance.
* Withdrawal should not exceed the available balance.
* Invalid menu choices should be handled.
* Program should continue until the user chooses Exit.

### Concepts

```text
while
if-elif-else
functions
variables
arithmetic
comparison
break
```

---

# 66. Mini Project — Quiz Program

Create a simple quiz.

Example:

```text
Question:
Which language is commonly used for AI and data science?

1. Python
2. HTML
3. CSS
4. SQL
```

The user selects an option.

Keep track of the score.

At the end:

```text
Your score: 3/5
```

### Concepts

```text
lists
dictionaries
loops
if
variables
functions
```

---

# 67. Mini Project — Student Management

Create a simple program that stores students.

Each student can contain:

```text
Name
Age
Course
Marks
```

The program should provide options to:

```text
1. Add student
2. Display students
3. Search student
4. Exit
```

This is a good beginner project for combining:

```text
Lists
Dictionaries
Functions
Loops
Conditions
Input
```

---

# 68. Practice Progress Levels

Use these levels to measure your progress.

## Level 1 — Beginner

Complete:

```text
1–10
```

You should understand:

```text
Variables
Input
Arithmetic
Conditions
Basic validation
```

---

## Level 2 — Loops

Complete:

```text
11–20
```

You should understand:

```text
for
while
range
break
continue
membership
```

---

## Level 3 — Functions

Complete:

```text
21–30
```

You should understand:

```text
Functions
Arguments
Parameters
return
*args
**kwargs
lambda
```

---

## Level 4 — Intermediate

Complete:

```text
31–50
```

You should be comfortable with:

```text
Lists
Strings
Dictionaries
Nested loops
Functions
Problem solving
```

---

## Level 5 — Interview

Complete:

```text
51–63
```

You should be able to explain:

```text
Function behavior
Object references
Identity
Mutability
Logical operators
Loop behavior
Default arguments
```

---

## Level 6 — Mini Projects

Complete:

```text
64–67
```

The goal is to combine multiple concepts into working programs.

---

# 69. How to Explain Your Code in an Interview

When an interviewer gives you a coding problem, explain your solution in this order:

### 1. Explain the requirement

Example:

> "The program needs to determine whether a number is even or odd."

### 2. Explain the logic

> "I will use the modulus operator. If the remainder after dividing by 2 is zero, the number is even."

### 3. Write the code

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 4. Explain the important line

```python
number % 2
```

returns the remainder after division by 2.

### 5. Test the program

For example:

```text
Input: 10
Output: Even
```

This approach demonstrates both coding ability and understanding.

---

# 70. Problem-Solving Checklist

Before writing code, ask:

```text
What is the input?
        ↓
What is the output?
        ↓
What conditions exist?
        ↓
Is repetition required?
        ↓
Do I need a function?
        ↓
Which data structure should I use?
        ↓
Which operators are required?
        ↓
What edge cases should I test?
```

---

# 71. Common Edge Cases

When solving problems, don't test only one normal input.

For example, for a marks program test:

```text
0
39
40
59
60
74
75
89
90
100
101
-1
```

For a division program test:

```text
10 / 2
10 / 3
0 / 5
5 / 0
```

For a list search test:

```text
Existing value
Missing value
Empty list
Duplicate values
```

Testing edge cases helps find bugs.

---

# 72. Practice Without Copying

A good learning cycle is:

```text
Read problem
    ↓
Try yourself
    ↓
Get stuck
    ↓
Review the relevant concept
    ↓
Try again
    ↓
Compare with solution
    ↓
Rewrite without looking
    ↓
Explain it aloud
```

Simply copying a solution is not enough.

The important goal is to understand why the code works.

---

# 73. Interview Preparation Strategy

For Python interviews, practice these areas repeatedly:

## Basics

```text
Python syntax
Variables
Data types
Input/output
Type conversion
```

## Operators

```text
Arithmetic
Comparison
Logical
Identity
Membership
Bitwise
```

## Control Flow

```text
if
elif
else
for
while
break
continue
```

## Functions

```text
Parameters
Arguments
return
Default arguments
*args
**kwargs
lambda
Recursion
```

## Data Structures

```text
List
Tuple
Set
Dictionary
String
```

## Python Concepts

```text
Mutable vs immutable
References
Identity
Scope
LEGB
Exception handling
Modules
Packages
Object-oriented programming
```

---

# 74. Recommended Practice Order

If you are starting from zero, follow this sequence:

```text
Day 1
→ Tasks 1–5

Day 2
→ Tasks 6–10

Day 3
→ Tasks 11–15

Day 4
→ Tasks 16–20

Day 5
→ Tasks 21–25

Day 6
→ Tasks 26–30

Day 7
→ Tasks 31–40

Day 8
→ Tasks 41–50

Day 9
→ Tasks 51–63

Day 10+
→ Mini Projects
```

Do not worry about finishing everything quickly.

Focus on understanding each solution.

---

# 75. Final Python Practice Roadmap

```text
Python Basics
      ↓
Variables & Data Types
      ↓
Memory & References
      ↓
Functions
      ↓
Operators
      ↓
Control Flow
      ↓
Practice Problems
      ↓
Data Structures
      ↓
Exception Handling
      ↓
File Handling
      ↓
Modules & Packages
      ↓
OOP
      ↓
Advanced Python
      ↓
Projects
      ↓
Interview Preparation
```

---

# 76. Final Checklist

Before saying **"I know Python basics"**, make sure you can explain and use:

### Python Basics

* [ ] What Python is
* [ ] Python features
* [ ] Python execution basics
* [ ] Comments
* [ ] Input/output
* [ ] Type conversion

### Variables and Data Types

* [ ] Variables
* [ ] Dynamic typing
* [ ] `int`
* [ ] `float`
* [ ] `complex`
* [ ] `bool`
* [ ] `str`
* [ ] `list`
* [ ] `tuple`
* [ ] `set`
* [ ] `dict`
* [ ] `None`

### Memory

* [ ] Objects
* [ ] References
* [ ] Identity
* [ ] `id()`
* [ ] Assignment
* [ ] Shallow copy
* [ ] Deep copy
* [ ] Reference counting
* [ ] Garbage collection
* [ ] Mutable vs immutable

### Functions

* [ ] Define a function
* [ ] Call a function
* [ ] Parameters
* [ ] Arguments
* [ ] `return`
* [ ] Default arguments
* [ ] Keyword arguments
* [ ] `*args`
* [ ] `**kwargs`
* [ ] Lambda
* [ ] Recursion
* [ ] Scope
* [ ] LEGB

### Operators

* [ ] Arithmetic
* [ ] Assignment
* [ ] Comparison
* [ ] Logical
* [ ] Identity
* [ ] Membership
* [ ] Bitwise
* [ ] Conditional expression
* [ ] Operator precedence

### Control Flow

* [ ] `if`
* [ ] `elif`
* [ ] `else`
* [ ] Nested conditions
* [ ] `for`
* [ ] `while`
* [ ] `range()`
* [ ] `break`
* [ ] `continue`
* [ ] `pass`
* [ ] `enumerate()`

### Practice

* [ ] Calculator
* [ ] Grade calculator
* [ ] Login validation
* [ ] Number problems
* [ ] Loop problems
* [ ] Function problems
* [ ] List problems
* [ ] String problems
* [ ] Dictionary problems
* [ ] Mini projects
* [ ] Interview output questions

---

# 77. Final Goal

The goal of these practice tasks is not to memorize Python programs.

You should eventually be able to look at a problem and think:

```text
What is the problem?
       ↓
What data do I need?
       ↓
What logic is required?
       ↓
Which Python concept solves it?
       ↓
How can I write the solution simply?
       ↓
How can I test it?
       ↓
Can I explain it?
```

If you can solve a problem **and explain why your solution works**, you are learning Python rather than simply memorizing code.
