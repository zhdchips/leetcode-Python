from typing import List


class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        
        target = (int) (s / 2)

        for num in nums:
            if num > target:
                return False

        n = len(nums)
        dp = [[True] + [False] * target for _ in range(n)]
        dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
        
        return dp[n - 1][target]

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        
        target = (int) (s / 2)

        for num in nums:
            if num > target:
                return False

        n = len(nums)
        dp = [True] + [False] * target

        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] | dp[j - nums[i]]
        
        return dp[target]

Solution().canPartition([2,2,3,5])