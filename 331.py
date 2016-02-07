class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        ss = preorder.split(',')
        stk = []
        for s in ss:
            if s == '#':
                while stk and stk[-1] == '#':
                    stk.pop()
                    if not stk: return False
                    stk.pop()
            stk.append(s)
        if len(stk) == 1 and stk[0] == '#': return True
        return False

test = Solution()
print test.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print not test.isValidSerialization("")
print test.isValidSerialization("#")
print not test.isValidSerialization("1")
print not test.isValidSerialization("1,#,1,#")
print test.isValidSerialization("1,#,#")
print not test.isValidSerialization("1,#,#,#")
print not test.isValidSerialization("1,#")
print not test.isValidSerialization("9,#,#,1")
