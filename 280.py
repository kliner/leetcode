import random
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def exch(a, i, j):
            t = a[i]
            a[i] = a[j]
            a[j] = t

        def partition3way(a, lo, hi):
            m = random.randrange(lo, hi)
            v = a[m]
            lt, gt, i = lo, hi, lo
            while i <= gt:
                c = cmp(a[i], v)
                if c < 0:
                    exch(a, lt, i)
                    lt += 1
                    i += 1
                elif c > 0:
                    exch(a, gt, i)
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def midDiv(a):
            lo, hi = 0, len(a)-1
            m = len(a) >> 1
            while lo < hi:
                lt, gt = partition3way(a, lo, hi)
                if m < lt:
                    hi = lt-1
                elif gt < m:
                    lo = gt+1
                else:
                    return

        midDiv(nums)
        #print nums
        n = len(nums)
        m = (n + 1) >> 1
        t = [0] * n
        for i in xrange(m):
            t[i*2] = nums[i]
        for i in xrange(n-m):
            t[i*2+1] = nums[m+i]
        for i in xrange(n):
            nums[i] = t[i]
        
test = Solution()
'''
a = [5,6,3,4,2,1]
test.wiggleSort(a)
print a
a = []
test.wiggleSort(a)
print a
a = [1]
test.wiggleSort(a)
print a
a = [1,1,1,1,1]
test.wiggleSort(a)
print a
a = [1,2,3,4]
test.wiggleSort(a)
print a
a = [2,3,1,4]
test.wiggleSort(a)
print a
a = [2,3,1]
test.wiggleSort(a)
print a
'''
a = [3,1,2]
test.wiggleSort(a)
print a
