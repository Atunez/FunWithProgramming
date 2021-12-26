class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for i in range(len(nums)):
            if i == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] * left[-1])
                
        for i in range(len(nums)):
            if i == 0:
                right.append(nums[-1])
            else:
                right.append(nums[len(nums) - i - 1] * right[-1])
        
        right.reverse()
        
        answer = []
        
        # right[0] is 
        
        # X X X X X X
        # X X X X X X
        
        for i in range(len(nums)):
            if i == 0:
                answer.append(right[1])
            elif i == len(nums) - 1:
                answer.append(left[-2])
            else:
                answer.append(left[i-1] * right[i+1])
                
        return answer
            
