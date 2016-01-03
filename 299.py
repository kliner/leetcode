class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        a, b = 0, 0
        st = [0 for i in xrange(10)]
        for i in xrange(n):
            if secret[i] == guess[i]:
                a += 1
            st[ord(secret[i])-0x30] += 1
        for i in xrange(n):
            if st[ord(guess[i])-0x30]:
                b += 1
                st[ord(guess[i])-0x30] -= 1
        return '%dA%dB' % (a, b-a)


if __name__ == '__main__':
    test = Solution()
    print test.getHint('1807', '7810')
    print test.getHint('1123', '1110')
    print test.getHint('1123', '0111')


