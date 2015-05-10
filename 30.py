import copy
class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):		
		if len(words) == 0:
			return []
		ans = []
		dct = {}
		for w in words:
			if w in dct:
				dct[w] += 1
			else:
				dct[w] = 1

		ttt = copy.copy(dct)

		n = len(words)
		l = len(words[0])
		# print len(s) - (n * l)
		for i in range(len(s) - (n * l) + 1):
			# print i
			r = i + l
			f = True
			for j in range(n):
				t = s[r - l:r]
				# print t
				if t in dct and dct[t] >= 1:
					dct[t] -= 1
				else:
					f = False
					break
				r += l
			if f:
				ans.append(i)
			dct = copy.copy(ttt)

		return ans

test = Solution()
print test.findSubstring("barfoothefoobarman", [])
print test.findSubstring("barfoothefoobarman", ["barfoothefoobarman"])
print test.findSubstring("barfoothefoobarman", ["foo", "bar"])
print test.findSubstring("barfoothefoobarman", ["foo", "bar", "foo", "bar", "the"])
print test.findSubstring("barfoothefoobar", ["foo", "bar"])
