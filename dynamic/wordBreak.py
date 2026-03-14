from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if s[i - len(word): i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break
        return dp[n]

Solution().wordBreak("leetcode", ["leet","code"])