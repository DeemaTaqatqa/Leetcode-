def longestConsecutive(nums):
    numsSet=set(nums)
    longest=0
    for n in nums:
        if (n-1) not in numsSet:
            length=0
            while (n+length) in numsSet:
                length += 1
            longest = max(length, longest)
    return longest

nums = [2,20,4,10,3,4,5]
result = longestConsecutive(nums)
print(result)

"""
the idea here is to create the sequance and that's by seeing the start if n -1 is not exist and then make the length 0
here we have to start calculate the length and add by checking if each element + 1 ( consequative ) is in the set
we used the set to check if the element is because checking in a set is O(1)
time is O(n) and space is O(n) for the nums where n is the length 

it's linear not n * n because each element is visited once so each nubmer is checked if it's the start
then go to the second loop for the same number no double visiting or nested loop

so O(n) for first loop and O(n) for the second n +  n is n 

The while loop (while (n + length) in numsSet:) does not repeat for every element in nums. 
Instead, it runs only for the start of each sequence (determined by if (n - 1) not in numsSet:). 
Because of this, the total work done by the while loop across all elements is linear (O(n)), not quadratic.
"""