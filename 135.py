class Solution:
	# @param {integer[]} ratings
	# @return {integer}
	def candy(self, ratings):
		n = len(ratings)
		a = [1 for i in xrange(n)]
		cur = 1
		for i in xrange(1, n):
			if ratings[i] > ratings[i-1]:
				cur += 1
				a[i] = cur
			else:
				cur = 1
		cur = 1
		for i in xrange(n-2, -1, -1):
			if ratings[i] > ratings[i+1]:
				cur += 1
				a[i] = max(a[i], cur)
			else:
				cur = 1
		return sum(a)

test = Solution()
print test.candy([1,2,3])
print test.candy([2,3,4])
print test.candy([1,2,3,1,2])
print test.candy([1,2,5,3,2])
print test.candy([2,3])
print test.candy([2,1])