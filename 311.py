class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        m1 = len(A)
        if m1 == 0: return []
        n1 = len(A[0])
        if n1 == 0: return []
        m2 = len(B)
        if m2 == 0: return []
        n2 = len(B[0])
        if n2 == 0: return []

        l1 = [(i, j, A[i][j]) for i in xrange(m1) for j in xrange(n1) if A[i][j] != 0]
        l2 = [(i, j, B[i][j]) for i in xrange(m2) for j in xrange(n2) if B[i][j] != 0]
        C = [[0] * n2 for i in xrange(m1)]

        for i1, j1, k1 in l1:
            for i2, j2, k2 in l2:
                if j1 == i2:
                    C[i1][j2] += k1*k2

        return C


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
test = Solution()
print test.multiply(A, B)
