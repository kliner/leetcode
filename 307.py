class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.T = [0 for i in xrange(len(nums)+1)]
        for i, v in enumerate(nums):
            self.updateAdd(i, v)

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            #print i
            s += self.T[i]
            i -= i & (-i)
        #print s
        return s

    def updateAdd(self, i, diff):
        i += 1
        while i <= self.n:
            self.T[i] += diff
            i += i & (-i)
        #print self.T
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.updateAdd(i, val - self.nums[i])
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i-1)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
if __name__ == '__main__':
    numArray = NumArray([1,3,5])
    print numArray.sumRange(0, 1)
    numArray.update(1, 10)
    print numArray.sumRange(1, 2)
