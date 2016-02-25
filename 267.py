import copy


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0: return []
        dct = {}
        for ch in s:
            dct[ch] = dct.get(ch, 0) + 1

        n = len(s)
        cur = [0] * ((n+1) >> 1)
        mid = False
        for k in dct:
            if dct[k] % 2 == 1:
                if not cur[0]:
                    cur[0] = k
                    dct[k] -= 1
                    mid = True
                else:
                    return []

        ans = []

        def visit(idx):
            if idx == ((n+1) >> 1):
                if mid:
                    ans.append(''.join(cur[::-1])+''.join(cur[1::]))
                else:
                    ans.append(''.join(cur[::-1])+''.join(cur))
                return

            for k1 in dct:
                if dct[k1] > 0:
                    dct[k1] -= 2
                    cur[idx] = k1
                    visit(idx + 1)
                    cur[idx] = 0
                    dct[k1] += 2

        if cur[0]:
            visit(1)
            return ans
        else:
            visit(0)
            return ans


test = Solution()
print test.generatePalindromes("")
print test.generatePalindromes("aabb")
print test.generatePalindromes("aab")
print test.generatePalindromes("ab")
print test.generatePalindromes("abc")
print test.generatePalindromes("aabbccaa")
print test.generatePalindromes("aabbccaae")
