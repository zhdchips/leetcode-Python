from typing import List


class Solution:
    def partition1(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def backTrack(start:int, path:List[str]):
            if start == n:
                res.append(path)
                return

            for i in range(start, n):
                if (s[start:i + 1] == s[start:i + 1][::-1]):
                    backTrack(i + 1, path + [s[start:i + 1]])
        
        backTrack(0, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        
        path = []
        res = []

        def backTrack(start:int):
            if start == n:
                res.append(path[:])
                return

            for i in range(start, n):
                if (dp[start][i]):
                    path.append(s[start:i + 1])
                    backTrack(i + 1)
                    path.pop()
        
        backTrack(0)
        return res

        
Solution().partition("aab")