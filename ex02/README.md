# 🧠 Python Function: `all_thing_is_obj`

This project is a small Python exercise aimed at practicing object type identification using `isinstance()` and Python conditionals.  
The goal is to define a function that prints the type of any given object, with special messages for some string values, and always returns the number `42`.

---

## 📁 Files

### `find_ft_type.py`

This file defines the function `all_thing_is_obj()` but does nothing when executed directly.

```python
def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List : <class 'list'>")
    elif isinstance(object, tuple):
        print("Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print("Set : <class 'set'>")
    elif isinstance(object, dict):
        print("Dict : <class 'dict'>")
    elif isinstance(object, str):
        if object == "Brian":
            print("Brian is in the kitchen : <class 'str'>")
        elif object == "Toto":
            print("Toto is in the kitchen : <class 'str'>")
        else:
            print("Type not found")
    else:
        print("Type not found")
    return 42
```

---

### `test.py`

This script imports the function and tests it with different types of objects:

```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

---

## ▶️ How to Run

1. Make sure both files are in the same directory.
2. Run the test file using Python 3:

```bash
python3 test.py
```

---

### ✅ Expected Output

```text
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
```

If you run `find_ft_type.py` by itself:

```bash
python3 find_ft_type.py
```

It will do nothing. This is expected, since the logic is only called from the test file.

---

## 🧾 Summary

- The function checks the type of an object.
- It prints a message for lists, tuples, sets, dicts, and for specific strings `"Brian"` and `"Toto"`.
- Any unhandled input results in `"Type not found"`.
- The function always returns the integer `42`.

This is a great warm-up for understanding Python's object model and type handling.

---



