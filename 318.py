class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        if n <= 1:
            return 0
        p = [2**i for i in xrange(26)]
        dct = [0 for i in xrange(n)]
        for i, word in enumerate(words):
            for ch in word:
                dct[i] |= p[ord(ch)-0x61]
        #print dct

        ans = 0
        for i in xrange(n):
            for j in xrange(i):
                #print dct[i], dct[j], dct[i] & dct[j]
                if dct[i] & dct[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
        
if __name__ == '__main__':
    test = Solution()
    print test.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print test.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
    print test.maxProduct(["a", "aa", "aaa", "aaaa"])
