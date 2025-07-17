# Initial objects
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Store initial IDs
list_id_before = id(ft_list)
tuple_id_before = id(ft_tuple)
set_id_before = id(ft_set)
dict_id_before = id(ft_dict)

# === Modify or reassign here ===

# Example of reassignment (this proves replacement)
# ft_list = ["Hello", "World!"]
# ft_tuple = ("Hello", "France!")
# ft_set = {"Hello", "Paris!"}
# ft_dict = {"Hello": "42Paris!"}

# Example of modification (this proves in-place change)
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")  # unavoidable reassignment
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

# Store IDs after
list_id_after = id(ft_list)
tuple_id_after = id(ft_tuple)
set_id_after = id(ft_set)
dict_id_after = id(ft_dict)

# === Test output ===
print(f"List modified in place? {list_id_before == list_id_after}")
print(f"Tuple modified in place? {tuple_id_before == tuple_id_after}")
print(f"Set modified in place? {set_id_before == set_id_after}")
print(f"Dict modified in place? {dict_id_before == dict_id_after}")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)