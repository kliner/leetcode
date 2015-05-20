class Solution:
	# @param {string} num1
	# @param {string} num2
	# @return {string}
	def multiply(self, num1, num2):
		l1 = len(num1)
		l2 = len(num2)
		n1 = []
		n2 = []
		nans = [0 for i in range(l1+l2)]
		for i in xrange(l1-1, -1, -1):
			n1.append(int(num1[i]))
		for i in xrange(l2-1, -1, -1):
			n2.append(int(num2[i]))
		for i in xrange(l1):
			for j in xrange(l2):
				nans[i+j] += n1[i] * n2[j]
				if nans[i+j] >= 10:
					nans[i+j+1] += nans[i+j] / 10
					nans[i+j] = nans[i+j] % 10
		ans = ''
		f = True
		for i in nans[::-1]:
			if i == 0 and f:
				continue
			f = False
			ans += str(i)
		if f:
			return '0'
		else:
			return ans

test = Solution()
print test.multiply('0', '0')
print test.multiply('0', '1002')
print test.multiply('110', '1002')