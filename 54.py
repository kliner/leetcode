class Solution:
	# @param {integer[][]} matrix
	# @return {integer[]}
	def spiralOrder(self, m):
		d = 'r'
		xn = len(m)
		if xn == 0:
			return []
		yn = len(m[0])
		if yn == 0:
			return []
		ans = []
		x = 0
		y = 0
		while True:
			ans.append(m[x][y])
			m[x][y] = 'x'
			if d == 'r':
				if y+1 < yn and m[x][y+1] != 'x':		
					y += 1
				elif x+1 < xn and m[x+1][y] != 'x':
					x += 1
					d = 'd'
				else:
					return ans
			elif d == 'd':
				if x+1 < xn and m[x+1][y] != 'x':
					x += 1
				elif y-1 >= 0 and m[x][y-1] != 'x':
					y -= 1
					d = 'l'
				else:
					return ans
			elif d == 'l':
				if y-1 >= 0 and m[x][y-1] != 'x':
					y -= 1
				elif x-1 >= 0 and m[x-1][y] != 'x':
					x -= 1
					d = 'u'
				else:
					return ans
			elif d == 'u':
				if x-1 >= 0 and m[x-1][y] != 'x':
					x -= 1
				elif y+1 < yn and m[x][y+1] != 'x':
					y += 1
					d = 'r'
				else:
					return ans

test = Solution()
print test.spiralOrder([[1,2,3]])
print test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

		