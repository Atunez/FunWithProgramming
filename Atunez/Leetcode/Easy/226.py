# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeRec(root)
    
    def invertTreeRec(self, root):
        if root is None:
            return root
        
        root.right, root.left = root.left, root.right
        
        root.left = self.invertTreeRec(root.left)
        root.right = self.invertTreeRec(root.right)
        
        
        return root
