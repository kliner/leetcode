class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if t < 0 or nums == None or len(nums) == 0:
            return False
        data = {}
        d = t + 1
        for i, n in enumerate(nums):
            if i > k:
                del data[nums[i-k-1] / d]
            if n / d in data:
                return True
            elif n / d - 1 in data and abs(data[n/d - 1] - n) <= t:
                return True
            elif n / d + 1 in data and abs(data[n/d + 1] - n) <= t:
                return True
            data[n/d] = n

        return False

if __name__ == '__main__':
    test = Solution()
    print test.containsNearbyAlmostDuplicate([], 1, 0)
    print test.containsNearbyAlmostDuplicate([1,2,3], 1, 0)
    print test.containsNearbyAlmostDuplicate([1,2,1], 1, 0)
    print test.containsNearbyAlmostDuplicate([1,2,1], 2, 0)
    print test.containsNearbyAlmostDuplicate([1,9,2], 2, 0)
    print test.containsNearbyAlmostDuplicate([1,9,2], 2, 1)
    print test.containsNearbyAlmostDuplicate([-1,-1], 1, -1)
