import heapq
from typing import Deque, List


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = [(-num, i) for i, num in enumerate(nums) if i < k]
        heapq.heapify(heap)
        ans = []
        ans.append(-heap[0][0])
        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        myQueue = Deque()
        for i in range(k):
            while myQueue and myQueue[-1][0] < nums[i]:
                myQueue.pop()
            myQueue.append((nums[i], i))
        
        ans = []
        ans.append(myQueue[0][0])
        for i in range(k, n):
            while myQueue and myQueue[-1][0] < nums[i]:
                myQueue.pop()
            myQueue.append((nums[i], i))
            while myQueue[0][1] < i - k + 1:
                myQueue.popleft()
            ans.append(myQueue[0][0])
        return ans

        

# Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)