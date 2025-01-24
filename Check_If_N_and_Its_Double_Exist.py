def checkIfExist(arr):
    seen =set()
    for num in arr:
        # to cover the 2 case from two dirctions and in division case it must be even number there no doubles for odd
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False


arr = [3,1,7,11]
print(checkIfExist(arr))


 