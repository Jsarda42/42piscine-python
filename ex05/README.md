# Character Counter

This Python program analyzes a given text and prints the number of:

- Uppercase letters
- Lowercase letters
- Punctuation marks
- Spaces
- Digits

## 📌 What I Learned

- How to use `sys.argv` for command-line argument handling.
- How to use `input()` to prompt the user when no argument is passed.
- How to raise `AssertionError` when too many arguments are provided.
- How to use built-in string methods like `.isupper()`, `.islower()`, `.isdigit()`, `.isspace()`, and `string.punctuation`.
- How to separate logic using a clean `main()` function and helper modules.
- Exception handling for clean exit (`EOFError`, `AssertionError`).
- Writing modular and user-friendly CLI tools in Python.
- Writing and using **docstrings** (`__doc__`) to document functions and modules for better code understanding and maintainability.

## 📖 Docstrings (`__doc__`)

Docstrings are special strings placed right below function, class, or module definitions that describe their purpose. They are accessible via the `__doc__` attribute and help users understand the code without reading the implementation.

Example of accessing docstrings:
```python
import counter
help(counter.counter)           # Shows detailed documentation
print(counter.counter.__doc__)  # Prints the docstring text directly.
```

## 🚀 Usage

```bash
$ python building.py "Hello, World! 123"
The text contains 18 characters:
2 upper letters
8 lower letters
2 punctuation marks
3 spaces
3 digits
```

```bash
$ python building.py
What is the text to count?
Python 3.10 is awesome!
The text contains 24 characters:
1 upper letters
17 lower letters
1 punctuation marks
3 spaces
2 digits
```

```bash
$ python building.py "One" "Two"
AssertionError: Please provide only one argument
```

## 🛠 Structure

- `building.py`: Main script that handles arguments and prompts.
- `counter.py`: Module that performs character counting.

## ✅ Requirements

- Python 3.x
- No external libraries needed (only `string` module)

