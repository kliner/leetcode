class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0]+nums[2], nums[1])

        a = [0 for i in xrange(n)]
        a[0] = nums[0]
        a[1] = nums[1]
        a[2] = nums[0]+nums[2]
        for i in xrange(3,n):
            a[i] = max(a[i-3],a[i-2])+nums[i]
        #print a
        return max(a[n-1],a[n-2])


if __name__ == '__main__':
    test = Solution()
    print test.rob([1,2,3,4,5])


