class Solution:
	# @param {integer} rowIndex
	# @return {integer[]}
	def getRow(self, rowIndex):
		rowIndex += 1
		if rowIndex == 1:
			return [1]
		if rowIndex == 2:
			return [1,1]
		last = [1,1]
		t = last[0]
		for i in range(2, rowIndex):
			temp = [1]
			for j in last[1:]:
				temp.append(t + j)
				t = j
			temp.append(1)
			last = temp
		return last

test = Solution()
print test.getRow(0)
print test.getRow(2)
print test.getRow(3)
print test.getRow(4)
print test.getRow(5)