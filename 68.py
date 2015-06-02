class Solution:
	# @param {string[]} words
	# @param {integer} maxWidth
	# @return {string[]}
	def fullJustify(self, words, maxWidth):
		ans = []
		line = []
		curWid = 0
		for w in words:
			if curWid == 0:
				line.append(w)
				curWid = len(w)
				continue
			if curWid + 1 + len(w) <= maxWidth:
				line.append(w)
				curWid += len(w) + 1
			else:
				ans.append(self.just(line, maxWidth))
				line = [w]
				curWid = len(w)
		ans.append(self.justLast(line, maxWidth))
		return ans

	def justLast(self, line, w):
		ret = line[0]
		for l in line[1:]:
			ret += ' ' + l
		for i in range(w - len(ret)):
			ret += ' '
		return ret


	def just(self, line, w):
		ret = ''
		c = len(line) - 1
		if c == 0:
			ret += line[0]
			for i in range(w - len(line[0])):
				ret += ' '
			return ret
		space = w 
		for l in line:
			space -= len(l)
		p = space % c
		n = space / c
		ret += line[0]
		for l in line[1:]:	
			if p > 0:
				for i in range(n+1):
					ret += ' '
				p -= 1
				ret += l
			else:
				for i in range(n):
					ret += ' '
				ret += l
		return ret

test = Solution()
for t in test.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16):
	print t, len(t)
for t in test.fullJustify(["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."], 25):
	print t, len(t)