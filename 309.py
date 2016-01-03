class Solution(object):

    # top-down, TLE
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cache = [None for i in xrange(len(prices))]
        self.hit = 0
        for i in xrange(0, len(prices)):
            self.visit(i, prices, cache)
        print self.hit
        if cache:   
            return max(cache)
        else:
            return 0
        
    def visit(self, start, nums, cache):
        ans = 0
        if start >= len(nums):
            return 0
        #print start, nums[start], cache
        if cache[start] != None:
            self.hit+=1
            return cache[start]
        for i in xrange(start, len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[j]>nums[i]:
                    ans = max(ans, nums[j]-nums[i]+self.visit(j+2, nums, cache))
        cache[start] = ans
        return ans


if __name__ == '__main__':
    test = Solution()
    print test.maxProfit([1,0,3])
    print test.maxProfit([1,2,3,0,2])
    print test.maxProfit([3,2,3,0,2,3])

