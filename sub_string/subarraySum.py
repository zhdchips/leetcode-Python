import re
from typing import List


class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        res = 0
        right = 0
        while right < len(nums):
            left = right
            sum = 0
            while left >= 0:
                sum += nums[left]
                if sum == k:
                    res += 1
                left -= 1
            right += 1
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_map = {}
        prefix_map[0] = 1
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                res += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return res


new_solution = Solution()
print(new_solution.subarraySum([1, 1, 1], 2))