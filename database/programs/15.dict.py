# Initial Dictionary
D = {'Name': 'Allen', 'Age': 27, 5: 123456}

# a. Insert new entry in D
D['Country'] = 'USA'

# Displaying Dictionary after insertion
print("Dictionary after inserting a new entry:", D)

# b. Delete an entry from D
if 'Age' in D:
    del D['Age']

# Displaying Dictionary after deletion
print("Dictionary after deleting 'Age' entry:", D)

# c. Check whether a key is present in D
key_to_check = 'Name'
if key_to_check in D:
    print(f"The key '{key_to_check}' is present in the dictionary.")
else:
    print(f"The key '{key_to_check}' is not present in the dictionary.")

# d. Clear dictionary D
D.clear()

# Displaying Dictionary after clearing
print("Dictionary after clearing:", D)