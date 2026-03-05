class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                curHeight = height[stack.pop()]
                if stack:
                    res += (i - stack[-1] - 1) * (min(height[stack[-1]], h) - curHeight)
            stack.append(i)
        return res
