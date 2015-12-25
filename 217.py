class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set([])
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return True
        return False
        
if __name__ == '__main__':
    test = Solution()
    print test.containsDuplicate([])
    print test.containsDuplicate([1,2,3])
    print test.containsDuplicate([1,1,3])
