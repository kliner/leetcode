class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
    	a = []
        while n != 0:
        	t = n % 5
        	a.append(t)
        	n = n / 5
        n = len(a)
        ans = 0
        b = [0]
        for i in range(n-1):        	
        	b.append(b[-1]*5+1)
        for i in range(n):
        	ans += a[i] * b[i]
        return ans


test = Solution()
print test.trailingZeroes(10) == 2
print test.trailingZeroes(25) == 1 * 5 + 1
print test.trailingZeroes(125) == 6 * 5 + 1