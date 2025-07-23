# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None  # Pointer to keep track of previous node
        
        def dfs(node):
            if not node:
                return
            
            # Reverse post-order: right -> left -> root
            dfs(node.right)
            dfs(node.left)
            
            # Rewire the pointers
            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)