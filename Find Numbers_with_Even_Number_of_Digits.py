def findNumbers(nums):
    count =0
    for num in nums:
        digits = len(str(num)) # in this case the number is always positive if it was bnegative take the abs before str
        if digits % 2 == 0 :
            count += 1
    return count


nums = [555,901,482,1771]
print(findNumbers(nums))


# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         evenNumber=0
#         for num in nums:
#             numOfDigits=1
#             num //=10 # floor division returns the interger of the result
#             while num!=0:
#                 numOfDigits+=1
#                 num //=10
#             if(numOfDigits%2)==0:
#                 evenNumber+=1
#         return evenNumber



# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         # Counter to count the number of even digit integers
#         even_digit_count = 0

#         for num in nums:
#             # Compute the number of digits in num
#             digit_count = int(math.floor(math.log10(num))) + 1
#             if digit_count % 2 == 0:
#                 even_digit_count += 1

#         return even_digit_count

# all of them are O(nlogm) the log for counting the digits of each nubmer * n the number of num in nums 
# the last 2 solution no extra memory is used so it's O(1) the first one is (logm) for each length of num