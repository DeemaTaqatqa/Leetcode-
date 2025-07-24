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
        if not root:
            return
        
        # Store original left and right before changing
        left = root.left
        right = root.right
        
        # Set left to None and move left to right
        root.left = None
        
        # Recursively flatten left and attach to right
        self.flatten(left)
        self.flatten(right)
        
        if left:
            root.right = left
            current = root.right
            while current.right:
                current = current.right
            current.right = right