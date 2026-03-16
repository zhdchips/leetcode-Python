class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        count = 1
        for i in range(1, n):
            if nums[i] == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count += 1
                    res = nums[i]
        return res