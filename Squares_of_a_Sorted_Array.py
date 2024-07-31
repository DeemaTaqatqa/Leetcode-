def sortedSquares(nums):
    return sorted(x**2 for x in nums)

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

# O(nlogn) and space O(n) for sorting
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         squared = []
#         for num in nums:
#             squared.append(num*num)
#         return sorted(squared)
                
            
            
            
        