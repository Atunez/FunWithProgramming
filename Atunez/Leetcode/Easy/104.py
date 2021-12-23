# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRec(root)
    
    def maxDepthRec(self, root):
        if root is None:
            return 0
        
        rl = 1 + self.maxDepthRec(root.right)
        ll = 1 + self.maxDepthRec(root.left)
        
        if root.right is None:
            return ll
        if root.left is None:
            return rl
        
        
        return max(rl, ll)
