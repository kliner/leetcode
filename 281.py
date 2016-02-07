from Queue import Queue
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1, v2]
        self.ids = [0, 1]
        self.idx = 0
        self.q = Queue()
        self.push()
    
    def push(self):
        nxt = []
        for i in self.ids:
            if self.idx < len(self.v[i]):
                self.q.put(self.v[i][self.idx])
                nxt.append(i)
        self.ids = nxt
        self.idx += 1

    def next(self):
        """
        :rtype: int
        """
        ans = self.q.get()
        if self.q.empty(): self.push()
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.q.empty()
        

# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2,3,4]
v2 = [5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print v
