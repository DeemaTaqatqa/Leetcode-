def sortedSquares(nums):
    res = [0] * len(nums)
    l=0
    r= len(nums) -1
    pos = r
    while l <= r :
        if abs(nums[l]) > abs(nums[r]):
           res[pos] = (nums[l] **2)
           l += 1
        else:
            res[pos] = (nums[r] **2)
            r -= 1
        pos -= 1
    return res
            
            
            
            
        
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

# O(nlogn) and space O(n) for sorting
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         squared = []
#         for num in nums:
#             squared.append(num*num)
#         return sorted(squared)
                
            
            
            
        