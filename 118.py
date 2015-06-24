class Solution:
	# @param {integer} numRows
	# @return {integer[][]}
	def generate(self, numRows):
		if numRows == 0:
			return []
		a = [[1]]
		if numRows == 1:
			return a
		a.append([1,1])
		if numRows == 2:
			return a
		for i in range(2, numRows):
			last = a[-1]
			temp = [1]
			t = last[0]
			for i in last[1:]:
				temp.append(t + i)
				t = i
			temp.append(1)
			a.append(temp)
		return a

test = Solution()
print test.generate(0)
print test.generate(1)
print test.generate(2)
print test.generate(5)