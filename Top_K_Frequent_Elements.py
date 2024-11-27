def topKFrequent(nums, k):
    count ={}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n, c in count.items():
        freq[c].append(n) # the opp of coutner 
    
    res=[]
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if (len(res) == k) :
                return res
                
        


nums = [1,2,2,3,3,3]
k = 2
res=topKFrequent(nums, k)
print(res)
"""
the idea here is to use bucket sort which is use a list and length of is len(list) +1 , for 6 element , 6 +1 , 0 to 6
and this list will have the index i as a frequancy of count and the value is numbers that match the count , opp of counter 
the idea is to iterate thorugh n each time in the count dict to count at the beining and in the freq list to return the result
also O(n) for space for both dic in the worst case each number is different and for the freq list too

"""