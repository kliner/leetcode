class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if not n: return 0
        a = [0] * (n+1)
        for i in xrange(n):
            a[i+1] += a[i] + nums[i]
        dct = {}
        for i in xrange(n+1): dct[a[i]] = i

        ans = 0
        for i in xrange(n+1):
            if k+a[i] in dct:
                ans = max(ans, dct[k+a[i]]-i)

        return ans

test = Solution()
print test.maxSubArrayLen([1, -1, 5, -2, 3], 3)
print test.maxSubArrayLen([-2, -1, 2, 1], 1)
print test.maxSubArrayLen([-2, -1, 2, 1], -2)
print test.maxSubArrayLen([-2, -1, 2, 1], -10)
