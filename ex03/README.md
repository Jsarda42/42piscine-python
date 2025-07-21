# NULL_not_found 🕵️‍♂️

`NULL_not_found` is a Python utility function designed to detect and report various "null-like" values commonly used to represent missing, empty, or false data. These include `None`, `NaN`, `0`, empty strings (`''`), and `False`.

It is particularly useful for debugging and educational purposes, offering insights into how different "null" types behave in Python and how they can be programmatically identified.

---

## 🔍 What It Does

- **Prints** the variable name, its value, and its type if the value is one of:
  - `None` → printed as `Nothing`
  - `float('NaN')` → printed as `Cheese`
  - `0` → printed as `Zero`
  - `''` → printed as `Empty`
  - `False` → printed as `Fake`
- **Returns:**
  - `0` if the object matches a known null-like value
  - `1` and prints `Type not Found` if it doesn't match

---

## 📚 Educational Purpose

This function uses Python introspection via the `inspect` module to:
- Analyze the caller’s local scope
- Identify which variable was passed
- Match values by identity (`is`) or, in the case of `NaN`, via `math.isnan()`

It illustrates:
- The difference between equality (`==`) and identity (`is`)
- Why `NaN != NaN` is true in Python
- How dynamic typing and value inspection work in Python

---

## 🧪 Example Output

```bash
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty:  <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
