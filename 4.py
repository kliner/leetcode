class Solution:
	# @return a float
	def mid(self, A):
		l = len(A)
		if l == 0:
			return 0
		# print l
		# print A
		if l % 2 == 0:
			# print A[l/2-1], A[l/2]
			return (A[l/2-1]+A[l/2])/2.
		else:
			# print A[l/2]
			return A[l/2]

	def find3m(self, A):
		for a in A:
			if a == max(A):
				A.remove(a)
				break
		for a in A:
			if a == min(A):
				A.remove(a)
				break
		return A[0]

	def find4m(self, A):
		for a in A:
			if a == max(A):
				A.remove(a)
				break
		for a in A:
			if a == min(A):
				A.remove(a)
				break
		return (A[0]+A[1])/2.

	def findMedianSortedArrays(self, A, B):
		la = len(A)
		lb = len(B)
		ma = self.mid(A)
		mb = self.mid(B)
		if la == lb == 1:
			return (A[0]+B[0])/2.
		if la == 0:
			return mb
		if lb == 0:
			return ma
		if ma == mb:
			return ma
		if la > lb:
			C = A
			A = B
			B = C
			mc = ma
			ma = mb
			mb = mc
			lc = la
			la = lb
			lb = lc

		if la == 1 and lb % 2 == 0:
			if A[0] >= B[lb/2-1] and A[0] <= B[lb/2]:
				return A[0]
			elif A[0] < B[lb/2-1]:
				return B[lb/2-1]
			elif A[0] > B[lb/2]:
				return B[lb/2]
		elif la == 1 and lb % 2 == 1:
			if A[0] >= B[lb/2-1] and A[0] <= B[lb/2+1]:
				return (A[0]+B[lb/2])/2.
			elif A[0] < B[lb/2-1]:
				return (B[lb/2-1]+B[lb/2])/2.
			elif A[0] > B[lb/2+1]:
				return (B[lb/2+1]+B[lb/2])/2.
		elif la == 2 and lb == 2:
			return self.find4m(A+B)
		elif la == 2 and lb % 2 == 0:
			return self.find4m([B[lb/2], B[lb/2-1], max(A[0], B[lb/2-2]), min(A[1], B[lb/2+1])])
		elif la == 2 and lb % 2 == 1:
			return self.find3m([max(A[0], B[lb/2-1]), min(A[1], B[lb/2+1]), B[lb/2]])

		if la % 2 == 0:
			k = la / 2 - 1
		else:
			k = la / 2
		if ma > mb:
			return self.findMedianSortedArrays(A[:la-k], B[k:])
		else:
			return self.findMedianSortedArrays(A[k:], B[:lb-k])		

test = Solution()
print test.findMedianSortedArrays([1,2], [1])