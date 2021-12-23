# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.mergeTreesRec(root1, root2)
    
    def mergeTreesRec(self, p, q):
        if p and q is None:
            return p
        if p is None:
            return q
        if q is None:
            return p
        
        p.val = p.val + q.val
        
        p.right = self.mergeTreesRec(p.right, q.right)
        p.left = self.mergeTreesRec(p.left, q.left)
        
        return p
        
