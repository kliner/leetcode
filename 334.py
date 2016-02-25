class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1 = 1e100
        n2 = 1e100
        for n in nums:
            if n > n2: return True
            elif n > n1: n2 = n
            else: n1 = n
        return False

test = Solution()
print test.increasingTriplet([])
print test.increasingTriplet([1])
print test.increasingTriplet([1,2])
print test.increasingTriplet([1,2,3])
print test.increasingTriplet([1,2,3,4,5])
print test.increasingTriplet([5,4,3,2,1])
