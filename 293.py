class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 1:
            return []
        ans = []
        for i in xrange(n-1):
            if s[i] == s[i+1] == '+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans

test = Solution()
print test.generatePossibleNextMoves('+')
print test.generatePossibleNextMoves('++')
print test.generatePossibleNextMoves('+++')
print test.generatePossibleNextMoves('+-+')
print test.generatePossibleNextMoves('++++')
