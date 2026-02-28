from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backTrack(tmp: List[int], visited: List[bool]):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            last = None
            for i in range(len(visited)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue

                tmp.append(nums[i])
                visited[i] = True
                backTrack(tmp, visited)
                tmp.pop()
                visited[i] = False
                last = nums[i]
        
        visited = [False] * len(nums)
        backTrack([], visited)
        return res