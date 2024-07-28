def reverse(nums, start, end):
    while start < end :
        nums[start], nums[end] = nums[end], nums[start]
        start , end = start +1 , end -1

def rotate(nums, k):
    # speed up the rotation
    k %= len(nums)
    n=len(nums)
    reverse(nums, 0, n-1) # reverse all list
    reverse(nums, 0, k-1) # reverse the first k elemnts after the reverse for all
    reverse(nums, k, n-1) # reverse the remaining
    
nums = [-1,-100,3,99]
k = 2
rotate(nums,k)
print(nums)

#nums[:]= nums[-k:] + nums[:-k]
# in this solution the time and memory is O(n) for both
# note that to make update in the same nums i have to add [:] that's why on leetcode the answer was wrong 
# not in place change but i have created a new nums memory