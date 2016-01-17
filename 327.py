class Solution(object):

    # n logn logn
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

        def solve(arr1, arr2, q):
            l1, l2 = len(arr1), len(arr2)
            i, j = 0, l2
            ans = 0
            while i < l1 and j > 0:
                if arr1[i] + arr2[j-1] >= q:
                    j-=1
                else:
                    ans += (l2-j)
                    i+=1
            ans += (l1-i)*l2
            return ans

        def divide(lo, hi):
            if lo == hi:
                if lower <= nums[lo] <= upper:
                    return 1
                else:
                    return 0
            m = (lo+hi) >> 1
            ans = divide(lo, m)
            ans += divide(m+1, hi)
            left = [getSum(i,m) for i in xrange(lo, m+1)]
            right = [getSum(m+1,i) for i in xrange(m+1, hi+1)]
            left.sort()
            right.sort()
            #print left, right
            ans += solve(left, right, lower) - solve(left, right, upper+1)
            #print ans
            return ans
        
        return divide(0, len(nums)-1)

test = Solution()
print test.countRangeSum([-2, 5, -1], -2, 2)
print test.countRangeSum([1,1,1,1,1,1,1], 2, 4)
