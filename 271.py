class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += '#'
            ans += s
        return ans
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans = []
        cnt = 0
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            if ch in '1234567890':
                cnt *= 10
                cnt += ord(ch)-0x30
                i += 1
            elif ch == '#':
                ans += [s[i+1:i+1+cnt]]
                i += cnt+1
                cnt = 0
        return ans

# Your Codec object will be instantiated and called as such:
codec = Codec()
print codec.decode(codec.encode(['a', 'b', 'c']))
