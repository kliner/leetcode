import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            if len(q) == 0 or num > q[-1]:
                q.clear()
                q.append(num)
            else:
                if num < q[0]:
                    q.appendleft(num)
                else:
                    while num > q[0]:
                        q.popleft()
                    q.appendleft(num)
            if i >= k and q[-1] == nums[i-k]: 
                q.pop()
            if i >= k-1:
                ans.append(q[-1])

        return ans

if __name__ == '__main__':
    test = Solution()
    print test.maxSlidingWindow([1,3,2,1,0,5], 3)
    print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print test.maxSlidingWindow([1,5,2,3,4,3,2,1], 3)
    print test.maxSlidingWindow([1,-1], 1)
    print test.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)
