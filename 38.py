class Solution:
	# @param {integer} n
	# @return {string}
	def countAndSay(self, n):
		if n <= 0:
			return ''
		if n == 1:
			return '1'
		res = '1'
		for i in xrange(n-1):
			t = ''
			ch = res[0]
			cnt = 1
			for j in xrange(1, len(res)):
				if res[j] == ch:
					cnt += 1
				else:
					t += bytes(cnt)
					t += ch
					ch = res[j]
					cnt = 1
			else:
				t += bytes(cnt) 
				t += ch
			res = t
		return res

test = Solution()
for i in xrange(10):
	print test.countAndSay(i)
