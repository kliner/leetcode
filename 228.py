class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start = nums[0]
        last = nums[0]
        ret = []
        for n in nums[1:]:
            if n == last + 1:
                last += 1
            else:
                if start != last:
                    ret.append("%d->%d" % (start, last))
                else:
                    ret.append(str(start))
                start = n
                last = n

        if start != last:
            ret.append("%d->%d" % (start, last))
        else:
            ret.append(str(start))

        return ret



        
if __name__ == '__main__':
    test = Solution()
    print test.summaryRanges([0,1,2,4,5,7,9,11])
