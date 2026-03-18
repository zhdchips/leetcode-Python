class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modifmatrixy  in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroCol = any(matrix[i][0] == 0 for i in range(m))
        zeroRow = any(matrix[0][i] == 0 for i in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if zeroCol:
            for i in range(m):
                matrix[i][0] = 0
        if zeroRow:
            for i in range(n):
                matrix[0][i] = 0