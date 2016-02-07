class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        if n == 0:
            return [""]

        ans = []
        def dfs(w, cur):
            if not w:
                ans.append(cur)
            for i in xrange(1, len(w)+1):
                if not cur:
                    dfs(w[i:], cur+w[:i])
                    dfs(w[i:], cur+str(i))
                elif cur[-1] in "1234567890":
                    dfs(w[i:], cur+w[:i])
                else:
                    dfs(w[i:], cur+str(i))
                    
        dfs(word, "")
        return ans

test = Solution()
print test.generateAbbreviations("w")
print test.generateAbbreviations("wd")
print test.generateAbbreviations("word")
