class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n < 3: 
            return 0
        ans = 0
        for i in xrange(n-2):
            lo, hi = i+1, n-1
            while lo < hi:
                if sum([nums[i], nums[lo], nums[hi]]) < target:
                    ans += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return ans

test = Solution()
print test.threeSumSmaller([3,1], 2) == 0
print test.threeSumSmaller([1,1,-2], 1) == 1
print test.threeSumSmaller([3,1,0,-2], 2) == 2
