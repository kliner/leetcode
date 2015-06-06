class Solution():
	def search(self, a, target):
		n = len(a)
		start = 0
		end = n
		while start < end:
			mid = start + ((end - start) >> 1)
			if a[mid] == target:
				return mid
			elif a[start] < a[mid]:
				# left ascend
				if target == a[start]:
					return start
				if target > a[start] and target < a[mid]:
					end = mid
				else:
					start = mid + 1
			else:
				# right ascend
				if target == a[end-1]:
					return end-1
				if target > a[mid] and target < a[end-1]:
					start = mid
				else:
					end = mid
		return -1

class Solution():
	def search(self, a, target):
		n = len(a)
		start = 0
		end = n
		while start < end:
			mid = start + ((end - start) >> 1)
			if a[mid] == target:
				return True
			if a[start] == a[mid]:
				t = mid
				while t < end and a[start] == a[t]:
					t += 1
				if t == end:
					end = mid
					continue
				else:
					mid = t
					if a[mid] == target:
						return True
			if a[start] < a[mid]:
				# left ascend
				if target == a[start]:
					return True
				if target > a[start] and target < a[mid]:
					end = mid
				else:
					start = mid + 1
			else:
				# right ascend
				if target == a[end-1]:
					return True
				if target > a[mid] and target < a[end-1]:
					start = mid
				else:
					end = mid
		return False

test = Solution()
print test.search([4,5,1,2,3], 2)
print test.search([4,5,1,2,3], 4)
print test.search([4,5,1,2,3], 1)
print test.search([4,5,1,2,3], 5)
print test.search([4,5,1,2,3], 3)
print test.search([4,5,1,2,3], 0)
print test.search([4,5,1,2,3], 6)
print test.search2([1,1,1,5,1], 3)
print test.search2([1,1,1,5,1], 5)
print test.search2([1,5,1,1,1], 3)
print test.search2([1,5,1,1,1], 5)