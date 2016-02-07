class Solution(object):

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        if not nums:
            return 0

        S = [nums[0]]
        for i in xrange(1, len(nums)):
            S += [S[-1]+nums[i]]

        def getSum(lo, hi):
            if lo == 0:
                return S[hi]
            else:
                return S[hi]-S[lo-1]
        
        minx = min(S)
        S = [n+minx for n in nums]
        T = [0] * max(S)
        


         


test = Solution()
print test.countRangeSum([-2, 5, -1], -2, 2)

