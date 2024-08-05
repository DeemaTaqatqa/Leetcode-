def replaceElements(arr):
    n = len(arr)
    max_right = -1
    for i in range(n-1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(arr[i], current)
    
    return arr

arr = [400]
result = replaceElements(arr)
print(result)
