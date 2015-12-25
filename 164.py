class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 2:
            return 0

        n = len(nums)
        a = [0 for i in xrange(n)]
        d10s = [10 ** i for i in range(10)]
        #print d10s

        for d in xrange(10):
            cnts = [0 for i in xrange(11)]
            for num in nums:
                cnts[ self.iAt(num, d10s[d]) + 1 ] += 1
            for i in xrange(1, 10):
                cnts[i+1] += cnts[i] 

            #print cnts
            for num in nums:
                #print cnts[self.iAt(num, d10s[d])] 
                a[ cnts[self.iAt(num, d10s[d])] ] = num
                cnts[self.iAt(num, d10s[d])] += 1
            for i, t in enumerate(a):
                nums[i] = t
                
        #print nums

        diff = [nums[i+1] - nums[i] for i in range(n-1)]
        return max(diff)
            


    def iAt(self, a, d):
        return a / d % 10


if __name__ == '__main__':
    a = [1, 3, 5, 9, 11, 15, 17, 22, 10021]
    test = Solution()
    print test.maximumGap(a)
