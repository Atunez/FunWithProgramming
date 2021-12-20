import math

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return (nums[0] == -1 or nums[0] == 1)
        gcd = math.gcd(nums[0], nums[1])
        l = 2
        while l != len(nums):
            gcd = math.gcd(gcd, nums[l])
            l += 1
        return gcd == 1
