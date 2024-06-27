def removeElement(nums, val):

    p2= len(nums)
    p1=0

    while(p1<p2):
        if nums[p1] == val:
            nums[p1]=nums[p2-1]
            p2-=1
        else:
        
            p1+=1

    return p2


nums=[0,1,2,2,3,0,4,2]
val=2
value=removeElement(nums, val)
print(value)
print(nums)
# O(n) for time and O(1) for space no extra space