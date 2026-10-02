# Python Variables, Objects, and Memory Management

This guide explains how Python names refer to objects, how built-in types behave, and how Python manages memory. The examples use standard Python syntax and focus on concepts that are useful for beginners and interviews.

---

# 1. What is a Variable in Python?

A Python variable is a **name bound to an object**.

It is useful to think of a variable as a **label pointing to an object**, rather than a box that physically contains the value.

For example:

```python
x = 10
```

Conceptually:

```text
x ───────> 10
           object
```

Here:

* `x` is the name.
* `10` is an integer object.
* The name `x` refers to that object.

---

# 2. Variables, Memory Allocation, and Deallocation

Variables allow a program to give names to values so that it can:

* Store state
* Perform calculations
* Pass data between functions
* Access objects later

In Python, assignment creates or changes a **binding between a name and an object**.

## Example

```python
x = 10
```

Think of it as:

```text
Name          Object

 x ─────────> 10
```

If we later write:

```python
x = 20
```

the name `x` is now bound to another object:

```text
x ─────────> 20
```

The original integer object `10` was not modified.

---

# 3. Two Names Can Refer to the Same Object

Consider:

```python
first = {"score": 10}

second = first

second["score"] = 20

print(first["score"])
```

Output:

```text
20
```

Why?

Because both names refer to the same dictionary object.

Conceptually:

```text
first  ─────┐
            ↓
        {"score": 10}
            ↑
second ─────┘
```

After:

```python
second["score"] = 20
```

the same dictionary becomes:

```text
{"score": 20}
```

Therefore:

```python
print(first["score"])
```

prints:

```text
20
```

This is called **aliasing**: multiple names refer to the same object.

---

# 4. Scope and Lifetime

There are two different concepts to understand:

## Name Lifetime

A name is available according to its scope.

For example:

```python
def test():
    value = 100
    print(value)
```

`value` is a local name inside the function.

Normally, it cannot be accessed outside the function:

```python
def test():
    value = 100

test()

print(value)
```

This produces a `NameError` because `value` is not available in that scope.

---

## Object Lifetime

An object can live longer than the function that created it if another reference still points to it.

Example:

```python
def make_list():

    values = [1, 2, 3]

    return values


items = make_list()

print(items)
```

Output:

```text
[1, 2, 3]
```

The local name `values` belongs to `make_list()`.

After the function returns, the local name is no longer available.

However, the list object remains alive because `items` refers to it.

Conceptually:

```text
make_list()
    |
    | creates
    ↓
[1, 2, 3]
    ↑
    |
 items
```

There is no general expiry timer for variables.

When an object is no longer reachable, it becomes eligible for memory reclamation. The runtime controls when the memory is actually reclaimed.

---

# 5. Memory Allocation in Python

Python manages memory automatically.

A Python program uses memory for things such as:

* Integers
* Strings
* Lists
* Dictionaries
* Functions
* Objects
* Runtime information
* Execution state

In **CPython**, Python's memory allocator manages object memory and obtains memory from the underlying process and operating system.

The exact memory-management implementation can differ between Python implementations.

Therefore, avoid assuming that Python always follows a simple rule such as:

```text
Variables → Stack
Objects → Heap
```

That is only a simplified analogy.

---

# 6. Are Values in Python Objects?

Yes.

Python's data model represents values as objects.

An object has:

1. **Identity**
2. **Type**
3. **Value**

Example:

```python
x = 10

print(id(x))
print(type(x))
print(x)
```

Possible output:

```text
140721234567890
<class 'int'>
10
```

The exact number returned by `id()` can differ between runs.

---

# 7. Object Identity

`id()` returns an identity for an object during its lifetime.

Example:

```python
x = 10

print(id(x))
```

In CPython, the identity is commonly related to the object's memory address, but Python code should not depend on that implementation detail.

The important idea is:

```text
id()   → identity
type() → type
value  → actual value
```

---

# 8. Built-in Data Types

Python provides many built-in data types.

## Common categories

| Category   | Types                              |
| ---------- | ---------------------------------- |
| Numeric    | `int`, `float`, `complex`          |
| Boolean    | `bool`                             |
| Text       | `str`                              |
| Sequences  | `list`, `tuple`, `range`           |
| Sets       | `set`, `frozenset`                 |
| Mapping    | `dict`                             |
| Binary     | `bytes`, `bytearray`, `memoryview` |
| Null value | `NoneType`                         |

---

# 9. Numeric Types

Python has three common numeric types.

## Integer

```python
age = 25
count = -10
```

The type is:

```python
int
```

Integers represent whole numbers.

---

## Float

```python
price = 99.0
percentage = 88.75
```

The type is:

```python
float
```

Floats represent numbers containing a fractional part.

---

## Complex

```python
z = 3 + 4j
```

The type is:

```python
complex
```

Complex numbers contain a real and imaginary component.

---

# 10. Boolean Type

Python has two Boolean values:

```python
True
False
```

They must start with a capital letter.

Example:

```python
is_active = True
is_logged_in = False
```

Boolean values are commonly used in conditions.

```python
if is_active:
    print("Account is active")
```

---

# 11. Truth Values

Many Python objects can be evaluated as either truthy or falsy.

Examples:

```python
print(bool(0))
print(bool(""))
print(bool("hello"))
```

Output:

```text
False
False
True
```

Common falsy values include:

* `0`
* `0.0`
* `False`
* `None`
* Empty strings
* Empty lists
* Empty tuples
* Empty dictionaries
* Empty sets

Most other objects are truthy.

---

# 12. Strings

A string is an **immutable sequence of characters**.

Example:

```python
name = "Aishu"
```

Characters can be accessed using indexes.

Python indexing starts at `0`.

```python
print(name[0])
print(name[1])
```

Output:

```text
A
i
```

Conceptually:

```text
A i s h u
0 1 2 3 4
```

Because strings are immutable, you cannot directly change an individual character.

For example:

```python
name[0] = "B"
```

raises a `TypeError`.

Instead, create a new string.

---

# 13. Lists

Lists are:

* Ordered
* Mutable
* Able to contain duplicate values
* Able to contain different data types

Example:

```python
numbers = [10, 20, 30]
```

A list can contain different types:

```python
data = [10, "python", 25.5, True]
```

Lists are mutable, meaning their contents can be changed.

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

---

# 14. Tuples

Tuples are:

* Ordered
* Immutable
* Able to contain duplicate values

Example:

```python
point = (10, 20)
```

Unlike lists, tuple contents cannot normally be changed after creation.

---

# 15. Sets

A set is a mutable collection of **unique elements**.

Example:

```python
numbers = {10, 10, 20, 30}

print(numbers)
```

The duplicate `10` is stored only once.

Conceptually, the set contains:

```text
10
20
30
```

Sets do not support positional indexing.

This will not work:

```python
numbers[0]
```

An empty set is created using:

```python
set()
```

because:

```python
{}
```

creates an empty dictionary.

For an immutable set, Python provides:

```python
frozenset()
```

---

# 16. Dictionaries

A dictionary stores data as **key-value pairs**.

Example:

```python
student = {
    "id": 101,
    "name": "Aishu",
    "marks": 85.5
}
```

Here:

```text
"id"     → 101
"name"   → "Aishu"
"marks"  → 85.5
```

Dictionary keys must be hashable.

Values can be of many different types.

Accessing a value:

```python
print(student["name"])
```

Output:

```text
Aishu
```

---

# 17. None

`None` represents the absence of a value.

Example:

```python
result = None
```

`None` is different from:

```text
0
False
""
[]
```

These values have different meanings and types.

To check for `None`, use:

```python
if result is None:
    print("No result yet")
```

Use `is None` rather than:

```python
result == None
```

---

# 18. Mutable and Immutable Objects

This is an important Python interview concept.

## Immutable Objects

An immutable object's value cannot be changed after the object is created.

Common immutable types include:

```text
int
float
bool
str
tuple
frozenset
```

Example:

```python
x = 10

x = 20
```

It may look like the value `10` changed into `20`, but that is not what happened.

Instead:

```text
Before:

x ─────> 10

After:

x ─────> 20
```

The name `x` was rebound to another object.

---

## Mutable Objects

Mutable objects can be changed in place.

Common mutable types include:

```text
list
dict
set
bytearray
```

Example:

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

The existing list was modified.

---

# 19. Rebinding a Name

Consider:

```python
x = 10

x = 20
```

After the first assignment:

```text
x ─────> 10
```

After the second assignment:

```text
x ─────> 20
```

The integer `10` was not modified.

The name `x` was simply **rebound** to another object.

---

# 20. Two Names Referring to One Immutable Object

Consider:

```python
a = 10

b = a
```

Conceptually:

```text
a ─────┐
       ↓
      10
       ↑
b ─────┘
```

Both names refer to the integer object representing `10`.

Now:

```python
a = 20
```

This does not change `b`.

```python
print(a)
print(b)
```

Output:

```text
20
10
```

Why?

Because `a = 20` rebinds `a`.

It does not change the object referred to by `b`.

---

# 21. Aliasing a Mutable Object

Consider:

```python
a = [10, 20]

b = a

b.append(30)

print(a)
```

Output:

```text
[10, 20, 30]
```

Why?

Because both names refer to the same list.

```text
a ─────┐
       ↓
 [10, 20]
       ↑
b ─────┘
```

After:

```python
b.append(30)
```

the shared list becomes:

```text
[10, 20, 30]
```

Therefore, both `a` and `b` see the change.

---

# 22. `==` vs `is`

This is an important interview question.

## `==`

`==` checks whether two objects have equal values.

Example:

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

Output:

```text
True
```

The lists contain equal values.

---

## `is`

`is` checks whether two names refer to the **same object**.

```python
print(a is b)
```

Output:

```text
False
```

The two lists contain the same values, but they are separate list objects.

Conceptually:

```text
a ─────> [1, 2]

b ─────> [1, 2]
```

Two different objects.

Therefore:

```text
a == b  → True
a is b  → False
```

### Remember

```text
== → value equality
is → object identity
```

Use `is` for identity checks such as:

```python
if result is None:
    ...
```

Do not use `is` as a general replacement for `==`.

---

# 23. Where Does Python Use Memory?

While a Python program is running, memory is used for:

* Objects
* Variables/names
* Lists
* Dictionaries
* Strings
* Functions
* Execution state
* Runtime bookkeeping

Python manages this memory automatically.

In CPython, objects are managed by Python's memory-management system.

The exact implementation details can differ between Python implementations.

---

# 24. Reference Counting in CPython

CPython primarily uses **reference counting**.

Conceptually, an object keeps track of references to it.

Example:

```python
a = [1, 2, 3]

b = a
```

Now both `a` and `b` refer to the same list.

```text
a ─────┐
       ↓
   [1, 2, 3]
       ↑
b ─────┘
```

If we remove:

```python
del b
```

the name `b` is removed.

But `a` still refers to the list:

```text
a ─────> [1, 2, 3]
```

Therefore, the list remains reachable.

Reference counting is primarily a **CPython implementation detail**, not a guarantee that every Python implementation works exactly this way.

---

# 25. What Does `del` Do?

`del` removes a name, reference, or item.

It does **not directly command Python to destroy an object**.

Example:

```python
numbers = [1, 2, 3]

b = numbers

del numbers

print(b)
```

Output:

```text
[1, 2, 3]
```

Why does the list still exist?

Because `b` still refers to it.

Conceptually:

```text
numbers ──X

b ────────> [1, 2, 3]
```

The list is still reachable.

---

# 26. Garbage Collection

Garbage collection is automatic memory management.

It identifies objects that the program can no longer reach and allows their memory to be reclaimed.

Python programmers normally do not manually free object memory.

For example:

```python
numbers = [1, 2, 3]

del numbers
```

If there are no other references to that list, the object may become eligible for reclamation.

However, becoming unreachable does not mean that the operating system's memory usage will immediately decrease.

Python may keep reclaimed memory available for future allocations.

---

# 27. Reference Counting and Cyclic Garbage Collection

Reference counting can reclaim many objects when their reference count reaches zero.

However, reference counting alone cannot handle every situation.

Consider a circular reference:

```python
a = []

a.append(a)
```

The list contains a reference to itself.

Conceptually:

```text
a ─────> [ reference to itself ]
           ↑              |
           └──────────────┘
```

This creates a cycle.

Even if the object is no longer reachable from the rest of the program, the references inside the cycle can prevent simple reference counting from reaching zero.

CPython therefore also has a **cyclic garbage collector** that can detect and collect many unreachable reference cycles.

The `gc` module provides controls for this system, but most programs do not need to manage it directly.

---

# 28. When Can an Object Be Reclaimed?

An object becomes eligible for reclamation when it is no longer reachable by the program.

Example:

```python
numbers = [1, 2, 3]

b = numbers

del numbers
```

The list is still reachable through:

```python
b
```

Now:

```python
del b
```

If no other references exist, the list is no longer reachable through these names.

In CPython, non-cyclic objects with no remaining references are often reclaimed promptly.

However, the exact timing is not a general Python guarantee.

Also, reclaimed memory does not necessarily get returned immediately to the operating system.

---

# 29. Useful Mental Model

A useful beginner mental model is:

```text
Name
  |
  ↓
Object
  |
  ├── Identity
  ├── Type
  └── Value
  |
  ↓
Memory managed by Python
  |
  ↓
Object becomes unreachable
  |
  ↓
Memory may eventually be reclaimed/reused
```

The important idea is:

> Names refer to objects, and Python manages the memory used by those objects.

This is a conceptual model, not a guarantee about the exact internal storage used by the Python implementation.

---

# 30. Why Doesn't `del` Always Destroy an Object Immediately?

Consider:

```python
numbers = [1, 2, 3]

b = numbers

del numbers
```

`del numbers` only removes the name `numbers`.

The object is still referenced by:

```python
b
```

Therefore, it remains reachable.

Only after all relevant references are removed can the object become unreachable.

Even then, the exact time of reclamation depends on the Python implementation and circumstances such as reference cycles.

---

# 31. Real-Life Example — Online Shopping Cart

Imagine an online shopping cart as a basket.

A variable is like a **label pointing to the basket**.

Two labels can point to the same basket.

Removing one label does not remove the basket if another label still points to it.

---

## Python Example

```python
def create_cart():

    cart = {
        "items": ["book"]
    }

    checkout_cart = cart

    return checkout_cart


active_cart = create_cart()

order_history = [active_cart]

del active_cart

order_history.clear()
```

### Step-by-step

Inside the function:

```python
cart = {
    "items": ["book"]
}
```

creates a cart object.

Then:

```python
checkout_cart = cart
```

creates another reference to the same object.

Then:

```python
return checkout_cart
```

returns that object.

The object continues to exist because:

```python
active_cart
```

refers to it.

Then:

```python
order_history = [active_cart]
```

creates another reference through the list.

Now:

```python
del active_cart
```

removes only the `active_cart` name.

The object still exists because:

```python
order_history
```

refers to it.

Finally:

```python
order_history.clear()
```

removes the reference from the list.

If no other references exist, the cart becomes unreachable.

In CPython, reference counting can often reclaim such an object promptly.

---

# 32. Stack and Heap Analogy

A common analogy is:

```text
Function call → temporary workspace
Object        → data stored in managed memory
```

Imagine a worker using a temporary clipboard while handling an order.

The clipboard contains temporary task information.

The shopping cart is like a basket stored in a shared stockroom.

When the worker finishes, the clipboard is no longer available to that task.

However, the basket can remain if another worker or the order-history system still has a reference to it.

This is only an analogy.

It is **not** a literal rule that:

```text
Every variable → stack
Every object   → heap
```

Python implementations can optimize how values and objects are stored.

---

# 33. Memory Allocation in Python — CPython

The following describes **CPython**, the most commonly used Python implementation.

* Names are bindings in a scope, such as a function's local scope or a module's global scope.
* Objects are managed by Python and are typically allocated in managed memory.
* CPython primarily uses reference counting.
* References to objects are tracked.
* When an object's reference count reaches zero, CPython can usually reclaim it promptly.
* Reference counting alone cannot handle unreachable reference cycles.
* CPython also has a cyclic garbage collector.
* Other Python implementations may use different memory-management strategies.
* Python code should not depend on exact cleanup timing.

---

# 34. Comparison — Node.js and Python

| Topic                         | Node.js                                        | Python / CPython                                                               |
| ----------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------ |
| Variable                      | Name/reference to a value                      | Name bound to an object                                                        |
| Function scope                | Local bindings exist within function execution | Local names exist within function scope                                        |
| Object memory                 | Managed by V8                                  | Managed by Python runtime                                                      |
| Garbage collection            | V8 garbage collector                           | CPython reference counting + cyclic GC                                         |
| Exact cleanup time            | Not guaranteed                                 | Often prompt for non-cyclic objects in CPython, but not universally guaranteed |
| Objects can outlive functions | Yes, if referenced                             | Yes, if referenced                                                             |
| Unwanted memory retention     | Objects remain reachable unintentionally       | Objects remain referenced unintentionally                                      |
| Cyclic references             | Garbage collector handles them                 | CPython cyclic GC handles many cycles                                          |

---

# 35. Node.js Example

Node.js uses JavaScript running on the V8 engine.

Example:

```javascript
function makeCounter() {

    let count = 0;

    return () => ++count;
}

const next = makeCounter();

console.log(next());
```

Output:

```text
1
```

Normally, `count` would be a local variable of `makeCounter()`.

However, the returned function still refers to `count`.

Therefore, the state represented by `count` remains reachable after `makeCounter()` returns.

This is an example of a **closure**.

---

# 36. Python Equivalent Concept

Python can also keep objects alive after a function returns when another reference retains them.

Example:

```python
def make_counter():

    count = 0

    def next_count():

        nonlocal count

        count += 1

        return count

    return next_count


next_count = make_counter()

print(next_count())
print(next_count())
```

Output:

```text
1
2
```

The inner function retains access to `count`.

Therefore, the state survives after `make_counter()` returns.

This is also an example of a **closure**.

---

# 37. Memory Leaks in Garbage-Collected Languages

Garbage collection does not mean memory can never be wasted.

A memory leak can occur when a program unintentionally keeps references to objects it no longer needs.

Examples include:

* A cache that keeps growing
* Event listeners that are never removed
* Global collections that continuously grow
* Closures retaining large objects
* Objects stored unnecessarily in long-lived data structures

The garbage collector cannot reclaim an object if the program still has a reachable reference to it.

For example:

```python
cache = []

while True:
    cache.append(large_object)
```

If the list continues to hold references to objects, those objects remain reachable.

Therefore, garbage collection cannot reclaim them.

---

# 38. Garbage Collection Does Not Mean Memory Immediately Goes Back to the OS

This is an important distinction.

When Python reclaims an object:

```text
Object becomes unreachable
        ↓
Object memory can be reused
```

It does **not** necessarily mean:

```text
Memory immediately returned to operating system
```

Python's memory allocator may keep the memory so that it can be reused by the Python process.

Therefore:

```text
Garbage collection
        ≠
Immediately reducing OS-level process memory
```

---

# 39. Key Takeaways

1. A Python variable is a **name bound to an object**.
2. Python values are represented as **objects**.
3. Objects have **identity, type, and value**.
4. Assignment creates or changes a name-to-object binding.
5. Assignment does not necessarily create a copy.
6. Two names can refer to the same object.
7. Mutable objects can be changed in place.
8. Immutable objects cannot be changed after creation.
9. `==` compares values.
10. `is` compares object identity.
11. `id()` provides an object's identity during its lifetime.
12. `type()` tells you the object's type.
13. `del` removes a name/reference; it does not guarantee immediate destruction.
14. Objects can outlive the function that created them if another reference exists.
15. CPython primarily uses reference counting.
16. CPython also has cyclic garbage collection.
17. An object becomes eligible for reclamation when it is no longer reachable.
18. Reclaimed memory may be reused by Python rather than immediately returned to the operating system.
19. Exact memory-management behavior can vary between Python implementations.
20. Garbage collection cannot reclaim objects that are still reachable, even if the program no longer logically needs them.

---

# 40. One-Line Interview Summary

> **In Python, variables are names bound to objects; objects have identity, type, and value, and Python manages their memory automatically. CPython primarily uses reference counting along with cyclic garbage collection to reclaim unreachable objects.**
