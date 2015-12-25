class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num < 1:
            return False
        if num == 1:
            return True
        
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                continue
            if num % 3 == 0:
                num = num / 3
                continue
            if num % 5 == 0:
                num = num / 5
                continue
            return False
        return True


if __name__ == '__main__':
    test = Solution()
    print test.isUgly(1)
    print test.isUgly(6)
    print test.isUgly(8)
    print test.isUgly(14)


