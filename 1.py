class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
    	dic = {}
    	for i in num:
    		dic[i] = 1
    	for i in range(len(num)):
    		if (target - num[i]) in dic:
    			a = target - num[i]
    			for j in range(len(num)):
    				if num[j] == a:
    					break
    			if i == j:
    				continue
    					
    			if i > j:
    				return (j+1, i+1)
    			else:
    				return (i+1, j+1)

a = Solution()
(i, j) = a.twoSum([3,2,4], 6)
print "index1=%d, index2=%d" % (i, j)