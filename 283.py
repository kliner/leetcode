class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)
        while i < n:
            if nums[i] == 0:
                i+=1
            else:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
                j+=1
        

if __name__ == '__main__':
    test = Solution()
    a = [0, 1, 0, 3, 2]
    test.moveZeroes(a)
    print a
    a = []
    test.moveZeroes(a)
    print a
    a = [1]
    test.moveZeroes(a)
    print a
