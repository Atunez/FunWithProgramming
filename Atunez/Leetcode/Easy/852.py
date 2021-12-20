class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if(nums[mid - 1] < nums[mid] > nums[mid + 1]):
                return mid
            if(nums[mid] > nums[mid+1]):
                high = mid - 1
            else:
                low = mid + 1
        return -1
