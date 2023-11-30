# String creation
string1 = "Hello"
string2 = "World"

# Concatenation
concatenated_string = string1 + " " + string2
print("Concatenated String:", concatenated_string)

# String deletion (slicing)
start_index = 2
end_index = 5
deleted_portion = concatenated_string[start_index:end_index]
remaining_string = concatenated_string[:start_index] + concatenated_string[end_index:]
print("Deleted Portion:", deleted_portion)
print("Remaining String:", remaining_string)