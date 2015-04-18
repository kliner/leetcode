class Solution:
	# @param x, an integer
	# @return a boolean
	def isPalindrome(self, x):
		while True:
			if x < 0:
				return False
			if x >= 0 and x < 10:
				return True
			if x >= 10 and x < 100:
				return x / 10 == x % 10

			if x >= 1000000000:
				if x / 1000000000 == x % 10:
					x = (x % 1000000000) / 10
					if x < 10000000:
						x += 10000001
				else:
					return False
			elif x >= 100000000:
				if x / 100000000 == x % 10:
					x = (x % 100000000) / 10
					if x < 1000000:
						x += 1000001
				else:
					return False
			elif x >= 10000000:
				if x / 10000000 == x % 10:
					x = (x % 10000000) / 10					
					if x < 100000:
						x += 100001
				else:
					return False
			elif x >= 1000000:
				if x / 1000000 == x % 10:
					x = (x % 1000000) / 10
					if x < 10000:
						x += 10001
				else:
					return False
			elif x >= 100000:
				if x / 100000 == x % 10:
					x = (x % 100000) / 10
					if x < 1000:
						x += 1001
				else:
					return False
			elif x >= 10000:
				if x / 10000 == x % 10:
					x = (x % 10000) / 10
					if x < 100:
						x += 101
				else:
					return False
			elif x >= 1000:
				if x / 1000 == x % 10:
					x = (x % 1000) / 10
					if x < 10:
						x += 101
				else:
					return False
			elif x >= 100:
				if x / 100 == x % 10:
					return True
				else:
					return False

test = Solution()
print test.isPalindrome(-1)
print test.isPalindrome(0)
print test.isPalindrome(11)
print test.isPalindrome(100)
print test.isPalindrome(13231)
print test.isPalindrome(1222221)
print test.isPalindrome(1222)
print test.isPalindrome(10021)
print test.isPalindrome(10201)
