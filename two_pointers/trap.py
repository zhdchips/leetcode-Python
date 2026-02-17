from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = height[left]
        right= len(height) - 1
        right_max = height[right]
        res = 0
        while left < right:
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res


new_solution = Solution()
print(new_solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))