class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        reach = 0
        ans = 0
        for num in nums:
            while num > reach + 1:
                ans += 1
                reach += reach + 1
                if reach >= n:
                    return ans
            reach += num
            if reach >= n:
                return ans
        while reach < n:
            ans += 1
            reach += reach + 1
        return ans
        
test = Solution()
print test.minPatches([1, 3], 6) == 1
print test.minPatches([1, 5, 10], 20) == 2  
print test.minPatches([1, 2, 2], 5) == 0
print test.minPatches([1,2,31,33], 2147483647) == 28
