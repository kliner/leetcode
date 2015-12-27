class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        a = [0 for i in xrange(n)]
        b = [0 for i in xrange(n)]
        a[0] = nums[0]
        a[1] = nums[1]
        a[2] = nums[0]+nums[2]
        b[0] = 0
        b[1] = nums[1]
        b[2] = nums[2]
        for i in xrange(3,n):
            a[i] = max(a[i-3],a[i-2]) + nums[i]
            b[i] = max(b[i-3],b[i-2]) + nums[i]
        a[n-1] -= nums[n-1]
        #print a
        #print b
        return max(a[n-2], a[n-1], b[n-2], b[n-1])


if __name__ == '__main__':
    test = Solution()
    print test.rob([1,2,3,4,5])

