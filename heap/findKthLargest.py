import heapq
from random import randint, randrange


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif  num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        targetIndex = n - k
        while True:
            pivotIndex = randint(left, right)
            pivotValue = nums[pivotIndex]
            nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
            i = left + 1
            j = right

            while i <= j:
                while i <= j and nums[i] < pivotValue:
                    i += 1
                while  i <= j and nums[j] > pivotValue:
                    j -= 1
                
                if i >= j:
                    break
                    
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            nums[left], nums[j] = nums[j], nums[left]

            if j == targetIndex:
                return nums[j]
            elif j < targetIndex:
                left = j + 1
            else:
                right = j - 1 