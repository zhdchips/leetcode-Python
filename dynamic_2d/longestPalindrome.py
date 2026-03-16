class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxLen = 1
        res = s[0:1]

        for L in range(2, n + 1):
            for i in range(n + 1 - L):
                j = i + L - 1
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        res = s[i:j + 1]
        
        return res