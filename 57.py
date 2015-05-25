class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param {Interval[]} intervals
	# @param {Interval} newInterval
	# @return {Interval[]}
	def insert(self, intervals, newInterval):
		start = newInterval.start
		end = newInterval.end
		t = ''
		ans = []
		if len(intervals) == 0:
			return [newInterval]

		for i in intervals:
			if t == '' and start > i.end:
				ans.append(i)
			elif t == '' and end < i.start:
				t = 'x'
				ans.append(newInterval)
				ans.append(i)
			elif t == '' and start < i.start and end <= i.end:
				t = 'x'
				newInterval.end = i.end
				ans.append(newInterval)
			elif t == '' and start >= i.start and end <= i.end:
				t = 'x'
				ans.append(i)
			elif t == '' and start > i.start:
				t = 'i'
				newInterval.start = i.start
			elif t == '' and start <= i.start:
				t = 'i'
			elif t == 'i' and end > i.end:
				pass
			elif t == 'i' and end >= i.start and end <= i.end:
				newInterval.end = i.end
				ans.append(newInterval)
				t = 'x'
			elif t == 'i':
				ans.append(newInterval)
				ans.append(i)
				t = 'x'
			elif t == 'x':
				ans.append(i)
		if newInterval.end > intervals[-1].end:
			ans.append(newInterval)
		return ans

test = Solution()
i1 = Interval(2,4)
i2 = Interval(5,7)
i3 = Interval(8,10)
i4 = Interval(3,8)
for i in test.insert([i1, i2, i3], i4):
	print i.start, i.end
print '---'
i1 = Interval(1,5)
i2 = Interval(1,5)
for i in test.insert([i1], i2):
	print i.start, i.end
print '---'
i1 = Interval(2,3)
i2 = Interval(4,5)
i3 = Interval(6,7)
i4 = Interval(4,6)
for i in test.insert([i1, i2, i3], i4):
	print i.start, i.end