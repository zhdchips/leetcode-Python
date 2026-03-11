class Solution:
    def jump1(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1
        step = 0
        while i > 0:
            j = i - 1
            while j >= 0:
                if j + nums[j] >= i:
                    tmp = j
                j -= 1
            i = tmp
            step += 1
        return step

    def jump(self, nums: List[int]) -> int:
        end = maxDistance = 0
        n = len(nums)
        step = 0
        for i in range(n - 1):
            maxDistance = max(maxDistance, i + nums[i])
            if i == end:
                step += 1
                end = maxDistance

        return step

