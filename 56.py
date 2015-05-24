# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
	# @param {Interval[]} intervals
	# @return {Interval[]}
	def merge(self, intervals):
		l = []
		ans = []
		for i in intervals:
			l.append((i.start, 0))
			l.append((i.end, 1))
		l.sort()
		# print l
		s = []
		for a, b in l:
			if b == 0:
				s.append(a)
			else:
				t = s.pop()
				if len(s) == 0:
					i = Interval(t, a)
					print t,a
					ans.append(i)
		return ans

test = Solution()
a = Interval(1,3)
b = Interval(2,6)
c = Interval(3,4)
test.merge([a,b,c])