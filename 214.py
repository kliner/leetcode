class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s + '#' + s[::-1]
        nxt = [0]
        for i in range(1, len(t)):
            x = nxt[i-1]
            while x > 0 and t[i] != t[x]:
                x = nxt[x-1]
            if t[i] == t[x]:
                nxt.append(x + 1)
            else:
                nxt.append(0)
        n = nxt[-1]
        return s[len(s):n-1:-1]+s
        
if __name__ == '__main__':
    test = Solution()
    print test.shortestPalindrome("abc")
    print test.shortestPalindrome("abacd")
    print test.shortestPalindrome("a")
