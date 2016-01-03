class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        plus = 1
        n = 0
        stack = []
        for ch in s:
            if ch == ' ':
                continue
            elif ch == '(':
                stack.append((ans, plus))
                ans = 0
                plus = 1
            elif ch == ')':
                n = ans + plus * n
                ans, plus = stack.pop()
            elif ch == '+':
                ans += (plus * n)
                plus = 1
                n = 0
            elif ch == '-':
                ans += (plus * n)
                plus = -1
                n = 0
            else:
                n *= 10
                n += int(ch)
        ans += (plus * n)
        return ans   


if __name__ == '__main__':
    test = Solution()
    print test.calculate("(1+(4+5+2)-3)+(6+8)")
    print test.calculate("2-1 + 2 ")
    print test.calculate("2-(5-6)")


