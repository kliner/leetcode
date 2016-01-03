class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal = []
        self.reverse = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.normal.append(x)
        for n in self.reverse:
            self.normal.append(n)
        self.reverse = self.normal
        self.normal = []
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.reverse = self.reverse[1:]
        

    def top(self):
        """
        :rtype: int
        """
        return self.reverse[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.reverse == []
        
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print s.top()
    s.pop()
    print s.top()
    print s.empty()
    s.pop()
    print s.empty()


