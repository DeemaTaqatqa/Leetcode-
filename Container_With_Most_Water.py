def maxArea(heights):
    res=0

    l = 0
    r = len(heights) -1
    print(l,r)
    while l < r :
        height = min(heights[l], heights[r])
        width = r - l
        area = height * width
        res = max(res, area)
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
    return res

heights = [1,7,2,5,4,7,3,6]
print(maxArea(heights))

"""
O(n) for time becuase i used two pointers from left and right so i only pass through the same element once
O(1) for space no extra space
"""