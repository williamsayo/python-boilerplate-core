# Result / Option Type Utility for Python

A lightweight Python utility providing **Result** and **Option** types for safer, functional-style error handling. Inspired by Rust’s `Result`/`Option` and functional programming paradigms.

---

## Table of Contents

- [Result / Option Type Utility for Python](#result--option-type-utility-for-python)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Installation](#installation)
    - [Helper Functions](#helper-functions)
    - [Types](#types)
    - [Type Guards](#type-guards)
  - [Usage Examples](#usage-examples)

---

## Overview

This package provides a Pythonic implementation of **Result** and **Option** types:

- `Ok` — Represents a successful computation containing a value.  
- `Fail` — Represents a failed computation containing an error value.  
- `Result` — Union type representing either `Ok` or `Fail`.  
- `Option` — Represents a value that may or may not exist (like `Option` in Rust), implemented as `Either[T, NothingType]`.  

Key features include:

- Type-safe error handling without exceptions.  
- Iterable support (`for val in Ok(value)`), for easy unpacking.  
- Type guards (`is_ok`, `is_fail`, `is_result`) for static type narrowing.  
- Helper functions for combining and unwrapping results.  

---

## Installation

To use this library locally after cloning the repository, follow these steps:

1. **Clone the repository**

```bash
git clone <repo-url>
cd <repo-folder>
```

2. **Install in editable mode (recommended for development)**

```bash
pip install -e .
```

This will install the package in your Python environment while allowing you to make changes to the code without reinstalling.

---

### Helper Functions

| Function                            | Description                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `result_ok(value)`                  | Create an `Ok` result. Defaults to `None`.                                                             |
| `result_fail(error)`                | Create a `Fail` result with the provided error.                                                        |
| `result_combine(results)`           | Combine a sequence of Results: returns `Ok` with all values if all succeed, or the first `Fail`.       |
| `value_or(result, default)`         | Returns the contained value of an Ok result, or default if Fail. Raises `TypeError` for invalid input. |
| `unwrap_or(result, default)`        | Returns the contained value if result is valid, otherwise returns default.                             |
| `result_equality(result1, result2)` | Compares two Results for equality **only if both are the same variant** (Ok vs Ok or Fail vs Fail).    |

---

### Types
from result.types import Either, Ok, Fail, Result

**Either represents a Result containing an Ok value or an error**

Either[S, F]
Result
Ok[S]
Fail[F]

---

### Type Guards
```bash
from result.utils import is_result, is_ok, is_fail

is_result(val)  # True if val is Ok or Fail
is_ok(val)      # True if val is Ok
is_fail(val)    # True if val is Fail
```

---

## Usage Examples
```bash
from result.utils import result_ok, result_fail

ok_result = result_ok(42)       # Ok(42)
fail_result = result_fail("Error occurred")  # Fail("Error occurred")
```

**Combining results**
```bash
from src.result.helpers import result_combine

result1 = result_ok(1)
result2 = result_ok(2)
failed_result = result_fail("oops")

combined = result_combine([result1, result2])           # Ok([1, 2])
combined_with_fail = result_combine([result1, failed_result]) # Fail("oops")
```

**Using value_or / unwrap_or**
```bash
value_or(ok_result, 0)      # Returns 42
value_or(fail_result, 0)    # Returns 0

unwrap_or(None, "default")  # Returns "default"
```

**Checking Result Type**
```bash
from result.utils import is_ok, is_fail

is_ok(ok_result)    # True
is_fail(ok_result)  # False
```