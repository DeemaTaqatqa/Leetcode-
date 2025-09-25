class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(subset, start):

            if k == len(subset):
                res.append(subset[:])
                return

            for i in range(start,n):
                subset.append(i+1)
                backtrack(subset, i+1)
                subset.pop()
        
        backtrack([],0)

        return res