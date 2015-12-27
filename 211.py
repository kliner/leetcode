class TrieNode(object):
    def __init__(self):
        self.next = [None for i in range(26)]
        self.val = None

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = None
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.root = self.put(self.root, word, 0)

    def put(self, x, word, d):
        if not x:
            x = TrieNode()
        if d == len(word):
            x.val = 1
            return x
        ch = word[d]
        x.next[ord(ch)-97] = self.put(x.next[ord(ch)-97], word, d+1)
        return x
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.get(self.root, word, 0)

    def get(self, x, word, d):
        if not x:
            return False
        if d == len(word):
            return x.val == 1
        ch = word[d]
        if ch == '.':
            for i in xrange(26):
                if self.get(x.next[i], word, d+1):
                    return True
            return False
        else:
            return self.get(x.next[ord(ch)-97], word, d+1)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print wordDictionary.search("pattern")
    print wordDictionary.search("word")
    print wordDictionary.search("w..d")
