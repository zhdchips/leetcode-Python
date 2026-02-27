import collections
from typing import List


class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        pre = [[] for _ in range(numCourses)]

        for arr in prerequisites:
            indegree[arr[0]] += 1
            pre[arr[1]].append(arr[0])

        queue = collections.deque()
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        while queue:
            pop = queue.pop()
            for course in pre[pop]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        for i in indegree:
            if i != 0:
                return False
        
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for _ in range(numCourses)]

        for arr in prerequisites:
            pre[arr[1]].append(arr[0])

        def dfs(status: List, pre: List[List[int]], cur: int) -> bool:
            if status[cur] == 2:
                return True

            if status[cur] == 1:
                return False
            
            status[cur] = 1
            for i in pre[cur]:
                if not dfs(status, pre, i):
                    return False
            status[cur] = 2
            return True
            


        status = [0] * numCourses
        for i in range(numCourses):
            if status[i] != 2:
                if not dfs(status, pre, i):
                    return False

        return True