import heapq
from random import randint
from typing import Counter, List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        heap = []

        for key, count in countMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, key))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, key))
        return [item[1] for item in heap]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        countList = list(countMap.items())
        n = len(countList)
        left = 0
        right = n - 1
        targetIndex = n - k

        while True:
            pivotIndex = randint(left, right)
            pivotValue = countList[pivotIndex][1]
            countList[left], countList[pivotIndex] = countList[pivotIndex], countList[left]

            i = left + 1
            j = right
            
            while i <= j:
                while i <= j and countList[i][1] < pivotValue:
                    i += 1
                while i <= j and countList[j][1] > pivotValue:
                    j -= 1
                if i > j:
                    break
                
                countList[i], countList[j] = countList[j], countList[i]
                i += 1
                j -= 1

            
            countList[left], countList[j] = countList[j], countList[left]
            if j == targetIndex:
                return [item[0] for item in countList[targetIndex:]]
            elif j < targetIndex:
                left = j + 1
            else:
                right = j - 1



    
# Solution().topKFrequent([1], 1)