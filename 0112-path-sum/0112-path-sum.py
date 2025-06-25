# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False  # If the tree is empty, there can be no path sum
        
        # Check if we are at a leaf node and the remaining targetSum matches the node's value
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract the current node's value from the targetSum and recurse on the left and right children
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)