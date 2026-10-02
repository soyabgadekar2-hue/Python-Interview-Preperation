# Python Basics — Learning & Interview Notes

## 1. What is Python?

Python is a **high-level, interpreted, general-purpose programming language** known for its simple and readable syntax.

Python is widely used for:

* Web development
* Automation and scripting
* Data analysis
* Artificial intelligence and machine learning
* Scientific computing
* Testing
* Desktop applications
* APIs and backend development
* Education and programming practice

### Interview answer

> Python is a high-level, interpreted, general-purpose programming language. It is dynamically typed, supports multiple programming paradigms, and is widely used in web development, automation, data science, AI, scripting, and many other areas.

---

# 2. Important Features of Python

## 2.1 Simple and readable

Python syntax is designed to be easy to read.

```python
name = "Soyab"
print(name)
```

Compared with many other languages, Python generally requires less code for the same basic task.

---

## 2.2 High-level language

Python is a high-level programming language.

It hides many low-level implementation details from the programmer, such as manually managing individual memory allocations.

This allows developers to focus more on solving the problem.

---

## 2.3 Interpreted

Python is commonly described as an **interpreted language** because Python programs are executed by the Python runtime.

A simplified CPython execution flow is:

```text
Python source code (.py)
        ↓
Tokenizer / Parser
        ↓
Compilation
        ↓
Python bytecode
        ↓
Python Virtual Machine / Runtime
        ↓
Execution
```

So, the statement:

> "Python is interpreted"

is useful for beginners, but it is a simplification.

In CPython, source code is compiled into bytecode before being executed by the Python runtime.

---

## 2.4 Dynamically typed

Python is dynamically typed.

You do not normally need to declare a variable's type explicitly.

Example:

```python
x = 10
print(type(x))

x = "Hello"
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

The name `x` is first bound to an integer object and later rebound to a string object.

---

## 2.5 Object-oriented

Python supports object-oriented programming.

Example:

```python
class Student:
    pass
```

Python supports:

* Classes
* Objects
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction

---

## 2.6 Supports multiple programming paradigms

Python supports multiple programming styles, including:

### Procedural programming

```python
x = 10
y = 20

print(x + y)
```

### Object-oriented programming

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### Functional programming

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

---

## 2.7 Portable / Cross-platform

Python can generally run on:

* Windows
* Linux
* macOS

provided that the appropriate Python version and required dependencies are available.

Example:

```python
print("Hello")
```

The same basic Python program can run on different operating systems.

---

## 2.8 Large standard library

Python provides many modules as part of its standard library.

Examples:

```python
import math
import os
import json
```

The standard library provides functionality for tasks such as:

* File handling
* Mathematics
* Dates and times
* Operating-system interaction
* JSON processing
* Networking
* Regular expressions

---

## 2.9 Automatic memory management

Python provides automatic memory management.

Programmers normally do not manually allocate and free every object.

Example:

```python
numbers = [1, 2, 3]
```

Python's runtime manages the memory associated with the list.

Detailed memory-management concepts are covered in:

**`03_Python_Memory_Management.md`**

---

## 2.10 Large ecosystem

Python has a large ecosystem of third-party packages.

Examples:

```text
NumPy
pandas
Django
Flask
FastAPI
Requests
TensorFlow
PyTorch
Matplotlib
```

Packages can commonly be installed using `pip`.

Example:

```bash
pip install requests
```

---

# 3. Advantages of Python

Important advantages include:

* Easy-to-read syntax
* Beginner-friendly
* Large ecosystem
* Cross-platform
* Strong community support
* Large standard library
* Useful for automation
* Useful for web development
* Widely used in data science
* Widely used in AI and machine learning
* Supports rapid development
* Supports multiple programming paradigms

---

# 4. Disadvantages of Python

Python also has some disadvantages.

## 4.1 Performance

Python can be slower than compiled languages such as C or C++ for many CPU-intensive workloads.

However, actual performance depends on:

* Python implementation
* Libraries
* Algorithms
* Hardware
* Type of workload

---

## 4.2 Memory usage

Some Python applications can use more memory than equivalent implementations in lower-level languages.

---

## 4.3 Runtime errors

Because Python is dynamically typed, some type-related errors may appear during runtime.

Example:

```python
x = 10
print(x + "Hello")
```

This produces a type-related error because an integer and string cannot be added in this way.

---

## 4.4 Not always suitable for low-level programming

Python is generally not the first choice for tasks requiring direct low-level hardware or system control.

Languages such as C, C++, or Rust may be more suitable for some such applications.

---

# 5. Python Versions

Python has two major generations that are commonly discussed:

```text
Python 2
Python 3
```

Python 2 reached **end-of-life in 2020**.

Modern Python development should use a **supported Python 3 release**.

When learning or starting a new project, use a currently supported Python 3 version.

---

# 6. Python File Extension

Python source-code files normally use:

```text
.py
```

Examples:

```text
main.py
calculator.py
student.py
app.py
```

---

# 7. Python Interpreter

The Python interpreter/runtime is responsible for executing Python programs.

Example:

```bash
python hello.py
```

On some systems:

```bash
python3 hello.py
```

---

# 8. Interactive Python Shell

You can start Python interactively from the terminal.

```bash
python
```

Then write:

```python
print("Hello Python")
```

Output:

```text
Hello Python
```

The interactive shell is useful for:

* Testing small pieces of code
* Learning syntax
* Checking functions
* Experimenting with expressions

---

# 9. Common Tools Used With Python

## 9.1 Python interpreter

Used to run Python programs.

---

## 9.2 pip

`pip` is commonly used to install Python packages.

Example:

```bash
pip install requests
```

---

## 9.3 Virtual environment

A virtual environment provides an isolated Python environment for a project.

Create one:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

---

## 9.4 Code editors / IDEs

Common Python development tools include:

* VS Code
* PyCharm
* IDLE
* Other Python-compatible editors

---

## 9.5 Git

Git is a version-control system commonly used to track source-code changes.

Python projects can be stored in Git repositories.

---

# 10. Terminal Commands Used With Python

These are **terminal/shell commands**, not Python language commands.

## Check Python version

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Run a Python file

```bash
python filename.py
```

Example:

```bash
python calculator.py
```

---

## Install a package

```bash
pip install package_name
```

Example:

```bash
pip install requests
```

---

## Show installed packages

```bash
pip list
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

---

## Activate virtual environment on Windows

```bash
.venv\Scripts\activate
```

---

## Activate virtual environment on Linux/macOS

```bash
source .venv/bin/activate
```

---

# 11. Indentation in Python

Indentation is extremely important in Python.

Python uses indentation to define blocks of code.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The indented line belongs to the `if` block.

Without correct indentation, Python may produce:

```text
IndentationError
```

or:

```text
SyntaxError
```

---

## Example of incorrect indentation

```python
age = 20

if age >= 18:
print("Adult")
```

Correct version:

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# 12. Comments in Python

Comments are used to explain code.

## Single-line comment

```python
# This is a comment

print("Hello")
```

Python ignores the comment during normal execution.

---

## Multiple-line documentation text

Triple-quoted strings can be used as string literals.

```python
"""
This is a string literal.
It can span multiple lines.
"""
```

When placed as the first statement inside a function, class, or module, such a string can serve as a **docstring**.

Example:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

# 13. Basic Python Program

The simplest Python program can be:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

---

# 14. How Python Works

Consider:

```python
a = 10
b = 20

print(a + b)
```

A simplified explanation is:

```text
Python source code
       ↓
Parser / Compiler
       ↓
Python bytecode
       ↓
Python runtime
       ↓
Execution
       ↓
Output
```

Output:

```text
30
```

This is a simplified conceptual model. The exact execution process depends on the Python implementation.

---

# 15. Python Architecture

Important conceptual components include:

1. Source code
2. Parser/compiler
3. Bytecode
4. Python runtime / virtual machine
5. Python objects
6. Memory-management system
7. Garbage-collection mechanisms
8. Standard library
9. Imported modules

Conceptual diagram:

```text
             Python Source Code
                    │
                    ↓
             Parser / Compiler
                    │
                    ↓
               Bytecode
                    │
                    ↓
            Python Runtime
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
       Objects          Memory Management
          │                   │
          └─────────┬─────────┘
                    ↓
                Program
                  Output
```

---

# 16. Python Applications

Python is used in many different areas.

---

## 16.1 Web development

Popular Python frameworks include:

```text
Django
Flask
FastAPI
```

Python can be used to build:

* Websites
* Backend applications
* REST APIs
* Authentication systems
* Database applications

---

## 16.2 Automation

Python is commonly used for automating repetitive tasks.

Examples:

* File processing
* Folder management
* Report generation
* Data processing
* Testing
* Web automation

Example:

```python
print("Automation task")
```

---

## 16.3 Data science

Python has a large data-science ecosystem.

Common libraries include:

```text
NumPy
pandas
Matplotlib
```

---

## 16.4 Artificial Intelligence and Machine Learning

Python is widely used for:

* Machine learning
* Deep learning
* Natural language processing
* Computer vision
* AI applications

Common libraries/frameworks include:

```text
scikit-learn
TensorFlow
PyTorch
```

---

## 16.5 Backend and API development

Python can be used to build:

* REST APIs
* Web servers
* Authentication systems
* Database applications
* Microservices

---

## 16.6 Testing

Python can be used for automated testing.

Examples of testing tools include:

```text
pytest
unittest
```

---

## 16.7 Education

Python is widely used to teach programming because its syntax is relatively simple and readable.

---

# 17. Examples of Well-Known Python Usage

Python has been used significantly in parts of many well-known products, organizations, and open-source projects.

Examples often associated with Python usage include:

* Instagram
* Spotify
* Dropbox
* Reddit
* Pinterest
* Quora
* Uber
* Disqus
* Blender
* OpenStack

### Important clarification

Do not say:

> "Instagram is completely built using Python."

Large real-world applications usually use multiple technologies and programming languages.

A safer statement is:

> "Python has been used significantly in parts of systems such as Instagram and many other large-scale products."

---

# 18. Official Python Website

The official Python website is:

```text
https://www.python.org/
```

It provides:

* Python downloads
* Documentation
* Tutorials
* Package information
* Community resources
* Python news and information

---

# 19. Important Python Terms

## High-level language

A language that abstracts many low-level implementation details.

---

## Interpreted

Python is commonly described as interpreted because Python code is executed by a Python runtime. CPython first compiles source code into bytecode.

---

## Dynamically typed

Types are associated with objects at runtime, and names can be rebound to objects of different types.

---

## General-purpose

Python can be used for many different types of applications rather than being designed for only one specific purpose.

---

## Open source

Python is open-source software and is developed by a global community.

---

## Portable

Python can run on multiple operating systems when the necessary runtime and dependencies are available.

---

# 20. Important Interview Questions

## Q1. What is Python?

**Answer:**

Python is a high-level, interpreted, general-purpose programming language known for its readable syntax. It is dynamically typed, supports multiple programming paradigms, and is widely used in web development, automation, data science, AI, scripting, and backend development.

---

## Q2. Why is Python popular?

Python is popular because:

* Its syntax is relatively easy to learn.
* It is readable.
* It has a large ecosystem.
* It supports many application domains.
* It has a large community.
* It provides a large standard library.
* It is useful for rapid development.

---

## Q3. Is Python compiled or interpreted?

A good interview answer is:

> Python is commonly described as an interpreted language. In CPython, source code is compiled into bytecode, which is then executed by the Python runtime.

---

## Q4. Is Python dynamically typed?

Yes.

Example:

```python
x = 10

x = "Hello"
```

The name `x` can be rebound to objects of different types.

---

## Q5. What is the extension of a Python file?

The standard extension is:

```text
.py
```

---

## Q6. What is indentation in Python?

Indentation is whitespace used to define blocks of code.

Example:

```python
if age >= 18:
    print("Adult")
```

---

## Q7. What is pip?

`pip` is a package installer commonly used to install Python packages.

Example:

```bash
pip install requests
```

---

## Q8. What is a virtual environment?

A virtual environment creates an isolated Python environment for a project.

It helps prevent dependency conflicts between projects.

---

## Q9. What is the difference between Python 2 and Python 3?

Python 2 is an older generation that reached end-of-life in 2020.

Python 3 is the modern generation used for current development.

---

## Q10. What can Python be used for?

Python can be used for:

* Web development
* Backend development
* API development
* Automation
* Data science
* AI/ML
* Testing
* Scripting
* Education
* Scientific computing

---

## Q11. Why is Python called a high-level language?

Because it provides abstractions that hide many low-level implementation details and allows programmers to write code using human-readable concepts.

---

## Q12. What is Python's main advantage?

One major advantage is its readable and relatively simple syntax, which allows developers to build and maintain programs efficiently.

---

## Q13. What is Python's main disadvantage?

One common disadvantage is that Python can be slower than compiled languages for certain CPU-intensive workloads.

---

## Q14. Is Python case-sensitive?

Yes.

Example:

```python
name = "Soyab"
Name = "Ashish"
```

These are different names.

---

# 21. Beginner Learning Order

A good learning sequence is:

```text
Python Basics
       ↓
Variables
       ↓
Data Types
       ↓
Operators
       ↓
Control Flow
       ↓
Functions
       ↓
Collections
       ↓
Modules
       ↓
File Handling
       ↓
Exception Handling
       ↓
Object-Oriented Programming
       ↓
Projects
```

For this note collection, the first seven files are arranged as:

```text
01 Python Basics
       ↓
02 Variables & Data Types
       ↓
03 Memory Management
       ↓
04 Functions
       ↓
05 Operators
       ↓
06 Control Flow
       ↓
07 Practice Tasks
```

---

# 22. Quick Revision

Remember these points:

```text
Python
→ High-level
→ General-purpose
→ Dynamically typed
→ Readable syntax
→ Multi-paradigm
→ Cross-platform
→ Automatic memory management
→ Large ecosystem
→ .py files
→ Modern development uses Python 3
```

### One-line interview answer

> Python is a high-level, interpreted, dynamically typed, general-purpose programming language with readable syntax and a large ecosystem, widely used for web development, automation, data science, AI, APIs, and scripting.
