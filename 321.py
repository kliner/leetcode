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
            n = len(nums)
            for i in xrange(n):
                while n-i+len(stk) > k and stk and stk[-1]<nums[i]:
                    stk.pop()
                if len(stk) < k:
                    stk.append(nums[i])
            return stk

        def greater(nums1, i, nums2, j):
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            return j == len(nums2) or (i < len(nums1) and j < len(nums2) and nums1[i]>nums2[j])

        def merge(nums1, nums2, k):
            ans = []
            i, j = 0, 0
            for _ in xrange(k):
                if greater(nums1, i, nums2, j):
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
            return ans

        l1, l2 = len(nums1), len(nums2)
        if not l1:
            return array(nums2, k)
        if not l2:
            return array(nums1, k)
        i = max(0, k-l2)
        ans = [0] * k
        while i <= k and i <= l1:
            #print i, k-i
            candi = merge( array(nums1, i), array(nums2, k-i), k)
            if greater(candi, 0, ans, 0):
                ans = candi
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
