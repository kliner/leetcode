class Solution:
	# @param {integer} n
	# @param {integer} k
	# @return {string}
	def getPermutation(self, n, k):
		k -= 1
		a = [1 for i in range(n-1)]
		for i in range(1, n-1):
			a[i] = a[i-1] * (i+1)
		l = [i+1 for i in range(n)]
		ans = ''
		for i in range(n-2, -1, -1):
			t = k / a[i]
			ans += str(l[t])
			l.remove(l[t])
			k = k % a[i]
		ans += str(l[0])
		return ans

test = Solution()
print test.getPermutation(3, 1)
print test.getPermutation(3, 2)
print test.getPermutation(3, 3)
print test.getPermutation(3, 4)
print test.getPermutation(3, 5)
print test.getPermutation(3, 6)
print test.getPermutation(9, 1)
