def containsDuplicate(nums):
    nums.sort()
    i=0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

    # #alternative code to make the run time O(n) isnstead of O(nlogn)
    # hashset= set()
    # for n in nums:
    #     if n in hashset:
    #         return True;
    #     hashset.add(n)
    # return False
            
        