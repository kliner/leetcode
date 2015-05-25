class Solution:
	# @param {integer} n
	# @return {integer[][]}
	def generateMatrix(self, n):
		m = []
		for x in range(n):
			l = [0 for i in range(n)]
			m.append(l)
		x, y = 0, 0
		d = 'r'
		if n == 1:
			return [[1]]
		for i in range(1, n**2+1):
			m[x][y] = i
			if d == 'r':
				if y+1 < n and m[x][y+1] == 0:
					y += 1
				elif m[x+1][y] == 0:
					x += 1
					d = 'd'
			elif d == 'd':
				if x+1 < n and m[x+1][y] == 0:
					x += 1
				elif m[x][y-1] == 0:
					y -= 1
					d = 'l'
			elif d == 'l':
				if y-1 >= 0 and m[x][y-1] == 0:
					y -= 1
				elif m[x-1][y] == 0:
					x -= 1
					d = 'u'
			elif d == 'u':
				if x-1 >= 0 and m[x-1][y] == 0:
					x -= 1
				elif m[x][y+1] == 0:
					y += 1
					d = 'r'
		return m

test = Solution()
print test.generateMatrix(1)
print test.generateMatrix(2)
print test.generateMatrix(3)
print test.generateMatrix(4)
print test.generateMatrix(5)
a = test.generateMatrix(7)
for i in a:
	print i
