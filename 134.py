class Solution:
	# @param {integer[]} gas
	# @param {integer[]} cost
	# @return {integer}
	def canCompleteCircuit(self, gas, cost):
		n = len(gas)
		start = n
		total = 0
		cur = 0
		curGas = 0
		for i in range(n):
			d = gas[cur] - cost[cur]
			if curGas + d >= 0:
				curGas += d
				total += d
				cur += 1
			else:
				start -= 1
				d = gas[start] - cost[start]
				curGas += d
				total += d
			print cur, start
		if total < 0:
			return -1
		elif start == n:
			return 0
		else:
			return start

test = Solution()
print test.canCompleteCircuit([3,2,1],[1,3,2])
print test.canCompleteCircuit([1,2,3],[1,3,2])
print test.canCompleteCircuit([2,3,1],[3,1,2])