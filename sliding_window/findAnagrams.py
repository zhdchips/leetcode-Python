from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res
        p_count = [0] * 26
        s_count = [0] * 26
        for index in range(len(p)):
            p_count[ord(p[index]) - ord('a')] += 1
            s_count[ord(s[index]) - ord('a')] += 1

        left = 0
        right = len(p)

        if s_count == p_count:
            res.append(left)

        while right < len(s):
            s_count[ord(s[left]) - ord('a')] -= 1
            left += 1
            s_count[ord(s[right]) - ord('a')] += 1
            right += 1

            if s_count == p_count:
                res.append(left)
        
        return res


new_solution = Solution()
print(new_solution.findAnagrams("cbaebabacd", "abc"))