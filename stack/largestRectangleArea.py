from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        n = len(heights)
        stack = [0]
        res = 0
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                curHeight = heights[stack.pop()]
                res = max(res, (i - stack[-1] - 1) * curHeight)
            stack.append(i)
        return res

Solution().largestRectangleArea([2,1,5,6,2,3])