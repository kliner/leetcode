class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        start = lower
        nums.append(upper+1)
        ans = []
        for num in nums:
            if num == start:
                pass
            elif num == start+1:
                ans += [str(start)]
            else:
                ans += [str(start)+'->'+str(num-1)]
            start = num + 1
        return ans

test = Solution()
print test.findMissingRanges([0, 1], 0, 1)
print test.findMissingRanges([0], 0, 1)
print test.findMissingRanges([1], 0, 1)
print test.findMissingRanges([0, 1, 3, 50, 75], 0, 99)

