class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return num - 9 * ((num-1)/9)


if __name__ == '__main__':
    test = Solution()
    print test.addDigits(36)
    print test.addDigits(37)
    print test.addDigits(38)
    print test.addDigits(39)
