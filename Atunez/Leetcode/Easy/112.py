# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumRec(root, targetSum, 0)
    
    def hasPathSumRec(self, root, targetSum, currentSum):
        if root is None:
            return False
        
        if currentSum + root.val == targetSum and root.left is None and root.right is None:
            return True
        
        right = self.hasPathSumRec(root.right, targetSum, root.val + currentSum)
        left = self.hasPathSumRec(root.left, targetSum, root.val + currentSum)
        
        return left or right
