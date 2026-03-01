from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        l = len(word)

        boardCount = {}
        wordCount = {}
        for i in range(n):
            for j in range(m):
                boardCount[board[i][j]] = boardCount.get(board[i][j], 0) + 1
        for c in word:
            wordCount[c] = wordCount.get(c, 0) + 1

        for key, val in wordCount.items():
            if val > boardCount.get(key, 0):
                return False

        if wordCount[word[0]] > wordCount[word[-1]]:
            word = word[::-1]


        def backTrack(i: int, j: int, curIndex: int) -> bool:
            if curIndex == l:
                return True

            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == '#' or board[i][j] != word[curIndex]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'
            curIndex += 1
            if backTrack(i - 1, j, curIndex) or backTrack(i + 1, j, curIndex) or backTrack(i, j - 1, curIndex) or backTrack(i, j + 1, curIndex):
                return True

            board[i][j] = tmp
            return False
        
        for i in range(n):
            for j in range(m):
                if backTrack(i, j, 0):
                    return True

        return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
Solution().exist(board, "ABCESEEEFS")