class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        dct = {}
        dictionary = set(dictionary)

        for s in dictionary:
            s2 = self.get(s)
            if s2 in dct:
                dct[s2] = -1
            else:
                dct[s2] = s
        self.dct = dct

    def get(self, s):
        n = len(s)
        if len(s) > 2:
            s = s[0] + str(n-2) + s[-1]
        return s

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if not self.dct:
            return True 
        abbr = self.get(word)
        if abbr in self.dct:
            if self.dct[abbr] != word:
                return False
            return True
        return True
        

# Your ValidWordAbbr object will be instantiated and called as such:
dictionary = [ "deer", "door", "cake", "card" ]
vwa = ValidWordAbbr(dictionary)
print vwa.isUnique("dear")
print vwa.isUnique("door")
print vwa.isUnique("cake")
print vwa.isUnique("card")
print vwa.isUnique("hello")
print vwa.isUnique("dxxr")
print vwa.isUnique("cxxe")
dictionary = [ "deer", "deer", "deer", "card" ]
vwa = ValidWordAbbr(dictionary)
print vwa.isUnique("deer")
print vwa.isUnique("door")
print vwa.isUnique("cake")
print vwa.isUnique("card")
print vwa.isUnique("hello")
print vwa.isUnique("dxxr")
print vwa.isUnique("cxxe")
