from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLowBound(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        lowBound = searchLowBound(nums, target)
        if lowBound == len(nums) or nums[lowBound] != target:
            return [-1, -1]
        else:
            return [lowBound, searchLowBound(nums, target + 1) - 1]
        