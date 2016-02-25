class Solution(object):
    def alienOrder(self, words):
        vertices = [0]*26
        adj = [ set([]) for _ in xrange(26) ]
        for w in words:
            for ch in w:
                vertices[ord(ch)-0x61]=1

        def addEdge(w1, w2):
            for i in xrange(min(len(w1),len(w2))):
                if w1[i] != w2[i]:
                    adj[ord(w1[i])-0x61].add(ord(w2[i])-0x61)
                    return

        if len(words) == 0: return ''
        w1 = words[0]
        for i in xrange(1,len(words)):
            w2 = words[i]
            addEdge(w1, w2)
            w1 = w2

        unfinish = [0] * 26
        marked = [0] * 26
        self.post = []
        self.cycle = 0

        def dfs(v):
            print v, adj[v]
            marked[v] = 1
            unfinish[v] = 1
            for w in adj[v]:
                if self.cycle: return
                if not marked[w]: 
                    dfs(w)
                if marked[w] and unfinish[w]: 
                    self.cycle = 1
                    return

            unfinish[v] = 0
            self.post += [v]

        for i in xrange(26):
            if vertices[i] and not marked[i]:
                dfs(i)
        if self.cycle: return ""

        ans = [chr(ch+0x61) for ch in self.post[::-1]]
        return ''.join(ans)

test = Solution()
print test.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
    ]) == 'wertf'
print test.alienOrder([
    "rftt"
    ])
print test.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ewt",
    "rftt"
    ]) == ''
print test.alienOrder([
    "za",
    "zb",
    "ca",
    "cb"
    ])
