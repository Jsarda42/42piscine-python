# 🧠 Python Function: all_thing_is_obj

This project is a small Python exercise focused on practicing types, conditionals, and function design.

We create a function that checks the type of an object, prints a message depending on that type, and always returns the number `42`. It’s a fun way to get familiar with `isinstance()` and working with Python's built-in types.

---

## 🔧 Files

### `find_ft_type.py`

This file defines the function:

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
This file does not execute anything when run directly. That’s intentional — the logic only runs when imported from another file.

test.py
This file is your tester. It imports the function and runs it with different types of values:

python
Copy code
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
▶️ How to Run
Make sure both files are in the same folder. Then run only the test file:

bash
Copy code
python3 test.py
You should see the following output:

python
Copy code
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
If you try to run find_ft_type.py by itself:

bash
Copy code
python3 find_ft_type.py
It will do nothing — and that’s the expected behavior.

✅ Summary
The function checks the type of an object and prints a custom message.

It handles list, tuple, set, dict, and specific strings like "Brian" and "Toto".

Anything else prints "Type not found".

It always returns the integer 42.

This is a great warm-up for understanding Python's type system and conditionals.


