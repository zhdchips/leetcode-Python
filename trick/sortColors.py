class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroIndex = -1
        for i in range(n):
            if nums[i] == 0:
                zeroIndex += 1
                nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
        
        oneIndex = zeroIndex
        for i in range(oneIndex + 1, n):
            if nums[i] == 1:
                oneIndex += 1
                nums[oneIndex], nums[i] = nums[i], nums[oneIndex]


    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        zeroIndex = oneIndex = -1

        for i in range(n):
            if nums[i] == 0:
                nums[zeroIndex + 1], nums[i] = nums[i], nums[zeroIndex + 1]
                if oneIndex != zeroIndex:
                    nums[oneIndex + 1], nums[i] = nums[i], nums[oneIndex + 1]

                oneIndex += 1
                zeroIndex += 1
            elif nums[i] == 1:
                nums[oneIndex + 1], nums[i] = nums[i], nums[oneIndex + 1]
                oneIndex += 1
    
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zeroIndex = -1
        towIndex = n

        i = 0
        while i < towIndex:
            if nums[i] == 0:
                zeroIndex += 1
                nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
                i += 1
            elif nums[i] == 2:
                towIndex -= 1
                nums[towIndex], nums[i] = nums[i], nums[towIndex]
            else:
                i += 1
        





        
