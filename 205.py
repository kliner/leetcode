class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n <= 1:
            return True
        dct = {}
        for i in xrange(n):
            if s[i] not in dct:
                dct[s[i]] = t[i]
            else:
                if dct[s[i]] != t[i]:
                    return False
        s, t = t, s
        dct = {}
        for i in xrange(n):
            if s[i] not in dct:
                dct[s[i]] = t[i]
            else:
                if dct[s[i]] != t[i]:
                    return False
        return True


if __name__ == '__main__':
    test = Solution()
    print test.isIsomorphic("egg", "add")
    print test.isIsomorphic("foo", "bar")
    print test.isIsomorphic("ab", "aa")

        
