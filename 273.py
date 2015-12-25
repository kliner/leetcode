class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 
                11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 
                30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred', 1000:'Thousand', 
                1e6:'Million', 1e9:'Billion'}

        if num == 0:
            return 'Zero'

        a = [num % (1000**(i+1)) / (1000**i) for i in range(3,-1,-1)]
        #print a

        ans = []
        for i, n in enumerate(a):
            ret = self.make3n(n, words)
            if len(ret) != 0:
                ans.extend(ret)
                if i != 3:
                    ans.append(words[1000 ** (3-i)])
        
        return ' '.join(ans)

    def make3n(self, num, words):
        a = num / 100;
        bc = num % 100;
        b = bc / 10;
        c = bc % 10;

        ret = []
        if a > 0:
            ret.append(words[a])
            ret.append(words[100])
        if b == 0 and c == 0:
            return ret
        if b <= 1:
            ret.append(words[bc])
            return ret
        else:
            ret.append(words[b * 10])
            if c != 0:
                ret.append(words[c])
        return ret

        
    
if __name__ == '__main__':
    test = Solution()
    a = 0
    print test.numberToWords(a)
    a = 1
    print test.numberToWords(a)
    a = 10
    print test.numberToWords(a)
    a = 11
    print test.numberToWords(a)
    a = 30
    print test.numberToWords(a)
    a = 45
    print test.numberToWords(a)
    a = 100
    print test.numberToWords(a)
    a = 1000
    print test.numberToWords(a)
    a = 1001
    print test.numberToWords(a)
    a = 12345
    print test.numberToWords(a)
    a = 1234567
    print test.numberToWords(a)
    a = 123456789
    print test.numberToWords(a)
