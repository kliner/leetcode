class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dct = {}
        val = set([])
        self.ans = False

        def visit(pi, si):
            if len(pattern) == pi and len(str) == si:
                self.ans = True
                return
            if len(pattern) == pi: return
            if len(str) == si: return
            ch = pattern[pi]
            if ch in dct:
                target = dct[ch]
                if si+len(target) <= len(str) and str[si:si+len(target)] == target: visit(pi+1, si+len(target))
                else: return
            else:
                for i in xrange(si, len(str)):
                    dct[ch] = str[si:i+1]
                    if self.ans: return
                    if dct[ch] in val: continue
                    else:
                        val.add(dct[ch])
                        visit(pi+1, i+1)
                        val.remove(dct[ch])
                else: dct.pop(ch)

        visit(0, 0)
        return self.ans

test = Solution()
print(test.wordPatternMatch("abab", "redblueredblue"))
print(test.wordPatternMatch("aaaa", "asdasdasdasd"))
print(test.wordPatternMatch("aabb", "xyzabcxzyabc"))
print(test.wordPatternMatch("d", "e"))
print(test.wordPatternMatch("ab", "aa"))
print(test.wordPatternMatch("aba", "aaaa"))
