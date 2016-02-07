class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {}
        for ch in s:
            if ch in dct:
                dct[ch]+=1
            else:
                dct[ch]=1
        cnt = 0
        for k in dct.keys():
            if dct[k] & 1 == 1:
                if cnt:
                    return False
                cnt += 1
        return True

test = Solution()
print test.canPermutePalindrome('')
print test.canPermutePalindrome('a')
print not test.canPermutePalindrome('code')
print test.canPermutePalindrome('aab')
print test.canPermutePalindrome('carerac')

