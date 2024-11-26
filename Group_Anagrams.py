from collections import defaultdict
def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result[tuple(count)].append(s)
    return list(result.values())



strs = ["act","pots","tops","cat","stop","hat"]
ans = groupAnagrams(strs)
print(ans)

"""
the idea here is to make the key of the dictionary is the count that contains the 26 letters as a way to encode the each str in strs
then adding or appening the strings to their same count 
to return the list i need the values not key and in a list
i used a non empty diction to aviod errors
i used tuple because in python strings can't be list so i converted to tuple
for time compelexiy i iterate throught each string char c- > n *  m -> the list length * 26 for the count of each letter 
to have m *n * 26 = > m *n 

For each string, a fixed-size array of 26 integers is used. This is O(1) per string, as its size is constant.
Result Dictionary (result):

In the worst case, every string has a unique anagram group. The dictionary stores 
𝑛
n keys, where each key is a tuple of size 26. The space for the dictionary keys is O(n \cdot 26) = O(n).
Each value in the dictionary is a list of strings, and the total space for all strings is O(n \cdot k).
Tuple Representation:

The tuples created for keys are derived from the count array, which is fixed at size 26. This does not contribute additional space for each string.
Overall Space Complexity
The dominant term comes from storing the strings and dictionary keys:

Space Complexity=O(n⋅k)

"""