from ast import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])
    
        arr = [[None] * m for _ in range(n)]
       
        for i in range(m):
            
            for j in range(n):
                arr[j][i] =matrix[i][j]

           

        return arr

        
           
       