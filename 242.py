class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = [0 for i in xrange(256)]
        if len(s) != len(t):
            return False
        for ch in s:
            a[ord(ch)]+=1
        for ch in t:
            a[ord(ch)]-=1
        for i in xrange(256):
            if a[i]:
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    print test.isAnagram("rat", "cat")
    print test.isAnagram("act", "cat")
