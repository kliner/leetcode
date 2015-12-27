import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        N = 0
        if n == 0:
            return 0
        for i in xrange(n):
            if N == 0 or nums[i] > nums[N-1]:
                #print nums
                nums[N] = nums[i]
                N += 1
            else:
                idx = bisect.bisect_left(nums, nums[i], hi=N)
                nums[idx] = nums[i]
                #print idx,nums

        #print nums
        return N
                    
if __name__ == '__main__':
    test = Solution()
    print test.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print test.lengthOfLIS([1,1,1,1])
    print test.lengthOfLIS([-21,-1])
