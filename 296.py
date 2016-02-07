class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ax = []
        ay = []
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    ax.append(i)
                    ay.append(j)
        
        def getTotal(nums):
            nums.sort()
            n = len(nums)
            ans = 0
            i, j = 0, n-1
            while i < j:
                ans += nums[j]-nums[i]
                i+=1
                j-=1
            return ans
        
        return getTotal(ax) + getTotal(ay)

test = Solution()
testCase = [
        [1,0,0,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]
        ]
print test.minTotalDistance(testCase) == 6
testCase = [
        [1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0]
        ]
print test.minTotalDistance(testCase) == 4
testCase = [
        [1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
print test.minTotalDistance(testCase) == 0
testCase = [
        [1],
        [0],
        [1]
        ]
print test.minTotalDistance(testCase) == 2
