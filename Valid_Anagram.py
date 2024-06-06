def isAnagram(s, t):
    s_list=  [char for char in s]
    t_list =  [char for char in t]
    t_list.sort()
    s_list.sort()
    return t_list == s_list
# alternative answer
# hashS, hashT ={}, {} # two hash table
# if len(hashS) != hashT: if the length is not equal 
#     return False

# for i in range(len(s)):
#     hashS[s[i]]= 1+ hashS.get(s[i],0) the hash key is the letter and the value is the frequancy 
#     hashT[t[i]]= 1+ hashS.get(t[i],0)

# for c in hashS:
#     if hashS[c]!= hashT[c]: if each letter frequancy is not equal 
#         return False
# return True
# the problem here is the time complextity is iterating in s and t O(s+t) the same for space because it makes 2 tabels with size s+t
# if want to make the space O(1) (usually O(nlogn)) considering sort funciton has no space
#return sorted(s)==sorted(t) # no extra space