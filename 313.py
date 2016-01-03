from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        q = [(p, 0, p) for p in primes]
        uglyNums = [1]
        s = set([1] + [p for p in primes])
        for i in xrange(1,n):
            x, idx, p = heappop(q)
            uglyNums.append(x)
            while uglyNums[idx] * p in s:
                idx+=1
            heappush(q, (uglyNums[idx] * p, idx, p))
            s.add(uglyNums[idx]*p)
        return uglyNums[-1]


if __name__ == '__main__':
    test = Solution()
    for i in xrange(13):
        print test.nthSuperUglyNumber(i, [2,7,13,19])




        
