class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = [nums[n-k+i] for i in xrange(k)]
        for i in xrange(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        for i in xrange(k):
            nums[i] = temp[i]
        
if __name__ == '__main__':
    test = Solution()
    a = [1,2,3,4,5,6,7]
    test.rotate(a,3)
    print a

