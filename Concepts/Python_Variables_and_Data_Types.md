# Python Variables and Data Types — Learning & Interview Notes

## 1. What is a Variable?

A **variable** is a name used to refer to an object in Python.

Example:

```python
age = 21
name = "Soyab"
marks = 85.5
```

Conceptually:

```text
age   ─────→  21
name  ─────→  "Soyab"
marks ─────→  85.5
```

A Python variable is better understood as a **name bound to an object**, rather than as a box that permanently stores a value.

---

## 2. Creating a Variable

Python does not require a separate declaration statement for ordinary variables.

You can create a variable simply by assigning a value:

```python
name = "Soyab"
age = 21
marks = 85.5
```

Python determines the type of the object from the value.

```python
age = 21
```

Here:

* `age` → variable/name
* `21` → integer object
* `=` → assignment operator

---

## 3. Variable Naming Rules

A variable name:

* Can contain letters
* Can contain digits
* Can contain `_`
* Cannot start with a digit
* Cannot contain spaces
* Is case-sensitive
* Cannot be a Python keyword

Valid:

```python
name = "Soyab"
student_age = 21
marks1 = 80
_total = 100
```

Invalid:

```python
1name = "Soyab"
student-age = 21
student age = 21
class = "BCA"
```

---

## 4. Case Sensitivity

Python is **case-sensitive**.

These are different names:

```python
name = "Soyab"
Name = "Ashish"
NAME = "Siddiq"
```

Python treats:

```text
name
Name
NAME
```

as three different identifiers.

---

## 5. Python Keywords

Keywords are reserved words that have special meaning in Python.

Examples:

```text
if
else
elif
for
while
def
class
return
import
try
except
True
False
None
and
or
not
is
in
```

You cannot normally use a keyword as a variable name.

You can view Python's keywords using:

```python
import keyword

print(keyword.kwlist)
```

---

## 6. Dynamic Typing

Python is a **dynamically typed language**.

You do not normally need to declare a variable's type before assigning a value.

```python
value = 10
value = "Hello"
value = 10.5
```

The name `value` is rebound to objects of different types.

Dynamic typing does **not** mean Python has no types. Python objects still have types.

---

## 7. Objects and Types

In Python, values are objects.

For example:

```python
age = 21
```

The integer `21` is an object.

An object has:

* A value
* A type
* An identity

You can check the type using:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

# 8. Built-in Data Types

| Category | Types                              |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Boolean  | `bool`                             |
| Text     | `str`                              |
| Sequence | `list`, `tuple`, `range`           |
| Set      | `set`, `frozenset`                 |
| Mapping  | `dict`                             |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| Special  | `NoneType`                         |

---

# 9. Integer (`int`)

Integers represent whole numbers.

```python
age = 21
marks = 85
temperature = -5
```

Python integers can grow beyond the size commonly available in fixed-width integer types, limited mainly by available memory.

---

# 10. Float (`float`)

Floats represent floating-point numbers.

```python
price = 99.50
percentage = 85.5
temperature = -2.75
```

Floating-point numbers may have small representation errors:

```python
print(0.1 + 0.2)
```

Possible output:

```text
0.30000000000000004
```

For exact decimal arithmetic, Python provides the `decimal` module.

---

# 11. Complex (`complex`)

Complex numbers contain a real and imaginary part.

```python
z = 3 + 4j
```

You can access the parts:

```python
print(z.real)
print(z.imag)
```

Output:

```text
3.0
4.0
```

Python uses `j` for the imaginary part.

---

# 12. Boolean (`bool`)

Python has two Boolean values:

```python
True
False
```

Example:

```python
is_student = True
is_admin = False
```

Booleans are commonly used in conditions.

---

# 13. String (`str`)

A string is a sequence of characters.

```python
name = "Soyab"
college = 'K.A. Lokapur College'
```

Strings are immutable.

Example:

```python
name = "Python"

print(name[0])
print(name[1])
```

Output:

```text
P
y
```

String slicing:

```python
print(name[0:3])
```

Output:

```text
Pyt
```

You cannot directly change an individual character:

```python
name[0] = "J"
```

This raises a `TypeError`.

---

# 14. List (`list`)

A list is an ordered, mutable collection.

```python
fruits = ["Apple", "Banana", "Mango"]
```

Lists can contain different types:

```python
data = [10, "Hello", 3.14, True]
```

Lists support indexing:

```python
print(fruits[0])
```

Lists are mutable:

```python
fruits[1] = "Orange"
```

---

# 15. Tuple (`tuple`)

A tuple is an ordered, immutable collection.

```python
coordinates = (10, 20)
```

Access values:

```python
print(coordinates[0])
```

You cannot modify an individual tuple element:

```python
coordinates[0] = 50
```

This raises a `TypeError`.

---

# 16. Set (`set`)

A set is a collection designed for unique elements and set operations.

```python
numbers = {1, 2, 3, 4}
```

Duplicate values are removed:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Sets do not support indexing:

```python
numbers = {10, 20, 30}

# numbers[0]   # TypeError
```

Example set operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union
print(a & b)   # Intersection
```

---

# 17. Dictionary (`dict`)

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Soyab",
    "age": 21,
    "course": "BCA"
}
```

Access a value:

```python
print(student["name"])
```

Add or update values:

```python
student["age"] = 22
student["college"] = "K.A. Lokapur College"
```

Dictionary keys must be hashable.

---

# 18. None (`NoneType`)

`None` represents the absence of a value.

```python
result = None
```

Check its type:

```python
print(type(result))
```

Output:

```text
<class 'NoneType'>
```

Use identity comparison when checking for `None`:

```python
if result is None:
    print("No result")
```

---

# 19. Mutable vs Immutable

## Mutable

Common mutable types:

```text
list
dict
set
bytearray
```

Their contents can be changed after creation.

## Immutable

Common immutable types:

```text
int
float
complex
bool
str
tuple
frozenset
bytes
```

Their contents cannot be changed after creation.

---

# 20. Why Mutability Matters

Consider:

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

Both names refer to the same list object.

Conceptually:

```text
a ──┐
    ├──→ [1, 2, 3, 4]
b ──┘
```

---

# 21. Assignment Does Not Necessarily Copy

```python
a = [10, 20, 30]
b = a
```

This does not create a new independent list.

```python
print(a is b)
```

Output:

```text
True
```

---

# 22. Shallow Copy

A shallow copy creates a new outer object.

```python
a = [1, 2, 3]
b = a.copy()

print(a is b)
```

Output:

```text
False
```

For nested objects, inner mutable objects can still be shared.

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)

print(a)
print(b)
```

The nested list is shared.

---

# 23. Deep Copy

A deep copy recursively copies nested objects where applicable.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(100)

print(a)
print(b)
```

Output:

```text
[[1, 2], [3, 4]]
[[1, 2, 100], [3, 4]]
```

---

# 24. `type()`

The `type()` function returns the type of an object.

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

---

# 25. `id()`

The `id()` function returns an integer identifying an object during its lifetime.

```python
x = 10

print(id(x))
```

The exact number can vary between executions and implementations.

Do not universally describe `id()` as a physical RAM address.

---

# 26. `==` vs `is`

`==` checks equality.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

`is` checks identity.

```python
print(a is b)
```

Output:

```text
False
```

The lists have equal contents but are different objects.

---

# 27. Truthy and Falsy Values

Some commonly falsy values are:

```text
False
None
0
0.0
0j
""
[]
()
{}
set()
```

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

---

# 28. Multiple Assignment

Python allows:

```python
a = b = c = 10
```

You can also assign multiple values:

```python
x, y, z = 10, 20, 30
```

---

# 29. Swapping Variables

Python makes swapping simple:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

---

# 30. Unpacking

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

---

# 31. Extended Unpacking

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
1
[2, 3, 4]
5
```

---

# 32. Constants in Python

Python does not provide an enforced `const` keyword for ordinary variables.

By convention, uppercase names are used for values intended to be treated as constants.

```python
PI = 3.14159
MAX_USERS = 100
```

However, Python does not prevent reassignment.

---

# 33. Type Conversion

Common conversion functions include:

```text
int()
float()
str()
bool()
list()
tuple()
set()
dict()
```

Example:

```python
age = "21"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
21
<class 'int'>
```

Other examples:

```python
x = 10

print(float(x))
print(str(x))
print(bool(x))
```

---

# 34. Beginner Practice

The following exercises are designed to be solved **without looking at the answers first**.

The goal is to become comfortable with:

* Variables
* `int`
* `float`
* `str`
* `bool`
* `list`
* `tuple`
* `set`
* `dict`
* `None`
* `type()`
* `id()`
* `==`
* `is`
* Type conversion
* Mutability
* Multiple assignment

---

## Practice 1 — Create Basic Variables

Create variables for:

```text
name
age
height
is_student
```

Use appropriate data types.

Print all four values.

---

## Practice 2 — Check Data Types

Create:

```python
age = 21
marks = 85.5
name = "Soyab"
is_student = True
```

Print the type of each variable using `type()`.

Expected types:

```text
int
float
str
bool
```

---

## Practice 3 — Student Information

Create variables for:

```text
Name
Age
Course
College
Percentage
```

Print them in a readable format.

Expected style:

```text
Name: Soyab
Age: 21
Course: BCA
...
```

---

## Practice 4 — Calculate Age

Create:

```python
birth_year = 2005
current_year = 2026
```

Calculate:

```text
age = current_year - birth_year
```

Print the result.

---

## Practice 5 — Type Conversion

Start with:

```python
age = "21"
marks = "85.5"
```

Convert:

* `age` to `int`
* `marks` to `float`

Then print their values and types.

---

## Practice 6 — String to Integer

Take two numbers as strings:

```python
a = "10"
b = "20"
```

Convert them to integers and print their sum.

Expected output:

```text
30
```

---

## Practice 7 — Integer to String

Create:

```python
age = 21
```

Convert it to a string.

Then create this message:

```text
I am 21 years old.
```

Do not use the integer directly with string concatenation.

---

## Practice 8 — Mutable or Immutable?

For each object, identify whether it is mutable or immutable:

```text
int
float
str
list
tuple
set
dict
bool
```

Write your answers before checking the notes above.

---

## Practice 9 — Modify a List

Create:

```python
numbers = [10, 20, 30]
```

Change `20` to `200`.

Expected result:

```text
[10, 200, 30]
```

---

## Practice 10 — Modify a String

Try:

```python
name = "Python"
```

Change the first character from `P` to `J`.

First try it directly.

Then think about why it fails.

Finally, create a new string:

```text
Jython
```

---

## Practice 11 — List vs Tuple

Create:

```python
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)
```

Try changing the first value of both.

Observe which operation works and which raises an error.

---

## Practice 12 — Remove Duplicates

Given:

```python
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
```

Convert the list into a set.

Expected unique values:

```text
1, 2, 3, 4, 5
```

---

## Practice 13 — Student Dictionary

Create a dictionary containing:

```text
name
age
course
marks
```

Example structure:

```python
student = {
    "name": "...",
    "age": ...,
    "course": "...",
    "marks": ...
}
```

Print each value separately.

---

## Practice 14 — Update a Dictionary

Start with:

```python
student = {
    "name": "Soyab",
    "age": 21
}
```

Update:

```text
age → 22
```

Then add:

```text
course → BCA
```

Print the dictionary.

---

## Practice 15 — `==` or `is`?

Predict the output before running:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Then explain **why** the two results are different.

---

## Practice 16 — Same Object

Predict:

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Then explain why both are `True`.

---

## Practice 17 — Copy a List

Create:

```python
a = [10, 20, 30]
```

Create a copy using:

```python
b = a.copy()
```

Then change `b`.

Check whether `a` changes.

---

## Practice 18 — Multiple Assignment

Use one statement to assign:

```text
x = 10
y = 20
z = 30
```

Then print all three.

---

## Practice 19 — Swap Two Variables

Given:

```python
a = 100
b = 200
```

Swap their values without using a temporary variable.

Expected:

```text
a = 200
b = 100
```

---

## Practice 20 — Truthy or Falsy?

Predict the result of each:

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))
print(bool(None))
```

Then explain the pattern.

---

## Practice 21 — Find the Type

Create these variables:

```python
a = 10
b = 10.5
c = "10"
d = True
e = [10]
f = (10,)
g = {10}
h = {"value": 10}
i = None
```

Print the type of every variable.

---

## Practice 22 — Type Conversion Challenge

Start with:

```python
a = "10"
b = "20.5"
c = "30"
```

Convert them appropriately and calculate:

```text
10 + 20.5 + 30
```

Expected result:

```text
60.5
```

---

## Practice 23 — Simple Student Calculation

Create:

```python
math = 80
science = 75
english = 90
```

Calculate:

```text
total
average
```

Print both.

Expected:

```text
Total: 245
Average: 81.666...
```

---

## Practice 24 — Nested List

Create:

```python
student = ["Soyab", 21, ["Python", "HTML", "CSS"]]
```

Print:

```text
Name
Age
First skill
Second skill
Third skill
```

This exercise helps you understand indexing inside nested collections.

---

## Practice 25 — Nested Dictionary

Create:

```python
student = {
    "name": "Soyab",
    "marks": {
        "python": 85,
        "java": 75,
        "dbms": 80
    }
}
```

Print:

```text
Student name
Python marks
Java marks
DBMS marks
```

---

## Practice 26 — `None` Practice

Create:

```python
result = None
```

Write a condition that prints:

```text
Result is not available
```

when `result` is `None`.

Use:

```python
is None
```

---

## Practice 27 — Variable Reassignment

Predict the output:

```python
value = 10
value = "Python"
value = [1, 2, 3]

print(value)
print(type(value))
```

Then explain why this is possible in Python.

---

## Practice 28 — Reference Practice

Predict the output:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Then explain why both lists contain `4`.

---

## Practice 29 — Shallow Copy Challenge

Predict the result:

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)

print(a)
print(b)
```

Explain why the inner list behaves differently from the outer list.

---

## Practice 30 — Mini Data Types Challenge

Create a Python program that stores information about a student using at least:

```text
str
int
float
bool
list
tuple
set
dict
None
```

Then:

1. Print every variable.
2. Print every variable's type.
3. Modify the mutable objects.
4. Try to modify an immutable object.
5. Explain which operations succeed and which fail.

---

# 35. Beginner Practice — Answers

Use this section **only after attempting the exercises yourself**.

## Answer 1

```python
name = "Soyab"
age = 21
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

---

## Answer 2

```python
age = 21
marks = 85.5
name = "Soyab"
is_student = True

print(type(age))
print(type(marks))
print(type(name))
print(type(is_student))
```

---

## Answer 3

```python
name = "Soyab"
age = 21
course = "BCA"
college = "K.A. Lokapur College"
percentage = 85.5

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("College:", college)
print("Percentage:", percentage)
```

---

## Answer 4

```python
birth_year = 2005
current_year = 2026

age = current_year - birth_year

print("Age:", age)
```

---

## Answer 5

```python
age = "21"
marks = "85.5"

age = int(age)
marks = float(marks)

print(age, type(age))
print(marks, type(marks))
```

---

## Answer 6

```python
a = "10"
b = "20"

a = int(a)
b = int(b)

print(a + b)
```

Output:

```text
30
```

---

## Answer 7

```python
age = 21

age_text = str(age)

message = "I am " + age_text + " years old."

print(message)
```

---

## Answer 8

```text
int       → Immutable
float     → Immutable
str       → Immutable
list      → Mutable
tuple     → Immutable
set       → Mutable
dict      → Mutable
bool      → Immutable
```

---

## Answer 9

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

---

## Answer 10

Direct modification fails because strings are immutable.

A correct approach:

```python
name = "Python"

name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

---

## Answer 11

```python
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)

numbers_list[0] = 100

print(numbers_list)
```

The list modification works.

The equivalent tuple modification raises a `TypeError`.

---

## Answer 12

```python
numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

---

## Answer 13

```python
student = {
    "name": "Soyab",
    "age": 21,
    "course": "BCA",
    "marks": 85
}

print(student["name"])
print(student["age"])
print(student["course"])
print(student["marks"])
```

---

## Answer 14

```python
student = {
    "name": "Soyab",
    "age": 21
}

student["age"] = 22
student["course"] = "BCA"

print(student)
```

---

## Answer 15

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

`==` checks equality of contents.

`is` checks whether both names refer to the same object.

---

## Answer 16

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Output:

```text
True
True
```

Both names refer to the same list object.

---

## Answer 17

```python
a = [10, 20, 30]

b = a.copy()

b.append(40)

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

---

## Answer 18

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

---

## Answer 19

```python
a = 100
b = 200

a, b = b, a

print(a)
print(b)
```

Output:

```text
200
100
```

---

## Answer 20

```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Python")) # True
print(bool([]))       # False
print(bool([1]))      # True
print(bool(None))     # False
```

---

## Answer 21

```python
a = 10
b = 10.5
c = "10"
d = True
e = [10]
f = (10,)
g = {10}
h = {"value": 10}
i = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
```

---

## Answer 22

```python
a = "10"
b = "20.5"
c = "30"

result = int(a) + float(b) + int(c)

print(result)
```

Output:

```text
60.5
```

---

## Answer 23

```python
math = 80
science = 75
english = 90

total = math + science + english
average = total / 3

print("Total:", total)
print("Average:", average)
```

---

## Answer 24

```python
student = ["Soyab", 21, ["Python", "HTML", "CSS"]]

print(student[0])
print(student[1])
print(student[2][0])
print(student[2][1])
print(student[2][2])
```

---

## Answer 25

```python
student = {
    "name": "Soyab",
    "marks": {
        "python": 85,
        "java": 75,
        "dbms": 80
    }
}

print(student["name"])
print(student["marks"]["python"])
print(student["marks"]["java"])
print(student["marks"]["dbms"])
```

---

## Answer 26

```python
result = None

if result is None:
    print("Result is not available")
```

---

## Answer 27

```python
value = 10
value = "Python"
value = [1, 2, 3]

print(value)
print(type(value))
```

Output:

```text
[1, 2, 3]
<class 'list'>
```

Python allows this because names are dynamically bound to objects.

---

## Answer 28

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

`a` and `b` refer to the same list object.

---

## Answer 29

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)

print(a)
print(b)
```

Output:

```text
[[1, 2, 100], [3, 4]]
[[1, 2, 100], [3, 4]]
```

The outer list was copied, but the nested lists were still shared.

---

## Answer 30

One possible solution:

```python
name = "Soyab"
age = 21
percentage = 85.5
is_student = True

skills = ["Python", "HTML", "CSS"]
coordinates = (15, 20)
unique_numbers = {1, 2, 3}

student = {
    "name": name,
    "age": age,
    "course": "BCA"
}

result = None

print(name)
print(age)
print(percentage)
print(is_student)
print(skills)
print(coordinates)
print(unique_numbers)
print(student)
print(result)
```

---

# 36. How to Practice This File

Follow this order:

```text
Step 1
Learn variables
        ↓
Step 2
Learn int, float, str, bool
        ↓
Step 3
Learn list, tuple, set, dict
        ↓
Step 4
Learn mutable vs immutable
        ↓
Step 5
Learn == vs is
        ↓
Step 6
Practice type()
        ↓
Step 7
Practice type conversion
        ↓
Step 8
Practice references and copying
        ↓
Step 9
Solve all 30 exercises
        ↓
Step 10
Explain your solutions without looking at the notes
```

For beginner practice, first solve **Practice 1–15**. Once those are comfortable, move to **16–30**.

---

# 37. Interview Questions and Answers

## Q1. What is a variable in Python?

A variable is a name bound to an object. Python variables do not require an explicit type declaration.

---

## Q2. Is Python statically typed or dynamically typed?

Python is dynamically typed. A name can be rebound to objects of different types during program execution.

---

## Q3. Is Python strongly typed?

Yes. Python is generally considered strongly typed because it does not freely treat unrelated types as interchangeable.

For example:

```python
print("10" + 5)
```

raises a `TypeError`.

---

## Q4. What is the difference between mutable and immutable objects?

Mutable objects can be changed after creation, while immutable objects cannot be changed after creation.

Examples:

```text
Mutable:
list, dict, set

Immutable:
int, float, bool, str, tuple
```

---

## Q5. What is the difference between `==` and `is`?

`==` checks equality, while `is` checks object identity.

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True
print(a is b)   # False
```

---

## Q6. What does `id()` do?

`id()` returns an integer identifying an object during its lifetime.

The exact representation is implementation-dependent.

---

## Q7. What does `type()` do?

`type()` returns the type of an object.

```python
x = 10

print(type(x))
```

---

## Q8. What is `None`?

`None` is a special singleton object representing the absence of a value.

---

## Q9. What is type conversion?

Type conversion means converting a value from one data type to another.

```python
age = "21"
age = int(age)
```

---

## Q10. What is the difference between a list and tuple?

Both are ordered collections, but lists are mutable while tuples are immutable.

---

## Q11. What is a set?

A set is a collection designed for unique elements and set operations. It does not support indexing like a list.

---

## Q12. What is a dictionary?

A dictionary stores data as key-value pairs.

---

## Q13. Does Python have constants?

Python does not provide an enforced `const` keyword for ordinary variables. Uppercase names are used by convention.

---

## Q14. What is variable reassignment?

Variable reassignment means binding an existing name to another object.

```python
x = 10
x = 20
```

---

# 38. Quick Revision

```text
Variable
→ A name bound to an object

Dynamic typing
→ A name can be rebound to objects of different types

int
→ Whole numbers

float
→ Floating-point numbers

complex
→ Real + imaginary numbers

bool
→ True / False

str
→ Text, immutable

list
→ Ordered, mutable collection

tuple
→ Ordered, immutable collection

set
→ Unique-element collection

dict
→ Key-value mapping

None
→ Absence of a value

Mutable
→ Can be changed after creation

Immutable
→ Cannot be changed after creation

type()
→ Returns an object's type

id()
→ Returns an object's identity identifier

==
→ Equality comparison

is
→ Identity comparison

int(), float(), str(), bool()
→ Common type-conversion functions

a = b
→ Both names can refer to the same object

a.copy()
→ Shallow copy

copy.deepcopy(a)
→ Deep copy
```

---

# 39. Final Interview Tip

When explaining Python variables in an interview, avoid saying only:

> "A variable is a container that stores a value."

That is a useful beginner analogy, but a more technically accurate answer is:

> **"In Python, a variable is a name that is bound to an object. The object has a type, value, and identity, and because Python is dynamically typed, the same name can later be rebound to an object of a different type."**
