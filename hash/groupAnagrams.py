from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in map:
                map[sorted_str].append(str)
            else:
                map[sorted_str] = [str]
        return list(map.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            tuple_count = tuple(count)
            if tuple_count in map:
                map[tuple_count].append(str)
            else:
                map[tuple_count] = [str]
        return list(map.values())

new_solution = Solution()
print(new_solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))