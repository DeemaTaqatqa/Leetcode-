def sumOfSquares(n):
    output = 0
    while n:
        digit = n %10
        output += digit **2
        n = n // 10 # floor division
    return output
        
def isHappy(n):
    visit = set()
    while n not in visit:
        visit.add(n)
        n =sumOfSquares(n)
        
        if n == 1:
            return True
    return False 

#both time and space complexity is O(n) watch neetcode for this
print(isHappy(19))
