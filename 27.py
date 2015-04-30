class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		n = len(A)
		if n <= 1:
			return n
		p = 1
		for i in xrange(1, n):
			if A[i] != A[i - 1]:
				A[p] = A[i]
				p += 1 
		return p

test = Solution()
A = [1]
A = [1,1,2]
n = test.removeDuplicates(A)
print A[:n]