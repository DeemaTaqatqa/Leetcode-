def hIndex(citations) :
        n = len(citations)
        paper_counts = [0] * (n+1)

        for c in citations:
            paper_counts[min(n,c)] += 1
        
        h=n
        papers = paper_counts[n]
        while papers < h:
            h -= 1
            papers += paper_counts[h]
        return h

# to solve this problem 
# first i made a count arrays using the counting sort to count the frequancies of citations for this paper with extra postion 
# then for the edge case for each number that is bigger than the length we added it to the length
# I started from the end of the array and i will continue if the papers < h until i find the oppisite to return
# I keep adding to the papers and updating the h
# O(n) for time and memory 