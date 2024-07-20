# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp=root
        while temp:
            if temp.val<p.val and temp.val<q.val:
                temp=temp.right
            if temp.val>p.val and temp.val>q.val:
                temp=temp.left
            if (temp.val >= p.val and temp.val <= q.val) or (temp.val >= q.val and temp.val <= p.val):
                return temp