import collections
from typing import List


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i: int, j: int, grid: List[List[str]]):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != '1':
                return

            grid[i][j] = '2'

            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j, grid)

        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '2'
                    queue.append((i, j))
                    while queue:
                        k, l = queue.popleft()
                        if k - 1 >= 0 and grid[k - 1][l] == '1':
                            grid[k - 1][l] = '2'
                            queue.append((k - 1, l))
                        if k + 1 < m and grid[k + 1][l] == '1':
                            grid[k + 1][l] = '2'
                            queue.append((k + 1, l))
                        if l - 1 >= 0 and grid[k][l - 1] == '1':
                            grid[k][l - 1] = '2'
                            queue.append((k, l - 1))
                        if l + 1 < n and grid[k][l + 1] == '1':
                            grid[k][l + 1] = '2'
                            queue.append((k, l + 1))
        return res



        
