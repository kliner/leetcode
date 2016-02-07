# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        cnt = 0
        while n > 0:
            buf4 = [""]*4
            t = read4(buf4)
            if not t:
                return cnt
            for i in xrange(min(t, n)):
                buf[cnt] = buf4[i]
                cnt += 1
                n -= 1
        return cnt

                
