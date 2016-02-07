class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        lo, hi = 0, n-1
        while lo < hi:
            if numbers[lo]+numbers[hi]>target:
                hi -= 1
            elif numbers[lo]+numbers[hi]<target:
                lo += 1
            else:
                return [lo+1, hi+1]
