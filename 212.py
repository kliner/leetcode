class TrieNode(object):
    def __init__(self):
        self.next = [None for i in range(26)]
        self.val = None

class Trie(object):
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self.put(self.root, word, 0)

    def put(self, x, word, d):
        if x == None:
            x = TrieNode()
        if len(word) == d:
            x.val = word
            return x
        ch = word[d]
        x.next[ord(ch)-97] = self.put(x.next[ord(ch)-97], word, d+1)
        return x

    def getNode(self, x, ch):
        if x == None:
            return None
        return x.next[ord(ch)-97]


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.dx = [0,1,0,-1]
        self.dy = [1,0,-1,0]
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []
        self.ans = set([])
        self.m, self.n = m, n

        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        #print trie.root.next

        visit = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.dfs(board, visit, i, j, self.trie.root)

        return list(self.ans)


    def dfs(self, board, visit, i, j, node):
        if not node:
            return
        visit[i][j] = 1
        newNode = self.trie.getNode(node, board[i][j])
        #print i, j, newWord, newNode
        if newNode:
            if newNode.val:
                self.ans.add(newNode.val)
            for k in range(4):
                x = i + self.dx[k]
                y = j + self.dy[k]
                if x >= 0 and x < self.m and y >= 0 and y < self.n and not visit[x][y]:
                    self.dfs(board, visit, x, y, newNode)
        visit[i][j] = 0
        
if __name__ == '__main__':
    test = Solution()
    print test.findWords([
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']],
                ["oath","pea","eat","rain"])
    print test.findWords([ ['a'] ], ['a'])
    print test.findWords([
                ['s','e','e','n','e','w'],
                ['t','m','r','i','v','a'],
                ['o','b','s','i','b','d'],
                ['w','m','y','s','e','n'],
                ['l','t','s','n','s','a'],
                ['i','e','z','l','g','n']],
                ["oath","pea","eat","rain"])
