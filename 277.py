# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return -1
        candidate = 0
        for i in xrange(1, n):
            if knows(candidate, i):
                candidate = i
        for i in xrange(n):
            if i == candidate or knows(i, candidate) and not knows(candidate, i):
                continue
            else:
                return -1
        return candidate
