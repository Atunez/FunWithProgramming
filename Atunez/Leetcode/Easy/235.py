# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestorRec(root, q, p)
        return self.lowestCommonAncestorRec(root, p, q)
    def lowestCommonAncestorRec(self, root, p, q):
        if root.val >= p.val and root.val <= q.val:
            return root
        else:
            # Abuse the fact that this is a bst....
            if p.val < root.val:
                return self.lowestCommonAncestorRec(root.left, p, q)
            else:
                return self.lowestCommonAncestorRec(root.right, p, q)
        
