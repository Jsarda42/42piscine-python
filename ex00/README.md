🧪 Object Modification vs Reassignment in Python
This mini-project demonstrates the difference between modifying existing data structures in place vs reassigning them in Python.

💡 Objective
Given the following initial data structures:

python
Copy
Edit
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
The goal is to modify their content to produce the following output:

python
Copy
Edit
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
✅ In-Place Modification (Preferred)
Instead of replacing the entire object, we modify it directly:

python
Copy
Edit
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")  # Tuples are immutable → must reassign
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"
🧪 How We Verified It
We use Python’s id() function to check whether the object was modified or replaced.

python
Copy
Edit
original_id = id(ft_list)
# Modify the list
ft_list[1] = "World!"
# Check if it's the same object
print(id(ft_list) == original_id)  # True → modified in place
A full test script to check all structures:

python
Copy
Edit
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Save original IDs
original_list_id = id(ft_list)
original_tuple_id = id(ft_tuple)
original_set_id = id(ft_set)
original_dict_id = id(ft_dict)

# Modify in place (or reassign if immutable)
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")  # Reassignment
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

# Check if IDs changed
print(f"List modified in place? {id(ft_list) == original_list_id}")
print(f"Tuple modified in place? {id(ft_tuple) == original_tuple_id}")
print(f"Set modified in place? {id(ft_set) == original_set_id}")
print(f"Dict modified in place? {id(ft_dict) == original_dict_id}")
📌 Key Learnings
✅ Lists, sets, and dictionaries are mutable — they can be modified in place.

⚠️ Tuples are immutable — they cannot be modified; you must reassign them.

🧠 Use id() to verify whether you're modifying or reassigning.