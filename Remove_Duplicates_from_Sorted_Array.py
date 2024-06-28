def removeDuplicates(nums):
    p1=0
    p2=1
    while(p1<p2 and p2<len(nums)):
        if(nums[p1] == nums[p2]):
            del nums[p2]
        else:
            p1+=1
            p2+=1
    return len(nums)



nums = []
k= removeDuplicates(nums)
print(k)
print(nums)