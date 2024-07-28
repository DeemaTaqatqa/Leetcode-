def removeDuplicates(nums):
        p1=0
        p2=p1+1
        count=0
        while p1<p2 and p2< len(nums):
            if nums[p1] == nums[p2] and count ==0:
                count+=1
                p1 , p2 = p1 +1 , p2 +1
            elif nums[p1] == nums[p2] and count == 1:
                del nums[p2]
            elif nums[p1] != nums[p2] :
                count = 0
                p1 , p2 = p1 +1 , p2 +1
        return len(nums)
# no extra memory O(1) and time O(n)

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))

