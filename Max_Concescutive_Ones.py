def findMaxConsecutiveOnes(nums):
    ones=0
    local_ones = 0
    
    for i in range(len(nums)):
        if (nums[i] == 1):
            local_ones += 1
        else:
            ones = max(local_ones, ones)
            local_ones = 0 

                
    return max(local_ones, ones) 
    


nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))
