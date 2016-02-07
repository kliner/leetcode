import math
import copy
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []

        def visit(n, lo, hi, cur):
            #print lo, hi
            for i in xrange(lo, hi+1):
                if n % i == 0:
                    nxt = n / i
                    if nxt >= i:
                        #print n, i, nxt, cur
                        cur.append(i)
                        cur.append(nxt)
                        ans.append(copy.copy(cur))
                        cur.pop()
                        visit(nxt, i, int(math.ceil(math.sqrt(nxt))), cur)
                        cur.pop()

        visit(n, 2, int(math.ceil(math.sqrt(n))), [])
        return ans

test = Solution()
print test.getFactors(1)
print test.getFactors(37)
print test.getFactors(12)
print test.getFactors(32)
