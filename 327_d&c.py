class Solution(object):

    # n logn
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        S = [0]
        for i in xrange(len(nums)):
            S += [S[-1]+nums[i]]
        aux = [0] * len(S)

        def merge(lo, m, hi):
            for i in xrange(lo, hi+1): aux[i] = S[i]
            i, j = lo, m+1
            for k in xrange(lo, hi+1):
                if i > m: 
                    S[k] = aux[j]
                    j += 1
                elif j > hi:
                    S[k] = aux[i]
                    i += 1
                elif aux[i] > aux[j]:
                    S[k] = aux[j]
                    j += 1
                else:
                    S[k] = aux[i]
                    i += 1

        def divide(lo, hi):
            if lo == hi:
                if lower <= S[lo] <= upper: return 1
                else: return 0
            m = (lo+hi) >> 1
            ans = divide(lo, m) + divide(m+1, hi)

            j, k = m+1, m+1
            for i in xrange(lo, m+1):
                while j <= hi and S[j] - S[i] < lower: j += 1
                while k <= hi and S[k] - S[i] < upper+1: k += 1
                ans += k - j

            merge(lo, m, hi)
            
            return ans
        
        return divide(1, len(S)-1)

test = Solution()
print test.countRangeSum([-2, 5, -1], -2, 2)
#print test.countRangeSum([1,1,1,1,1,1,1], 2, 4)

