class Solution:
	# @param {integer[]} digits
	# @return {integer[]}
	def plusOne(self, digits):
		f = True
		for i in digits:
			if i != 9:
				f = False
				break
		if f:
			a = [1]
			a.extend([0 for i in range(len(digits))])
			return a

		carry = True		
		for i in range(len(digits)-1,-1,-1):
			if carry:
				if digits[i] == 9:
					digits[i] = 0
					carry = True
				else:
					digits[i] += 1
					carry = False

		return digits

test = Solution()
print test.plusOne([9,9,9])
print test.plusOne([5,9,9])
print test.plusOne([5,6,7])


