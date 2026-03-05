class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if c in map:
                a = stack[-1]
                b = map[c]
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

Solution().isValid('()')