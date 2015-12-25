from Queue import PriorityQueue

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = PriorityQueue(k)

        for i, n in enumerate(nums):
            if i < k:
                pq.put(n)
                continue

            m = pq.get()
            if n > m:
                pq.put(n)
            else:
                pq.put(m)

        return pq.get()

        
if __name__ == '__main__':
    test = Solution()
    print test.findKthLargest([3,2,1,5,6,4], 2)
