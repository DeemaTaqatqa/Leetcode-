def isAnagram(s, t):
    hashS, hashT ={}, {} # two hash table
    if len(s) != len(t): #if the length is not equal 
        return False

    for i in range(len(s)): # the two strings have the same length so iterate through one doesn't matter
        hashS[s[i]]= 1+ hashS.get(s[i],0) #the hash key is the letter and the value is the frequancy 
        # the point of using get to not thorugh an error if the key doesn't exist 
        # the line is c = 1 + c
        hashT[t[i]]= 1+ hashS.get(t[i],0)

    for c in hashS:
        if hashS[c]!= hashT.get(c,0): #if each letter frequancy is not equal 
            return False
    return True

# the other way to make this is counter(s) == counter(t) make dictonary with counters of the frequancy

# the problem here is the time complextity is iterating in s and t O(s+t) the same for space because it makes 2 tabels with size s+t

# if want to make the space O(1) (usually O(nlogn)) considering sort funciton has no space
#return sorted(s)==sorted(t) # no extra space
