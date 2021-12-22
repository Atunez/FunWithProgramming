# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        level = 0
        levels = self.averageOfLevelsRecur(root, levels, level)
        print(levels)
        answer = []
        for i in range(len(levels)):
            if(levels[i][1] == 0):
                continue
            answer.append(levels[i][0]/levels[i][1])
        return answer
            
    def averageOfLevelsRecur(self, root: Optional[TreeNode], levels: List[List[float]], level: int) -> List[List[float]]:
        
        # Child Node....
        if root is None:
            return levels
        
        if(len(levels) != level+1):
            levels.append([0,0])
        
        levels[level][0] += root.val
        levels[level][1] += 1
        
        levels = self.averageOfLevelsRecur(root.right, levels, level+1)
        levels = self.averageOfLevelsRecur(root.left, levels, level+1)

        return levels
        
        
