# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     

duplicate = []

#input n from user
n=int(input("enter n"))

#take list input from the user
for i in range(0,n):
    element=int(input("Enter element in the list"))
    duplicate.append(element)

print(f"Input list: {duplicate}")

print(f"Update list: {Remove(duplicate)}")