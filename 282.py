class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        self.ans = []
        
        def calc(idx, cur, pre, path):
            if idx == len(num):
                if cur + pre == target:
                    self.ans.append("".join(map(str, path)))
                return
            n = 0
            for i in xrange(idx, len(num)):
                n *= 10
                n += ord(num[i])-0x30
                path += ['+', n]
                calc(i+1, cur + pre, n, path)
                path.pop()
                path.pop()
                path += ['-', n]
                calc(i+1, cur + pre, -n, path)
                path.pop()
                path.pop()
                path += ['*', n]
                calc(i+1, cur, pre*n, path)
                path.pop()
                path.pop()
                if num[idx] == '0':
                    break

        n = 0
        for i in xrange(len(num)):
            n *= 10
            n += ord(num[i])-0x30
            calc(i+1, 0, n, [n])
            if num[0] == '0':
                break
        return self.ans
                
test = Solution()
print test.addOperators('123', 6)
print test.addOperators('023', 6)
print test.addOperators('00', 0)
print test.addOperators('10009', 9)
