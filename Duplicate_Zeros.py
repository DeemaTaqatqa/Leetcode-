class Solution:
    def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        length= len(arr)
        i=0
        while(i<length):
            if arr[i] == 0:
                arr.insert(i+1,0)
                i+=1
            i+=1
        del arr[length:]

