# list
print("=== List Examples ===")

my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sliced (1:4):", my_list[1:4])
print("Sliced (::2):", my_list[::2])
my_list.append(6)
print("Appended List:", my_list)

# tuple
print("\n=== Tuple Examples ===")

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Sliced (1:4):", my_tuple[1:4])
print("Sliced (::2):", my_tuple[::2])
# my_tuple[0] = 10  # ❌ This will raise an error

# dictionary
print("\n=== Dictionary Examples ===")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)
print("Value for key 'a':", my_dict['a'])
my_dict['d'] = 4
print("Updated Dictionary:", my_dict)

# set
print("\n=== Set Examples ===")
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
my_set.add(6)
print("Updated Set:", my_set)