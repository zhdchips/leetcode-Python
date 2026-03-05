class Solution:
    def decodeString1(self, s: str) -> str:
        res = ''
        multi  = 0
        stack = []
        for c in s:
            if '[' == c:
                stack.append((res, multi))
                res = ''
                multi = 0
            elif ']' == c:
                lastRes, lastMulti = stack.pop()
                res = lastRes + lastMulti * res
            elif c >= '0' and c <= '9':
                multi = multi * 10 + ord(c) - ord('0')
            else:
                res += c
        return res

    def decodeString(self, s: str) -> str:
        def recur(s: str, i: int) -> tuple[str, int]:
            res = ''
            multi  = 0
            while i < len(s):
                c = s[i]
                if '[' == c:
                    innerRes, i = recur(s, i + 1)
                    res = res + multi * innerRes
                    multi = 0
                elif ']' == c:
                    return res, i
                elif c >= '0' and c <= '9':
                    multi = multi * 10 + ord(c) - ord('0')
                else:
                    res += c
                i += 1
            return res, i
        
        res, i = recur(s, 0)
        return res