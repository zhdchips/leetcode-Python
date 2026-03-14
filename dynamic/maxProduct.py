class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        n = len(nums)
        minDp = [0] * n
        maxDp = [0] * n
        res = minDp[0] = maxDp[0] = nums[0]
        for i in range(1, n):
            minDp[i] = min(nums[i], nums[i] * minDp[i - 1], nums[i] * maxDp[i - 1])
            maxDp[i] = max(nums[i], nums[i] * minDp[i - 1], nums[i] * maxDp[i - 1])
            res = max(res, maxDp[i])
        return res


    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = minMulti = maxMulti = nums[0]
        for i in range(1, n):
            minMultiTmp = min(nums[i], nums[i] * minMulti, nums[i] * maxMulti)
            maxMultiTmp = max(nums[i], nums[i] * minMulti, nums[i] * maxMulti)
            minMulti = minMultiTmp
            maxMulti = maxMultiTmp
            res = max(res, maxMulti)
        return res 