class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = set([])
        ret = set([])
        for i in range(10,len(s)+1):
            if s[i-10:i] not in d:
                d.add(s[i-10:i])
            else:
                ret.add(s[i-10:i])
        return list(ret)

        
if __name__ == '__main__':
    test = Solution()
    print test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print test.findRepeatedDnaSequences("AAAAAAAAAAA")
