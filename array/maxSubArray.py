from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        def subArray(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) >> 1
            return max(subArray(left, mid), subArray(mid + 1, right), subArrayCrossMid(left, mid, right))

        def subArrayCrossMid(left: int, mid: int, right: int) -> int:
            index1 = mid - 1
            sum1 = 0
            max1 = 0
            if index1 >= 0:
                while index1 >= left:
                    sum1 += nums[index1]
                    max1 = max(max1, sum1)
                    index1 -= 1
            
            index2 = mid + 1
            sum2 = 0
            max2 = 0
            if index2 < len(nums):
                while index2 <= right:
                    sum2 += nums[index2]
                    max2 = max(max2, sum2)
                    index2 += 1

            return max1 + max2 + nums[mid]
        
        return subArray(0, len(nums) - 1)
            

Solution().maxSubArray([5,4,-1,7,8])