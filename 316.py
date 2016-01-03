class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = [0] * 26
        for ch in s:
            cnts[ord(ch)-0x61]+=1
        stk = []
        marked = [0] * 26
        for ch in s:
            if marked[ord(ch)-0x61]:
                cnts[ord(ch)-0x61] -= 1
                continue
            while stk and ch < stk[-1] and cnts[ord(stk[-1])-0x61]:
                a = stk.pop()
                marked[ord(a)-0x61] = 0
            stk.append(ch)
            marked[ord(ch)-0x61] = 1
            cnts[ord(ch)-0x61] -= 1
        return ''.join(stk)
                
    
if __name__ == '__main__':
    test = Solution()
    print test.removeDuplicateLetters('bcabc')
    print test.removeDuplicateLetters('cbacdcbc')
    print test.removeDuplicateLetters('bbcaac')

