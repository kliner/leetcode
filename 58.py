class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		ss = s.split()
		if len(ss) == 0:
			return 0
		else:
			return len(ss[-1])

test = Solution()
print test.lengthOfLastWord("")
print test.lengthOfLastWord(" ")
print test.lengthOfLastWord("a ")
print test.lengthOfLastWord(" a")
print test.lengthOfLastWord(" a  ")
print test.lengthOfLastWord(" a  abc ")