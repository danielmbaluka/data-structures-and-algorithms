def search(arr, t):
    if not arr:
        return -1
    
    size = len(arr)
    mid = size // 2
    if t < arr[mid]:
        return search(arr[0:mid], t)

    return binary_search(arr, t)


print(search([1,2,3,4,5,6], 2))