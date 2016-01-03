class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E >= C or G <= A or H <= B or F >= D: 
            common = 0
        else:
            common = (min(C,G) - max(A,E))*(min(D,H)-max(B,F))
        return (C-A)*(D-B)+(H-F)*(G-E)-common
        
if __name__ == '__main__':
    test = Solution()
    print test.computeArea(0,0,1,1,2,2,3,3)
    print test.computeArea(0,0,2,2,1,1,3,3)
    print test.computeArea(0,1,2,3,1,0,3,2)
    print test.computeArea(0,0,0,0,-1,-1,1,1)
