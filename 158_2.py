# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.remain = 0
        self.cur = 0
        self.buf4 = ['']*4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0

        while total < n:
            if self.remain == self.cur:
                self.remain = read4(self.buf4)
                self.cur = 0
                if self.remain == 0:
                    return total
            buf[total] = self.buf4[self.cur]
            self.cur += 1
            total += 1
            
        return total

