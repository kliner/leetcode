class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        const = [0,0,0]
        if n < 3:
            return const[n]
        ans = 0
        F = [1 for i in xrange(n)]
        i = 2
        while i < n:
            while i < n and not F[i]:
                i += 1
            if i == n:
                return ans
            ans += 1
            for t in xrange(i, n, i):
                F[t] = 0
            i += 1
        return ans   


if __name__ == '__main__':
    test = Solution()
    print test.countPrimes(3) #2 1
    print test.countPrimes(4) #23 2
    print test.countPrimes(7) #235 3
    print test.countPrimes(10) #2357 4
