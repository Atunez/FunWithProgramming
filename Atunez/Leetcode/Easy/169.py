class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm...
        # Regardless of how the array is done, the most common number
        # will always be the best
        if len(nums) == 1:
            return nums[0]
        
        best = nums[0]
        seen = 1
        
        for num in nums:
            if num == best:
                seen += 1
            else:
                seen -= 1
                if(seen == 0):
                    best = num
                    seen = 1
        
        return best
