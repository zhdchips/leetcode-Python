class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
        
        res = []
        maxLast = 0
        start = 0
        for i, c in enumerate(s):
            maxLast = max(maxLast, last[ord(c) - ord('a')])
            
            if i == maxLast:
                res.append(i - start + 1)
                start = i + 1

        return res