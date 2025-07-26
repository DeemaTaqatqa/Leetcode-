# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res

        queue = deque([root])
        #level_num = 0

        left_to_right = True

        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            #if level_num %2 != 0: #odd number
            #    level = level [::-1] # reverse the level in this case
            
            if not left_to_right:
                level.reverse()
            
            res.append(level)
            
            #level_num += 1  
            left_to_right = not left_to_right # toggle or flip to make it zigzag one-time true and one-time false
        
        return res
            
