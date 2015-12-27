class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNums = [1]
        for num in nums:
            if num:
                myNums.append(num)
        myNums.append(1)
        n = len(myNums)
        F = [[0] * n for i in xrange(n)]
        return self.dp(myNums, F, 0, n-1)

    def dp(self, nums, F, lo, hi):
        if F[lo][hi]:
            return F[lo][hi]
        for i in xrange(lo+1, hi):
            F[lo][hi] = max(F[lo][hi], self.dp(nums,F,lo,i)+self.dp(nums,F,i,hi)+nums[lo]*nums[i]*nums[hi])
        return F[lo][hi]

if __name__ == '__main__':
    test = Solution()
    print test.maxCoins([3,1,5,8])
