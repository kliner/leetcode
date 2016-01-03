class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enums):
            #print enums
            n = len(enums)
            if n <= 1:
                return enums
            m = n >> 1
            left, right = sort(enums[:m]), sort(enums[m:])
            #print left, right
            for i in xrange(n-1,-1,-1):
                if left and right and left[-1][1] > right[-1][1]:
                    ans[left[-1][0]] += len(right)
                    enums[i] = left[-1]
                    left.pop()
                elif left and right:
                    enums[i] = right[-1]
                    right.pop()
                elif left:
                    enums[i] = left[-1]
                    left.pop()
                elif right:
                    enums[i] = right[-1]
                    right.pop()
            #print ans
            return enums
        ans = [0] * len(nums)
        sort(list(enumerate(nums)))
        return ans

if __name__ == '__main__':
    test = Solution()
    print test.countSmaller([5,2,6,1])
