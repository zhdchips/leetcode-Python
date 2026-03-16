class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = i
                break
        
        if flag != -1:
            for i in range(n - 1, flag, -1):
                if nums[flag] < nums[i]:
                    nums[flag], nums[i] = nums[i], nums[flag]
                    break

        left = flag + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

