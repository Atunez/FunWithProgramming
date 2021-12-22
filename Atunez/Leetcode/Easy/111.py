# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.minDepthRec(root)
    
    def minDepthRec(self, root):
        if root is None:
            return 0
        
        rl = 1 + self.minDepthRec(root.right)
        ll = 1 + self.minDepthRec(root.left)
        
        if root.right is None:
            return ll
        if root.left is None:
            return rl
        
        
        return min(rl, ll)
