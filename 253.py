# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        arr = []
        for i in intervals:
            arr.append((i.start, 1))
            arr.append((i.end, 0))
        arr.sort()
        cur = 0
        ans = 0
        for i, t in arr:
            if t == 1:
                cur += 1
            else:
                cur -= 1
            ans = max(ans, cur)

        return ans
        
test = Solution()
testCase = []
print test.minMeetingRooms(testCase) == 0
testCase = [Interval(0, 100), Interval(1,99), Interval(2,98)]
print test.minMeetingRooms(testCase) == 3
testCase = [Interval(0, 30), Interval(5,10), Interval(15,20)]
print test.minMeetingRooms(testCase) == 2
