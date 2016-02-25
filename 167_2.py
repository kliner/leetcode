import bisect
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1
        while i < j:
            print i, j
            cur = numbers[i]
            idx = bisect.bisect_left(numbers, target - cur, i, j+1)
            if idx < len(numbers) and cur + numbers[idx] == target:
                if i == idx: 
                    if i < len(numbers) and numbers[i+1] == numbers[i]:
                        return [i+1, i+2]
                else:
                    return [i+1, idx+1]
            j = idx - 1
            i = bisect.bisect_left(numbers, target - numbers[j], i, j+1)
            
test = Solution()
print test.twoSum([2,3,4], 6)
print test.twoSum([1,2,3,5], 5)
print test.twoSum([0,0,3,5], 0)
print test.twoSum([0,0,3,5], 8)
print test.twoSum([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,14,15,16,17,18], 13)
print test.twoSum([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,14,15,16,17,18], 29)
print test.twoSum([-10,-8,-6,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,14,15,16,17,18,34,36,38], 29)
print test.twoSum([-100,-98,-96,-94,0,0,95,97,99], 0)
