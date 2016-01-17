class Solution(object):

    # n logn
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        if not nums:
            return 0

        n = len(nums)
        S = [0]
        for i in xrange(n):
            S += [S[-1]+nums[i]]
        aux = [0] * (n+1)

        def merge(lo, m, hi):
            i, j, l, r = lo, m+1, m+1, m+1
            t = 0
            for k in xrange(lo, hi+1):
                aux[k] = S[k]

            def update(i, l, r):
                while l <= hi and aux[l]-aux[i] < lower:
                    l += 1
                while r <= hi and aux[r]-aux[i] <= upper:
                    r += 1
                #print l, r, aux[i], aux[l:r+1]
                return l, r

            for k in xrange(lo, hi+1):
                if i > m:
                    S[k] = aux[j]
                    j += 1
                elif j > hi:
                    l, r = update(i, l, r)
                    t += r-l
                    S[k] = aux[i]
                    i += 1
                elif aux[j] < aux[i]:
                    S[k] = aux[j]
                    j += 1
                else:
                    l, r = update(i, l, r)
                    t += r-l
                    S[k] = aux[i]
                    i += 1
            #print S
            return t

        def divide(lo, hi):
            if lo >= hi:
                return 0
            m = (lo+hi) >> 1
            ans = divide(lo, m) + divide(m+1, hi) + merge(lo, m, hi)
            return ans
        
        return divide(0, len(nums))

test = Solution()
print test.countRangeSum([-2, 5, -1], -2, 2) # 3
print test.countRangeSum([1,1,1], 2, 4) # 3
print test.countRangeSum([1,1,1,1,1,1,1], 2, 4) # 15

