class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.data = []
        t = 0
        for n in nums:
            t += n
            self.data.append(t)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.data[j]
        return self.data[j]-self.data[i-1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    nums = [-2,0,3,-5,2,-1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 0)
    print numArray.sumRange(0, 1)
    print numArray.sumRange(0, 2)
    print numArray.sumRange(1, 2)
    print numArray.sumRange(0, 5)
