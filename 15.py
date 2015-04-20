class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		if len(num) < 3:
			return []
		dic = {}
		for n in num:
			if n in dic:
				dic[n] += 1
			else:
				dic[n] = 1

		# print dic
		res = []
		for i in dic:
			for j in dic:
				t = 0 - i - j
				if t in dic:
					if t == i and t == j and dic[t] <= 2:
						continue
					elif t == i and dic[t] <= 1:
						continue
					elif t == j and dic[t] <= 1:
						continue
					elif i == j and dic[i] <= 1:
						continue
					else:
						if i <= j and j <= t:
							res.append([i, j, t])
		return res


test = Solution()
print test.threeSum([-1, 0, 1, 2, -1, -4])
print test.threeSum([-2, 0, 1, 1, 2])
print test.threeSum([-4, 0, 1, 1, 4, 2, 2, 3, 3])
print test.threeSum([-2, 0, -1, -1, 2])
print test.threeSum([-1, 0, 1, 2, -1, -1, 0, 1, 2, -1, -1, 0, 1, 2, -1, -1, 0, 1, 2, -1, -1, 0, 1, 2, -1, -1, 0, 1, 2, -1, -4])
