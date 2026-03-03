class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[n - 1]:
                if nums[0] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid

        return left if left != n and nums[left] == target else -1
