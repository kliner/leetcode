class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = [ v for v in vec2d if len(v) != 0]
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.data[self.i][self.j]
        self.j += 1
        if self.j == len(self.data[self.i]):
            self.i += 1
            self.j = 0
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.data) and self.j < len(self.data[self.i])
        

# Your Vector2D object will be instantiated and called as such:
vec2d = [[]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
print v
vec2d = [[1],[],[2]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
print v
vec2d = [[1,2],[3],[4,5,6]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
print v
