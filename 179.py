

class Solution(object):
    def cp(self, a, b):
        #print a,b
        return -a*(10**len(str(b)))-b + b*(10**len(str(a)))+a

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        nums.sort(self.cp)
        nums = [str(a) for a in nums]
        s = "".join(nums)
        while len(s) > 1 and s[0]=='0':
            s = s[1:]
        return s

        
        
if __name__ == '__main__':
    test = Solution()
    print test.largestNumber([3,30,34,5,9])
    print test.largestNumber([0,0,0])
