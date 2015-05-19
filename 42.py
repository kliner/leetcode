class Solution:
	# @param {integer[]} height
	# @return {integer}
	def trap(self, height):
		n = len(height)
		if n <= 2:
			return 0
		i = 0
		ans = 0
		m = max(height)
		while height[i] < m:
			j = i+1
			while height[i] > height[j]:
				j += 1
			# print i,j
			for k in xrange(i+1,j):
				ans += height[i] - height[k]
			i = j
		l = i 
		i = n-1
		while height[i] < m:
			j = i-1
			while height[i] > height[j]:
				j -= 1
			for k in xrange(j+1,i):
				ans += height[i] - height[k]
			i = j
		r = i
		for i in xrange(l+1, r):
			ans += m - height[i]
		return ans

test = Solution()
print test.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print test.trap([0,1,2,3])
print test.trap([3,2,1,0])
print test.trap([4,2,3])
print test.trap([4,2,3,5,3,4])