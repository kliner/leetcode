class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        #print fast
        new = 0
        while new != slow:
            slow = nums[slow]
            new = nums[new]
        return new


if __name__ == '__main__':
    test = Solution()
    print test.findDuplicate([1,3,4,3,3,5,6,7,8,9,10])
    print test.findDuplicate([1,3,4,2,2])
    print test.findDuplicate([1,2,2])

