class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0: return 0

        cur = costs[0]
        for i in xrange(1, n):
            nxt = [1e100]*3
            nxt[0] = min(cur[1], cur[2])+costs[i][0]
            nxt[1] = min(cur[0], cur[2])+costs[i][1]
            nxt[2] = min(cur[0], cur[1])+costs[i][2]
            cur = nxt
        return min(cur)
            
