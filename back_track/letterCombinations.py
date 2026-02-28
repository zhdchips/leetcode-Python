from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        n = len(digits)
        res = []
        def backTrack(path: List[str], start: int):
            if start == n:
                res.append("".join(path))
                return
            
            for c in mapping[digits[start]]:
                path.append(c)
                backTrack(path, start + 1)
                path.pop()
        
        backTrack([], 0)
        return res
