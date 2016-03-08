from collections import deque
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def array(nums, k):
            stk = []
            for i, num in enumerate(nums):
                while stk and len(nums) - i + len(stk) > k and stk[-1] < num: stk.pop()
                if len(stk) < k: stk += [num]
            return stk

        def merge(nums1, nums2):
            a, b, l = deque(nums1), deque(nums2), len(nums1) + len(nums2)
            return [max(a, b).popleft() for _ in xrange(l)]

        l1, l2 = len(nums1), len(nums2)
        if l1 == 0: return array(nums2, k)
        if l2 == 0: return array(nums1, k)
        i = max(0, k-l2)
        ans = []
        while i <= k and i <= l1:
            candi = merge(array(nums1, i), array(nums2, k-i))
            if candi > ans: ans = candi
            i += 1
        return ans


test = Solution()
print test.maxNumber([9], [], 1)
print test.maxNumber([9, 1, 2, 5, 8, 3], [], 5)
print test.maxNumber([9, 1, 2, 5, 8, 3], [], 1)
print test.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print test.maxNumber([6, 7], [6, 0, 4], 5)
print test.maxNumber([3, 9], [8, 9], 3)
print test.maxNumber([4, 3], [4, 3, 5], 5)
print test.maxNumber([4, 3, 5], [4, 3], 5)

