class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dct = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        i, j = 0, len(num)-1
        while i <= j:
            if num[i] in dct and num[j] in dct and dct[num[i]] == num[j]:
                i+=1
                j-=1
            else:
                return False
        return True

test = Solution()
print test.isStrobogrammatic('0')
print test.isStrobogrammatic('1')
print not test.isStrobogrammatic('2')
print not test.isStrobogrammatic('3')
print test.isStrobogrammatic('818')
print test.isStrobogrammatic('619')
print not test.isStrobogrammatic('66')
