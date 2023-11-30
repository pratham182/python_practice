# Dictionary creation
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding a new key-value pair:", my_dict)

# Updating the value of an existing key
my_dict['age'] = 26
print("Dictionary after updating the value of 'age':", my_dict)

# Deleting a key-value pair
removed_value = my_dict.pop('city')
print(f"Dictionary after removing the 'city' key (removed value: {removed_value}):", my_dict)

# Check if a key is present in the dictionary
key_to_check = 'gender'
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' is present in the dictionary.")
else:
    print(f"The key '{key_to_check}' is not present in the dictionary.")

# Get all keys and values
keys = my_dict.keys()
values = my_dict.values()
print("Keys in the dictionary:", keys)
print("Values in the dictionary:", values)