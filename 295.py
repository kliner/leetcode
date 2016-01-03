from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.left:
            self.left += [-num]
            return
        m = self.findMedian()
        if num <= m:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        if len(self.left)-len(self.right)>1:
            heappush(self.right, -heappop(self.left))
        if len(self.right)-len(self.left)>1:
            heappush(self.left, -heappop(self.right))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        c = cmp(len(self.left), len(self.right))
        if c > 0:
            return -self.left[0]
        elif c < 0:
            return self.right[0]
        else:
            return (self.right[0]-self.left[0])/2.0
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(3)
    print mf.findMedian()  
    mf.addNum(2)
    print mf.findMedian()  
    mf.addNum(1)
    print mf.findMedian()  
    mf.addNum(-1)
    print mf.findMedian()  
    mf.addNum(-2)
    print mf.findMedian()  
    mf.addNum(-3)
    print mf.findMedian()  
    mf.addNum(1)
    print mf.findMedian()  
    mf.addNum(2)
    print mf.findMedian()  
