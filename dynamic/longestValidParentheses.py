class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        for i, c in enumerate(s):
            if c == '(':
                continue
            else:
                if i == 0:
                    continue
                else:
                    if s[i - 1] == '(':
                        dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                    elif dp[i - 1] > 0 and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = 2 + dp[i - 1] + (dp[i - 1 - dp[i - 1] - 1] if i - 1 - dp[i - 1] - 1 >= 0 else 0)
        return max(dp)

print(Solution().longestValidParentheses("(()"))