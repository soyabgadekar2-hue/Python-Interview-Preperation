# Python Functions — Learning & Interview Notes

## 1. What Is a Function?

A **function** is a reusable block of code designed to perform a specific task.

Instead of writing the same code repeatedly, we can place it inside a function and call it whenever needed.

Example:

```python
def greet():
    print("Hello, Soyab")

greet()
```

Output:

```text
Hello, Soyab
```

### Basic structure

```python
def function_name():
    # function body
```

* `def` → keyword used to define a function
* `function_name` → name of the function
* `()` → parameter list
* `:` → starts the function body
* Indented code → function body

---

# 2. Why Do We Use Functions?

Functions provide:

* **Code reuse**
* **Better organization**
* **Readability**
* **Easier testing**
* **Easier debugging**
* **Modularity**
* **Less duplicate code**

Without a function:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With a function:

```python
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()
```

The function lets us write the logic once and reuse it.

---

# 3. Defining and Calling a Function

Defining a function does not execute its body.

```python
def hello():
    print("Hello")
```

The function runs when it is called:

```python
hello()
```

Output:

```text
Hello
```

Think of it as:

```text
Define
  ↓
Store function
  ↓
Call function
  ↓
Execute function body
```

---

# 4. Parameters and Arguments

These two terms are related but different.

### Parameter

A **parameter** is a variable written in the function definition.

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

An **argument** is the actual value supplied when calling the function.

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
Parameter → function definition
Argument  → function call
```

---

# 5. Function with Multiple Parameters

A function can accept multiple parameters.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

Here:

```text
a → 10
b → 20
```

---

# 6. The `return` Statement

`return` sends a value back to the code that called the function.

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

Conceptually:

```text
add(10, 20)
      ↓
    30
      ↓
result
```

---

# 7. `print()` vs `return`

This is an important interview concept.

### `print()`

Displays something on the screen.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

The function displays the result but does not return it for further use.

### `return`

Sends the result back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Now the returned value can be stored, used in another calculation, or passed to another function.

### Simple difference

```text
print() → display
return  → send value back
```

---

# 8. Function Without `return`

If a function reaches the end without returning a value, Python returns `None`.

```python
def hello():
    print("Hello")

result = hello()

print(result)
```

Output:

```text
Hello
None
```

The function printed `"Hello"` but returned `None`.

---

# 9. Returning Multiple Values

Python allows a function to return multiple values.

```python
def calculate(a, b):
    return a + b, a - b

result1, result2 = calculate(10, 5)

print(result1)
print(result2)
```

Output:

```text
15
5
```

Technically, Python returns these values together as a tuple:

```python
return (a + b, a - b)
```

---

# 10. Default Parameters

A parameter can have a default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Soyab")
```

Output:

```text
Hello Guest
Hello Soyab
```

If an argument is not provided, the default value is used.

---

# 11. Positional Arguments

With positional arguments, values are matched according to their position.

```python
def student(name, age):
    print(name)
    print(age)

student("Soyab", 21)
```

Mapping:

```text
name → "Soyab"
age  → 21
```

The order matters.

---

# 12. Keyword Arguments

Keyword arguments specify the parameter name explicitly.

```python
def student(name, age):
    print(name)
    print(age)

student(age=21, name="Soyab")
```

Although the order in the call is different, the parameter names identify the values.

---

# 13. Positional and Keyword Arguments Together

You can combine positional and keyword arguments, but positional arguments must come before keyword arguments.

Correct:

```python
def student(name, age, course):
    print(name, age, course)

student("Soyab", age=21, course="BCA")
```

Incorrect:

```python
student(name="Soyab", 21, course="BCA")
```

A positional argument cannot normally appear after a keyword argument in the same call.

---

# 14. Types of Parameters and Arguments

| Type                | Example           |
| ------------------- | ----------------- |
| Positional          | `add(10, 20)`     |
| Keyword             | `add(a=10, b=20)` |
| Default             | `def add(a=10)`   |
| Variable positional | `*args`           |
| Variable keyword    | `**kwargs`        |

These mechanisms allow functions to accept different kinds of input.

---

# 15. `*args`

`*args` allows a function to accept a variable number of positional arguments.

```python
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))
```

Output:

```text
30
100
```

Inside the function, `args` is a tuple.

Conceptually:

```text
add_numbers(10, 20, 30)

args → (10, 20, 30)
```

The name `args` is a convention; the `*` is what matters.

---

# 16. `**kwargs`

`**kwargs` allows a function to accept a variable number of keyword arguments.

```python
def student_info(**kwargs):
    print(kwargs)

student_info(name="Soyab", age=21, course="BCA")
```

Output:

```text
{'name': 'Soyab', 'age': 21, 'course': 'BCA'}
```

Inside the function, `kwargs` is a dictionary.

Conceptually:

```text
kwargs
  ↓
{
    "name": "Soyab",
    "age": 21,
    "course": "BCA"
}
```

Again, `kwargs` is only a conventional name. The `**` is what provides the behavior.

---

# 17. `*args` vs `**kwargs`

| Feature         | `*args`              | `**kwargs`         |
| --------------- | -------------------- | ------------------ |
| Accepts         | Positional arguments | Keyword arguments  |
| Inside function | Tuple                | Dictionary         |
| Example         | `func(10, 20)`       | `func(a=10, b=20)` |

---

# 18. Using `*args` and `**kwargs` Together

A function can accept both.

```python
def show_data(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

show_data(10, 20, name="Soyab", age=21)
```

Output:

```text
Arguments: (10, 20)
Keyword arguments: {'name': 'Soyab', 'age': 21}
```

---

# 19. Parameter Ordering

When defining a function, Python has rules about parameter ordering.

A common pattern is:

```python
def example(a, b=10, *args, **kwargs):
    pass
```

Here:

* `a` → required positional parameter
* `b` → default parameter
* `*args` → extra positional arguments
* `**kwargs` → extra keyword arguments

Python also supports keyword-only parameters:

```python
def create_user(name, *, age, city):
    print(name, age, city)

create_user("Soyab", age=21, city="Athani")
```

The `*` means `age` and `city` must be supplied as keyword arguments.

---

# 20. Scope of Variables

**Scope** determines where a name can be accessed.

Example:

```python
def test():
    x = 10
    print(x)

test()
```

`x` is a local name inside the function.

Trying to use it outside:

```python
print(x)
```

will normally produce:

```text
NameError
```

---

# 21. Local Variables

A variable created inside a function is generally local to that function.

```python
def calculate():
    result = 100
    print(result)

calculate()
```

`result` belongs to the function's local scope.

---

# 22. Global Variables

A name defined outside functions is generally in the global scope of that module.

```python
x = 100

def show():
    print(x)

show()
```

The function can read the global `x`.

However, assigning to a name inside a function creates a local binding by default:

```python
x = 100

def change():
    x = 200
    print(x)

change()

print(x)
```

Output:

```text
200
100
```

The `x` inside `change()` is a different local binding.

---

# 23. The `global` Keyword

If a function needs to rebind a global name, use `global`.

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

Output:

```text
1
```

Using `global` should be done carefully because excessive global state can make programs harder to understand and test.

---

# 24. Nested Functions

A function can be defined inside another function.

```python
def outer():
    def inner():
        print("Inside inner")

    inner()

outer()
```

Here:

```text
outer()
  ↓
inner()
```

The inner function belongs to the enclosing function's scope.

---

# 25. Enclosing Scope and `nonlocal`

A nested function can access variables from its enclosing function.

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

If the nested function needs to **rebind** the enclosing variable, use `nonlocal`.

```python
def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase

c = counter()

print(c())
print(c())
```

Output:

```text
1
2
```

---

# 26. LEGB Rule

Python searches for names using the **LEGB** rule:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Example:

```python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()
```

Python finds the nearest matching name according to the scope rules.

---

# 27. Functions Are Objects

In Python, functions are objects.

This means a function can be:

* Stored in a variable
* Passed to another function
* Returned from a function
* Stored in a collection

Example:

```python
def greet():
    print("Hello")

message = greet

message()
```

Output:

```text
Hello
```

Both names refer to the same function object.

---

# 28. Passing a Function as an Argument

Because functions are objects, they can be passed to other functions.

```python
def greet():
    return "Hello"

def execute(function):
    print(function())

execute(greet)
```

Output:

```text
Hello
```

The function `greet` is passed without calling it.

Notice the difference:

```python
execute(greet)      # pass function
execute(greet())    # pass result of calling function
```

---

# 29. Higher-Order Functions

A **higher-order function** is a function that:

1. Accepts another function as an argument, or
2. Returns a function.

Example:

```python
def apply_operation(operation, a, b):
    return operation(a, b)

def add(a, b):
    return a + b

print(apply_operation(add, 10, 20))
```

Output:

```text
30
```

---

# 30. Returning a Function

A function can return another function.

```python
def create_greeting():
    def greet():
        return "Hello"

    return greet

message = create_greeting()

print(message())
```

Output:

```text
Hello
```

The returned function can continue to exist after `create_greeting()` finishes.

---

# 31. Lambda Functions

A **lambda** is a small anonymous function.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

A lambda is useful for short operations where defining a full named function would be unnecessary.

---

# 32. Lambda with `sorted()`

A common practical use is providing a small key function.

```python
students = [
    ("Amit", 75),
    ("Rahul", 90),
    ("Soyab", 85)
]

students.sort(key=lambda student: student[1])

print(students)
```

The lambda tells `sort()` to use the marks at index `1` as the sorting key.

---

# 33. `map()`

`map()` applies a function to every item in an iterable.

Example:

```python
numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16]
```

In Python 3, `map()` returns a lazy iterator rather than immediately creating a list.

---

# 34. `filter()`

`filter()` keeps items for which a function returns a truthy value.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))
```

Output:

```text
[2, 4, 6]
```

Like `map()`, `filter()` returns an iterator in Python 3.

---

# 35. Recursion

**Recursion** occurs when a function calls itself.

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

A recursive function needs a **base case** to stop the recursion.

---

# 36. Base Case

The base case is the condition that stops recursive calls.

In:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

This is the base case:

```python
if n == 0:
    return
```

Without a suitable stopping condition, recursion can continue until Python raises a recursion-related error.

---

# 37. Recursive Factorial

Mathematically:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive implementation:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

The recursive calls eventually reach the base case.

---

# 38. Functions and Type Hints

Python allows optional type hints.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This communicates that:

```text
a → expected int
b → expected int
return → expected int
```

Important:

> Type hints generally are not automatically enforced at runtime by Python itself.

They are useful for:

* Readability
* Documentation
* IDE support
* Static type checking

---

# 39. Docstrings

A **docstring** documents a function.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

The docstring can be accessed with:

```python
print(add.__doc__)
```

Docstrings are useful for explaining what a function does, its parameters, and its return value.

---

# 40. Mutable Default Argument Trap

This is an important Python interview topic.

Avoid using a mutable object such as a list as a default parameter when you intend to create a fresh object for every call.

Problematic pattern:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same default list can be reused across calls.

A safer pattern is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now a new list is created when no list is supplied.

### Why?

Default argument values are evaluated when the function is defined, not every time the function is called.

---

# 41. Function Arguments Are Passed by Assignment

Python's argument passing is often described as **call by sharing** or **pass-by-object-reference**.

A useful precise explanation is:

> Python passes object references by assignment. The parameter becomes a local name bound to the same object supplied by the caller.

Example with a mutable object:

```python
def add_item(items):
    items.append(100)

numbers = [1, 2, 3]

add_item(numbers)

print(numbers)
```

Output:

```text
[1, 2, 3, 100]
```

The function modified the existing list object.

But rebinding the parameter is different:

```python
def change(items):
    items = [100, 200]

numbers = [1, 2, 3]

change(numbers)

print(numbers)
```

Output:

```text
[1, 2, 3]
```

The parameter `items` was rebound locally; the caller's name `numbers` was not changed.

---

# 42. Function Design Principles

A good function should usually:

* Have one clear responsibility
* Have a meaningful name
* Accept only necessary parameters
* Return useful results
* Avoid unnecessary global variables
* Be easy to test
* Avoid excessive length

Instead of:

```python
def process_everything():
    # hundreds of lines
    pass
```

Prefer smaller functions with clear responsibilities:

```python
def calculate_total():
    pass

def validate_user():
    pass

def save_data():
    pass
```

---

# 43. Common Function Mistakes

### Mistake 1 — Forgetting parentheses when calling

```python
def hello():
    print("Hello")

hello
```

This refers to the function object but does not call it.

Correct:

```python
hello()
```

---

### Mistake 2 — Confusing `print()` with `return`

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

The function displayed the result but returned `None`.

---

### Mistake 3 — Forgetting the base case in recursion

Incorrect recursive logic can continue until Python raises a recursion-related error.

Always design a clear stopping condition.

---

### Mistake 4 — Using mutable default arguments carelessly

Avoid:

```python
def function(items=[]):
    ...
```

when each call is expected to have its own fresh list.

---

### Mistake 5 — Passing a function incorrectly

```python
execute(greet)
```

passes the function.

```python
execute(greet())
```

calls the function first and passes its result.

---

# 44. Beginner Practice

Try these before looking at the answers.

## Practice 1 — Greeting Function

Create a function:

```python
greet()
```

that prints:

```text
Hello, Soyab
```

---

## Practice 2 — Addition

Create:

```python
add(a, b)
```

that returns the sum of two numbers.

---

## Practice 3 — Even Number

Create:

```python
is_even(number)
```

Return `True` if the number is even; otherwise return `False`.

---

## Practice 4 — Default Parameter

Create:

```python
greet(name="Guest")
```

It should print a greeting using the supplied name.

---

## Practice 5 — Multiple Values

Create a function that accepts two numbers and returns:

```text
sum
difference
product
```

---

## Practice 6 — `*args`

Create a function that accepts any number of numbers and returns their total.

Example:

```python
total(10, 20, 30, 40)
```

Expected:

```text
100
```

---

## Practice 7 — `**kwargs`

Create a function that accepts student information such as:

```text
name
age
course
```

and prints the dictionary of values.

---

## Practice 8 — Lambda

Create a lambda that calculates the cube of a number.

Example:

```text
5 → 125
```

---

## Practice 9 — `map()`

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Use `map()` to create their squares.

Expected:

```text
[1, 4, 9, 16, 25]
```

---

## Practice 10 — `filter()`

Given:

```python
numbers = [10, 15, 20, 25, 30]
```

Use `filter()` to select only numbers divisible by `10`.

---

## Practice 11 — Recursion

Create a recursive function to print numbers from `5` down to `1`.

---

## Practice 12 — Factorial

Create:

```python
factorial(n)
```

using recursion.

Test:

```python
factorial(5)
```

Expected:

```text
120
```

---

## Practice 13 — Function as Argument

Create:

```python
apply_operation(function, a, b)
```

and use it with an addition function.

---

## Practice 14 — Scope

Create a global variable and a local variable with the same name.

Observe which value is printed inside and outside the function.

---

## Practice 15 — Mutable Default Argument

Write a function that demonstrates why using:

```python
items=[]
```

as a default parameter can cause unexpected behavior.

Then fix it using:

```python
items=None
```

---

# 45. Practice Answers

## Answer 1

```python
def greet():
    print("Hello, Soyab")

greet()
```

---

## Answer 2

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

---

## Answer 3

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))
```

Output:

```text
True
False
```

---

## Answer 4

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Soyab")
```

---

## Answer 5

```python
def calculate(a, b):
    return a + b, a - b, a * b

s, d, p = calculate(10, 5)

print(s)
print(d)
print(p)
```

Output:

```text
15
5
50
```

---

## Answer 6

```python
def total(*args):
    return sum(args)

print(total(10, 20, 30, 40))
```

Output:

```text
100
```

---

## Answer 7

```python
def student_info(**kwargs):
    print(kwargs)

student_info(
    name="Soyab",
    age=21,
    course="BCA"
)
```

---

## Answer 8

```python
cube = lambda x: x ** 3

print(cube(5))
```

Output:

```text
125
```

---

## Answer 9

```python
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## Answer 10

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x % 10 == 0, numbers)

print(list(result))
```

Output:

```text
[10, 20, 30]
```

---

## Answer 11

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

---

## Answer 12

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

---

## Answer 13

```python
def add(a, b):
    return a + b

def apply_operation(function, a, b):
    return function(a, b)

print(apply_operation(add, 10, 20))
```

Output:

```text
30
```

---

## Answer 14

```python
x = "global"

def test():
    x = "local"
    print(x)

test()

print(x)
```

Output:

```text
local
global
```

---

## Answer 15

Problematic version:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
```

The default list is reused.

Safer version:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
```

Each call without an explicit list gets a new list.

---

# 46. Interview Questions and Answers

## Q1. What is a function?

**Answer:**

A function is a reusable block of code designed to perform a specific task. It improves code reuse, organization, readability, and maintainability.

---

## Q2. How do you define a function in Python?

**Answer:**

We use the `def` keyword.

```python
def greet():
    print("Hello")
```

---

## Q3. What is the difference between a parameter and an argument?

**Answer:**

A parameter is a variable in the function definition, while an argument is the actual value passed during the function call.

---

## Q4. What is `return`?

**Answer:**

`return` ends the current function execution and sends a value back to the caller.

---

## Q5. What happens if a function has no `return` statement?

**Answer:**

If the function reaches the end without returning a value, it returns `None`.

---

## Q6. What is the difference between `print()` and `return`?

**Answer:**

`print()` displays a value, while `return` sends a value back to the caller so it can be stored or used by other code.

---

## Q7. What are default parameters?

**Answer:**

Default parameters have predefined values that are used when the caller does not provide an argument.

```python
def greet(name="Guest"):
    print(name)
```

---

## Q8. What are positional arguments?

**Answer:**

Positional arguments are matched to parameters according to their position.

```python
add(10, 20)
```

---

## Q9. What are keyword arguments?

**Answer:**

Keyword arguments specify the parameter name explicitly.

```python
add(a=10, b=20)
```

---

## Q10. What is `*args`?

**Answer:**

`*args` allows a function to accept a variable number of positional arguments. Inside the function, those arguments are available as a tuple.

---

## Q11. What is `**kwargs`?

**Answer:**

`**kwargs` allows a function to accept a variable number of keyword arguments. Inside the function, they are available as a dictionary.

---

## Q12. What is a lambda function?

**Answer:**

A lambda is a small anonymous function containing a single expression.

Example:

```python
square = lambda x: x * x
```

---

## Q13. What is recursion?

**Answer:**

Recursion occurs when a function calls itself. A recursive function needs a base case to stop the recursive calls.

---

## Q14. What is a higher-order function?

**Answer:**

A higher-order function accepts another function as an argument, returns a function, or both.

---

## Q15. What is a closure?

**Answer:**

A closure occurs when an inner function retains access to variables from its enclosing scope even after the enclosing function has finished executing.

Example:

```python
def outer():
    message = "Hello"

    def inner():
        return message

    return inner

greet = outer()

print(greet())
```

Output:

```text
Hello
```

---

## Q16. What is LEGB?

**Answer:**

LEGB describes Python's common name lookup order:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

## Q17. What is the `global` keyword?

**Answer:**

`global` tells Python that a name inside a function refers to a global variable rather than creating a new local binding when assigning to it.

---

## Q18. What is the `nonlocal` keyword?

**Answer:**

`nonlocal` allows a nested function to rebind a variable from its nearest enclosing function scope.

---

## Q19. Does Python support function overloading?

**Answer:**

Python does not provide traditional compile-time function overloading based on different parameter signatures like some statically typed languages. A later definition with the same function name replaces the earlier definition in the same namespace. Similar behavior can be designed using default arguments, `*args`, `**kwargs`, or tools such as `functools.singledispatch`.

---

## Q20. Are functions objects in Python?

**Answer:**

Yes. Functions are first-class objects, so they can be assigned to variables, passed as arguments, stored in collections, and returned from other functions.

---

## Q21. What is a mutable default argument problem?

**Answer:**

Default argument values are evaluated when the function is defined. If a mutable object such as a list is used as a default, the same object can be reused across calls.

A common solution is:

```python
def function(items=None):
    if items is None:
        items = []
```

---

## Q22. How are arguments passed in Python?

**Answer:**

Python passes arguments by assignment. The parameter becomes a local name bound to the object supplied by the caller. This is also commonly described as call-by-sharing.

---

## Q23. What are type hints?

**Answer:**

Type hints are optional annotations that communicate expected types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

They improve readability and tooling but are generally not enforced automatically at runtime.

---

## Q24. What is a docstring?

**Answer:**

A docstring is a string placed inside a function, class, or module to document its purpose and behavior.

Example:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

# 47. Quick Revision

```text
Function
→ Reusable block of code

def
→ Defines a function

Call
→ Executes a function

Parameter
→ Variable in function definition

Argument
→ Actual value passed to function

return
→ Sends value back to caller

print()
→ Displays value

Default parameter
→ Uses a predefined value when no argument is supplied

Positional argument
→ Matched by position

Keyword argument
→ Matched by parameter name

*args
→ Variable positional arguments → tuple

**kwargs
→ Variable keyword arguments → dictionary

Scope
→ Determines where a name can be accessed

LEGB
→ Local → Enclosing → Global → Built-in

global
→ Rebind a global name inside a function

nonlocal
→ Rebind an enclosing-scope name

Lambda
→ Small anonymous function

Higher-order function
→ Accepts or returns functions

map()
→ Applies a function to each item

filter()
→ Keeps items satisfying a condition

Recursion
→ Function calls itself

Base case
→ Stops recursion

Docstring
→ Documents a function

Type hint
→ Communicates expected types

Closure
→ Inner function retains access to enclosing variables

Mutable default trap
→ Mutable defaults can be reused across calls
```

---

# 48. Final Interview Explanation

If an interviewer asks:

> **"What are functions in Python?"**

A strong beginner-friendly answer is:

> **"A function in Python is a reusable block of code designed to perform a specific task. We define functions using the `def` keyword and call them when needed. Functions can accept parameters, receive arguments, and return values using `return`. Python also supports default arguments, positional and keyword arguments, `*args`, `**kwargs`, lambda functions, recursion, and higher-order functions. Functions improve code reuse, readability, and maintainability."**
