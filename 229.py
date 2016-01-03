class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, n2 = 0, 0
        c1, c2 = None, None
        for num in nums:
            if n1 == 0:
                n1 += 1
                c1 = num
            elif c1 == num:
                n1 += 1
            elif n2 == 0:
                n2 += 1
                c2 = num
            elif c2 == num:
                n2 += 1
            else:
                n1 -= 1
                n2 -= 1
        n1, n2 = 0, 0
        if c1 == c2:
            c2 = None
        for num in nums:
            if num == c1:
                n1 += 1
            if num == c2:
                n2 += 1
        ans = []
        n = len(nums)
        if n1 > n / 3:
            ans.append(c1)
        if n2 > n / 3:
            ans.append(c2)
        return ans

if __name__ == '__main__':
    test = Solution()
    print test.majorityElement([])
    print test.majorityElement([1])
    print test.majorityElement([1,2])
    print test.majorityElement([1,2,3])
    print test.majorityElement([1,1,2,3,3])
    print test.majorityElement([2,1,3,1])
    print test.majorityElement([-1,1,1,1,2,1])
