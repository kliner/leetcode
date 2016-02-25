class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        dct = {}
        n = len(words)
        for i in xrange(n):
            if words[i] in dct: dct[words[i]].append(i)
            else: dct[words[i]] = [i]
        self.dct = dct
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a1 = self.dct[word1]
        a2 = self.dct[word2]
        a = [0] * (len(a1)+len(a2))
        l1, l2 = 0, 0
        for i in xrange(len(a)):
            if l1 == len(a1):
                a[i] = (a2[l2], 2)
                l2 += 1
            elif l2 == len(a2):
                a[i] = (a1[l1], 1)
                l1 += 1
            elif a1[l1] < a2[l2]:
                a[i] = (a1[l1], 1)
                l1 += 1
            else:
                a[i] = (a2[l2], 2)
                l2 += 1

        lasti, lastj = a[0]
        ans = 1e10
        for i, j in a[1:]:
            if lastj|j == 3:
                ans = min(ans, abs(lasti-i))
            lasti, lastj = i, j
        return ans

# Your WordDistance object will be instantiated and called as such:
wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print wordDistance.shortest("coding", "practice")
print wordDistance.shortest("coding", "makes")
