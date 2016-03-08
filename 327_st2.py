import bisect
class Solution(object):
    def countRangeSum(self, nums, lo, hi):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def getSum(a, idx):
            ans = 0
            if idx <= 0: return 0
            if idx >= len(a): idx = len(a)-1
            while idx:
                ans += a[idx]
                idx -= (idx & -idx)
            return ans
        
        def add(a, idx, v):
            while idx < len(a):
                a[idx] += v
                idx += (idx & -idx)

        prefix = [0]
        for num in nums:
            prefix += [prefix[-1] + num]

        def findInsertIndex(dct, target):
            return bisect.bisect(dct, target) - 1
        
        n = len(prefix)
        dct = list(set(prefix))
        dct += [-1e100]
        dct.sort()
        
        bit = [0] * (n+1)
        ans = 0
        for i in xrange(len(nums), 0, -1):
            add(bit, findInsertIndex(dct, prefix[i]), 1)
            #print bit
            ans -= getSum(bit, findInsertIndex(dct, prefix[i-1] + lo - 1))
            #print ans
            ans += getSum(bit, findInsertIndex(dct, prefix[i-1] + hi))
            #print ans
        return ans
            
test = Solution()
print test.countRangeSum([-2, 5, -1], -2, 2)
