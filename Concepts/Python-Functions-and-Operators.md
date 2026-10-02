# Python Functions and Operators

These notes explain **Python functions and operators** in simple language, with examples and practice tasks.

---

# Part 1: Functions

## 1. What is a Function?

A **function** is a reusable block of code that performs a particular task.

Instead of writing the same code again and again, we can put it inside a function and call the function whenever we need it.

### Simple Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### How it works

```text
def
 ↓
Creates a function

add
 ↓
Function name

a, b
 ↓
Parameters

10, 20
 ↓
Arguments

return
 ↓
Sends the result back
```

---

# 2. Function Syntax

The basic syntax of a Python function is:

```python
def function_name(parameters):
    # code
    return value
```

Example:

```python
def greet(name):
    return "Hello " + name

message = greet("Soyab")

print(message)
```

Output:

```text
Hello Soyab
```

---

# 3. Parameters and Arguments

These two terms are important in Python.

### Parameter

A **parameter** is the variable written inside the function definition.

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name
```

is a parameter.

### Argument

An **argument** is the actual value passed when calling the function.

```python
greet("Soyab")
```

Here:

```text
"Soyab"
```

is an argument.

### Easy way to remember

```text
Parameter = variable in function definition

Argument = actual value passed to function
```

---

# 4. Function With Multiple Return Values

A Python function can return multiple values.

Example:

```python
def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


add_result, sub_result = calculate(10, 5)

print(add_result)
print(sub_result)
```

Output:

```text
15
5
```

The function returns two values:

```python
return addition, subtraction
```

We receive them using:

```python
add_result, sub_result = calculate(10, 5)
```

---

# Part 2: Operators

## 5. What is an Operator?

An **operator** is a symbol or keyword used to perform an operation on values or variables.

Example:

```python
a = 10
b = 5

print(a + b)
```

Here:

```text
+ = operator
10 and 5 = operands
```

The `+` operator performs addition.

---

# 6. Types of Operators in Python

Python has the following major types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Ternary Operator / Conditional Expression

---

# 7. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | -----: |
| `+`      | Addition       | `10 + 5`  |   `15` |
| `-`      | Subtraction    | `10 - 5`  |    `5` |
| `*`      | Multiplication | `10 * 5`  |   `50` |
| `/`      | Division       | `10 / 5`  |  `2.0` |
| `//`     | Floor Division | `10 // 3` |    `3` |
| `%`      | Remainder      | `10 % 3`  |    `1` |
| `**`     | Power          | `2 ** 3`  |    `8` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

### Important operators

#### `/` Division

Returns the normal division result.

```python
10 / 3
```

Result:

```text
3.3333333333333335
```

#### `//` Floor Division

Returns the floor division result.

```python
10 // 3
```

Result:

```text
3
```

#### `%` Remainder

Returns the remainder after division.

```python
10 % 3
```

Result:

```text
1
```

#### `**` Power

Used to calculate powers.

```python
2 ** 3
```

means:

```text
2 × 2 × 2 = 8
```

---

# 8. Assignment Operators

Assignment operators are used to assign or update values in variables.

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
| `=`      | `a = 10`  | Assign value |
| `+=`     | `a += 5`  | `a = a + 5`  |
| `-=`     | `a -= 5`  | `a = a - 5`  |
| `*=`     | `a *= 5`  | `a = a * 5`  |
| `/=`     | `a /= 5`  | `a = a / 5`  |
| `//=`    | `a //= 5` | `a = a // 5` |
| `%=`     | `a %= 5`  | `a = a % 5`  |
| `**=`    | `a **= 2` | `a = a ** 2` |

### Example

```python
a = 10

a += 5

print(a)
```

Output:

```text
15
```

This:

```python
a += 5
```

is the same as:

```python
a = a + 5
```

---

# 9. Comparison Operators

Comparison operators are used to compare two values.

The result is always:

```text
True
```

or:

```text
False
```

| Operator | Meaning                  | Example    |
| -------- | ------------------------ | ---------- |
| `==`     | Equal to                 | `10 == 10` |
| `!=`     | Not equal to             | `10 != 5`  |
| `>`      | Greater than             | `10 > 5`   |
| `<`      | Less than                | `5 < 10`   |
| `>=`     | Greater than or equal to | `10 >= 10` |
| `<=`     | Less than or equal to    | `5 <= 10`  |

### Example

```python
a = 10
b = 5

print(a > b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
True
```

---

# 10. Logical Operators

Logical operators are used to combine multiple conditions.

Python has three main logical operators:

```text
and
or
not
```

---

## `and`

`and` returns `True` only when **all conditions are true**.

Example:

```python
age = 20
marks = 70

print(age >= 18 and marks >= 60)
```

Both conditions are true, so the result is:

```text
True
```

### Easy example

```text
Condition 1 = True
Condition 2 = True

True and True = True
```

If one condition is false:

```text
True and False = False
```

---

## `or`

`or` returns `True` when **at least one condition is true**.

Example:

```python
age = 16
is_employee = True

print(age >= 18 or is_employee)
```

The first condition is false, but the second is true.

Therefore:

```text
True
```

---

## `not`

`not` reverses a Boolean value.

Example:

```python
is_logged_in = True

print(not is_logged_in)
```

Output:

```text
False
```

Because:

```text
not True = False
```

---

# 11. Identity Operators

Identity operators check whether two variables refer to the **same object**.

Python has:

```python
is
is not
```

Example:

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Both variables refer to the same list object.

---

## `==` vs `is`

This is an important interview question.

### `==`

Checks whether two values are equal.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

The values are equal.

### `is`

Checks whether two variables refer to the same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

They contain the same values, but they are two different list objects.

### Easy way to remember

```text
== → Same value?

is → Same object?
```

---

# 12. Membership Operators

Membership operators check whether a value exists inside a collection such as a list, tuple, set, or string.

Python has:

```python
in
not in
```

### Example

```python
skills = ["Python", "SQL", "Git"]

print("Python" in skills)
print("Java" in skills)
```

Output:

```text
True
False
```

### `not in`

```python
skills = ["Python", "SQL", "Git"]

print("Java" not in skills)
```

Output:

```text
True
```

---

# 13. Bitwise Operators

Bitwise operators work with numbers at the **binary/bit level**.

Python provides:

| Operator | Name        |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left Shift  |            |
| `>>`     | Right Shift |            |

### Example: Bitwise AND

```python
a = 5
b = 3

print(a & b)
```

Binary representation:

```text
5 = 101
3 = 011
```

Bitwise AND:

```text
101
011
---
001
```

Therefore:

```text
1
```

### Why?

For `AND`:

```text
1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
```

---

# 14. Ternary Operator

Python has a **conditional expression**, commonly called the ternary operator.

It is a short way to write a simple `if-else`.

### Normal `if-else`

```python
age = 20

if age >= 18:
    result = "Adult"
else:
    result = "Minor"

print(result)
```

### Ternary version

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

### Syntax

```python
value_if_true if condition else value_if_false
```

### Easy way to remember

```text
If condition is true → first value
Otherwise            → second value
```

---

# Part 3: Functions + Operators Together

Operators are commonly used inside functions.

Example:

```python
def calculate(a, b):
    addition = a + b
    multiplication = a * b
    remainder = a % b

    return addition, multiplication, remainder


result1, result2, result3 = calculate(10, 3)

print("Addition:", result1)
print("Multiplication:", result2)
print("Remainder:", result3)
```

Output:

```text
Addition: 13
Multiplication: 30
Remainder: 1
```

### Program flow

```text
Function
   ↓
Receives arguments
   ↓
Uses operators
   ↓
Calculates result
   ↓
Returns result
```

This is the basic relationship between **functions and operators**.

---

# Part 4: Practice Tasks

# Task 1: Calculator

Write a calculator program that performs:

* Addition
* Subtraction
* Multiplication
* Division
* Floor Division
* Remainder

The program should accept two numbers and an operator.

### Operators to support

```text
+
-
*
/
//
%
```

### Concepts practiced

* `input()`
* Functions
* Arithmetic operators
* Conditions
* Division by zero

---

# Task 2: Number Checking

Create a function that accepts an integer and determines:

* Whether the number is even or odd
* Whether it is divisible by 3
* Whether it is divisible by 5

### Useful conditions

Check even or odd:

```python
number % 2 == 0
```

Check divisibility by 3:

```python
number % 3 == 0
```

Check divisibility by 5:

```python
number % 5 == 0
```

### Concepts practiced

* Functions
* Parameters
* `%` operator
* `if-else`

---

# Task 3: Student Marks

Create a function that accepts student marks and returns:

* **Distinction** if marks are `>= 75`
* **Pass** if marks are `>= 35`
* **Fail** otherwise

### Important

Check Distinction first.

Correct order:

```text
marks >= 75 → Distinction
marks >= 35 → Pass
otherwise   → Fail
```

Why?

Suppose marks are `80`.

If we check this first:

```python
marks >= 35
```

it is already `True`, so the student would incorrectly receive `Pass`.

Therefore, check the higher condition first.

### Concepts practiced

* Functions
* Comparison operators
* `if-elif-else`

---

# Task 4: Student Eligibility

Create a function that accepts:

* Marks
* Attendance percentage
* Backlog status

A student is eligible only when:

```text
Marks >= 60
AND
Attendance >= 75
AND
Backlog == False
```

Return:

```text
Eligible
```

or:

```text
Not Eligible
```

### Logic

```python
marks >= 60 and attendance >= 75 and backlog == False
```

All three conditions must be true.

### Concepts practiced

* Functions
* Comparison operators
* Logical `and`
* Boolean values

---

# Task 5: Username and Password Validation

Create a function that accepts:

* Username
* Password

The user is valid only when:

```python
username == "admin"
```

and:

```python
password == "Pyhton123"
```

Otherwise, the user is invalid.

### Logic

```python
username == "admin" and password == "Pyhton123"
```

### Concepts practiced

* Functions
* Parameters
* Strings
* Comparison operator `==`
* Logical `and`

> **Note:** `Pyhton123` is kept exactly as written in your original task.

---

# Task 6: Purchase Discount

Create a function that accepts the purchase amount.

Apply these discount rules:

| Purchase Amount   | Discount |
| ----------------- | -------: |
| `₹5000` or more   |      20% |
| `₹300` to `₹4999` |      10% |
| Below `₹300`      |       5% |

The function should return:

1. Discount amount
2. Final payable amount

### Formula

```text
Discount Amount = Purchase Amount × Discount Rate
```

```text
Final Amount = Purchase Amount - Discount Amount
```

### Example

Purchase amount:

```text
₹6000
```

Discount:

```text
20%
```

Discount amount:

```text
₹1200
```

Final amount:

```text
₹4800
```

### Multiple return values

The function can return:

```python
return discount, final_amount
```

And receive them using:

```python
discount, final_amount = calculate_discount(amount)
```

### Concepts practiced

* Functions
* `if-elif-else`
* Arithmetic operators
* Comparison operators
* Multiple return values

---

# Task 7: Access Control

Create a function that accepts:

* `age`
* `has_id`
* `is_employee`

Allow access when:

```text
Age >= 18 AND has_id == True
```

**OR**

```text
is_employee == True
```

### Logic

```python
(age >= 18 and has_id == True) or is_employee == True
```

If the condition is true:

```text
Access Granted
```

Otherwise:

```text
Access Denied
```

### Concepts practiced

* Functions
* `and`
* `or`
* Comparison operators
* Boolean values

---

# Task 8: Required Skills

Create a list of required skills:

```python
required_skills = ["python", "Sql", "Git", "Html"]
```

Create a function that accepts a skill name and checks whether it exists in the list.

If it exists:

```text
Skill Available
```

Otherwise:

```text
Skill Not Available
```

### Example logic

```python
if skill in required_skills:
    print("Skill Available")
else:
    print("Skill Not Available")
```

### Concepts practiced

* Lists
* Functions
* Membership operator `in`
* Conditions

> Python string matching is case-sensitive. For example, `"python"` and `"Python"` are different strings.

---

# Task 9: Calculator Function With Multiple Operators

Create a function:

```python
calculate(a, b, operator)
```

The function should support:

```text
+
-
*
/
//
%
**
```

### Meaning

| Operator | Operation      |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Remainder      |
| `**`     | Power          |

### Requirements

The function should:

1. Perform the selected operation.
2. Handle invalid operators.
3. Handle division by zero.
4. Return the result.

### Example

```python
calculate(10, 5, "+")
```

Result:

```text
15
```

Another example:

```python
calculate(2, 3, "**")
```

Result:

```text
8
```

### Division by zero

These operations cannot use `0` as the second number:

```text
/
//
%
```

For example:

```python
calculate(10, 0, "/")
```

should display an appropriate error message instead of performing the calculation.

### Concepts practiced

* Functions
* Parameters
* Arithmetic operators
* Conditions
* `match` or `if-elif-else`
* Error handling
* Division by zero

---

# Task 10: Placement Eligibility

Create a function that accepts:

* Age
* Marks
* Attendance
* Experience
* Backlog status

## Placement Eligibility Rule

A candidate is eligible when:

```text
Marks >= 60
AND
Attendance >= 75
AND
Has Backlog == False
```

If all conditions are true:

```text
Placement Eligible: Yes
```

Otherwise:

```text
Placement Eligible: No
```

---

## Candidate Category

Determine the category based on experience.

|             Experience | Category    |
| ---------------------: | ----------- |
|              `0` years | Fresher     |
|       `1` to `2` years | Junior      |
| Greater than `2` years | Experienced |

### Examples

```text
Experience = 0
Category = Fresher
```

```text
Experience = 1
Category = Junior
```

```text
Experience = 2
Category = Junior
```

```text
Experience = 3
Category = Experienced
```

### Final Output

Example:

```text
Placement Eligible: Yes
Candidate Category: Fresher
```

### Important Note

The task accepts `age`, but the requirements do not specify an age condition.

Therefore, based strictly on the given requirements:

```text
Age → accepted by the function
Marks → used for eligibility
Attendance → used for eligibility
Backlog → used for eligibility
Experience → used for category
```

Age does not currently affect the result.

---

# Part 5: What These Tasks Teach

These 10 tasks combine functions and operators with real-world-style conditions.

| Task    | Main Concepts                                  |
| ------- | ---------------------------------------------- |
| Task 1  | Arithmetic operators, input, conditions        |
| Task 2  | Functions, `%`, conditions                     |
| Task 3  | Comparison operators, `if-elif-else`           |
| Task 4  | Logical `and`, Boolean values                  |
| Task 5  | Strings, `==`, `and`                           |
| Task 6  | Arithmetic, conditions, multiple return values |
| Task 7  | `and`, `or`, Boolean values                    |
| Task 8  | Lists, `in`, functions                         |
| Task 9  | Functions, multiple operators, validation      |
| Task 10 | Logical operators, conditions, categorization  |

---

# Part 6: Quick Revision

## Arithmetic Operators

```python
+    # Addition
-    # Subtraction
*    # Multiplication
/    # Division
//   # Floor Division
%    # Remainder
**   # Power
```

---

## Assignment Operators

```python
=
+=
-=
*=
/=
//=
%=
**=
```

---

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

---

## Logical Operators

```python
and
or
not
```

---

## Identity Operators

```python
is
is not
```

Remember:

```text
== → checks value equality
is → checks object identity
```

---

## Membership Operators

```python
in
not in
```

---

## Bitwise Operators

```python
&
|
^
~
<<
>>
```

---

## Ternary / Conditional Expression

```python
value_if_true if condition else value_if_false
```

Example:

```python
result = "Pass" if marks >= 35 else "Fail"
```

---

# Part 7: Most Important Things to Remember

### 1. `%` gives the remainder

```python
10 % 3
```

Result:

```text
1
```

It is useful for checking even/odd and divisibility.

---

### 2. `//` gives floor division

```python
10 // 3
```

Result:

```text
3
```

---

### 3. `==` checks equality

```python
10 == 10
```

Result:

```text
True
```

---

### 4. `=` assigns a value

```python
x = 10
```

It means:

```text
Put/bind the value 10 to x.
```

It does **not** mean "is equal to" in a comparison.

---

### 5. `and` requires all conditions to be true

```python
age >= 18 and has_id == True
```

Both conditions must be true.

---

### 6. `or` requires at least one condition to be true

```python
age >= 18 or is_employee == True
```

Only one condition needs to be true.

---

### 7. `in` checks membership

```python
"Python" in skills
```

It checks whether `"Python"` exists in `skills`.

---

### 8. `is` checks object identity

```python
a is b
```

It checks whether `a` and `b` refer to the same object.

---

### 9. Functions make code reusable

Instead of writing:

```python
10 + 20
```

and then writing the same logic again for other numbers, create:

```python
def add(a, b):
    return a + b
```

Then:

```python
add(10, 20)
add(50, 30)
add(100, 200)
```

---

# Final Mental Model

Think about Python functions and operators like this:

```text
                FUNCTION
                   |
                   ↓
          Receives parameters
                   |
                   ↓
          Receives arguments
                   |
                   ↓
            Performs logic
                   |
                   ↓
              Uses operators
                   |
                   ↓
             Gets a result
                   |
                   ↓
               return
                   |
                   ↓
          Result goes back
```

For example:

```python
def is_eligible(marks, attendance):
    if marks >= 60 and attendance >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
```

Here:

```text
Function       → is_eligible()
Parameters     → marks, attendance
Arguments      → actual values passed to the function
Comparison     → >=
Logical        → and
Condition      → if
Return         → sends the answer back
```

This is the basic foundation for understanding **Python functions, conditions, and operators**.
