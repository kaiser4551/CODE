# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=set()
        def dfs(node):
            if not node: return None
            val=node.val
            s.add(val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        s=list(s)
        s.sort()
        return s[k-1]