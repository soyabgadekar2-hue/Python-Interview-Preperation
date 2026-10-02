# Python Memory Management — Learning & Interview Notes

## 1. What is Memory Management?

**Memory management** is the process of allocating, using, and releasing memory while a program runs.

When a Python program creates objects such as:

```python
name = "Soyab"
age = 21
numbers = [10, 20, 30]
```

Python needs memory to store those objects.

Python provides an automatic memory-management system, so programmers normally do not manually allocate and free memory like they might in languages such as C.

---

# 2. Why Does Python Need Memory Management?

Every program needs memory to store things such as:

* Variables and references
* Objects
* Function execution information
* Lists and dictionaries
* Strings
* Temporary results
* Imported modules and application data

For example:

```python
numbers = [10, 20, 30, 40, 50]
```

Python needs memory for the list object and the objects it contains.

---

# 3. Python Variables and Memory

A Python variable is a **name bound to an object**.

Example:

```python
x = 10
```

Conceptually:

```text
x ─────→ integer object 10
```

The name `x` is not best thought of as a box that physically contains `10`.

Instead:

```text
Name
 ↓
Object
```

This distinction becomes important when understanding references, copying, and garbage collection.

---

# 4. Objects in Python

Python objects have three important characteristics:

```text
Object
 ├── Identity
 ├── Type
 └── Value
```

Example:

```python
x = 100
```

The object `100` has:

* An identity
* A type: `int`
* A value: `100`

You can inspect the type:

```python
print(type(x))
```

And identity:

```python
print(id(x))
```

---

# 5. Object Identity

Every Python object has an identity during its lifetime.

The built-in `id()` function returns an integer identifying that object.

Example:

```python
x = 10

print(id(x))
```

The exact number can vary between executions and Python implementations.

Important:

> `id()` should not universally be described as "the RAM address."

In CPython, an object's `id()` is commonly related to its memory address, but Python's language-level concept is object identity.

---

# 6. References

A **reference** is a way of accessing an object through a name or another object.

Example:

```python
a = [1, 2, 3]
b = a
```

Conceptually:

```text
a ──┐
    ├──→ [1, 2, 3]
b ──┘
```

Both `a` and `b` refer to the same list object.

We can check:

```python
print(a is b)
```

Output:

```text
True
```

---

# 7. Assignment and References

Consider:

```python
a = [10, 20, 30]
b = a
```

A common beginner assumption is:

> "Python created another list for `b`."

That is not what happened.

Instead, `b` was bound to the same list.

```text
a ──┐
    ├──→ [10, 20, 30]
b ──┘
```

Therefore:

```python
b.append(40)

print(a)
```

Output:

```text
[10, 20, 30, 40]
```

---

# 8. Assignment vs Copy

Assignment:

```python
b = a
```

does not normally create a copy.

A shallow copy can be created with:

```python
b = a.copy()
```

A deep copy can be created using:

```python
import copy

b = copy.deepcopy(a)
```

---

# 9. Shallow Copy

A shallow copy creates a new outer object.

Example:

```python
a = [1, 2, 3]
b = a.copy()

print(a is b)
```

Output:

```text
False
```

Now the two lists are separate:

```python
b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

# 10. Shallow Copy with Nested Objects

Consider:

```python
a = [[1, 2], [3, 4]]
b = a.copy()
```

Conceptually:

```text
a ──→ outer list A ──→ inner list 1
                    └→ inner list 2

b ──→ outer list B ──→ inner list 1
                    └→ inner list 2
```

The outer list is new, but the inner lists are shared.

Therefore:

```python
b[0].append(100)

print(a)
print(b)
```

Both can show the changed inner list.

---

# 11. Deep Copy

A deep copy recursively copies nested objects where appropriate.

Example:

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

Conceptually:

```text
a → outer A → inner A1, inner A2

b → outer B → inner B1, inner B2
```

The nested mutable objects are independent.

---

# 12. Reference Count

In **CPython**, memory management includes **reference counting**.

A reference count tracks how many references point to an object.

Conceptual example:

```python
a = [1, 2, 3]
b = a
```

The list has references from:

```text
a
b
```

So conceptually it has two references from these names.

If we remove one:

```python
del b
```

the object still has a reference from `a`.

```text
a ───→ [1, 2, 3]
```

---

# 13. What Happens When References Disappear?

Consider:

```python
a = [1, 2, 3]
b = a

del a
```

The object is still referenced by `b`.

```text
b ───→ [1, 2, 3]
```

Now:

```python
del b
```

There are no references from these names to the list.

In CPython, when an object's reference count reaches zero, its memory can generally be reclaimed immediately.

However, Python's language specification does not require every Python implementation to use reference counting.

---

# 14. The `del` Statement

`del` removes a name binding or an item from a collection.

Example:

```python
x = 10

del x
```

After this:

```python
print(x)
```

raises:

```text
NameError
```

Important:

> `del x` removes the name `x`; it does not mean "physically delete this object from RAM immediately."

If another reference exists, the object can still be accessed.

Example:

```python
a = [1, 2, 3]
b = a

del a

print(b)
```

Output:

```text
[1, 2, 3]
```

---

# 15. `del` with Collections

You can also delete items.

For a list:

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30]
```

For a dictionary:

```python
student = {
    "name": "Soyab",
    "age": 21
}

del student["age"]

print(student)
```

Output:

```text
{'name': 'Soyab'}
```

---

# 16. Garbage Collection

Python also has a **garbage collector** that helps detect and clean up certain objects that cannot be reclaimed simply through reference counting.

This is especially important for **reference cycles**.

For example:

```text
Object A → Object B
   ↑          ↓
   └──────────┘
```

The objects reference each other.

Even if no outside reference points to them, their reference counts may not reach zero.

The cyclic garbage collector can detect such unreachable cycles.

---

# 17. Reference Cycle

A reference cycle occurs when objects refer to one another in a cycle.

Example:

```python
a = []
b = []

a.append(b)
b.append(a)
```

Conceptually:

```text
a → b
↑   ↓
└───┘
```

There is a cycle between the two lists.

Python's garbage collector can help identify and reclaim unreachable cyclic objects.

---

# 18. The `gc` Module

Python provides the `gc` module for interacting with the cyclic garbage collector.

Example:

```python
import gc

print(gc.isenabled())
```

This tells you whether automatic cyclic garbage collection is enabled.

You can manually request a collection:

```python
gc.collect()
```

Important:

> You normally do not need to manually call `gc.collect()` in everyday Python programs.

Python manages memory automatically.

---

# 19. Reference Counting vs Garbage Collection

These concepts are related but not identical.

## Reference Counting

In CPython, reference counting helps reclaim objects when their reference count reaches zero.

```text
No references
      ↓
Reference count = 0
      ↓
Object can be reclaimed
```

## Cyclic Garbage Collection

The cyclic garbage collector helps deal with unreachable reference cycles.

```text
Unreachable cycle
       ↓
Garbage collector detects it
       ↓
Objects can be reclaimed
```

So a simplified CPython picture is:

```text
Python Memory Management
        │
        ├── Reference Counting
        │
        └── Cyclic Garbage Collection
```

---

# 20. Is Garbage Collection the Same as `del`?

No.

`del` is a Python statement used to remove a name binding or collection item.

Garbage collection is a memory-management mechanism that helps reclaim objects that are no longer reachable.

Example:

```python
a = [1, 2, 3]
b = a

del a
```

The list is still reachable through `b`.

So `del a` does not make the list garbage.

---

# 21. Object Lifetime

**Object lifetime** means the period during which an object exists.

Conceptually:

```text
Object created
      ↓
Object used
      ↓
Object no longer reachable
      ↓
Memory can be reclaimed
```

The exact timing of memory reclamation depends on the Python implementation and situation.

---

# 22. Scope vs Lifetime

These concepts should not be confused.

## Scope

Scope describes **where a name can be accessed**.

Example:

```python
def test():
    x = 10
    print(x)
```

The local name `x` is accessible within the function's scope.

## Lifetime

Lifetime describes **how long an object exists**.

Scope and lifetime are related in many common cases, but they are not the same concept.

---

# 23. Local Variables and Memory

Consider:

```python
def calculate():
    x = 10
    y = 20

    return x + y
```

When the function executes, Python creates the function's execution context and local bindings.

Conceptually:

```text
calculate()
     ↓
local names
 ├── x → 10
 └── y → 20
```

After the function returns, those local names normally cease to be accessible from outside the function.

The objects they referred to may be reclaimed if no other references keep them alive.

---

# 24. Returning an Object from a Function

Consider:

```python
def create_numbers():
    numbers = [10, 20, 30]
    return numbers

result = create_numbers()
```

The local name:

```text
numbers
```

ceases to exist after the function returns, but the list remains alive because:

```text
result ───→ [10, 20, 30]
```

The object has another reference.

This demonstrates an important point:

> A local variable disappearing does not necessarily mean the object disappears.

---

# 25. Conceptual Stack and Heap

You may hear that Python uses a **stack and heap**.

For beginner understanding, a simplified model is:

```text
Stack
 └── Function execution information

Heap
 └── Python objects
      ├── integers
      ├── strings
      ├── lists
      ├── dictionaries
      └── other objects
```

However, this is a conceptual model.

The exact memory layout and implementation details depend on the Python implementation.

---

# 26. Function Calls and Frames

When a function is called:

```python
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)
```

Python needs execution information for the function call.

Conceptually:

```text
Main program
     ↓
add() frame
 ├── a
 ├── b
 └── result
```

After the function completes, its execution frame is no longer active in the same way.

If returned objects are still referenced elsewhere, those objects can continue to exist.

---

# 27. What Happens to Temporary Objects?

Consider:

```python
result = 10 + 20
```

Python creates or uses objects required to perform the operation.

Temporary objects that become unreachable can eventually have their memory reclaimed.

You normally do not have to manually clean them.

---

# 28. Memory Allocation

Python automatically allocates memory when objects are created.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

Python handles the memory required for the list.

When objects are no longer needed and become reclaimable, Python's memory-management system can release or reuse that memory.

---

# 29. Python's Private Memory Management

CPython has its own memory-management mechanisms in addition to the operating system.

A simplified model is:

```text
Python Program
      ↓
Python Runtime
      ↓
Python Memory Management
      ↓
Operating System Memory
```

CPython manages memory for Python objects using its allocator and related mechanisms.

Programmers normally interact with objects rather than directly managing raw memory.

---

# 30. Memory Allocator

CPython has specialized memory allocation mechanisms for Python objects.

For example, CPython's small-object allocator is commonly associated with **pymalloc**.

You do not normally need to interact with the allocator directly.

The important beginner concept is:

> Python automatically manages memory for normal Python objects.

---

# 31. Does Python Have Memory Leaks?

Python's automatic memory management greatly reduces the need for manual memory cleanup, but memory problems can still occur.

Examples include:

* Keeping unnecessary references alive
* Large global collections
* C extensions with memory-management bugs
* Caching too much data
* Unbounded queues or lists
* Objects remaining reachable unintentionally

Example:

```python
data = []

while True:
    data.append("large amount of data")
```

If the list continues growing without a practical limit, memory usage can become very large.

Automatic garbage collection cannot remove objects that are still reachable.

---

# 32. Garbage Collection Cannot Remove Everything Unused by Your Logic

Suppose:

```python
cache = {}

cache["user1"] = large_object
```

If `cache` remains alive and contains the object, the object is still reachable.

The garbage collector cannot assume that you no longer need it.

Therefore:

> Garbage collection removes objects that are unreachable, not objects that your program simply "doesn't logically need anymore."

---

# 33. Weak References

Python provides the `weakref` module for creating references that do not necessarily keep an object alive.

Example:

```python
import weakref
```

Weak references are useful in advanced situations such as:

* Caches
* Object tracking
* Avoiding certain ownership/reference problems

For beginner Python development, you usually do not need weak references immediately.

---

# 34. Memory Management Example

Consider:

```python
def create_data():
    data = [10, 20, 30]
    return data

numbers = create_data()
```

During the function:

```text
data ───→ [10, 20, 30]
```

After returning:

```text
numbers ───→ [10, 20, 30]
```

The list remains alive because `numbers` refers to it.

If later:

```python
del numbers
```

and no other references exist, the object becomes unreachable.

At that point, its memory can be reclaimed according to the Python implementation's memory-management behavior.

---

# 35. Example: Same Object

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

In this case, the identity values are the same because both names refer to the same object.

You can also use:

```python
print(a is b)
```

Output:

```text
True
```

---

# 36. Example: Different Objects

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

The values are equal, but the objects are different.

---

# 37. Memory Management and Mutable Objects

Mutable objects make reference behavior especially important.

Example:

```python
numbers = [1, 2, 3]

other = numbers

other.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

Because both names refer to the same mutable object.

With immutable objects, the object itself cannot be modified.

---

# 38. Why Immutable Objects Help

Immutable objects cannot be changed after creation.

Examples:

```text
int
float
str
tuple
```

Example:

```python
name = "Python"
```

An operation that appears to modify the string actually produces another string object.

```python
name = name + " Programming"
```

The name `name` is rebound to the resulting string.

---

# 39. Python Memory Management vs Manual Memory Management

## Manual Memory Management

Languages such as C can require programmers to explicitly allocate and free memory.

Conceptually:

```text
Allocate memory
      ↓
Use memory
      ↓
Free memory
```

Forgetting to free memory can cause problems.

## Python

Python automatically manages normal object memory.

Conceptually:

```text
Create object
      ↓
Use object
      ↓
Object becomes unreachable
      ↓
Python can reclaim memory
```

This makes Python easier to work with, although developers still need to avoid unnecessary references and uncontrolled data growth.

---

# 40. Python vs JavaScript Memory Management

Both Python and JavaScript provide automatic memory management and garbage collection.

A simplified comparison:

| Feature                                | Python          | JavaScript                   |
| -------------------------------------- | --------------- | ---------------------------- |
| Manual `free()` for normal objects     | No              | No                           |
| Automatic memory management            | Yes             | Yes                          |
| Garbage collection                     | Yes             | Yes                          |
| Reference counting                     | Used by CPython | Not the normal primary model |
| Cyclic garbage handling                | Yes             | Yes                          |
| Programmer manages raw memory normally | No              | No                           |

The exact implementation differs between Python implementations and JavaScript engines.

---

# 41. Python vs Node.js

Node.js uses the V8 JavaScript engine.

A simplified view:

```text
Python
→ Python implementation/runtime
→ Automatic memory management

Node.js
→ V8 JavaScript engine
→ Automatic memory management
```

Both automatically manage normal application objects, but their internal garbage collectors and allocation strategies are different.

---

# 42. Important Memory Terms

| Term               | Meaning                                               |
| ------------------ | ----------------------------------------------------- |
| Object             | Data/value managed by Python                          |
| Reference          | Way of reaching an object                             |
| Identity           | Object's unique identity during its lifetime          |
| `id()`             | Returns an integer identifying an object              |
| Reference count    | Number of references tracked by CPython for an object |
| Garbage collection | Process for reclaiming certain unreachable objects    |
| Reference cycle    | Objects referring to each other in a cycle            |
| Mutable            | Object can be changed                                 |
| Immutable          | Object cannot be changed                              |
| Shallow copy       | New outer object, nested references may be shared     |
| Deep copy          | Recursively copies nested objects where applicable    |
| Scope              | Where a name can be accessed                          |
| Lifetime           | How long an object exists                             |

---

# 43. Common Beginner Mistakes

## Mistake 1: Thinking `b = a` creates a copy

Incorrect assumption:

```python
a = [1, 2, 3]
b = a
```

This does not create an independent list.

---

## Mistake 2: Thinking `del` immediately deletes the object

```python
a = [1, 2, 3]
b = a

del a
```

The list still exists because `b` refers to it.

---

## Mistake 3: Thinking `id()` is always a RAM address

`id()` provides object identity.

Its exact implementation is Python-implementation-dependent.

---

## Mistake 4: Thinking garbage collection fixes every memory problem

If an object is still reachable, the garbage collector generally cannot reclaim it.

---

## Mistake 5: Confusing scope and lifetime

Scope describes where a name can be accessed.

Lifetime describes how long an object exists.

They are not the same thing.

---

## Mistake 6: Assuming Python has exactly one memory model

Python is a language specification implemented by different Python implementations.

CPython uses reference counting and cyclic garbage collection, but other implementations can use different strategies.

---

# 44. Beginner Practice

Try these exercises yourself before looking at the answers.

---

## Practice 1 — Basic Reference

Create:

```python
a = [10, 20, 30]
b = a
```

Then:

1. Print `a`.
2. Print `b`.
3. Print `a is b`.
4. Add `40` using `b`.
5. Print `a`.

Explain why `a` changed.

---

## Practice 2 — Independent Copy

Create:

```python
a = [10, 20, 30]
```

Create a separate list using:

```python
b = a.copy()
```

Append `40` to `b`.

Print both lists.

Explain why only `b` changed.

---

## Practice 3 — `id()`

Create:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
```

Print:

```python
id(a)
id(b)
id(c)
```

Then print:

```python
a is b
a is c
```

Explain the result.

---

## Practice 4 — `==` vs `is`

Predict the output:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Then explain the difference.

---

## Practice 5 — `del`

Predict what happens:

```python
a = [1, 2, 3]
b = a

del a

print(b)
```

Why does `b` still work?

---

## Practice 6 — Reassignment

Predict:

```python
a = [1, 2, 3]
b = a

a = [4, 5, 6]

print(a)
print(b)
```

Explain why changing `a` does not change `b`.

---

## Practice 7 — Nested Shallow Copy

Predict:

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)

print(a)
print(b)
```

Explain why both contain `100`.

---

## Practice 8 — Deep Copy

Use:

```python
import copy
```

Create a deep copy of:

```python
a = [[1, 2], [3, 4]]
```

Modify the first inner list in the copy.

Verify that the original does not change.

---

## Practice 9 — Function Lifetime

Create:

```python
def create_data():
    data = [10, 20, 30]
    return data

result = create_data()

print(result)
```

Explain why `data` can still exist after the function finishes.

---

## Practice 10 — Memory Explanation

Explain this code in your own words:

```python
a = [1, 2, 3]
b = a

del a
```

Answer these questions:

1. How many names refer to the list before `del a`?
2. What happens after `del a`?
3. Is the list automatically guaranteed to disappear at that exact moment?
4. What happens if `b` is also deleted?

---

# 45. Practice Answers

## Answer 1

```python
a = [10, 20, 30]
b = a

print(a)
print(b)
print(a is b)

b.append(40)

print(a)
```

Output:

```text
[10, 20, 30]
[10, 20, 30]
True
[10, 20, 30, 40]
```

Both names refer to the same list.

---

## Answer 2

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

The outer list was copied.

---

## Answer 3

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
```

`a` and `b` have the same identity because they refer to the same object.

`c` is a separate list object.

---

## Answer 4

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

`==` compares equality.

`is` compares identity.

---

## Answer 5

```python
a = [1, 2, 3]
b = a

del a

print(b)
```

Output:

```text
[1, 2, 3]
```

`del a` removes the name `a`, but `b` still refers to the list.

---

## Answer 6

```python
a = [1, 2, 3]
b = a

a = [4, 5, 6]

print(a)
print(b)
```

Output:

```text
[4, 5, 6]
[1, 2, 3]
```

Reassigning `a` does not change what `b` refers to.

---

## Answer 7

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

The outer lists are different, but their inner lists are shared.

---

## Answer 8

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

The nested objects were copied as well.

---

## Answer 9

```python
def create_data():
    data = [10, 20, 30]
    return data

result = create_data()

print(result)
```

The local name `data` stops being accessible after the function returns, but the list remains alive because `result` now refers to it.

---

## Answer 10

Before:

```text
a ──┐
    ├──→ [1, 2, 3]
b ──┘
```

After:

```python
del a
```

Conceptually:

```text
b ───→ [1, 2, 3]
```

The list remains reachable through `b`.

If `b` is also deleted and no other references exist, the object becomes unreachable. In CPython, its reference count can reach zero and its memory can generally be reclaimed.

---

# 46. Interview Questions and Answers

## Q1. What is memory management?

**Answer:**

Memory management is the process of allocating, using, and reclaiming memory required by a program. Python automatically manages memory for normal Python objects.

---

## Q2. Does Python use automatic memory management?

**Answer:**

Yes. Python automatically manages memory for normal objects using mechanisms provided by the Python implementation. CPython uses reference counting together with cyclic garbage collection.

---

## Q3. What is reference counting?

**Answer:**

Reference counting is a memory-management technique in which CPython tracks references to objects. When an object's reference count reaches zero, its memory can generally be reclaimed.

---

## Q4. What is garbage collection?

**Answer:**

Garbage collection is the process of detecting and reclaiming certain unreachable objects. In CPython, the cyclic garbage collector helps handle unreachable reference cycles that reference counting alone cannot handle.

---

## Q5. What is a reference cycle?

**Answer:**

A reference cycle occurs when objects refer to each other directly or indirectly in a cycle.

Example:

```text
A → B
↑   ↓
└───┘
```

The cyclic garbage collector can help reclaim such objects when they become unreachable.

---

## Q6. What does `del` do?

**Answer:**

`del` removes a name binding or an item from a collection. It does not necessarily immediately destroy the object.

---

## Q7. What is the difference between `del` and garbage collection?

**Answer:**

`del` is a Python statement used to remove a reference or collection item. Garbage collection is a memory-management mechanism that helps reclaim unreachable objects.

---

## Q8. What happens when `b = a`?

**Answer:**

The name `b` is bound to the same object that `a` refers to. It does not normally create a copy.

---

## Q9. What is shallow copy?

**Answer:**

A shallow copy creates a new outer object while nested objects may still be shared.

---

## Q10. What is deep copy?

**Answer:**

A deep copy recursively copies nested objects where applicable, creating an independent object structure.

---

## Q11. What is the difference between scope and lifetime?

**Answer:**

Scope describes where a name can be accessed, while lifetime describes how long an object exists.

---

## Q12. Is `id()` a memory address?

**Answer:**

Not as a universal Python-language rule. `id()` returns an integer identifying an object during its lifetime. In CPython, it is commonly related to the object's memory address.

---

## Q13. Can Python have memory leaks?

**Answer:**

Python's automatic memory management reduces many manual-memory problems, but memory usage can still grow because of unnecessary references, unbounded data structures, caches, or bugs in extensions.

---

## Q14. Can garbage collection delete an object that is still referenced?

**Answer:**

Normally, no. An object that is still reachable through active references is not considered unreachable garbage.

---

## Q15. Does Python use a stack and heap?

**Answer:**

Python implementations use memory structures for execution and object storage, and "stack" and "heap" are useful conceptual terms. However, the exact memory layout depends on the Python implementation, so simple stack/heap diagrams should not be treated as the complete implementation model.

---

# 47. Quick Revision

```text
Memory Management
→ Managing allocation and reclamation of memory

Python variable
→ Name bound to an object

Object
→ Has identity, type, and value

Reference
→ A way of reaching an object

id()
→ Returns an integer identifying an object

Assignment
→ Usually binds another name to an existing object

b = a
→ b and a can refer to the same object

Shallow copy
→ New outer object, nested objects may be shared

Deep copy
→ Recursively copies nested objects where applicable

Reference counting
→ Used by CPython to track references

Garbage collection
→ Helps reclaim unreachable cyclic objects

Reference cycle
→ Objects refer to each other in a cycle

del
→ Removes a name binding or collection item

Scope
→ Where a name can be accessed

Lifetime
→ How long an object exists

Memory leak
→ Memory remains in use or retained when it is no longer practically needed

gc module
→ Provides access to Python's cyclic garbage collector

weakref
→ Provides weak references that do not necessarily keep objects alive
```

---

# 48. Final Interview Explanation

If an interviewer asks:

> **"How does Python manage memory?"**

A strong beginner-friendly answer is:

> **"Python provides automatic memory management. Python implementations allocate memory for objects and reclaim memory when objects are no longer needed. In CPython, reference counting is a major mechanism, and a cyclic garbage collector handles unreachable reference cycles. As developers, we normally work with objects and references instead of manually allocating and freeing raw memory."**

This answer is simple enough for a fresher interview while avoiding the common mistake of saying that Python relies only on garbage collection.
