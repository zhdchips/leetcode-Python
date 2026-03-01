class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [None] * n
        col = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        res = []

        def backTrack(r: int):
            if r == n:
                res.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return

            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:
                    queens[r] = c
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    backTrack(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False

        backTrack(0)
        return res