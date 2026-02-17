from turtle import right
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1; # 第一个 0 的位置
        right = 0; # index
        while right < len(nums):
            if nums[right] == 0:
                if left == -1:
                    left = right
            else:
                if left != -1:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
            right += 1
    
new_solution = Solution()
list = [1,0,1]
print(list)
new_solution.moveZeroes(list)
print(list)
