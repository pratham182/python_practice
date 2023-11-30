def binary_search(arr, k, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr_binary = [1, 3, 5, 7, 9]
key_binary = int(input("Enter element that want to search"))
result_binary = binary_search(arr_binary, key_binary, 0, len(arr_binary) - 1)

if result_binary != -1:
    print("Element is present at index:", result_binary)
else:
    print("Not found")