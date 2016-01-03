class Solution(object):
    def diffWaysToCompute(self, inp):
        """
        :type input: str
        :rtype: List[int]
        """
        ret = []
        f = True
        for i, ch in enumerate(inp):
            if ch in ['+','-','*']:
                f = False
                l = self.diffWaysToCompute(inp[:i])
                r = self.diffWaysToCompute(inp[i+1:])
                for a in l:
                    for b in r:
                        if ch == '+':
                            ret.append(a+b)
                        elif ch == '-':
                            ret.append(a-b)
                        else:
                            ret.append(a*b)
        if f:
            if inp == '0':
                return [0]
            else:
                return [int(inp)]
        return ret
    
if __name__ == '__main__':
    test = Solution()
    print test.diffWaysToCompute("0+1")
    print test.diffWaysToCompute("2-1-1")
    print test.diffWaysToCompute("2*3-4*5")
