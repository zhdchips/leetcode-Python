from calendar import c
from tkinter.constants import S
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for first in range(len(sorted_nums) - 2):
            if sorted_nums[first] > 0:
                break
            if first > 0 and sorted_nums[first] == sorted_nums[first - 1]:
                continue
            target = -sorted_nums[first]
            second = first + 1
            third = len(sorted_nums) - 1
            while second < third:
                current_sum = sorted_nums[second] + sorted_nums[third]
                if current_sum < target:
                    second += 1
                elif current_sum > target:
                    third -= 1
                elif current_sum == target:
                    res.append([sorted_nums[first], sorted_nums[second], sorted_nums[third]])
                    second += 1
                    third -= 1
                    while second < third and sorted_nums[second] == sorted_nums[second - 1]:
                        second += 1
                    while second < third and sorted_nums[third] == sorted_nums[third + 1]:
                        third -= 1
        return res


new_solution = Solution()
print(new_solution.threeSum([-1,0,1,2,-1,-4]))