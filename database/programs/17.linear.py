def linear_search(array, n, k):
    for j in range(0, n):
        if array[j] == k:
            return j
    return -1

array_linear = [11, 33, 85, 97, 99]
key_linear = int(input("Enter the key element for search :  "))
n_linear = len(array_linear)
result_linear = linear_search(array_linear, n_linear, key_linear)

if result_linear == -1:
    print("Element not found")
else:
    print("Element found at index:", result_linear)