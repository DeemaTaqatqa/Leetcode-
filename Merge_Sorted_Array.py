def merge(nums1, nums2, m,n):
    nums1cp= nums1[:m]
    p1= m -1
    p2= n - 1
    for p in range(n+m-1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p]=nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2-=1
        
#here O(n+m) and space O(n) both from sorting function

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, nums2, m,n)
print(nums1)
#because of sort runtime O(n+mlog(m+n)) and space O(n)
# def merge(nums1, nums2, m,n):
#     for i in range(n):
#                 nums1[m+i] = nums2[i]
#             nums1.sort()

# O(n+m) and O(1) no extra space
            # p2= n-1
            # p1= m-1
    
            # for p in range(n+m-1, -1, -1):
            #     if p2 <0 :
            #         break
            #     if p1 >= 0  and nums1[p1] > nums2[p2]:
            #         nums1[p]=nums1[p1]
            #         p1-=1
            #     else:
            #         nums1[p]=nums2[p2]
            #         p2-=1
