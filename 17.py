class Solution:
	dic = {1:[], 2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z'], 0:[' ']}
	# @param digits, a string
	# @return a string[]
	def letterCombinations(self, digits):
		output = []
		if len(digits) == 0:
			return []
		self.solve('', digits, output)
		return output

	def solve(self, s, d, o):
		if len(d) == 1:
			for ch in self.dic[int(d)]:
				o.append(s + ch)
		else:
			for ch in self.dic[int(d[0])]:
				self.solve(s + ch, d[1:], o)	

test = Solution()
print test.letterCombinations("")
print test.letterCombinations("1")
print test.letterCombinations("3")
print test.letterCombinations("0")
print test.letterCombinations("23")
print test.letterCombinations("209")