class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.find(nums, 0, n)
    
    def find(self, nums, lo, hi):
        m = (lo + hi) >> 1
        #print lo, hi, m
        clo, chi = 0, 0
        for i in nums:
            if i < m:
                clo += 1
            elif i > m:
                chi += 1
        #print clo, chi
        if clo > m - 1:
            return self.find(nums, lo, m)
        elif chi > len(nums) - 1 - m:
            return self.find(nums, m, hi)
        else:
            return m






if __name__ == '__main__':
    test = Solution()
    print test.findDuplicate([1,3,4,3,3,5,6,7,8,9,10])
    print test.findDuplicate([1,2,2])
            
