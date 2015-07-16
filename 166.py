class Solution:
	# @param {integer} numerator
	# @param {integer} denominator
	# @return {string}
	def fractionToDecimal(self, numerator, denominator):
		l = len(str(denominator))
		n = 10 ** l
		p = numerator / denominator
		q = numerator % denominator
		ans = str(p) + "."
		dct = {}
		while q not in dct:
			dct[q] = 0
			q += n
			s = str(q / denominator)
			a = ['0' for i in xrange(l - len(s))]
			ans += ''.join(a)
			ans += s
			q %= denominator
		print ans, q, str(q)
		if q == 0:
			if ans[-2] == '.':
				ans = ans[:-2]
			else:
				ans = ans[:-1]
		else:
			i = ans.rfind(str(q))
			ans = ans[:i] + '(' + ans[i:] + ')'
		return ans

test = Solution()
print test.fractionToDecimal(1, 90)