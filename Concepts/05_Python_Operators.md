# Python Operators — Learning & Interview Notes

## 1. What Are Operators?

**Operators** are symbols or keywords used to perform operations on values and objects.

Example:

```python
a = 10
b = 3

print(a + b)
```

Here:

* `a` and `b` → operands
* `+` → operator

Output:

```text
13
```

---

# 2. Types of Python Operators

Python provides several categories of operators:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
8. Conditional expression

---

# 3. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Name           | Example   |     Result |
| -------- | -------------- | --------- | ---------: |
| `+`      | Addition       | `10 + 3`  |       `13` |
| `-`      | Subtraction    | `10 - 3`  |        `7` |
| `*`      | Multiplication | `10 * 3`  |       `30` |
| `/`      | Division       | `10 / 3`  | `3.333...` |
| `//`     | Floor division | `10 // 3` |        `3` |
| `%`      | Modulus        | `10 % 3`  |        `1` |
| `**`     | Exponentiation | `10 ** 3` |     `1000` |

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

---

# 4. Division `/`

The `/` operator performs true division.

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

Even when both operands are integers, `/` normally produces a `float`.

```python
print(type(10 / 2))
```

Output:

```text
<class 'float'>
```

---

# 5. Floor Division `//`

Floor division returns the mathematical floor of the division result.

```python
print(10 // 3)
```

Output:

```text
3
```

An important detail is that floor division is **not simply truncation toward zero**.

For example:

```python
print(-10 // 3)
```

Output:

```text
-4
```

Because:

```text
-10 / 3 ≈ -3.333
floor(-3.333) = -4
```

---

# 6. Modulus `%`

The modulus operator returns the remainder from division.

```python
print(10 % 3)
```

Output:

```text
1
```

A common use is checking whether a number is even:

```python
number = 10

if number % 2 == 0:
    print("Even")
```

---

# 7. Exponentiation `**`

`**` calculates a power.

```python
print(2 ** 3)
```

Output:

```text
8
```

Meaning:

```text
2 × 2 × 2 = 8
```

---

# 8. Assignment Operators

Assignment operators assign or update values.

### Basic assignment

```python
x = 10
```

The `=` operator assigns the value `10` to the name `x`.

### Compound assignment operators

| Operator | Example   | Equivalent idea        |      |                       |
| -------- | --------- | ---------------------- | ---- | --------------------- |
| `=`      | `x = 5`   | Assign                 |      |                       |
| `+=`     | `x += 5`  | `x = x + 5`            |      |                       |
| `-=`     | `x -= 5`  | `x = x - 5`            |      |                       |
| `*=`     | `x *= 5`  | `x = x * 5`            |      |                       |
| `/=`     | `x /= 5`  | `x = x / 5`            |      |                       |
| `//=`    | `x //= 5` | `x = x // 5`           |      |                       |
| `%=`     | `x %= 5`  | `x = x % 5`            |      |                       |
| `**=`    | `x **= 5` | `x = x ** 5`           |      |                       |
| `&=`     | `x &= 5`  | Bitwise AND assignment |      |                       |
| `        | =`        | `x                     | = 5` | Bitwise OR assignment |
| `^=`     | `x ^= 5`  | Bitwise XOR assignment |      |                       |
| `<<=`    | `x <<= 1` | Left-shift assignment  |      |                       |
| `>>=`    | `x >>= 1` | Right-shift assignment |      |                       |

Example:

```python
x = 10

x += 5
print(x)

x *= 2
print(x)
```

Output:

```text
15
30
```

---

# 9. Comparison Operators

Comparison operators compare values.

The result is normally a Boolean value:

```text
True
False
```

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
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
```

Output:

```text
False
True
True
False
True
False
```

---

# 10. `==` vs `is`

This is an important interview question.

### `==`

Checks whether two objects are equal in value.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

### `is`

Checks whether two names refer to the same object.

```python
print(a is b)
```

Output:

```text
False
```

So:

```text
== → equality
is → identity
```

Use `is` for identity checks, especially:

```python
if value is None:
    ...
```

Do not generally use `is` as a replacement for `==` when comparing ordinary values.

---

# 11. Chained Comparisons

Python allows comparisons to be chained.

Instead of:

```python
age >= 18 and age <= 60
```

you can write:

```python
18 <= age <= 60
```

Example:

```python
age = 21

print(18 <= age <= 60)
```

Output:

```text
True
```

This is equivalent in meaning to checking both comparisons with `and`.

---

# 12. Logical Operators

Python has three logical operators:

```text
and
or
not
```

They work with truth values and use short-circuit evaluation.

---

# 13. `and`

`and` requires both conditions to be truthy for the overall expression to be truthy.

Example:

```python
age = 21
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

Output:

```text
Allowed
```

### Important Python behavior

`and` does not always return `True` or `False`.

It returns one of its operands.

Example:

```python
print("Hello" and "Python")
```

Output:

```text
Python
```

Python first evaluates `"Hello"`. Since it is truthy, it evaluates and returns `"Python"`.

---

# 14. `or`

`or` returns the first truthy operand, or the last operand if none is truthy.

Example:

```python
print("" or "Guest")
```

Output:

```text
Guest
```

This behavior is often used for default values.

```python
name = ""

display_name = name or "Guest"

print(display_name)
```

Output:

```text
Guest
```

---

# 15. `not`

`not` reverses truthiness.

```python
is_logged_in = False

if not is_logged_in:
    print("Please login")
```

Output:

```text
Please login
```

Unlike `and` and `or`, `not` produces a Boolean result.

---

# 16. Short-Circuit Evaluation

Python may stop evaluating a logical expression as soon as its result is known.

### With `and`

If the first operand is falsy, Python does not need to evaluate the rest.

```python
False and some_function()
```

`some_function()` is not called.

### With `or`

If the first operand is truthy, Python does not need to evaluate the rest.

```python
True or some_function()
```

`some_function()` is not called.

This can improve efficiency and can also prevent unnecessary or unsafe operations.

Example:

```python
numbers = []

if numbers and numbers[0] > 10:
    print("Greater than 10")
```

Because `numbers` is empty and therefore falsy, Python does not evaluate:

```python
numbers[0]
```

This prevents an `IndexError`.

---

# 17. Truthy and Falsy Values

Python uses **truthiness** when evaluating objects in conditions.

Common falsy values include:

```text
False
None
0
0.0
""
[]
()
{}
set()
```

Most other objects are truthy.

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

# 18. Identity Operators

Python has two identity operators:

```text
is
is not
```

They check object identity.

Example:

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a is not c)
```

Output:

```text
True
False
True
```

Remember:

```text
is → same object?
is not → different objects?
```

---

# 19. Membership Operators

Membership operators check whether a value exists in a collection or other supported container.

Python provides:

```text
in
not in
```

Example with a list:

```python
languages = ["Python", "Java", "JavaScript"]

print("Python" in languages)
print("C++" not in languages)
```

Output:

```text
True
True
```

---

# 20. Membership with Strings

Membership can also be used with strings.

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
```

Output:

```text
True
False
```

String membership is case-sensitive:

```python
print("python" in "Python")
```

Output:

```text
False
```

---

# 21. Membership with Dictionaries

For dictionaries, membership normally checks **keys**, not values.

```python
student = {
    "name": "Soyab",
    "age": 21
}

print("name" in student)
print("Soyab" in student)
```

Output:

```text
True
False
```

To check values:

```python
print("Soyab" in student.values())
```

Output:

```text
True
```

---

# 22. Bitwise Operators

Bitwise operators work with the bits of integer values.

Python provides:

| Operator | Name        |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left shift  |            |
| `>>`     | Right shift |            |

These are commonly used in areas such as:

* Low-level programming
* Flags
* Binary data
* Algorithms
* Networking
* Performance-sensitive operations

---

# 23. Bitwise AND `&`

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

Output:

```text
1
```

A bit becomes `1` only when both corresponding bits are `1`.

---

# 24. Bitwise OR `|`

A bit becomes `1` if at least one corresponding bit is `1`.

```python
print(5 | 3)
```

Binary:

```text
101
011
---
111
```

Output:

```text
7
```

---

# 25. Bitwise XOR `^`

XOR produces `1` when the corresponding bits are different.

```python
print(5 ^ 3)
```

Binary:

```text
101
011
---
110
```

Output:

```text
6
```

---

# 26. Bitwise NOT `~`

`~` inverts the bits according to Python's integer representation.

Example:

```python
print(~5)
```

Output:

```text
-6
```

For integers, Python's behavior can be understood using the identity:

```text
~x == -(x + 1)
```

Therefore:

```text
~5 = -(5 + 1) = -6
```

---

# 27. Left Shift `<<`

Left shift moves the bits to the left.

```python
print(5 << 1)
```

Conceptually:

```text
101 → 1010
```

Output:

```text
10
```

For non-negative integers, shifting left by one position is equivalent to multiplying by 2.

---

# 28. Right Shift `>>`

Right shift moves the bits to the right.

```python
print(10 >> 1)
```

Conceptually:

```text
1010 → 0101
```

Output:

```text
5
```

For non-negative integers, shifting right by one position is equivalent to integer division by 2.

---

# 29. Conditional Expression

Python supports a compact conditional expression:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 21

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

It is commonly called a **ternary operator**, although **conditional expression** is the more precise Python terminology.

---

# 30. Conditional Expression vs Normal `if`

Normal `if`:

```python
age = 21

if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

Conditional expression:

```python
status = "Adult" if age >= 18 else "Minor"
```

Use the conditional expression for short, simple choices.

For complex logic, normal `if` statements are usually clearer.

---

# 31. Operator Precedence

When an expression contains multiple operators, Python follows rules that determine which operations are performed first.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication happens before addition:

```text
5 * 2 = 10
10 + 10 = 20
```

---

# 32. Parentheses

Use parentheses when you want to make the order explicit.

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

Compare:

```python
10 + 5 * 2
```

with:

```python
(10 + 5) * 2
```

The parentheses change the order.

### Good practice

Even when you know the precedence rules, parentheses can make complex expressions easier to read.

---

# 33. Simplified Operator Precedence

A useful simplified order is:

```text
1. Parentheses
2. Exponentiation **
3. Unary +, -, ~
4. *, /, //, %
5. +, -
6. Comparisons
7. not
8. and
9. or
```

Python's complete precedence table contains additional details, so use the official documentation when dealing with complex expressions.

---

# 34. Operators with Strings

The `+` operator can concatenate strings.

```python
first = "Hello"
second = "Python"

print(first + " " + second)
```

Output:

```text
Hello Python
```

The `*` operator can repeat a string:

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

Operators can have different meanings depending on the operand types.

---

# 35. Operators with Lists

The `+` operator can concatenate lists.

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

Output:

```text
[1, 2, 3, 4]
```

The `*` operator can repeat a list:

```python
print([1, 2] * 3)
```

Output:

```text
[1, 2, 1, 2, 1, 2]
```

---

# 36. Operator Overloading

Python allows classes to define how certain operators behave for their objects.

For example, a class can implement:

```text
__add__()  → +
__eq__()   → ==
__lt__()   → <
```

Example:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(10)
b = Number(20)

result = a + b

print(result.value)
```

Output:

```text
30
```

The `+` operator is being customized for the `Number` class.

---

# 37. Operator Categories — Quick Table

| Category    | Operators                                               |
| ----------- | ------------------------------------------------------- |
| Arithmetic  | `+ - * / // % **`                                       |
| Assignment  | `= += -= *= /= //= %= **=` and bitwise assignment forms |
| Comparison  | `== != > < >= <=`                                       |
| Logical     | `and or not`                                            |
| Identity    | `is is not`                                             |
| Membership  | `in not in`                                             |
| Bitwise     | `& \| ^ ~ << >>`                                        |
| Conditional | `x if condition else y`                                 |

---

# 38. Common Mistakes

## Mistake 1 — Using `=` instead of `==`

Incorrect:

```python
if age = 18:
    print("18")
```

Correct:

```python
if age == 18:
    print("18")
```

`=` assigns.

`==` compares.

---

## Mistake 2 — Using `is` for normal value comparison

Avoid:

```python
a is 10
```

when the intention is to compare values.

Prefer:

```python
a == 10
```

Use `is` for identity checks.

A common and correct use is:

```python
value is None
```

---

## Mistake 3 — Assuming `//` truncates toward zero

For example:

```python
-10 // 3
```

is:

```text
-4
```

because floor division uses mathematical floor.

---

## Mistake 4 — Assuming `and` and `or` always return Boolean values

For example:

```python
print("Hello" and "Python")
```

returns:

```text
Python
```

They return operands according to Python's short-circuit rules.

---

## Mistake 5 — Forgetting operator precedence

```python
10 + 5 * 2
```

is:

```text
20
```

not:

```text
30
```

Use parentheses when clarity is important.

---

## Mistake 6 — Forgetting dictionary membership checks keys

```python
student = {"name": "Soyab"}

print("Soyab" in student)
```

returns:

```text
False
```

because dictionary membership checks keys by default.

---

# 39. Beginner Practice

## Practice 1 — Arithmetic

Write a program that accepts two numbers and displays:

* Addition
* Subtraction
* Multiplication
* Division
* Floor division
* Modulus
* Exponentiation

---

## Practice 2 — Even or Odd

Use `%` to determine whether a number is even or odd.

Example:

```text
Input: 10
Output: Even
```

---

## Practice 3 — Comparison

Take two numbers and display whether:

* First is greater
* First is smaller
* Both are equal

---

## Practice 4 — Logical Operators

Create a simple access check using:

```text
age >= 18
has_id == True
```

Allow access only when both conditions are true.

---

## Practice 5 — Membership

Given:

```python
languages = ["Python", "Java", "JavaScript"]
```

Check whether `"Python"` and `"C++"` are present.

---

## Practice 6 — Dictionary Membership

Given:

```python
student = {
    "name": "Soyab",
    "age": 21,
    "course": "BCA"
}
```

Check:

1. Whether `"name"` is a key.
2. Whether `"Soyab"` is a key.
3. Whether `"Soyab"` is a value.

---

## Practice 7 — Identity

Create:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
```

Test:

```python
a is b
a is c
```

Explain the results.

---

## Practice 8 — Conditional Expression

Write a conditional expression that assigns:

```text
"Pass"
```

when marks are at least `40`, otherwise:

```text
"Fail"
```

---

## Practice 9 — Bitwise

Predict the results:

```python
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 << 1)
print(10 >> 1)
```

---

## Practice 10 — Operator Precedence

Predict:

```python
result = 10 + 5 * 2
```

Then change it to:

```python
result = (10 + 5) * 2
```

Explain why the answers differ.

---

# 40. Practice Answers

## Answer 1

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

---

## Answer 2

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Answer 3

```python
a = 10
b = 20

if a > b:
    print("First is greater")
elif a < b:
    print("First is smaller")
else:
    print("Both are equal")
```

---

## Answer 4

```python
age = 21
has_id = True

if age >= 18 and has_id:
    print("Access allowed")
else:
    print("Access denied")
```

---

## Answer 5

```python
languages = ["Python", "Java", "JavaScript"]

print("Python" in languages)
print("C++" in languages)
```

Output:

```text
True
False
```

---

## Answer 6

```python
student = {
    "name": "Soyab",
    "age": 21,
    "course": "BCA"
}

print("name" in student)
print("Soyab" in student)
print("Soyab" in student.values())
```

Output:

```text
True
False
True
```

---

## Answer 7

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
```

Output:

```text
True
False
```

`b` refers to the same object as `a`, while `c` is a different list with equal contents.

---

## Answer 8

```python
marks = 65

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

Output:

```text
Pass
```

---

## Answer 9

```python
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 << 1)
print(10 >> 1)
```

Output:

```text
1
7
6
10
5
```

---

## Answer 10

First:

```python
result = 10 + 5 * 2
```

Output:

```text
20
```

Because multiplication has higher precedence.

Second:

```python
result = (10 + 5) * 2
```

Output:

```text
30
```

Because parentheses force addition to happen first.

---

# 41. Interview Questions and Answers

## Q1. What is an operator?

**Answer:**

An operator is a symbol or keyword used to perform an operation on one or more operands.

---

## Q2. What are the types of operators in Python?

**Answer:**

The main categories are arithmetic, assignment, comparison, logical, identity, membership, bitwise, and conditional expressions.

---

## Q3. What is the difference between `/` and `//`?

**Answer:**

`/` performs true division and normally returns a floating-point result. `//` performs floor division and returns the mathematical floor of the division result.

---

## Q4. What does `%` do?

**Answer:**

The `%` operator returns the remainder of a division operation.

Example:

```python
10 % 3
```

returns:

```text
1
```

---

## Q5. What is the difference between `=` and `==`?

**Answer:**

`=` is used for assignment, while `==` checks equality.

---

## Q6. What is the difference between `==` and `is`?

**Answer:**

`==` checks whether two objects are equal according to their values, while `is` checks whether two references point to the same object.

---

## Q7. What are logical operators?

**Answer:**

Python has `and`, `or`, and `not`. They are used for logical expressions and use short-circuit evaluation. `and` and `or` can return operands rather than only Boolean values.

---

## Q8. What is short-circuit evaluation?

**Answer:**

Short-circuit evaluation means Python stops evaluating a logical expression once the result is already determined.

For example:

```python
False and function()
```

does not need to call `function()`.

---

## Q9. What are identity operators?

**Answer:**

The identity operators are `is` and `is not`. They test whether two references refer to the same object.

---

## Q10. What are membership operators?

**Answer:**

The membership operators are `in` and `not in`. They test whether an item is contained in a supported collection or container.

---

## Q11. What are bitwise operators?

**Answer:**

Bitwise operators operate on the binary representation of integers. They include `&`, `|`, `^`, `~`, `<<`, and `>>`.

---

## Q12. What is a ternary operator in Python?

**Answer:**

Python uses a conditional expression:

```python
value1 if condition else value2
```

It is commonly called the ternary operator, although "conditional expression" is more precise in Python terminology.

---

## Q13. What is operator precedence?

**Answer:**

Operator precedence determines the order in which operators are evaluated when an expression contains multiple operators.

For example:

```python
10 + 5 * 2
```

produces `20` because multiplication has higher precedence than addition.

---

## Q14. Can operators work differently depending on the data type?

**Answer:**

Yes. Python operators can have different behavior depending on the operand types.

For example:

```python
2 + 3
```

performs numeric addition, while:

```python
"Hello" + "Python"
```

concatenates strings.

---

## Q15. What is operator overloading?

**Answer:**

Operator overloading allows a class to define how operators behave with its objects using special methods such as `__add__()` and `__eq__()`.

---

## Q16. What does `and` return in Python?

**Answer:**

`and` returns one of its operands based on short-circuit evaluation. It does not necessarily return a Boolean.

Example:

```python
print("Hello" and "Python")
```

returns:

```text
Python
```

---

## Q17. What does `or` return in Python?

**Answer:**

`or` returns the first truthy operand. If all operands are falsy, it returns the last operand.

Example:

```python
print("" or "Guest")
```

returns:

```text
Guest
```

---

## Q18. Why should `is` be used with `None`?

**Answer:**

`None` is a singleton object in Python, so identity comparison is appropriate:

```python
if value is None:
    ...
```

Using `is` for ordinary value comparisons is generally incorrect because equality and identity are different concepts.

---

# 42. Quick Revision

```text
Operator
→ Performs an operation on operands

Arithmetic
→ +  -  *  /  //  %  **

Assignment
→ =  +=  -=  *=  /=  //=  %=  **=

Comparison
→ ==  !=  >  <  >=  <=

Logical
→ and  or  not

Identity
→ is  is not

Membership
→ in  not in

Bitwise
→ &  |  ^  ~  <<  >>

Conditional expression
→ value1 if condition else value2

/
→ True division

//
// → Floor division

%
→ Remainder

**
→ Power

==
→ Equality

is
→ Identity

and
→ Returns an operand using short-circuit evaluation

or
→ Returns the first truthy operand or the last operand

not
→ Negates truthiness

in
→ Membership check

Precedence
→ Determines evaluation order

Operator overloading
→ Classes can customize operator behavior
```

---

# 43. Final Interview Explanation

If an interviewer asks:

> **"What are operators in Python?"**

A strong answer is:

> **"Operators are symbols or keywords used to perform operations on values and objects. Python provides arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators, as well as conditional expressions. Some important distinctions are that `==` checks equality while `is` checks identity, `/` performs true division while `//` performs floor division, and `and` and `or` use short-circuit evaluation and can return operands."**
