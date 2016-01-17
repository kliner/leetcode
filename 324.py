import random
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 

        
        def exch(a, i, j):
            t = a[i] 
            a[i] = a[j]
            a[j] = t
        
        def partition3way(a, lo, hi):
            #print a[lo:hi+1]
            lt, gt = lo, hi
            i = lo
            m = random.randrange(lo, hi)
            v = a[m]
            #print v
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
            #print a[lo:hi+1]
            return lt, gt
        
        def kthSmallestWithDuplicates(arr, k):
            lo, hi = 0, len(arr)-1
            while lo < hi:
                lt, gt = partition3way(arr, lo, hi)
                #print lt, gt, k
                if k < lt:
                    hi = lt-1
                elif gt < k:
                    lo = gt+1
                else:
                    return lo, hi
            return lo, hi

        n, m = len(nums), len(nums)>>1
        l, r = kthSmallestWithDuplicates(nums, m)
        #print nums

        m = (n+1)>>1
        i, j = 0, m-1
        while i < j:
            exch(nums, i, j)
            i += 1
            j -= 1
        i, j = m, n - 1
        while i < j:
            exch(nums, i, j)
            i += 1
            j -= 1
        #print nums

        t = [0] * n
        for i in xrange(m):
            t[i*2] = nums[i]
        for i in xrange(n-m):
            t[i*2+1] = nums[m+i]
        for i in xrange(n):
            nums[i] = t[i]

test = Solution()
a = []
test.wiggleSort(a)
print a
a = [1,2,3,2,1,2,3]
test.wiggleSort(a)
print a
a = [1,2,3,2]
test.wiggleSort(a)
print a
a = [1,5,1,1,6,4]
test.wiggleSort(a)
print a
a = [1,3,2,2,3,1]
test.wiggleSort(a)
print a
a = [4,1,3,1]
test.wiggleSort(a)
print a
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
test.wiggleSort(a)
print a
