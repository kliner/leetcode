class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            if s == t: return False
            cnt = 0
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    if cnt: return False
                    cnt = 1
            return cnt == 1
        if len(s) > len(t):
            s, t = t, s
        if len(s)+1 != len(t): return False
        shift = 0
        for i in xrange(len(s)):
            if s[i-shift] != t[i]:
                if shift: return False
                shift = 1
        if shift:
            return s[-1] == t[-1]
        return True

test = Solution()
print test.isOneEditDistance("", "") == False
print test.isOneEditDistance("a", "")
print test.isOneEditDistance("a", "b")
print test.isOneEditDistance("a", "ac")
print test.isOneEditDistance("a", "a") == False
print test.isOneEditDistance("ab", "ac")
print test.isOneEditDistance("ab", "a")
print test.isOneEditDistance("ab", "abc")
print test.isOneEditDistance("abc", "a") == False
print test.isOneEditDistance("abc", "ab")
print test.isOneEditDistance("abc", "abd")
print test.isOneEditDistance("abc", "abcd")
print test.isOneEditDistance("abc", "bbabc")
