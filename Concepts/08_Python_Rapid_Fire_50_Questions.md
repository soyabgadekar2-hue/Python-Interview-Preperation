# ⚡ Python Rapid Fire — 50 Questions & One-Line Answers

## Variables & Data Types

### 1. What is Python?

→ A high-level, dynamically typed, general-purpose programming language.

### 2. What is a variable in Python?

→ A name that refers to an object.

### 3. Is Python statically or dynamically typed?

→ Dynamically typed.

### 4. Is Python strongly typed?

→ Yes, Python is generally considered strongly typed.

### 5. What is an object?

→ A runtime entity containing a value, type, and identity.

### 6. What are the main built-in data types?

→ `int`, `float`, `complex`, `bool`, `str`, `list`, `tuple`, `set`, `dict`, and `NoneType`.

### 7. What is `None`?

→ A special object representing the absence of a value.

### 8. What is type conversion?

→ Converting a value from one data type to another.

### 9. What does `input()` return?

→ A string.

### 10. What does `type()` do?

→ Returns the type of an object.

---

## Operators

### 11. What is an operator?

→ A symbol or keyword that performs an operation on operands.

### 12. What is `=`?

→ Assignment operator.

### 13. What is `==`?

→ Equality comparison operator.

### 14. What is the difference between `==` and `is`?

→ `==` compares values; `is` compares object identity.

### 15. What does `/` do?

→ Performs division and normally returns a float.

### 16. What does `//` do?

→ Performs floor division.

### 17. What does `%` do?

→ Returns the remainder.

### 18. What does `**` do?

→ Performs exponentiation.

### 19. What is short-circuit evaluation?

→ Python stops evaluating a logical expression when the result is already known.

### 20. What do `and` and `or` return?

→ They return one of their operands, not necessarily a Boolean.

---

## Functions

### 21. What is a function?

→ A reusable block of code designed to perform a specific task.

### 22. How do you define a function?

→ Using the `def` keyword.

### 23. What is a parameter?

→ A variable defined in a function declaration.

### 24. What is an argument?

→ A value passed to a function when calling it.

### 25. What does `return` do?

→ Sends a value back to the caller.

### 26. What does a function return without `return`?

→ `None`.

### 27. What is a default parameter?

→ A parameter with a predefined value.

### 28. What is `*args`?

→ It collects variable positional arguments into a tuple.

### 29. What is `**kwargs`?

→ It collects variable keyword arguments into a dictionary.

### 30. Are functions first-class objects in Python?

→ Yes, functions can be stored, passed, and returned like other objects.

---

## Memory & References

### 31. What is object identity?

→ The unique identity of an object during its lifetime.

### 32. How do you check an object's identity?

→ Using `id()`.

### 33. What does `is` check?

→ Whether two names refer to the same object.

### 34. What does `==` check?

→ Whether two objects are equal in value.

### 35. What is a mutable object?

→ An object whose contents can be changed after creation.

### 36. Give examples of mutable types.

→ `list`, `dict`, and `set`.

### 37. Give examples of immutable types.

→ `int`, `float`, `str`, `tuple`, and `bool`.

### 38. Are variables mutable or immutable?

→ Neither; mutability is a property of objects.

### 39. What is reference counting?

→ A CPython memory-management technique that tracks references to objects.

### 40. Why does Python need garbage collection?

→ To handle unreachable objects, including reference cycles that reference counting alone cannot clean up.

---

## Interview Traps

### 41. What happens with `a = b` when `b` is a list?

→ Both names refer to the same list object.

### 42. What happens when you modify that list through `a`?

→ The change is visible through `b` because both reference the same object.

### 43. Does `a = a + [1]` modify the original list?

→ No, it creates a new list and rebinds `a`.

### 44. Does `a.append(1)` modify the original list?

→ Yes, `append()` mutates the existing list.

### 45. What is a mutable default argument problem?

→ A mutable default value is reused across function calls.

### 46. What is LEGB?

→ Local, Enclosing, Global, and Built-in name lookup order.

### 47. What is a reference cycle?

→ A situation where objects reference each other in a cycle.

### 48. Can Python have memory leaks despite garbage collection?

→ Yes, if unwanted objects remain reachable.

### 49. What is the difference between stack and heap?

→ Stack-like execution frames manage calls, while objects are generally managed in heap memory; exact implementation varies.

### 50. What is the most important rule when explaining Python internals?

→ Distinguish Python language behavior from CPython implementation details.

---

# ⚡ Quick Revision

| Concept            | Remember                               |
| ------------------ | -------------------------------------- |
| Python             | High-level, dynamically typed language |
| Variable           | Name referring to an object            |
| Object             | Has value, type, and identity          |
| `None`             | Absence of a value                     |
| `input()`          | Returns a string                       |
| `type()`           | Returns object type                    |
| `=`                | Assignment                             |
| `==`               | Equality                               |
| `is`               | Identity                               |
| `/`                | True division                          |
| `//`               | Floor division                         |
| `%`                | Remainder                              |
| `**`               | Exponentiation                         |
| `and` / `or`       | Can return operands                    |
| Function           | Reusable block of code                 |
| `*args`            | Positional arguments → tuple           |
| `**kwargs`         | Keyword arguments → dictionary         |
| Mutable            | Can be changed                         |
| Immutable          | Cannot be changed                      |
| `id()`             | Object identity                        |
| Reference counting | Tracks references in CPython           |
| Garbage collection | Handles unreachable objects/cycles     |
| LEGB               | Name lookup order                      |
| Reference cycle    | Objects reference each other           |

---

# 🎯 5 Must-Remember Interview Points

1. **Python is dynamically typed but strongly typed.**

2. **`==` checks equality; `is` checks identity.**

3. **Mutability belongs to objects, not variables.**

4. **`a = b` does not copy a list; both names refer to the same object.**

5. **Python language behavior and CPython implementation details are not always the same.**
