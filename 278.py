# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 0

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.visit(0, n)
        
    def visit(self, lo, hi):
        if lo == hi:
            return lo
        m = (lo+hi)>>1
        if isBadVersion(m):
            return self.visit(lo, m)
        else:
            return self.visit(m+1, hi)


if __name__ == '__main__':
    test = Solution()
    print test.firstBadVersion(100)
