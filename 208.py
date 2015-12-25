class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None for i in range(26)]
        self.val = None

class Trie(object):

    def __init__(self):
        self.root = None

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        x = self.root
        if not x:
            return False
        for w in word:
            if x.next[ord(w)-97]:
                x = x.next[ord(w)-97]
            else:
                return False
        return x.val != None
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        x = self.root
        if not x:
            return False
        for w in prefix:
            if x.next[ord(w)-97]:
                x = x.next[ord(w)-97]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__ == '__main__':
    trie = Trie()
    trie.insert("shell")
    trie.insert("shellsort")
    print trie.search("sh")
    print trie.startsWith("sh")
    print trie.search("shell")
    print trie.search("shellsort")
