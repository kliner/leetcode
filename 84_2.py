class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        height.append(0)
        stack = []
        ans = 0
        for i, x in enumerate(height):
            if not stack or x >= stack[-1][0]:
                stack.append((x, i))
            else:
                while stack and x < stack[-1][0]:
                    t = stack.pop()
                    ans = max(ans, (i - t[1]) * t[0])
                    #print ans, t
                stack.append((x, t[1]))
        return ans


if __name__ == '__main__':
    test = Solution()
    print test.largestRectangleArea([1,2,5,6,2,3])
    print test.largestRectangleArea([2,1,2])



