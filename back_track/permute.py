from typing import List


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(tmp: List[int], visited: List[bool]):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for i in range(len(visited)):
                if not visited[i]:
                    tmp.append(nums[i])
                    visited[i] = True
                    backTrack(tmp, visited)
                    tmp.pop()
                    visited[i] = False
        
        visited = [False] * len(nums)
        backTrack([], visited)
        return res
                    
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backTrack(first: int):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backTrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
        
        backTrack(0)
        return res

