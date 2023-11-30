L_insertion = []
n_insertion = int(input("Enter the number of elements: "))
print("Enter the elements of the list:")
for item in range(n_insertion):
    a_insertion = int(input(" "))
    L_insertion.append(a_insertion)
print("Original List:", L_insertion)

for i in range(1, len(L_insertion)):
    key = L_insertion[i]
    j = i - 1
    while j >= 0 and key < L_insertion[j]:
        L_insertion[j + 1] = L_insertion[j]
        j -= 1
    L_insertion[j + 1] = key

print("Sorted List (Insertion Sort):", L_insertion)