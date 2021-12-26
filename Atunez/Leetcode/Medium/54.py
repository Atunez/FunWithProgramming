class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralOrderRec(matrix, 0)
    
    def spiralOrderRec(self, matrix, order):
        if len(matrix) == 0:
            return []
        if order == 0:
            answer = matrix.pop(0)
            return answer + self.spiralOrderRec(matrix, 1)
        if order == 1: # top right...
            answer = []
            for i in range(len(matrix)):
                if len(matrix[i]) == 0:
                    continue
                answer.append(matrix[i].pop(len(matrix[i]) - 1)) 
            return answer + self.spiralOrderRec(matrix, 2)
        if order == 2:
            answer = matrix.pop()
            answer.reverse()
            return answer + self.spiralOrderRec(matrix, 3)
        if order == 3:
            answer = []
            for i in range(len(matrix)):
                if len(matrix[i]) == 0:
                    continue
                answer.append(matrix[i].pop(0))
            answer.reverse()
            return answer + self.spiralOrderRec(matrix, 0)
