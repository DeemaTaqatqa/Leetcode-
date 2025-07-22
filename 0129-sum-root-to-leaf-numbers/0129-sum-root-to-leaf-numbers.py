# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val

            # If it's a leaf node, return the number formed
            if not node.left and not node.right:
                return current_sum

            # Otherwise, return the sum from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)
