class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = {'A':'1','C':'2','G':'3','T':'4'}
        revertm = {1:'A',2:'C',3:'G',4:'T'}
        d = set([])
        ret = set([])
        bit = ""
        for ch in s:
            bit += m[ch]
            
        for i in range(10,len(s)+1):
            cur = int(bit[i-10:i])
            if cur not in d:
                d.add(cur)
            else:
                ret.add(cur)

        ans = []
        for word in ret:
            s = ''
            for i in range(10):
                t = word % 10
                s = revertm[t] + s
                word /= 10
            ans.append(s)

        return ans

        
if __name__ == '__main__':
    test = Solution()
    print test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print test.findRepeatedDnaSequences("AAAAAAAAAAA")
