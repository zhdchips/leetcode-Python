class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        multi = 1
        res = [0] * n
        for i in range(n):
            res[i] = multi
            multi *= nums[i]
        
        multi = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * multi
            multi *= nums[i]
        
        return res

