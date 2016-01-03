class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) <= 2:
            return False
        for i in xrange(1, 1+len(num)>>1):
            for j in xrange(1, 1+len(num)>>1):
                if self.dfs(num[:i], num[i:i+j], num[i+j:]):
                    return True
        return False

    def dfs(self, n1, n2, num):
        #print n1, n2, num
        if (len(n1)>1 and n1[0] == '0') or (len(n2)>1 and n2[0] == '0'):
            return False
        s = str(int(n1)+int(n2))
        if s == num:
            return True
        elif s == num[:len(s)] and num[len(s)] != '0':
            return self.dfs(n2, s, num[len(s):])
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print test.isAdditiveNumber("123")
    print test.isAdditiveNumber("101")
    print test.isAdditiveNumber("112358")
    print test.isAdditiveNumber("110058")
    print test.isAdditiveNumber("199100199")
    print test.isAdditiveNumber("0235813")

    
