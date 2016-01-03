class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue:
            self.queue.pop()
        else:
            while self.stack:
                self.queue.append(self.stack.pop())
            self.queue.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        else:
            while self.stack:
                self.queue.append(self.stack.pop())
            return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack == [] and self.queue == []
        
if __name__ == '__main__':
    s = Queue()
    s.push(1)
    s.pop()
    print s.empty()
    s.push(1)
    s.push(2)
    print s.peek()
    s.pop()
    print s.peek()
    print s.empty()
    s.pop()
    print s.empty()


