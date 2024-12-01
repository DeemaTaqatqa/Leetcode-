
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        elif curSum == target:
            return [l + 1, r + 1]
    return []

numbers = [2,3,4]
target = 6
twoSum(numbers, target)

"""
the idea here is to iterate thorugh the list with two pointers and since the list is sorted each time i get the sum of p1 and p2 i check with the target
instead of iterating from i 0 to len and hte same for j for p2 and have O(n2) even if will didn't do that tell the end by comapring with target 
and negleting the sum which is bigger but still we got throught each elemnet twice
for the second approach
i have two pointers from ends i go up if smaller and down if bigger until i got the values
i used elif not else at the end since that will make this case :
[5,25,75], target = 100
i got [1,3] instead of [2,3]

space is O(1), time O(n) which is the worst case to iterate through all elements
"""