# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        min_diff = float('inf')
        prev = None

        def dfs(node):
            nonlocal prev, min_diff

            if not node:
                return 

            dfs(node.left)

            if prev is not None:
                diff = abs(node.val - prev)
                min_diff = min(min_diff, diff)

            prev = node.val
            
            dfs(node.right)
        
        dfs(root)
            
        return min_diff
