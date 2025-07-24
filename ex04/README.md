# WhatIs - Even or Odd Checker

This project is a simple Python script named `whatis.py` that accepts exactly one command-line argument, validates that it is an integer, and determines whether the number is even or odd. If the input conditions are not met, it raises clear `AssertionError`s with descriptive messages.

---

## What I Learned

- **Command-line argument handling**: Using `sys.argv` to access and validate command-line inputs.
- **Input validation**: Ensuring the exact number of arguments and that the argument is an integer, including negatives.
- **Error handling with assertions**: Raising `AssertionError` with clear messages for invalid input.
- **Type conversion and exception handling**: Safely converting strings to integers with `try/except`.
- **Using modulo operator `%`**: Determining even or odd numbers.
- **Writing user-friendly CLI output**: Printing precise and formatted messages.

---

## Usage

Run the script from the command line with a single integer argument:

python whatis.py <number>

---

## Examples

$ python whatis.py 14  
I'm Even.

$ python whatis.py -5  
I'm Odd.

$ python whatis.py  
AssertionError: argument missing

$ python whatis.py 13 5  
AssertionError: more than one argument is provided

$ python whatis.py Hi!  
AssertionError: argument is not an integer

---

This exercise helped me understand fundamental concepts in Python scripting, such as command-line argument processing, validation, error handling, and basic number operations, which are crucial for building robust CLI tools.
