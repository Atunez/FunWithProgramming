class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ppn = -1
        pn = -1
        answer = []
        for i in range(len(nums)):
            while nums[i]-1 != i:
                # Swap it, it should go to num[num[i] - 1]
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] =  nums[i]
                nums[i] = t
                if pn == -1:
                    pn = t
                    continue
                if pn != -1:
                    ppn = pn
                    pn = t
                if nums[i] == ppn:
                    break

        for i in range(len(nums)):
            if nums[i] != i+1:
                answer.append(i+1)
        return answer
                
