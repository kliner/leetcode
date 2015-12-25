class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == None or len(nums) <= 1:
            return []
        
        xor = 0
        for n in nums:
            xor ^= n

        mask = 1
        while xor & 1 != 1:
            xor >>= 1
            mask <<= 1

        a, b = [], []
        for n in nums:
            if n & mask == mask:
                a.append(n)
            else:
                b.append(n)
        #print a, b

        ra, rb = 0, 0
        for n in a:
            ra ^= n 
        for n in b:
            rb ^= n 
        return [ra, rb]

                
if __name__ == '__main__':
    test = Solution()
    print test.singleNumber([1,2,3,1,2,5])



