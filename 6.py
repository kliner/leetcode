class Solution:
	# @return a string
	def convert(self, s, nRows):
		a = []
		for i in range(nRows):
			a.append([])
		i = 0
		j = 0
		direct = 1
		while i < len(s):
			a[j].append(s[i])
			j = j + direct
			if j >= nRows:
				j = j - 2
				direct = -1
			elif j < 0:
				j = j + 2
				direct = 1
			i = i + 1

		s = ""
		for i in range(nRows):
			for ch in a[i]:
				s = s + ch
		return s

test = Solution()
print test.convert("PAYPALISHIRING", 3)
