import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num):
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]:
            a = -heapq.heappop(self.left)
            b = heapq.heappop(self.right)

            heapq.heappush(self.left, -b)
            heapq.heappush(self.right, a)

        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2.0