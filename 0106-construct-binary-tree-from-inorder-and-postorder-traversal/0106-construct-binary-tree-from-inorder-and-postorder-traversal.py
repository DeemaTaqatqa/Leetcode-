# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        # Start from the last postorder element
        self.post_idx = len(postorder) - 1
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Get root value and create the node
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            
            # Move to the next root in postorder
            self.post_idx -= 1
            
            # Build right subtree first (because postorder is L → R → root)
            root_idx = idx_map[root_val]
            root.right = helper(root_idx + 1, right)
            root.left = helper(left, root_idx - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)