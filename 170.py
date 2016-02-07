class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.nums: self.nums[number] += 1
        else: self.nums[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.nums:
            if i+i == value:
                if self.nums[i] > 1: return True
            elif value-i in self.nums: return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
twoSum = TwoSum()
print twoSum.find(1)
twoSum.add(1)
twoSum.add(2)
twoSum.add(3)
print twoSum.find(3)
print twoSum.find(4)
print twoSum.find(5)
print twoSum.find(6)
twoSum = TwoSum()
twoSum.add(-1)
twoSum.add(0)
twoSum.add(1)
print twoSum.find(0)
