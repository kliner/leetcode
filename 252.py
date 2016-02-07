# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        arr = []
        for a in intervals:
            arr.append((a.start, 1))
            arr.append((a.end, 0))
        arr.sort()
        s = 1
        for a in arr:
            if a[1] != s: return False
            else: s ^= 1

        return True
            
test = Solution()
print test.canAttendMeetings([])
print test.canAttendMeetings([Interval(0, 10)])
print test.canAttendMeetings([Interval(0, 10),Interval(15, 20)])
print test.canAttendMeetings([Interval(0, 30),Interval(5, 10)])

        
