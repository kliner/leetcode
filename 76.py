class Solution:
	# @param {string} s
	# @param {string} t
	# @return {string}
	def minWindow(self, s, t):
		ls = len(s)
		lt = len(t)
		if ls == 0 or lt == 0:
			return ""
		start = 0
		cur = 0
		dct = {}
		ans = ""
		words = {}
		for i in range(lt):
			if t[i] in words:
				words[t[i]] += 1
			else:
				words[t[i]] = 1
		while cur < ls:
			if s[cur] in words:
				words[s[cur]] -= 1
				# print words
				if max(words.values()) <= 0:
					while (s[start] in words and words[s[start]] < 0) or (s[start] not in words):
						if s[start] in words:
							words[s[start]] += 1
						start += 1
					# print s[start:cur+1], words
					if ans == "" or len(ans) > cur - start:
						ans = s[start:cur+1]
			cur += 1
		return ans

test = Solution()
print test.minWindow("AA", "AA")
print test.minWindow("A", "A")
print test.minWindow("a", "a")
print test.minWindow("ADOBECODEBANC", "ABC")