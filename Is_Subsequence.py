def isSubsequence(s,t):
    i,j =0 , 0 # i is the right pointer and j is the left pointer for t 
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return i == len(s)

# O (n+m) and O (1) for memory , solved by two pointers


s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))