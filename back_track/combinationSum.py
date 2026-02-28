from typing import List


class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        def backTrack(path: List[int], start, sum: int):
            if start == n or sum >= target:
                return
            
            for i in range(start, n):
                path.append(candidates[i])
                sum += candidates[i]
                if sum == target:
                    res.append(path[:])
                backTrack(path, i, sum)
                sum -= candidates[i]
                path.pop()
        
        backTrack([], 0, 0)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backTrack(path: List[int], start, target: int):
            if target == 0:
                res.append(path[:])
            
            for i in range(start, n):
                if target - candidates[i] < 0:
                    break

                path.append(candidates[i])
                backTrack(path, i, target - candidates[i])
                path.pop()
        
        backTrack([], 0, target)
        return res


