class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print bin(n)
        d = [0, 8, 4, 0b1100, 2, 0b1010, 6, 0b1110, 1, 9, 5, 0b1101, 3, 0b1011, 7, 0xf] 

        r = 0
        for i in range(8):
            r <<= 4
            r |= d[n & 0xf]
            n >>= 4
        #print bin(r)
        return r

if __name__ == '__main__':
    test = Solution()
    print test.reverseBits(43261596)

