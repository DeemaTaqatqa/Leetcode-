def checkIfExist(arr):
    if len(arr) == 0 or arr == 0:
        return False

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and (arr[i] == 2 * arr[j] or arr[i]/2 == arr[j]):
                return True
    return False


arr = [3,1,7,11]
print(checkIfExist(arr))


 