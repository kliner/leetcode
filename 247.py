class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dct = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        if n == 0: return []
        if n == 1: return ['0','1','8']

        def find(n): 
            if n == 0: return []
            if n == 1: return ['0','1','8']
            ans = []
            t = find(n-2)
            if t:
                for s in t:
                    for c in dct:
                        ans += [c+s+dct[c]]
            else:
                for c in dct:
                    ans += [c+dct[c]]
                        
            return ans

        candi = find(n)
        ans = []
        for n in candi:
            if n[0] != '0':
                ans += [n]
        return ans



            
test = Solution()
print test.findStrobogrammatic(0)
print test.findStrobogrammatic(1)
print test.findStrobogrammatic(2)
print test.findStrobogrammatic(3)
print test.findStrobogrammatic(4)
