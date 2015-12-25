from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        LRH = buildings
        i, n = 0, len(buildings)
        alivesHR = []
        
        while i < n or alivesHR:
            if not alivesHR or (i < n and -alivesHR[0][1] >= LRH[i][0] ):
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(alivesHR, (-LRH[i][2], -LRH[i][1]))
                    print alivesHR
                    i += 1
                h = -alivesHR[0][0]
                if not ret or ret[-1][1] != h:
                    ret.append([x, h])
            else:
                x = -alivesHR[0][1]
                while alivesHR and -alivesHR[0][1] <= x:
                    heappop(alivesHR)
                    print alivesHR

                if not alivesHR:
                    h = 0
                else:
                    h = -alivesHR[0][0]
                if ret[-1][1] != h:
                    ret.append([x, h])


            print "ret", ret

        return ret

if __name__ == '__main__':
    test = Solution()
    print test.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ])

