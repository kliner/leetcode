class Solution:	
	# @param s, a string
	# @return a string
	def longestPalindrome(self, s):
		l = len(s)
		a = [1]
		m = 1
		for i in range(1, l):
			if a[i-1] == 1 and s[i] == s[i-1]:
				a.append(2)
			elif i-a[i-1] > 0 and s[i] == s[i - a[i-1] - 1]:
				a.append(a[i-1]+2)
			else:
				for j in range(i-a[i-1], i):
					# print s[j:i+1]					
					if self.isPalid(s[j:i+1]):
						a.append(i-j+1)
						break					
				else:
					a.append(1)
			if a[i] > m:
				m = a[i]
			# print a, m

		for i in range(l):
			if a[i] == m:
				return s[i-m+1:i+1]

	def isPalid(self, s):
		l = len(s)
		for i in range(l/2):
			if s[i] != s[l - i - 1]:
				return False

		return True


test = Solution()
print test.longestPalindrome("a")
