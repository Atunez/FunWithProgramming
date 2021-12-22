class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        answer = []
        for i in range(m):
            t = []
            for j in range(n):
                t.append(original[i * n + j])
            answer.append(t)
        return answer
