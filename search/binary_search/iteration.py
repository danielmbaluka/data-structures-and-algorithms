import math

def search(arr, t):
    left = 0
    right = len(arr) - 1
    
    while(left <= right):
        mid = (right + left) // 2
        if t < arr[mid]:
            right = mid
        elif t > arr[mid]:
            left = mid + 1
        else:
            return mid
    
    return -1

print(search([1, 2, 3, 4, 5, 6], 60))



# Example arr = [1, 2, 3, [4], 4, 5, 7, 10]