from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        retLH = []
        LRH = buildings
        i, n = 0, len(buildings)
        aliveHR = []
        
        while i < n or aliveHR:
            if not aliveHR or (i < n and -aliveHR[0][1] >= LRH[i][0]):
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(aliveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
                if not retLH or retLH[-1][1] != -aliveHR[0][0]:
                    retLH.append( [x, -aliveHR[0][0]])
            else:
                x = -aliveHR[0][1]
                while aliveHR and -aliveHR[0][1] <= x:
                    heappop(aliveHR)
                if aliveHR:
                    h = -aliveHR[0][0]
                else:
                    h = 0
                if retLH[-1][1] != h:
                    retLH.append([x, h])
            #print aliveHR, retLH

        return retLH

if __name__ == '__main__':
    test = Solution()
    print test.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ])
    print [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]


