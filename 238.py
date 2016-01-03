class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return []
        a, b = [1], [1]
        for i in xrange(n-1):
            a.append(a[-1]*nums[i])
            b.append(b[-1]*nums[n-1-i])
        ans = [a[i]*b[n-1-i] for i in xrange(n)]
        return ans


if __name__ == '__main__':
    test = Solution()
    print test.productExceptSelf([1,2,3,4])
