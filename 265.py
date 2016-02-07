class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])
        if k == 0: return 0
        if k == 1 and n > 1: return 0

        min1, min2 = -1, -1
        dp = [0] * k
        for i in xrange(n):
            last1, last2 = min1, min2
            nxt = [0] * k
            for j in xrange(k):
                if last1 == -1: nxt[j] = costs[0][j]
                elif j == last1: nxt[j] = dp[last2]+costs[i][j]
                else: nxt[j] = dp[last1]+costs[i][j]
            dp = nxt
            min1, min2 = -1, -1
            for j in xrange(k):
                if min1 == -1 or dp[j] < dp[min1]:
                    min2 = min1
                    min1 = j
                elif min2 == -1 or dp[j] < dp[min2]: 
                    min2 = j
            print dp, min1, min2

        return min(dp)

test = Solution()
print test.minCostII([
    [1,2,3,4]
    ]) == 1
print test.minCostII([
    [1,2,3,4],
    [1,2,3,4]
    ]) == 3
print test.minCostII([
    [4,3,2,1],
    [4,3,2,1]
    ]) == 3
print test.minCostII([
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
    ]) == 4
print test.minCostII([
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
    ]) == 6
print test.minCostII([
    [1,5,3],
    [2,9,4],
    ]) == 5
