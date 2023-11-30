L = [10, 20, 30]

# Displaying Initial List
print("Initial List:", L)

# Insert new numbers to List L
L.append(40)
L.extend([50, 60])

# Displaying List after insertion
print("List after inserting new numbers:", L)

# Delete numbers from List L
L.remove(20)

# Displaying List after deletion
print("List after deleting 20:", L)

# Sum all numbers in List L
sum_of_numbers = sum(L)
print("Sum of numbers in the list:", sum_of_numbers)

# Delete the List L
L.clear()

# Displaying List after clearing
print("List after clearing:", L)
