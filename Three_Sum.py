def threeSum(nums):
    res = [] # i ahve to return a list
    
    # the idea to solve it with sorting to avoid duplicates
    nums.sort()
    
    # first i want to get the first element and iterate to find the second and third element
    for i, a in enumerate(nums):
        # this means if this is not the first element and it has the same value of the previous element i don't want to consider it 
        # to avoid having duplicates in the answer, i don't want to get the 3 numbers again or serach twice
        
        if i>0 and nums[i-1] == a:
            continue
        
        # i will start searching by the 2 sum in sorting method, two pointers left and right 
        
        l = i + 1
        r = len(nums) -1
        while l < r:
            ThreeSum= a + nums[r] + nums [l]
            
            if ThreeSum < 0:
                l += 1
            elif ThreeSum > 0 :
                r -= 1
            else:
                res.append([a,nums[r] , nums [l]])
                # i have to update the pointers i need to update the left since it's sorted to avoid getting the same number
                l += 1
                # if after updating i got the same number i want to keep passing unless l < r 
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res


nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(result)

"""
time is O(nlogn) for sorting and O (n2) for iterating thorught the elements twice one to get the first element and then the second 
to get the other two elements by two sum in sorting method

so it's O(n2)

for space it's O(1) or O(n) according to the sort space
"""