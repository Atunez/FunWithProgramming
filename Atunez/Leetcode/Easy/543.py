# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthRec(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        
        rl = 1 + self.maxDepthRec(root.right)
        ll = 1 + self.maxDepthRec(root.left)
        
        return max(rl, ll)

    
    def simpleDiameter(self, root):
        extra = 0
        
        r = self.maxDepthRec(root.right)
        if root.right is not None:
            extra += 1
            
        l = self.maxDepthRec(root.left)
        if root.left is not None:
            extra += 1

        return l + r + extra
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        best = self.simpleDiameter(root)
        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        
        return max(best, l, r)
        
