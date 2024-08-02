def validMountainArray(arr):

    p1 = 0
    length = len(arr) 
    
    if length < 3:
        return False
    
    while p1 + 1 < length and arr[p1] < arr[p1+1]:
            p1 +=1
            
    if p1 == 0 or p1 == length - 1:
        return False
    
    while p1 + 1 < length and arr[p1] > arr[p1+1]:
            p1 += 1
        
             
    return (p1 == length - 1)


arr = [0,3,2,1]
print(validMountainArray(arr))