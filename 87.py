class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        n += 1
        F = [[[[None] * n for i in xrange(n)] for j in xrange(n)] for k in xrange(n)]
        n -= 1
        return self.dfs(s1, s2, 0, n, 0, n, F)

    def dfs(self, s1, s2, lo1, hi1, lo2, hi2, F):
        #print s1[lo1:hi1] , s2[lo2:hi2]
        if s1[lo1:hi1] == s2[lo2:hi2]:
            F[lo1][hi1][lo2][hi2] = 1
            return True

        if F[lo1][hi1][lo2][hi2] != None:
            return F[lo1][hi1][lo2][hi2] == 1

        count = [0 for i in xrange(128)]
        for i in xrange(0, hi1-lo1):
            count[ord(s1[lo1+i])] += 1
            count[ord(s2[lo2+i])] -= 1
        for i in xrange(128):
            if count[i]:
                F[lo1][hi1][lo2][hi2] = 0
                return False

        for i in xrange(1, hi1-lo1):
            if self.dfs(s1, s2, lo1, lo1+i, lo2, lo2+i, F) and self.dfs(s1, s2, lo1+i, hi1, lo2+i, hi2, F):
                F[lo1][hi1][lo2][hi2] = 1
                return True
            if self.dfs(s1, s2, lo1, lo1+i, hi2-i, hi2, F) and self.dfs(s1, s2, lo1+i, hi1, lo2, hi2-i, F):
                F[lo1][hi1][lo2][hi2] = 1
                return True
        F[lo1][hi1][lo2][hi2] = 0
        return False
        

if __name__ == '__main__':
    test = Solution()
    #print test.isScramble("at", "ta")
    #print test.isScramble("eat", "tae")
    print test.isScramble("great", "taerg")
    print test.isScramble("great", "aetrg")
    print test.isScramble("abcdefghijklmn", "efghijklmncadb")
    print test.isScramble("pcighfdjnbwfkohtklrecxnooxyipj", "npodkfchrfpxliocgtnykhxwjbojie")
