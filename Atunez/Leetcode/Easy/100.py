# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameTreeRec(p, q)
    
    def isSameTreeRec(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        right = self.isSameTreeRec(p.right, q.right)
        left = self.isSameTreeRec(p.left, q.left)
        
        return right and left
        # 95% speed
