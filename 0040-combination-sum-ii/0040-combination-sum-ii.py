class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()

        def backtracking(start, subset,total):
            if total == target:
                res.append(subset[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                subset.append(candidates[i])
                backtracking(i+1 ,subset, total + candidates[i] )
                subset.pop()
        
        backtracking(0,[],0)
        return res        