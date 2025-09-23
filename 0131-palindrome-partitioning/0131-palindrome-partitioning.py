class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(start, subset):
            if start == len(s):
                res.append(subset[:])
                return

            for i in range( start, len(s)):
                if isPal(s, start, i):
                    subset.append(s[start:i+1])
                    backtrack(i + 1, subset)
                    subset.pop()
    
        def isPal(s, l, r):
            while l < r :
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0, [])
        return res