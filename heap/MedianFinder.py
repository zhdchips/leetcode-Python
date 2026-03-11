from cgitb import small
import heapq


class MedianFinder:

    def __init__(self):
        self.smallPartHeap = []
        self.bigPartHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.smallPartHeap or num <= -self.smallPartHeap[0]:
            heapq.heappush(self.smallPartHeap, -num)
            if len(self.smallPartHeap) > len(self.bigPartHeap) + 1:
                heapq.heappush(self.bigPartHeap, -heapq.heappop(self.smallPartHeap))
        else:
            heapq.heappush(self.bigPartHeap, num)
            if len(self.smallPartHeap) < len(self.bigPartHeap):
                heapq.heappush(self.smallPartHeap, -heapq.heappop(self.bigPartHeap))
        

    def findMedian(self) -> float:
        if len(self.smallPartHeap) > len(self.bigPartHeap):
            return -self.smallPartHeap[0]
        else:
            return (-self.smallPartHeap[0] + self.bigPartHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
obj.addNum(3)
param_2 = obj.findMedian()