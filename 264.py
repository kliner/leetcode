class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]
        x, y, z = 0, 0, 0
        for i in range(n):
            target = a[-1]
            while a[x] * 2 <= target:
                x += 1
            while a[y] * 3 <= target:
                y += 1
            while a[z] * 5 <= target:
                z += 1
            tx, ty, tz = a[x] * 2, a[y] * 3, a[z] * 5
            a.append(min(tx, ty, tz))
        return a[n-1]

if __name__ == '__main__':
    test = Solution()
    for i in range(1,11):
        print test.nthUglyNumber(i)
