class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = 1e10
        q = []
        total = 0
        i = 0
        while i < len(nums):
            while total < s:
                if i == len(nums):
                    if ans == 1e10:
                        ans = 0
                    return ans
                q.append(nums[i])
                total += nums[i]
                i += 1
            while q and total - q[0] >= s:
                total -= q[0]
                q = q[1:]
            
            ans = min(ans, len(q))
            #print q
            
            while q and total >= s:
                total -= q[0]
                q = q[1:]

        if ans == 1e10:
            ans = 0
        return ans


if __name__ == '__main__':
    test = Solution()
    print test.minSubArrayLen(7, [2,3,1,2,4,3])
    print test.minSubArrayLen(80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8])

