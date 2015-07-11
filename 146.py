class ListNode:
	def __init__(self, k, v):
		self.key = k
		self.val = v
		self.next = None
		self.prev = None

class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		self.capacity = capacity - 1
		self.n = 0
		self.head = None
		self.tail = None
		self.map = {}

	# @return an integer
	def get(self, key):
		if self.capacity == -1 or self.head == None or key not in self.map:
			return -1
		if self.head.key == key:
			return self.head.val
		if self.tail.key == key:
			t = self.tail
			self.tail = self.tail.prev
			t.prev = None
			t.next = self.head
			self.head.prev = t
			self.head = t
			return self.head.val

		cur = self.map[key]
		
		cur.prev.next = cur.next
		cur.next.prev = cur.prev

		cur.next = self.head
		self.head.prev = cur
		cur.prev = None
		self.head = cur
		return self.head.val

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		if self.head == None:
			self.head = ListNode(key, value)
			self.tail = self.head
			self.map[key] = self.head
			return
		cur = self.head
		if cur.key == key:
			cur.val = value
			return

		if self.get(key) == -1:
			# not found
			t = ListNode(key, value)
			self.map[key] = t
			t.next = self.head
			self.head.prev = t
			self.head = t
			if self.n < self.capacity:
				self.n += 1
			else:
				self.map.pop(self.tail.key)
				p = self.tail.prev
				p.next = None
				self.tail = p
		else:
			# found, already move to head
			self.head.val = value

	def printl(self):
		print '-----%d-----' % self.n 
		print self.map.keys()
		cur = self.head
		for i in range(self.n+1):
			print cur.val
			cur = cur.next

test = LRUCache(4)
test.set(1,1)
test.get(1)
test.printl()
test.set(2,2)
test.get(2)
test.get(1)
test.printl()
test.set(3,3)
test.printl()
test.set(2,100)
test.printl()
test.set(4,4)
test.set(5,5)
test.printl()
test.get(1)
test.printl()
test.get(3)
test.printl()
test = LRUCache(1)
test.set(2,1)
test.get(2)
test.printl()
test.set(3,2)
test.printl()
test.get(2)
test.printl()