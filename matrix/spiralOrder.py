class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        ans = []
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if left < right and top < bottom:
                for j in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][j])
                for i in range(bottom - 1, top, -1):
                    ans.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return ans