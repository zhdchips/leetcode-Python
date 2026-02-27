import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                k, l = queue.popleft()
                if k - 1 >= 0 and grid[k - 1][l] == 1:
                    grid[k - 1][l] = 2
                    queue.append((k - 1, l))
                if k + 1 < m and grid[k + 1][l] == 1:
                    grid[k + 1][l] = 2
                    queue.append((k + 1, l))
                if l - 1 >= 0 and grid[k][l - 1] == 1:
                    grid[k][l - 1] = 2
                    queue.append((k, l - 1))
                if l + 1 < n and grid[k][l + 1] == 1:
                    grid[k][l + 1] = 2
                    queue.append((k, l + 1))
            if queue:
                minutes += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes