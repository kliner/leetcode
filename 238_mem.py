class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return []
        a = [1]
        for i in xrange(n-1):
            a.append(a[-1]*nums[i])
        b = 1
        for i in xrange(n-1, -1, -1):
            a[i] *= b
            b *= nums[i]
        return a


if __name__ == '__main__':
    test = Solution()
    print test.productExceptSelf([1,2,3,4])

