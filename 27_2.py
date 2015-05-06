class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		count = 0
		n = len(A)
		j = n - 1
		for i in xrange(n):
			while i > j and A[j] == elem:
				j -= 1
				count += 1
			if A[i] == elem:
				A[i] = A[j]
				j -= 1
				count += 1
		return n - count

test = Solution()
A = [1,2,3,4,5,1,2,3,4,5,6,1,2,3,4]
l = test.removeElement(A, 1)
print A[:l]
l = test.removeElement(A, 5)
print A[:l]
l = test.removeElement(A, 6)
print A[:l]
l = test.removeElement(A, 0)
print A[:l]
