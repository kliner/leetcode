class Solution:
	# @param {string} haystack
	# @param {string} needle
	# @return {integer}
	def strStr(self, haystack, needle):
		l1 = len(haystack)
		l2 = len(needle)
		if l2 == 0 and l1 == 0:
			return 0
		if l2 > l1:
			return -1
		for i in range(l1-l2+1):
			f = True
			for j in range(l2):
				if haystack[i+j] != needle[j]:
					f = False
					break			
			if f:
				return i	
		return -1
		
test = Solution()
print test.strStr("", "")
print test.strStr("a", "a")
print test.strStr("aa", "aa")
print test.strStr("baa", "aa")
print test.strStr("aab", "aa")
print test.strStr("abc", "")
print test.strStr("", "abc")
print test.strStr("asdfbqwer", "bqw123456789")
print test.strStr("asdfbqwer", "bqw")
print test.strStr("asdfbqwer", "bqwa")