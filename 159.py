class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 2: return n
        dp = [ [0]*2 for i in xrange(n) ]
        ss = [s[0]]
        dp[0][0] = 1
        dp[0][1] = 1

        for i in xrange(1,n):
            if s[i] == s[i-1]:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = 1
                if s[i] in ss:
                    dp[i][1] = dp[i-1][1]+1
                else:
                    dp[i][1] = dp[i-1][0]+1
                    ss = [s[i-1], s[i]]
        return max(dp[i][1] for i in xrange(n))

test = Solution()
print test.lengthOfLongestSubstringTwoDistinct('aaa')
print test.lengthOfLongestSubstringTwoDistinct('abaad')
print test.lengthOfLongestSubstringTwoDistinct('ababa')
print test.lengthOfLongestSubstringTwoDistinct('abacd')

