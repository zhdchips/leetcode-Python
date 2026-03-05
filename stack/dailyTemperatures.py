class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            cur = temperatures[i]
            while stack and temperatures[stack[-1]] <= cur:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(0, n):
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res
