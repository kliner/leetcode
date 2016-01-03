class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = s.split()
        dct = {}
        dct2 = {}
        n = len(pattern)
        if len(ss) != n:
            return False
        for i in xrange(n):
            if pattern[i] not in dct and ss[i] not in dct2:
                ch = pattern[i]
                dct[ch] = ss[i]
                dct2[ss[i]] = ch
            elif pattern[i] in dct and ss[i] in dct2:
                if dct[pattern[i]] != ss[i] or dct2[ss[i]] != pattern[i]:
                    return False
            else:
                return False
        return True

        
if __name__ == '__main__':
    test = Solution()
    print test.wordPattern("abba", "dog cat cat dog")
    print test.wordPattern("abba", "dog cat cat fish")
