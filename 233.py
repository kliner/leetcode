class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        length = len(str(n))
        a = [0, 1]
        for i in xrange(1,length):
            a.append(a[i] * 10 + 10**i)
        #print a
        ans = 0
        for i in xrange(length-1, -1, -1):
            mod = 10**i
            if n / mod > 1:
                ans += mod
                ans += (n / mod)*a[i]
            elif n / mod == 1:
                ans += n % mod
                ans += a[i] + 1
            n = n % mod
            #print n
        return ans

if __name__ == '__main__':
    test = Solution()
    print test.countDigitOne(0) # = 
    print test.countDigitOne(1) # = 
    print test.countDigitOne(2) # = 
    print test.countDigitOne(11) # = 
    print test.countDigitOne(13) # = 
    print test.countDigitOne(1111) # = 
    print (112 + 300) + (12 + 20) + (2 + 1) + 1
