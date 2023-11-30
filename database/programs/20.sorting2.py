L_selection = []
n_selection = int(input("Enter the number of elements: "))
print("Enter the elements of the list:")
for item in range(n_selection):
    a_selection = int(input(" "))
    L_selection.append(a_selection)
print("Original List:", L_selection)

for i in range(len(L_selection)):
    min_index = i
    for j in range(i + 1, len(L_selection)):
        if L_selection[j] < L_selection[min_index]:
            min_index = j
    L_selection[i], L_selection[min_index] = L_selection[min_index], L_selection[i]

print("Sorted List (Selection Sort):", L_selection)