Python has below operators 
1)Arithmatic operators
2)Assignment operators
3)Comparison operators 
4)Logical operators
5)Identity operators
6)Membership operators
7)Bitwise operators
8)Ternary operators

task 1: Write calculator program which should return addition ,substraction ,multiplication ,division ,floordivision ,reminder.

task 2: Create a function that accepts an integer and Determines.
*Whether the number is even or odd 
*Whether it is divisible by 3
*Whether it divisible by 5

task 3: Create a function that accepts a students marks and returns.
*Pass  if marks are > or = 35
*Fail  otherwise 
*Distiction if marks are > or = 75

task 4: Create a function that accepts 
*Marks
*Attendence percwntage 
*Backlog status
*A student is eligible only when marks > or = 60
Attendents >= 75
backlog == false
*return eligible or not eligible

task 5 : Create a function that accepts username and password.
*the user should be considered valid only when username =="admin" and password=="Pyhton123"

task 6 : Create a function that accepts the purchage amount 
apply rs5000 or more (20%) discount 
rs300 to 4999 (10%) discount
below rs300 (5%) discount  
return discount amount and final payable amount 

task 7 : Create a function that accepts age , has_id ,id_empoyee
allow access when 
age >= 18  and has_id==true
or when is_employee ==true
return access granted or access denied

task 8 : Create a list of required skills 
["python","Sql","Git","Html"]
create a function that accept skill name and judge whether it exist in the list
display skill available or skill not available

task 9 : Create Functions(a + b)
the function should support (+,-,*,/,//.%,**)
handle invalid operators and division by zero

task 10: Create a function that accepts age ,marks, attendence , experience ,has_backlog
determine placement eligibility
marks >= 60 and attendence >=75 and has_backlog==false 
then determine a categary experience = 0 ->fresher
experience 1 to 2 -> junior
experience>2 -> Experienced
finally display 
placement eligible :yes/no
Candidate catagary :fresher or junior or experienced


# Python Functions and Operators

## 1. Functions

A **function** is a reusable block of code that performs a specific task.

### Syntax

```python
def function_name(parameters):
    # code
    return value
```

### Example

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

Here:

* `def` → defines a function
* `add` → function name
* `a, b` → parameters
* `10, 20` → arguments
* `return` → sends the result back

---

## 2. Function With Multiple Return Values

A function can return more than one value.

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

The line:

```python
add_result, sub_result = calculate(10, 5)
```

receives the two values returned by the function.

---

# Operators in Python

Operators are symbols or keywords used to perform operations on values and variables.

Python has the following major types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Ternary Operator

---

## 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Meaning        | Example   | Result |
| -------- | -------------- | --------- | -----: |
| `+`      | Addition       | `10 + 5`  |   `15` |
| `-`      | Subtraction    | `10 - 5`  |    `5` |
| `*`      | Multiplication | `10 * 5`  |   `50` |
| `/`      | Division       | `10 / 5`  |  `2.0` |
| `//`     | Floor Division | `10 // 3` |    `3` |
| `%`      | Remainder      | `10 % 3`  |    `1` |
| `**`     | Power          | `2 ** 3`  |    `8` |

Example:

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

---

## 2. Assignment Operators

Used to assign or update values in variables.

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
| `=`      | `a = 10`  | Assign       |
| `+=`     | `a += 5`  | `a = a + 5`  |
| `-=`     | `a -= 5`  | `a = a - 5`  |
| `*=`     | `a *= 5`  | `a = a * 5`  |
| `/=`     | `a /= 5`  | `a = a / 5`  |
| `//=`    | `a //= 5` | `a = a // 5` |
| `%=`     | `a %= 5`  | `a = a % 5`  |
| `**=`    | `a **= 2` | `a = a ** 2` |

Example:

```python
a = 10

a += 5

print(a)
```

Output:

```text
15
```

---

## 3. Comparison Operators

Used to compare two values.

The result is always `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

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

## 4. Logical Operators

Used to combine multiple conditions.

### `and`

Returns `True` when **all conditions are true**.

```python
age = 20
marks = 70

print(age >= 18 and marks >= 60)
```

Output:

```text
True
```

### `or`

Returns `True` when **at least one condition is true**.

```python
age = 16
is_employee = True

print(age >= 18 or is_employee)
```

Output:

```text
True
```

### `not`

Reverses the Boolean result.

```python
is_logged_in = True

print(not is_logged_in)
```

Output:

```text
False
```

---

## 5. Identity Operators

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

`a` and `b` refer to the same list object.

### Important

`is` is different from `==`.

```python
==  → checks whether values are equal
is  → checks whether they are the same object
```

---

## 6. Membership Operators

Used to check whether a value exists inside a sequence such as a list, string, tuple, etc.

Operators:

```python
in
not in
```

Example:

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

---

## 7. Bitwise Operators

Bitwise operators work with numbers at the **binary/bit level**.

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left Shift  |    |
| `>>`     | Right Shift |    |

Example:

```python
a = 5
b = 3

print(a & b)
```

Binary representation:

```text
5 → 101
3 → 011
     ---
     001
```

Therefore:

```text
1
```

---

## 8. Ternary Operator

The ternary operator is a short way of writing a simple `if-else`.

### Normal if-else

```python
age = 20

if age >= 18:
    result = "Adult"
else:
    result = "Minor"
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

---

# Functions + Operators Together

Operators are frequently used inside functions.

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

Here:

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

This is the basic relationship between **functions and operators** in Python.
