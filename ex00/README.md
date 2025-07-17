# Modifying vs Reassigning Python Data Structures

This small Python script explores the difference between **modifying data structures in place** and **reassigning them entirely**.

---

## 💭 Context

I was given a basic exercise where I needed to change the contents of some variables:

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
```

And make them display:

```python
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

At first, I just replaced the entire structures with new ones. It worked — but I started wondering: **am I really modifying these variables, or just reassigning new values to them?**

That led me to dig into how Python handles **mutability**, and how I can detect the difference.

---

## 🧪 How to Tell If You're Modifying or Reassigning

Python has a handy built-in function called `id()` that tells you an object’s memory address. If the `id()` stays the same after a change, you’ve modified the object in place. If it changes, you reassigned it.

---

## ✅ Final Script (With Explanation)

Here’s a script that:

1. Initializes the original objects
2. Saves their IDs
3. Applies the required modifications
4. Prints the final values
5. Verifies which objects were modified in place

```python
# Initial data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")        # Immutable
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Save original IDs to compare later
id_list = id(ft_list)
id_tuple = id(ft_tuple)
id_set = id(ft_set)
id_dict = id(ft_dict)

# Modify in place (or reassign if needed)
ft_list[1] = "World!"                      # List is mutable → modify in place
ft_tuple = (ft_tuple[0], "France!")        # Tuples are immutable → must reassign
ft_set.remove("tutu!")                     
ft_set.add("Paris!")                       # Set is mutable → modify in place
ft_dict["Hello"] = "42Paris!"              # Dict is mutable → modify in place

# Output final results
print(ft_list)     # ['Hello', 'World!']
print(ft_tuple)    # ('Hello', 'France!')
print(ft_set)      # {'Hello', 'Paris!'}
print(ft_dict)     # {'Hello': '42Paris!'}

# Check if objects were modified or reassigned
print(f"List modified in place? {id(ft_list) == id_list}")
print(f"Tuple modified in place? {id(ft_tuple) == id_tuple}")
print(f"Set modified in place? {id(ft_set) == id_set}")
print(f"Dict modified in place? {id(ft_dict) == id_dict}")
```

---

## 🧠 What I Learned

- ✅ **Lists**, **sets**, and **dictionaries** are mutable — they can be changed without replacing the whole object.
- ⚠️ **Tuples** are immutable — to "change" a tuple, you must create a new one.
- 🔍 The `id()` function is great for checking if you’re modifying something in place or just pointing the variable to a new object.
- 📌 Just because your program prints the right output doesn’t mean you followed the instructions correctly — sometimes it’s about *how* you do it, not just the end result.

---

## 🖨️ Example Output

```bash
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
List modified in place? True
Tuple modified in place? False
Set modified in place? True
Dict modified in place? True
```

---

If you’re learning Python, playing with mutability and identity like this is a super useful exercise. It teaches you a lot about how Python handles data under the hood.
