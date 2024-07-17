# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def ina(node):
            if not node:
                return 0
            return 1+max(ina(node.left),ina(node.right))
        return ina(root)
        if not root:
            return None
        

        # levels=[]
        # queue=deque([root])
        # c=0
        # while queue:
        #     cur_level_size=len(queue)
        #     cur_level=[]
        #     c+=1
        #     for _ in range(cur_level_size):

        #         front=queue.popleft()

        #         cur_level.append(front.val)

        #         if front.left:
        #             queue.append(front.left)
        #         if front.right:
        #             queue.append(front.right)
                
        #     levels.append(cur_level)
        # return c