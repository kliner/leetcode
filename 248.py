class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
        dct = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}

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

        if low == '0':
            ans = 1
        else:
            ans = 0
        n1, n2 = len(low), len(high)
        for i in xrange(n1, n2+1):
            candi = find(i)
            for s in candi:
                if s[0] == '0': continue
                if i == n1 and s < low: continue
                if i == n2 and s > high: continue
                #print s
                ans += 1

        #print ans
                
        return ans
                
test = Solution()
print test.strobogrammaticInRange("0", "10") == 3
print test.strobogrammaticInRange("0", "1") == 2
print test.strobogrammaticInRange("50", "100") == 3
print test.strobogrammaticInRange("0", "1000000000000") 
