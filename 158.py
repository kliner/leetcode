# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    buf4 = [""]*4
    remain_start = 0
    remain_cnt = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        cnt = 0
        while n > 0:
            if self.remain_cnt >= n:
                for i in xrange(self.remain_start, self.remain_start + n):
                    buf[cnt] = self.buf4[i]
                    self.remain_start += 1
                    self.remain_cnt -= 1
                    cnt += 1
                return cnt
            else:
                for i in xrange(self.remain_start, self.remain_start + self.remain_cnt):
                    buf[cnt] = self.buf4[i]
                    cnt += 1
                    n -= 1

            self.buf4 = [""]*4
            self.remain_start = 0
            self.remain_cnt = read4(self.buf4)
            if not self.remain_cnt:
                return cnt
            l = min(self.remain_cnt, n)
            for i in xrange(l):
                buf[cnt] = self.buf4[i]
                cnt += 1
                self.remain_start += 1
                self.remain_cnt -= 1
                n -= 1
        return cnt

