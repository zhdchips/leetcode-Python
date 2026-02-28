from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(leftCount: int, rightCount: int, path:List[str]):
            if rightCount == n:
                res.append(''.join(path))
                return

            if leftCount < n:
                path.append('(')
                backTrack(leftCount + 1, rightCount, path)
                path.pop()

            if rightCount < leftCount:
                path.append(')')
                backTrack(leftCount, rightCount + 1, path)
                path.pop()

        backTrack(0, 0, [])
        return res

