class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 0
        i = 0
        n = len(nums)
        while i <= maxStep:
            maxStep = max(maxStep, i + nums[i])
            if maxStep >= n - 1:
                return True
            i += 1
        return False
            
            

