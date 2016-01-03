class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
    def getAllResult(self, num):
        if len(num) == 1:
            return [ord(num)-0x30]
        if num in self.dct:
            return self.dct[num]
        ans = set([])
        for i in xrange(1, len(num)-1):
            left = self.getAllResult(num[:i])
            right = self.getAllResult(num[i+1:])
            for l in left:
                for r in right:
                    ans.add(l+r)
                    ans.add(l*r)
                    ans.add(l-r)
        self.dct[num] = ans
        return ans


