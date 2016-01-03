class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        while num >= 10:
            nxt = 0
            while num >= 10:
                nxt += num % 10 
                num /= 10
            nxt += num
            num = nxt
        return num


if __name__ == '__main__':
    test = Solution()
    print test.addDigits(38)
