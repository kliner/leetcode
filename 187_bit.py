class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dct = [0 for i in xrange(26)]
        dct[ord('C')-0x41] = 1
        dct[ord('G')-0x41] = 2
        dct[ord('T')-0x41] = 3
        enc = 0
        if len(s) <= 10:
            return []
        for i in xrange(9):
            enc <<= 2
            enc |= dct[ord(s[i])-0x41]
        once = set([])
        twice = set([])
        ans = []
        for i in xrange(9, len(s)):
            enc <<= 2
            enc &= 0xfffff
            enc |= dct[ord(s[i])-0x41]
            if enc not in once:
                once.add(enc)
            elif enc not in twice:
                twice.add(enc)
                ans.append(s[i-9:i+1])
        return ans

        
if __name__ == '__main__':
    test = Solution()
    print test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print test.findRepeatedDnaSequences("AAAAAAAAAAA")

