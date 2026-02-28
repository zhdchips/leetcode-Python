from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + curr for curr in res]
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backTrack(tmp: List[int], curi: int):
            if curi == n:
                res.append(tmp[:])
                return
            backTrack(tmp, curi + 1)
            tmp.append(nums[curi])
            backTrack(tmp, curi + 1)
            tmp.pop()

        backTrack([], 0)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backTrack(path: List[int], start: int):
            res.append(path[:])

            for i in range(start, n):
                path.append(nums[i])
                backTrack(path, i + 1)
                path.pop()

        backTrack([], 0)
        return res