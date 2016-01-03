class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        op = '+'
        n = 0
        s = s + '+0'
        stack = []
        for ch in s:
            #print ans, op, n, ch
            if ch in ['+','-']:
                if stack:
                    n = self.calc(ans, op, n)
                    ans, op = stack.pop()
                ans = self.calc(ans, op, n)
                op = ch
                n = 0
            elif ch in ['*','/']:
                if not stack:
                    stack.append((ans, op))
                    ans = n
                else:
                    ans = self.calc(ans, op, n)
                op = ch
                n = 0
            elif ch >= '0' and ch <= '9':
                n *= 10
                n += int(ch)

        return ans


    def calc(self, ans, op, n):
        if not ans:
            ans = 0
        if ans == True:
            ans = 1
        if not n:
            n = 0
        if n == True:
            n = 1

        if op is '+':
            return int(ans + n)
        if op is '-':
            return int(ans - n)
        if op is '*':
            return int(ans * n)
        if op is '/':
            return int(ans / n)

        
if __name__ == '__main__':
    test = Solution()
    print test.calculate("3+2*2")# = 7
    print test.calculate("3/2 ")# = 1
    print test.calculate("3+5 / 2 ")# = 5
    print test.calculate("  30")
    print test.calculate("0")
    print test.calculate("0*0")
    print test.calculate("1 + 1")
    print test.calculate("1 + 1")

