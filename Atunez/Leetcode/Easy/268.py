class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums) * (len(nums)+1)) // 2
        for n in nums:
            total -= n
        return total
      # 90.84%, 79.71% (S, M)
