# List creation
my_list = [1, 3, 5, 7, 9]

# Print the original list
print("Original List:", my_list)

# Append an element to the list
new_element = 11
my_list.append(new_element)
print("List after appending element:", my_list)

# Insert an element at a specific index
index_to_insert = 2
new_element_at_index = 4
my_list.insert(index_to_insert, new_element_at_index)
print("List after inserting element at index 2:", my_list)

# Remove an element by value
value_to_remove = 7
my_list.remove(value_to_remove)
print("List after removing element 7:", my_list)

# Remove an element by index
index_to_remove = 3
removed_element = my_list.pop(index_to_remove)
print(f"List after removing element at index 3 (removed element: {removed_element}):", my_list)

# Find the maximum and minimum values in the list
max_value = max(my_list)
min_value = min(my_list)
print("Maximum value in the list:", max_value)
print("Minimum value in the list:", min_value)

# Calculate the sum and average of the list
sum_of_list = sum(my_list)
average_of_list = sum_of_list / len(my_list)
print("Sum of the list:", sum_of_list)
print("Average of the list:", average_of_list)
