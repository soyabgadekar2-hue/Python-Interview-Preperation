# Python Control Flow — Learning & Interview Notes

## 1. What Is Control Flow?

**Control flow** means the order in which Python executes statements in a program.

Normally, Python executes code from top to bottom:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

But real programs need to make decisions and repeat actions.

For example:

* If a student passes, display `"Pass"`.
* If the password is incorrect, reject login.
* Repeat a task 10 times.
* Stop a loop when a condition is satisfied.

Python provides:

1. Conditional statements
2. Loops
3. Loop-control statements

---

# 2. Conditional Statements

Conditional statements allow Python to **make decisions**.

The main conditional statements are:

```text
if
if-else
if-elif-else
nested if
```

---

# 3. `if` Statement

The `if` statement executes code only when a condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

Output:

```text
You are eligible to vote
```

If the condition is `False`, the indented code is skipped.

---

# 4. Indentation

Python uses **indentation** to define blocks of code.

Correct:

```python
age = 20

if age >= 18:
    print("Adult")
```

Incorrect:

```python
age = 20

if age >= 18:
print("Adult")
```

Usually, Python code uses **4 spaces** for indentation.

Indentation is not just formatting in Python. It is part of the syntax.

---

# 5. `if-else` Statement

Use `if-else` when there are two possible paths.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

The `if` block runs when the condition is `True`.

The `else` block runs when the condition is `False`.

---

# 6. `if-elif-else`

When there are multiple conditions, use `elif`.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
else:
    statement
```

### Example

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

Output:

```text
A
```

Python checks the conditions from top to bottom.

Once it finds a `True` condition, its block executes and the remaining `elif` conditions are skipped.

---

# 7. Order of Conditions Matters

Consider:

```python
marks = 85

if marks >= 60:
    print("B")
elif marks >= 75:
    print("A")
```

Output:

```text
B
```

Why?

Because:

```python
marks >= 60
```

is already `True`.

Python does not continue checking the later `elif`.

Correct ordering:

```python
if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

Put more specific or higher thresholds first when the conditions overlap.

---

# 8. Nested `if`

An `if` statement inside another `if` statement is called a **nested if**.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

Output:

```text
Entry allowed
```

Nested conditions are useful when one decision depends on another.

However, too much nesting can make code difficult to read.

---

# 9. Combining Conditions

Conditions can be combined using logical operators:

```python
and
or
not
```

### Example with `and`

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

Both conditions must be true.

### Example with `or`

```python
is_student = True
has_pass = False

if is_student or has_pass:
    print("Access allowed")
```

At least one condition must be true.

### Example with `not`

```python
logged_in = False

if not logged_in:
    print("Please login")
```

---

# 10. Conditions Use Truthiness

Python conditions do not have to produce an actual `True` or `False` value.

Python evaluates objects according to their **truth value**.

Example:

```python
name = "Soyab"

if name:
    print("Name is available")
```

An empty string is falsey:

```python
name = ""

if not name:
    print("Name is empty")
```

Common falsey values include:

```python
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

---

# 11. `for` Loop

A `for` loop is used to iterate over items in an iterable.

### Example

```python
for number in [1, 2, 3, 4, 5]:
    print(number)
```

Output:

```text
1
2
3
4
5
```

The loop takes one item at a time.

---

# 12. `for` Loop with a String

Strings are iterable.

```python
name = "Python"

for character in name:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

---

# 13. `for` Loop with a List

```python
sports = ["Cricket", "Football", "Basketball"]

for sport in sports:
    print(sport)
```

Output:

```text
Cricket
Football
Basketball
```

---

# 14. `for` Loop with a Dictionary

Iterating over a dictionary directly gives its keys.

```python
student = {
    "name": "Soyab",
    "age": 21
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

To access both keys and values:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Soyab
age 21
```

---

# 15. `range()`

`range()` is commonly used when you want a sequence of numbers.

### Example

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

The stop value is not included.

---

# 16. `range(start, stop)`

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

Here:

```text
start = 1
stop = 6
```

The loop stops before `6`.

---

# 17. `range(start, stop, step)`

The third argument controls the step.

```python
for number in range(1, 10, 2):
    print(number)
```

Output:

```text
1
3
5
7
9
```

Negative steps are also possible:

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

---

# 18. `while` Loop

A `while` loop repeatedly executes code as long as its condition is true.

### Syntax

```python
while condition:
    statement
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# 19. How a `while` Loop Works

Consider:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

Execution:

```text
count = 1
1 <= 3 → True → print 1
count = 2
2 <= 3 → True → print 2
count = 3
3 <= 3 → True → print 3
count = 4
4 <= 3 → False → stop
```

The condition is checked before each iteration.

---

# 20. Infinite `while` Loop

A loop becomes infinite when its condition never becomes false.

Example:

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes, so the condition remains true.

A common solution is to update the loop variable:

```python
count += 1
```

---

# 21. `break`

`break` immediately stops the loop.

### Example

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

When `number` becomes `5`, the loop terminates.

---

# 22. `continue`

`continue` skips the current iteration and moves to the next iteration.

### Example

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

Only the iteration containing `3` is skipped.

---

# 23. `break` vs `continue`

| Statement  | Purpose                     |
| ---------- | --------------------------- |
| `break`    | Stops the entire loop       |
| `continue` | Skips the current iteration |

Example:

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Output:

```text
1
2
```

With `continue`:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

---

# 24. `pass`

`pass` does nothing.

It is used as a placeholder when Python requires a statement but you do not want to execute anything yet.

Example:

```python
age = 20

if age >= 18:
    pass
```

The program does nothing inside the block.

You can later replace `pass` with actual code.

---

# 25. `pass` vs `continue`

These are different.

### `pass`

Does nothing.

```python
for number in range(3):
    pass
```

### `continue`

Skips the rest of the current iteration.

```python
for number in range(3):
    if number == 1:
        continue

    print(number)
```

---

# 26. Loop `else`

Python allows an `else` block with `for` and `while` loops.

The `else` block executes when the loop finishes **normally**, meaning it was not terminated by `break`.

### Example

```python
for number in range(3):
    print(number)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
Loop completed
```

With `break`:

```python
for number in range(5):
    if number == 2:
        break

    print(number)
else:
    print("Loop completed")
```

Output:

```text
0
1
```

The `else` block does not execute because `break` terminated the loop.

---

# 27. `enumerate()`

`enumerate()` gives both the index and the item while iterating.

Without `enumerate()`:

```python
sports = ["Cricket", "Football", "Basketball"]

for sport in sports:
    print(sport)
```

With `enumerate()`:

```python
sports = ["Cricket", "Football", "Basketball"]

for index, sport in enumerate(sports):
    print(index, sport)
```

Output:

```text
0 Cricket
1 Football
2 Basketball
```

You can choose the starting index:

```python
for index, sport in enumerate(sports, start=1):
    print(index, sport)
```

Output:

```text
1 Cricket
2 Football
3 Basketball
```

---

# 28. Nested Loops

A loop inside another loop is called a **nested loop**.

Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

For every iteration of the outer loop, the inner loop runs completely.

---

# 29. Practical Example — Check Marks

```python
marks = 78

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# 30. Practical Example — Grade System

```python
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)
```

Output:

```text
Grade: A
```

---

# 31. Practical Example — Login Validation

```python
username = "soyab"
password = "1234"

if username == "soyab" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
```

---

# 32. Practical Example — Discount

```python
amount = 2500

if amount >= 5000:
    discount = 20
elif amount >= 2000:
    discount = 10
else:
    discount = 0

print("Discount:", discount, "%")
```

---

# 33. Practical Example — Access Control

```python
age = 21
has_id = True

if age >= 18:
    if has_id:
        print("Access allowed")
    else:
        print("ID required")
else:
    print("Access denied")
```

---

# 34. Practical Example — Check Skills

```python
skills = ["Python", "HTML", "CSS"]

if "Python" in skills:
    print("Python skill found")
else:
    print("Python skill not found")
```

---

# 35. Practical Example — Placement Eligibility

```python
percentage = 72
has_backlog = False

if percentage >= 60 and not has_backlog:
    print("Eligible for placement")
else:
    print("Not eligible")
```

---

# 36. Practical Example — Electricity Bill

A simple example using conditions:

```python
units = 120

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Bill:", bill)
```

This is only a programming exercise. Real electricity tariffs depend on the applicable utility and tariff structure.

---

# 37. Practical Example — Find Even Numbers

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

Output:

```text
2
4
6
8
10
```

---

# 38. Practical Example — Sum of Numbers

```python
total = 0

for number in range(1, 6):
    total += number

print("Sum:", total)
```

Output:

```text
Sum: 15
```

---

# 39. Practical Example — Search for a Value

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found")
        break
```

Here `break` prevents unnecessary further iteration after finding the required value.

---

# 40. Choosing the Correct Loop

### Use `for` when:

You are iterating over a collection or a known sequence of values.

```python
for item in items:
    print(item)
```

### Use `while` when:

The repetition depends mainly on a condition and the number of iterations may not be known beforehand.

```python
while condition:
    ...
```

---

# 41. `for` vs `while`

| `for`                                                | `while`                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| Commonly used for iterables                          | Commonly used for condition-based repetition                 |
| Convenient with lists, strings, ranges, dictionaries | Useful when the stopping condition changes during execution  |
| Often used when iterating through known data         | Useful when the number of iterations is not known in advance |

Example:

```python
for number in range(5):
    print(number)
```

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Both can produce similar results, but the appropriate choice depends on the problem.

---

# 42. Common Control Flow Mistakes

## Mistake 1 — Forgetting `:`

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 2 — Incorrect indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 3 — Infinite `while` loop

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Mistake 4 — Using `=` instead of `==`

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

`=` is assignment.

`==` compares values.

---

## Mistake 5 — Incorrect condition order

Incorrect:

```python
marks = 95

if marks >= 40:
    print("Pass")
elif marks >= 90:
    print("A+")
```

The first condition is already true.

Correct:

```python
if marks >= 90:
    print("A+")
elif marks >= 40:
    print("Pass")
```

---

## Mistake 6 — Confusing `break` and `continue`

Remember:

```text
break    → stop the loop
continue → skip this iteration
```

---

# 43. Beginner Practice

Try solving these without looking at the answers first.

## Task 1 — Positive, Negative, or Zero

Write a program that checks whether a number is:

* Positive
* Negative
* Zero

---

## Task 2 — Even or Odd

Write a program that checks whether a number is even or odd.

Example:

```text
Input: 8
Output: Even
```

---

## Task 3 — Grade Calculator

Accept marks and display:

```text
90+  → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → F
```

---

## Task 4 — Print Numbers

Use a `for` loop to print:

```text
1
2
3
4
5
```

---

## Task 5 — Print Even Numbers

Print all even numbers from 1 to 20.

---

## Task 6 — Reverse Countdown

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

---

## Task 7 — Sum

Find the sum of numbers from 1 to 100.

---

## Task 8 — Multiplication Table

Accept a number and print its multiplication table.

Example:

```text
Input: 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Task 9 — Find a Number

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Search for `30`.

Stop the loop when the number is found.

---

## Task 10 — Skip Multiples of 3

Print numbers from 1 to 20 but skip numbers divisible by 3.

Use `continue`.

---

## Task 11 — Login Attempts

Allow a user three attempts to enter the correct password.

Stop immediately when the correct password is entered.

Use:

* `while`
* `if`
* `break`

---

## Task 12 — Placement Eligibility

Accept:

* Percentage
* Backlog status

Display whether the student is eligible.

---

# 44. Practice Answers

## Answer 1

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## Answer 2

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Answer 3

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("F")
```

---

## Answer 4

```python
for number in range(1, 6):
    print(number)
```

---

## Answer 5

```python
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
```

---

## Answer 6

```python
count = 10

while count >= 1:
    print(count)
    count -= 1
```

---

## Answer 7

```python
total = 0

for number in range(1, 101):
    total += number

print(total)
```

---

## Answer 8

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

---

## Answer 9

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found")
        break
```

---

## Answer 10

```python
for number in range(1, 21):
    if number % 3 == 0:
        continue

    print(number)
```

---

## Answer 11

```python
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")
    attempts += 1
```

---

## Answer 12

```python
percentage = float(input("Enter percentage: "))
has_backlog = input("Do you have a backlog? (yes/no): ")

if percentage >= 60 and has_backlog == "no":
    print("Eligible for placement")
else:
    print("Not eligible")
```

---

# 45. Interview Questions and Answers

## Q1. What is control flow in Python?

**Answer:**

Control flow is the order in which Python executes statements. Python provides conditional statements, loops, and control statements to control program execution.

---

## Q2. What is an `if` statement?

**Answer:**

An `if` statement executes a block of code when its condition evaluates to true.

Example:

```python
if age >= 18:
    print("Adult")
```

---

## Q3. What is the difference between `if`, `elif`, and `else`?

**Answer:**

* `if` checks the first condition.
* `elif` checks additional conditions if previous conditions were false.
* `else` executes when none of the preceding conditions are true.

---

## Q4. What is a nested `if`?

**Answer:**

A nested `if` is an `if` statement placed inside another `if` statement.

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

---

## Q5. What is a loop?

**Answer:**

A loop repeatedly executes a block of code.

Python mainly provides:

```text
for
while
```

---

## Q6. What is a `for` loop?

**Answer:**

A `for` loop iterates over an iterable such as a list, string, tuple, dictionary, set, or range.

Example:

```python
for number in range(5):
    print(number)
```

---

## Q7. What is a `while` loop?

**Answer:**

A `while` loop repeatedly executes a block as long as its condition remains true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Q8. What is the difference between `for` and `while`?

**Answer:**

`for` is commonly used to iterate over an iterable, while `while` is commonly used when repetition depends on a condition.

---

## Q9. What does `break` do?

**Answer:**

`break` immediately terminates the nearest enclosing loop.

---

## Q10. What does `continue` do?

**Answer:**

`continue` skips the remaining statements in the current iteration and proceeds to the next iteration.

---

## Q11. What does `pass` do?

**Answer:**

`pass` is a null statement. It performs no operation and is commonly used as a placeholder.

---

## Q12. Can `else` be used with loops?

**Answer:**

Yes. Python allows `else` with both `for` and `while` loops. The `else` block runs when the loop completes normally without encountering `break`.

---

## Q13. What is `range()`?

**Answer:**

`range()` represents an arithmetic sequence of integers and is commonly used for iteration.

Example:

```python
range(1, 6)
```

produces values:

```text
1, 2, 3, 4, 5
```

---

## Q14. What is `enumerate()`?

**Answer:**

`enumerate()` allows you to iterate over an iterable while receiving both the index and the value.

```python
names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)
```

---

## Q15. What is an infinite loop?

**Answer:**

An infinite loop is a loop whose condition never becomes false.

Example:

```python
while True:
    print("Running")
```

It can be intentionally used in some programs, but an accidental infinite loop is usually caused by incorrect loop logic.

---

## Q16. Why is indentation important in Python?

**Answer:**

Python uses indentation to define code blocks. Incorrect indentation can result in an `IndentationError` or change the structure of the program.

---

## Q17. What happens if multiple `elif` conditions are true?

**Answer:**

Python executes the first matching `if` or `elif` block and skips the remaining branches.

---

## Q18. What is short-circuit evaluation?

**Answer:**

Python may stop evaluating a logical expression as soon as its final result is known.

For example:

```python
False and something
```

does not need to evaluate `something`.

Similarly:

```python
True or something
```

does not need to evaluate `something`.

This behavior is useful for both performance and safe conditional checks.

---

# 46. Quick Revision

## Conditional Statements

```python
if
if-else
if-elif-else
nested if
```

## Loops

```python
for
while
```

## Loop Control

```python
break
continue
pass
```

## Useful Tools

```python
range()
enumerate()
```

---

# 47. Control Flow Cheat Sheet

```text
if
↓
Make one decision

if-else
↓
Choose between two paths

if-elif-else
↓
Choose between multiple paths

for
↓
Iterate over an iterable

while
↓
Repeat while a condition is true

break
↓
Stop the loop

continue
↓
Skip current iteration

pass
↓
Do nothing / placeholder

range()
↓
Generate an integer sequence

enumerate()
↓
Get index + value while iterating
```

---

# 48. Final Interview Explanation

If an interviewer asks:

**"Explain control flow in Python."**

You can answer:

> "Control flow determines the order in which Python executes a program. Python provides conditional statements such as `if`, `elif`, and `else` for decision-making. It provides `for` and `while` loops for repetition. We can control loops using `break`, `continue`, and `pass`. Python also provides useful tools such as `range()` for integer sequences and `enumerate()` for accessing both indexes and values while iterating."

This is a concise and interview-ready answer.

---

# 49. Learning Order

For beginners, learn control flow in this order:

```text
1. if
2. if-else
3. if-elif-else
4. Nested if
5. Logical conditions
6. for loop
7. range()
8. while loop
9. break
10. continue
11. pass
12. Loop else
13. enumerate()
14. Nested loops
15. Practical problems
```

After learning this file, you should be able to build programs involving:

* Decision making
* Repetition
* Searching
* Validation
* Number processing
* Student grading
* Login checks
* Eligibility checks
* Simple menus
* Basic business logic
