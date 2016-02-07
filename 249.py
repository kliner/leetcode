class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ans = {}

        def getKey(s):
            a = ord(s[0])
            key = 1
            for ch in s:
                key <<= 4
                t = ord(ch)-a
                if t < 0:
                    t += 26
                key += t
            return key

        for s in strings:
            k = getKey(s)
            if k in ans:
                ans[k].append(s)
            else:
                ans[k] = [s]
        ret = []
        for k in ans:
            ans[k].sort()
            ret.append(ans[k])
        return ret

test = Solution()
print test.groupStrings(["aa", "b", "bb"])
print test.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
