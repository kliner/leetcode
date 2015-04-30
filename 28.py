class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		count = 0
		n = len(A)
		j = n-1
		i = 0
		while i <= j:
			if A[j] == elem:
				j -= 1
			elif A[i] == elem:
				A[i] = A[j]
				i += 1
				j -= 1
				count += 1
			else:
				i += 1
				count += 1
		return count

# A = [1,2,3,4,5,1,2,3,4,5,6,2,3,3,3]
# A = []
# A = [1]
A = [2]
test = Solution()
n = test.removeElement(A, 1)
print A[:n]