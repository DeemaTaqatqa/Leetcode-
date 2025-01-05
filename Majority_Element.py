import collections

# O(n) for time and O(1) for space no extra space using Boyer Moore Algorithem
def majorityElement(nums):
    count= 0
    candiate= None
    for num in nums:
        if count == 0:
            candiate = num
        count += 1 if num == candiate else -1
    return candiate
        

nums = [2,2,1,1,2]
k= majorityElement(nums)
print(k)

# O(n) for time and O(n) for space
# counts= collections.Counter(nums)
# return max (counts.keys(), key=counts.get) 
# but this is O(n) and no extra space