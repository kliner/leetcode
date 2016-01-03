class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        if n > 45 or k > 9:
            self.ans = []
        self.dfs(k, n, [0]*10, 1)
        return self.ans

    def dfs(self, k, n, marked, idx):
        if n == 0 and k == 0:
            a = [i for i in xrange(1, 10) if marked[i] == 1]
            self.ans.append(a)
            return
        if n <= 0 or k <= 0:
            return 
        for i in xrange(idx, 10):
            if not marked[i]:
                marked[i] = 1
                self.dfs(k-1, n-i, marked, i+1) 
                marked[i] = 0

                
if __name__ == '__main__':
    test = Solution()
    print test.combinationSum3(3,9)
    print test.combinationSum3(3,7)
