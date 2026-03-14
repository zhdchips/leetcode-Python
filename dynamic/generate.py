class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or i == j:
                    dp[i].append(1)
                else:
                    dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
        return dp