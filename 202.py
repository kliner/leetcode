class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        dct = set([]) 
        while n not in dct:
            dct.add(n)
            n = self.makeNum(n)
            #print n
            if n == 1:
                return True

        return False 

    def makeNum(self, n):
        s = str(n)
        a = 0
        for ch in s:
            a += int(ch) ** 2
        return a

if __name__ == '__main__':
    test = Solution()
    print test.makeNum(19) # 82
    print test.isHappy(0) # False
    print test.isHappy(1) # True
    print test.isHappy(2) # False

