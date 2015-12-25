class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0

        for i in xrange(1, n+1):
            if (i+1)*(i+1) > n:
                return i  
           

if __name__ == '__main__':
    test = Solution()
    print test.bulbSwitch(0)
    print test.bulbSwitch(1)
    print test.bulbSwitch(3)
    print test.bulbSwitch(4)
    print test.bulbSwitch(8)
    print test.bulbSwitch(9)
    print test.bulbSwitch(9999999)

