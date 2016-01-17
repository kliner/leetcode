class Solution(object):
    
    def getSum(self, T, idx):
        ans = 0
        while idx:
            ans += T[idx]
            idx -= idx & (-idx)
        return ans
    
    def update(self, T, idx, val):
        while idx <= len(T)-1:
            T[idx] += val
            idx += idx & (-idx)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        padding = min(nums)
        if padding <= 0:
            nums = [a + 1 - padding for a in nums]
        m = max(nums)
        T = [0] * (m+1)
        ans = []
        t = 0
        for num in nums[::-1]:
            ans.append(self.getSum(T, num-1))
            self.update(T, num, 1)
        return ans[::-1]
        

if __name__ == '__main__':
    test = Solution()
    print test.countSmaller([5,2,6,1])
    print test.countSmaller([-5,-2,-6,-1])

