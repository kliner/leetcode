import copy
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        vertices = set([])
        adj = {}
        for ticket in tickets:
            vertices.add(ticket[0])
            if ticket[0] in adj:
                if ticket[1] in adj[ticket[0]]: adj[ticket[0]][ticket[1]] += 1
                else: adj[ticket[0]][ticket[1]] = 1
            else: adj[ticket[0]] = {ticket[1]:1}

        self.find = False
        self.ans = None

        def dfs(v, i, cur):
            if self.find: return
            if i == len(tickets):
                self.ans = copy.copy(cur)
                self.find = True
                return
            if v not in vertices: return
            nxt = adj[v].keys();
            nxt.sort()
            for w in nxt:
                if adj[v][w] > 0:
                    adj[v][w] -= 1
                    cur.append(w)
                    dfs(w, i+1, cur)
                    cur.pop()
                    adj[v][w] += 1
                    
        dfs("JFK", 0, ["JFK"])
        return self.ans

test = Solution()
print test.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print test.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print test.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
