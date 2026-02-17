from typing import List


class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[zero_index + 1] = nums[zero_index + 1], nums[i]
                zero_index += 1

        one_index = zero_index
        for i in range(zero_index + 1, len(nums)):
            if nums[i] == 1:
                nums[i], nums[one_index + 1] = nums[one_index + 1], nums[i]
                one_index += 1

    def sortColors2(self, nums: List[int]) -> None:
        zero_next_index = 0
        one_next_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[zero_next_index] = nums[zero_next_index], nums[i]
                if zero_next_index != one_next_index:
                    nums[i], nums[one_next_index] = nums[one_next_index], nums[i]
                zero_next_index += 1
                one_next_index += 1
            elif nums[i] == 1:
                nums[i], nums[one_next_index] = nums[one_next_index], nums[i]
                one_next_index += 1

    def sortColors(self, nums: List[int]) -> None:
        zero_next_index = 0
        two_last_index = len(nums) - 1
        index = 0
        while index <= two_last_index:
            if nums[index] == 0:
                nums[index], nums[zero_next_index] = nums[zero_next_index], nums[index]
                zero_next_index += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[two_last_index] = nums[two_last_index], nums[index]
                two_last_index -= 1
            else:
                index += 1



new_solution = Solution()
arr = [2,0,2,1,1,0]
print(arr)
new_solution.sortColors(arr)
print(arr)