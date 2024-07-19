class Solution:
    def twoSum(nums, target):
        hashTable= {} # val: index
        for i, n in enumerate(nums):
            diff= target -n  # get the differnce for 
            if diff in hashTable:
                return [hashTable[diff] , i]
            hashTable[n]=i
#space and run time = O(n)
# i=0
#         j=0
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if (nums[i] + nums[j] == target) and (i != j):
#                     return [i,j]
                