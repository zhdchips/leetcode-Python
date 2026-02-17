import re


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = right = 0
        max_length = 1
        num_set = set()
        while right < len(s):
            if s[right] in num_set:
                max_length = max(max_length, len(num_set))
                while s[right] in num_set:
                    num_set.remove(s[left])
                    left += 1    
            num_set.add(s[right])
            right += 1
        max_length = max(max_length, len(num_set))
        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        left = right = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in index_map and index_map[s[right]] >= left:
                left = index_map[s[right]] + 1
            index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
            

new_solution = Solution()
print(new_solution.lengthOfLongestSubstring("abcabcbb"))
