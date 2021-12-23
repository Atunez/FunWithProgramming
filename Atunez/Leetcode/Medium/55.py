class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        reach = -1
        
        for i in range(len(nums)):
            # for every number...
            if reach == -1: # base case...
                reach = nums[i]
            if reach >= i:
                reach = max(reach, i + nums[i])
            if reach >= len(nums)-1:
                return True
            if i > reach:
                return False
