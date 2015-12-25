class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set([])
        for i, n in enumerate(nums):
            if i < k:
                if n not in s:
                    s.add(n)
                else:
                    return True
            else:
                if n not in s:
                    s.add(n)
                    s.remove(nums[i-k])
                else:
                    return True
        return False
        
if __name__ == '__main__':
    test = Solution()
    print test.containsNearbyDuplicate([], 1)
    print test.containsNearbyDuplicate([1,2,3], 1)
    print test.containsNearbyDuplicate([1,2,1], 2)
    print test.containsNearbyDuplicate([1,2,1], 1)
