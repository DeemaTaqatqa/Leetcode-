def duplicateZeros(arr):
    n = len(arr)
    zeros = arr.count(0)  # Count zeros to determine the final shift
    
    # Iterate from the end of the array
    for i in range(n - 1, -1, -1):
        # Check if the position after shifting is within bounds
        if i + zeros < n:
            arr[i + zeros] = arr[i]
        
        # If the element is zero, we need to duplicate it
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0

# Test it
arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)
print(arr)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]
