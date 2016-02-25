class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        arr = []
        n = len(words)
        if word1 == word2:
            for i in xrange(n):
                if words[i] == word1: arr.append(i)
            last = arr[0]
            ans = 1e10
            for i in arr[1:]:
                ans = min(ans, i-last)
                last = i
            return ans

        for i in xrange(n):
            if words[i] == word1:
                arr.append((i, 1))
            elif words[i] == word2:
                arr.append((i, 2))
        lasti, lastj = arr[0]
        ans = 1e10
        for i, j in arr[1:]:
            if lastj|j == 3:
                ans = min(ans, abs(lasti-i))
            lasti, lastj = i, j
        return ans
        
test = Solution()
print test.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
print test.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
print test.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "practice", "coding")

