class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = [ set([]) for i in xrange(26) ]
        vertices = set([])
        for s in words:
            for ch in s:
                vertices.add(ord(ch)-0x61)
        
        def getEdge(s1, s2):
            for i in xrange(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    return ord(s1[i])-0x61, ord(s2[i])-0x61

        n = len(words)
        if n == 0:
            return ""
        s1 = words[0]
        for i in xrange(1, n):
            t = getEdge(s1, words[i])
            if t:
                a, b = t
                edges[a].add(b)
            s1 = words[i]
        
        #print vertices
        #print edges

        finish = [1] * 26
        marked = [0] * 26
        postorder = []
        cycle = [False]
        
        def dfs(v):
            finish[v] = 0
            marked[v] = 1
            for w in edges[v]:
                if cycle[0]:
                    return
                if not marked[w]:
                    dfs(w)
                elif not finish[w]:
                    cycle[0] = True
                    return
            postorder.append(v)
            finish[v] = 1
                    
        for i in xrange(26):
            if i in vertices and not marked[i]:
                dfs(i)
                    
        if cycle[0]:
            return ""
        ans = ""
        postorder = postorder[::-1]
        for ch in postorder:
            ans += chr(ch+0x61)
        return ans


        
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

'''
t<f, w<e, r<t, e<r
'''
