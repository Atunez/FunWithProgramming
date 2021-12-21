class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        answer = [0, 1]
        
        i = 1
        while len(answer) != n+1:
            for j in range(2**i):
                if len(answer) == n+1:
                    break
                answer.append(answer[j] + 1)
            i += 1
        return answer
        
