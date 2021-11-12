class Queue:
	def __init__(self):
	    self.items = []

	def isEmpty(self):
	    return self.items == []

	def enque(self, item):
	    self.items.insert(0,item)

	def deque(self):
	    return self.items.pop()

	def size(self):
	    return len(self.items)

e=Queue()
print(e.isEmpty())
e.enque(24)
e.enque(98)
e.enque('Dnya')
e.enque('Prasad')
e.enque(True)
print(e.size())
print(e.isEmpty())
e.enque(8.4)
print(e.deque())
print(e.deque())
