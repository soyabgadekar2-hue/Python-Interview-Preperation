# ⚡ Python vs Node.js — Rapid Fire

## Important Before Starting

* 🐍 **Python** is a programming language.
* 🟨 **JavaScript** is a programming language.
* 🟢 **Node.js** is a JavaScript runtime.
* ⚙️ **V8** is the JavaScript engine used by Node.js.
* Node.js is **not** a programming language.

---

# 1. Languages, Runtime & Engines

### 1. Is Python dynamically typed?

**Answer:** ✅ Yes.

**Why?**
Python determines variable types at runtime.

**🔑 Difference:**
🐍 Python → dynamically typed
🟨 JavaScript → dynamically typed

---

### 2. Is Node.js a programming language?

**Answer:** ❌ No.

**Why?**
Node.js is a runtime environment for executing JavaScript outside the browser.

**🔑 Difference:**
🟨 JavaScript → language
🟢 Node.js → runtime

---

### 3. Is Node.js a JavaScript runtime?

**Answer:** ✅ Yes.

**Why?**
Node.js provides an environment for running JavaScript outside browsers.

---

### 4. Is Python strongly typed?

**Answer:** ✅ Yes.

**Why?**
Python generally does not silently treat unrelated types as interchangeable.

---

### 5. Is JavaScript dynamically typed?

**Answer:** ✅ Yes.

**Why?**
JavaScript variables can hold values of different types during execution.

---

### 6. Does Node.js use the V8 engine?

**Answer:** ✅ Yes.

**Why?**
Node.js uses Google's V8 JavaScript engine to execute JavaScript.

---

### 7. Does CPython compile source code to bytecode?

**Answer:** ✅ Yes.

**Why?**
CPython compiles Python source into bytecode, which is then executed by the Python virtual machine.

**🔑 Difference:**
🐍 CPython → Python bytecode + Python runtime
🟢 Node.js → JavaScript execution through V8

---

# 2. Asynchronous Programming & Event Loop

### 8. Does Node.js use an event loop?

**Answer:** ✅ Yes.

**Why?**
The event loop coordinates asynchronous callbacks and I/O operations.

---

### 9. Does normal synchronous Python code automatically use an event loop?

**Answer:** ❌ No.

**Why?**
Normal Python code runs synchronously unless asynchronous mechanisms such as `asyncio` are used.

---

### 10. Can Python perform asynchronous programming?

**Answer:** ✅ Yes.

**Why?**
Python supports asynchronous programming using features such as `async`, `await`, and `asyncio`.

---

### 11. Can Node.js perform asynchronous programming?

**Answer:** ✅ Yes.

**Why?**
Asynchronous I/O is a major part of Node.js programming.

---

### 12. Does Python have an event loop?

**Answer:** ✅ Yes, when an asynchronous framework/runtime such as `asyncio` is used.

**Why?**
Python supports event-loop-based asynchronous programming, but ordinary synchronous Python code does not automatically run on an event loop.

---

### 13. Can CPU-heavy JavaScript block Node.js's main event loop?

**Answer:** ✅ Yes.

**Why?**
Long-running JavaScript execution can prevent the main event loop from processing other work.

---

# 3. Functions

### 14. Is `def` used to define a Python function?

**Answer:** ✅ Yes.

```python
def hello():
    print("Hello")
```

---

### 15. Is `function` required to define every JavaScript function?

**Answer:** ❌ No.

**Why?**
JavaScript also supports arrow functions.

```javascript
const hello = () => {
    console.log("Hello");
};
```

---

### 16. Are Python functions first-class objects?

**Answer:** ✅ Yes.

**Why?**
Functions can be stored in variables, passed as arguments, and returned from other functions.

---

### 17. Are JavaScript functions first-class objects?

**Answer:** ✅ Yes.

**Why?**
JavaScript functions can also be stored, passed, and returned.

---

# 4. Values, Equality & Identity

### 18. Is `None` a Python value?

**Answer:** ✅ Yes.

**Why?**
`None` is a special singleton object representing the absence of a value.

---

### 19. Is `None` the same as JavaScript `null`?

**Answer:** ❌ No.

**Why?**
They serve similar purposes, but they are values from different languages and type systems.

**🔑 Difference:**

```text
Python      → None
JavaScript  → null
```

---

### 20. Does Python have `is` for identity comparison?

**Answer:** ✅ Yes.

**Why?**
`is` checks whether two references point to the same object.

---

### 21. Does JavaScript have Python's `is` operator?

**Answer:** ❌ No.

**Why?**
JavaScript uses operators such as `===` for equality comparisons; object identity is involved when object references are compared with `===`.

---

### 22. Does `===` perform strict equality in JavaScript?

**Answer:** ✅ Yes.

**Why?**
It compares values without performing the usual implicit type coercion associated with `==`.

---

### 23. Does Python use `==` for value equality?

**Answer:** ✅ Yes.

**Why?**
`==` checks equality according to the objects' equality rules.

---

### 24. Does Python use `==` for object identity?

**Answer:** ❌ No.

**Why?**
Python uses `is` for identity.

---

# 5. Concurrency, GIL & Processes

### 25. Does traditional CPython have a GIL?

**Answer:** ✅ Yes, traditionally.

**Why?**
Traditional CPython uses the Global Interpreter Lock to protect certain interpreter operations.

**Important:** Modern CPython also provides free-threaded builds where the GIL can be disabled.

---

### 26. Does Node.js have Python's GIL?

**Answer:** ❌ No.

**Why?**
Node.js does not use Python's Global Interpreter Lock.

---

### 27. Can Python use multiple processes for CPU-bound work?

**Answer:** ✅ Yes.

**Why?**
Multiple processes can execute work independently.

---

### 28. Can Node.js use multiple processes?

**Answer:** ✅ Yes.

**Why?**
Node.js applications can use multiple processes for scaling or parallel work.

---

### 29. Can Node.js use worker threads?

**Answer:** ✅ Yes.

**Why?**
Node.js provides worker threads for running JavaScript work in separate threads.

---

# 6. Memory Management & Garbage Collection

### 30. Does Python automatically garbage-collect memory?

**Answer:** ✅ Yes.

**Why?**
Python implementations provide automatic memory management; CPython uses reference counting along with cyclic garbage collection.

---

### 31. Does Node.js automatically garbage-collect memory?

**Answer:** ✅ Yes.

**Why?**
V8 automatically manages JavaScript memory using garbage collection.

---

### 32. Does CPython use reference counting?

**Answer:** ✅ Yes.

**Why?**
CPython uses reference counting as a major part of its memory-management system.

---

### 33. Does V8 use garbage collection?

**Answer:** ✅ Yes.

**Why?**
V8 automatically identifies and reclaims memory that is no longer reachable.

---

### 34. Can both Python and Node.js applications have memory leaks?

**Answer:** ✅ Yes.

**Why?**
Garbage collection cannot remove objects that are still reachable but no longer needed.

---

### 35. Does garbage collection guarantee that all unused memory is immediately returned to the OS?

**Answer:** ❌ No.

**Why?**
Memory management and memory returned to the operating system are separate implementation concerns.

---

# 7. Data Structures & Mutability

### 36. Is a Python list mutable?

**Answer:** ✅ Yes.

---

### 37. Is a JavaScript Array mutable?

**Answer:** ✅ Yes.

**🔑 Difference:**
🐍 Python → `list`
🟨 JavaScript → `Array`

Both are commonly used as mutable ordered collections.

---

### 38. Is a Python string mutable?

**Answer:** ❌ No.

---

### 39. Is a JavaScript string mutable?

**Answer:** ❌ No.

**🔑 Difference:**
Both Python and JavaScript strings are immutable.

---

### 40. Is Python's `dict` similar to a JavaScript object for many use cases?

**Answer:** ✅ Yes.

**Why?**
Both can represent key-value data, although their behavior and type systems are different.

---

# 8. Package Management

### 41. Does Python use `pip` for package management?

**Answer:** ✅ Yes.

**Why?**
`pip` is the standard package installer commonly used with Python.

---

### 42. Does Node.js commonly use `npm` for package management?

**Answer:** ✅ Yes.

**Why?**
`npm` is a widely used package manager and registry for the Node.js ecosystem.

---

# 9. Exception Handling

### 43. Does Python have `try/except`?

**Answer:** ✅ Yes.

```python
try:
    ...
except:
    ...
```

---

### 44. Does JavaScript have `try/catch`?

**Answer:** ✅ Yes.

```javascript
try {
    // code
} catch (error) {
    // handle error
}
```

---

### 45. Does Python use `raise` to explicitly raise an exception?

**Answer:** ✅ Yes.

```python
raise ValueError("Invalid value")
```

---

### 46. Does JavaScript use `throw` to explicitly throw an exception?

**Answer:** ✅ Yes.

```javascript
throw new Error("Invalid value");
```

---

# 10. Backend & Web Development

### 47. Can Python be used to build REST APIs?

**Answer:** ✅ Yes.

**Why?**
Frameworks such as Django, Flask, and FastAPI can be used to build APIs.

---

### 48. Can Node.js be used to build REST APIs?

**Answer:** ✅ Yes.

**Why?**
Node.js frameworks such as Express, Fastify, and NestJS can be used to build APIs.

---

### 49. Is Node.js particularly suited to I/O-heavy applications?

**Answer:** ✅ Yes.

**Why?**
Node.js uses event-driven, non-blocking I/O, making it well suited to many I/O-heavy workloads.

---

### 50. Is Python only useful for AI and data science?

**Answer:** ❌ No.

**Why?**
Python is also widely used for web development, automation, scripting, testing, education, and many other areas.

---

### 51. Can both Python and Node.js be used for backend development?

**Answer:** ✅ Yes.

**🔑 Difference:**

```text
Python
→ Django
→ Flask
→ FastAPI

Node.js
→ Express
→ Fastify
→ NestJS
```

---

# 11. Syntax & Code Style

### 52. Does Python use indentation to define code blocks?

**Answer:** ✅ Yes.

**🔑 Difference:**
🐍 Python → indentation is syntactically significant.
🟨 JavaScript → normally uses `{}` for blocks.

---

### 53. Does JavaScript use `{}` to define code blocks?

**Answer:** ✅ Yes.

```javascript
if (age >= 18) {
    console.log("Adult");
}
```

---

### 54. Does Python require semicolons at the end of normal statements?

**Answer:** ❌ No.

```python
name = "Soyab"
print(name)
```

---

### 55. Does JavaScript require semicolons in every situation?

**Answer:** ❌ No.

**Why?**
JavaScript has automatic semicolon insertion, although many coding styles still use semicolons explicitly.

---

# 12. Variables & Scope

### 56. Does Python use `let` and `const`?

**Answer:** ❌ No.

**🔑 Difference:**
🐍 Python uses normal assignment:

```python
name = "Soyab"
```

🟨 JavaScript commonly uses:

```javascript
let name = "Soyab";
const age = 21;
```

---

### 57. Does JavaScript use `let` and `const`?

**Answer:** ✅ Yes.

---

### 58. Does Python have local, global, and nonlocal scope concepts?

**Answer:** ✅ Yes.

Python provides keywords such as:

```python
global
nonlocal
```

---

### 59. Does JavaScript have block scope with `let` and `const`?

**Answer:** ✅ Yes.

**Why?**
Variables declared with `let` and `const` are block-scoped.

---

# 13. Type Conversion & Coercion

### 60. Does Python commonly require explicit conversion between strings and integers?

**Answer:** ✅ Yes.

Example:

```python
age = int("21")
```

---

### 61. Does JavaScript perform implicit type coercion in some operations?

**Answer:** ✅ Yes.

Example:

```javascript
"5" + 2
```

produces:

```text
"52"
```

---

### 62. Can `Number("5")` convert a string to a number in JavaScript?

**Answer:** ✅ Yes.

```javascript
Number("5")
```

produces:

```text
5
```

---

# 14. Collections

### 63. Does Python have tuples as a built-in immutable sequence?

**Answer:** ✅ Yes.

```python
numbers = (1, 2, 3)
```

---

### 64. Does JavaScript have a built-in tuple type?

**Answer:** ❌ No.

**🔑 Difference:**
🐍 Python → built-in `tuple`
🟨 JavaScript → no built-in tuple type

---

### 65. Does Python have a built-in `set` type?

**Answer:** ✅ Yes.

```python
numbers = {1, 2, 3}
```

---

### 66. Does JavaScript have a built-in `Set` type?

**Answer:** ✅ Yes.

```javascript
const numbers = new Set([1, 2, 3]);
```

---

### 67. Does Python's `dict` preserve insertion order?

**Answer:** ✅ Yes.

**Why?**
Modern Python language semantics guarantee insertion order for dictionaries.

---

### 68. Does JavaScript have `Map` for key-value collections?

**Answer:** ✅ Yes.

```javascript
const users = new Map();
```

---

# 15. Object-Oriented Programming

### 69. Is everything in Python an object?

**Answer:** ✅ Yes, in Python's object model.

**Why?**
Values such as numbers, strings, functions, and classes are objects.

---

### 70. Is JavaScript prototype-based?

**Answer:** ✅ Yes.

**Why?**
JavaScript's object inheritance system is based on prototypes.

---

### 71. Does JavaScript support classes?

**Answer:** ✅ Yes.

**Important:**
JavaScript `class` syntax is built on top of its prototype-based object model.

---

### 72. Does Python support classes and inheritance?

**Answer:** ✅ Yes.

```python
class Animal:
    pass
```

---

# 16. Modules & Packages

### 73. Does Python have `import` for modules?

**Answer:** ✅ Yes.

```python
import math
```

---

### 74. Does JavaScript support `import` and `export` modules?

**Answer:** ✅ Yes.

```javascript
import something from "./file.js";
```

---

### 75. Is `require()` the only module system in Node.js?

**Answer:** ❌ No.

**Why?**
Node.js supports both CommonJS and ECMAScript modules.

---

# 17. Project Files & Dependencies

### 76. Does Node.js commonly use `package.json`?

**Answer:** ✅ Yes.

**Why?**
It commonly stores project metadata, dependencies, scripts, and configuration.

---

### 77. Does Python commonly use `requirements.txt`?

**Answer:** ✅ Yes.

**Important:**
Modern Python projects can also use tools and files such as `pyproject.toml`.

---

# 18. HTTP & Web Servers

### 78. Can Python create an HTTP server without a web framework?

**Answer:** ✅ Yes.

**Why?**
Python includes standard-library modules that can provide basic HTTP server functionality.

---

### 79. Can Node.js create an HTTP server using its built-in `http` module?

**Answer:** ✅ Yes.

```javascript
const http = require("http");
```

---

# 19. JSON & Databases

### 80. Does Python have a built-in JSON module?

**Answer:** ✅ Yes.

```python
import json
```

---

### 81. Does JavaScript have built-in JSON parsing and stringifying?

**Answer:** ✅ Yes.

```javascript
JSON.parse()
JSON.stringify()
```

---

### 82. Can both Python and Node.js connect to SQL databases?

**Answer:** ✅ Yes.

**Why?**
Both ecosystems provide drivers and libraries for databases such as MySQL and PostgreSQL.

---

### 83. Can both Python and Node.js work with MongoDB?

**Answer:** ✅ Yes.

---

# 20. Testing & Development

### 84. Does Python have `pytest` as a popular testing tool?

**Answer:** ✅ Yes.

---

### 85. Does Node.js have a built-in test runner?

**Answer:** ✅ Yes.

**Why?**
Modern Node.js includes a built-in test runner.

---

# 21. TypeScript

### 86. Can Node.js projects be written in TypeScript?

**Answer:** ✅ Yes.

**Why?**
TypeScript is commonly used to develop Node.js applications with appropriate tooling.

---

### 87. Is TypeScript the same language as JavaScript?

**Answer:** ❌ No.

**Why?**
TypeScript is a separate language that extends JavaScript with additional features such as static typing and is commonly transformed into JavaScript.

---

# 22. Browser & Server Environment

### 88. Can Python normally run directly in a browser as its native scripting language?

**Answer:** ❌ No.

**🔑 Difference:**
🟨 JavaScript is the standard native scripting language of web browsers.
🐍 Python normally runs through a Python runtime rather than directly as the browser's native scripting language.

---

### 89. Can JavaScript run directly in browsers?

**Answer:** ✅ Yes.

---

# 23. Performance

### 90. Is Python always slower than Node.js?

**Answer:** ❌ No.

**Why?**
Performance depends on the workload, implementation, libraries, algorithms, and many other factors.

---

### 91. Does algorithm choice often matter significantly for application performance?

**Answer:** ✅ Yes.

**Why?**
An efficient algorithm can have a much larger impact than simply choosing one language over another.

---

# 24. Deployment

### 92. Can both Python and Node.js run on Linux servers?

**Answer:** ✅ Yes.

---

### 93. Can both Python and Node.js applications be containerized with Docker?

**Answer:** ✅ Yes.

---

# 25. Environment Variables

### 94. Can Python read environment variables?

**Answer:** ✅ Yes.

Example:

```python
import os

value = os.getenv("DATABASE_URL")
```

---

### 95. Can Node.js read environment variables?

**Answer:** ✅ Yes.

Example:

```javascript
const value = process.env.DATABASE_URL;
```

---

# 26. Command-Line Applications

### 96. Can Python be used to build command-line applications?

**Answer:** ✅ Yes.

---

### 97. Can Node.js be used to build command-line applications?

**Answer:** ✅ Yes.

---

# 27. Programming Paradigms

### 98. Does Python support object-oriented programming?

**Answer:** ✅ Yes.

---

### 99. Does JavaScript support object-oriented programming?

**Answer:** ✅ Yes.

---

### 100. Does Python support functional programming features?

**Answer:** ✅ Yes.

**Examples:**

```python
map()
filter()
lambda
```

---

### 101. Does JavaScript support functional programming features?

**Answer:** ✅ Yes.

**Examples:**

```javascript
map()
filter()
reduce()
```

---

# 🧠 Compact Python vs JavaScript Cheat Sheet

| Topic                    | 🐍 Python                                  | 🟨 JavaScript                           |
| ------------------------ | ------------------------------------------ | --------------------------------------- |
| Language                 | Python                                     | JavaScript                              |
| Runtime                  | Python interpreter/runtime                 | Browser or Node.js                      |
| Node.js                  | —                                          | JavaScript runtime                      |
| Engine                   | CPython is an implementation               | V8 in Node.js                           |
| Typing                   | Dynamically typed, strongly typed          | Dynamically typed                       |
| Block syntax             | Indentation                                | `{}`                                    |
| Function keyword         | `def`                                      | `function` / arrow functions            |
| Null-like value          | `None`                                     | `null`                                  |
| Equality                 | `==`                                       | `===` commonly used for strict equality |
| Identity                 | `is`                                       | Object reference comparison with `===`  |
| List/Array               | `list`                                     | `Array`                                 |
| Tuple                    | `tuple`                                    | No built-in tuple type                  |
| Dictionary/object        | `dict`                                     | `Object` / `Map`                        |
| Set                      | `set`                                      | `Set`                                   |
| Package tool             | `pip`                                      | `npm`                                   |
| Common dependency file   | `requirements.txt`, `pyproject.toml`       | `package.json`                          |
| Exception syntax         | `try/except`                               | `try/catch`                             |
| Raise/throw              | `raise`                                    | `throw`                                 |
| Async                    | `async` / `await` / `asyncio`              | `async` / `await` / Promise             |
| Event loop               | Used by async frameworks such as `asyncio` | Core part of Node.js async I/O          |
| REST APIs                | Django / Flask / FastAPI                   | Express / Fastify / NestJS              |
| JSON                     | `json` module                              | `JSON.parse()` / `JSON.stringify()`     |
| SQL                      | Supported                                  | Supported                               |
| MongoDB                  | Supported                                  | Supported                               |
| CLI                      | Supported                                  | Supported                               |
| Docker                   | Supported                                  | Supported                               |
| Browser native scripting | No                                         | Yes                                     |

---

# 🚨 Don't Mix These Up

```text
Python ≠ Node.js

Python
→ Programming language

JavaScript
→ Programming language

Node.js
→ JavaScript runtime

V8
→ JavaScript engine

npm
→ Node.js/JavaScript package manager

pip
→ Python package installer
```

---

# 🎯 Short Interview Answer

If an interviewer asks:

> **"What is the difference between Python and Node.js?"**

You can say:

> **"Python is a programming language, while Node.js is a runtime environment used to execute JavaScript outside the browser. Python is dynamically and strongly typed, while JavaScript is dynamically typed. Python is commonly used for web development, automation, AI, and data-related work, while Node.js is widely used for server-side JavaScript and I/O-heavy applications. Both can be used to build APIs, work with databases, and develop backend applications."**

---

# ⚡ Final Revision

```text
Python
→ Programming language

JavaScript
→ Programming language

Node.js
→ JavaScript runtime

V8
→ JavaScript engine

Python
→ Dynamically typed + strongly typed

JavaScript
→ Dynamically typed

Python async
→ async / await / asyncio

Node.js async
→ Event loop + non-blocking I/O

Python package manager
→ pip

Node.js package manager
→ npm

Python equality
→ ==

Python identity
→ is

JavaScript strict equality
→ ===

Python list
→ Mutable

JavaScript Array
→ Mutable

Python string
→ Immutable

JavaScript string
→ Immutable

Python exception
→ try / except / raise

JavaScript exception
→ try / catch / throw

Python API frameworks
→ Django / Flask / FastAPI

Node.js API frameworks
→ Express / Fastify / NestJS
```

## 🔥 Most Important Differences

| Remember            | Python                             | JavaScript / Node.js                     |
| ------------------- | ---------------------------------- | ---------------------------------------- |
| What is it?         | Language                           | JavaScript = language; Node.js = runtime |
| Main engine/runtime | CPython is a common implementation | V8 + Node.js                             |
| Blocks              | Indentation                        | `{}`                                     |
| Function            | `def`                              | `function` / arrow                       |
| Null-like value     | `None`                             | `null`                                   |
| Identity            | `is`                               | Reference comparison with `===`          |
| List                | `list`                             | `Array`                                  |
| Tuple               | Built-in                           | No built-in tuple type                   |
| Package manager     | `pip`                              | `npm`                                    |
| Exceptions          | `try/except`                       | `try/catch`                              |
| Backend             | Django / Flask / FastAPI           | Express / Fastify / NestJS               |
| Async               | `asyncio` and `async/await`        | Event loop + `async/await` + Promises    |

