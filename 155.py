class MinStack:
	# initialize your data structure here.
	def __init__(self):
		self.stack = []
		self.mins = []

	# @param x, an integer
	# @return nothing
	def push(self, x):
		self.stack.append(x)        
		if self.mins == [] or x <= self.mins[-1]:
			self.mins.append(x)

	# @return nothing
	def pop(self):
		t = self.stack.pop()
		if t == self.mins[-1]:
			self.mins.pop()


	# @return an integer
	def top(self):
		return self.stack[-1]

	# @return an integer
	def getMin(self):
		return self.mins[-1]

test = MinStack()
test.push(5)
test.push(3)
test.push(1)
test.push(2)
print test.getMin()
test.pop()
print test.getMin()
test.pop()
print test.getMin()