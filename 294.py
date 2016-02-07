class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.cache = {}
        return self.judge(s)
                
    def judge(self, s):
        if s in self.cache:
            return self.cache[s]
        a = self.generatePossibleNextMoves(s)
        if not a:
            self.cache[s] = False
            return False
        for t in a:
            if not self.judge(t):
                self.cache[s] = True
                return True
        self.cache[s] = False
        return False
        
    def generatePossibleNextMoves(self, s):
        n = len(s)
        if n <= 1:
            return []
        ans = []
        for i in xrange(n-1):
            if s[i] == s[i+1] == '+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans

test = Solution()
print not test.canWin("+")
print not test.canWin("+-")
print test.canWin("++")
print not test.canWin("+--+")
print test.canWin("++++")
print not test.canWin("+++++")
print test.canWin("+--++")
