from collections import defaultdict
from email.policy import default
from typing import Counter


class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        count1 = Counter()
        count2 = Counter(t)

        m = len(s)
        n = len(t)

        if m < n:
            return ''

        for i in range(n):
            count1[s[i]] += 1

        if count1 == count2:
            return s[0: n]
        
        left = 0
        right = n
        minLen = m
        ans = ''
        while right < m:
            count1[s[right]] += 1
            while count1 >= count2:
                if right - left + 1 <= minLen:
                    minLen = right - left + 1
                    ans = s[left:right + 1]
                count1[s[left]] -= 1
                left += 1
            right += 1
            
        return ans
            
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m < n:
            return ''

        diff = defaultdict(int)
        for c in t:
            diff[c] -= 1
        kinds = 0
        for item in diff:
            kinds += 1

        minLen = m
        ans = ''
        left = right = 0
        while right < m:
            diff[s[right]] += 1
            if diff[s[right]] == 0:
                kinds -= 1
            while kinds == 0 and left <= right:
                if right - left + 1 <= minLen:
                    minLen = right - left + 1
                    ans = s[left:right + 1]
                if diff[s[left]] == 0:
                    kinds += 1
                diff[s[left]] -= 1
                left += 1
            right += 1
        return ans
        
Solution().minWindow("ADOBECODEBANC", "ABC")