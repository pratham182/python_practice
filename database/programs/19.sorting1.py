L = []
n = int(input("Enter the number of elements: "))
print("Enter the elements of the list:")
for item in range(n):
    a = int(input(" "))
    L.append(a)
print("Original List:", L)

for i in range(len(L)):
    for j in range(0, (len(L)-1)-i):
        if L[j] > L[j+1]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp

print("Sorted List (Bubble Sort):", L)