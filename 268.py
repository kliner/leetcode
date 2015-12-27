class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        x = 0
        for i in xrange(n):
            x ^= i
        for i in nums:
            x ^= i
        return x
      
        
if __name__ == '__main__':
    test = Solution()
    print test.missingNumber([0,1,3])

