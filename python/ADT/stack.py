class Stack:
	def __init__(self, size):
		self.elements=[]
		self.size = size
	def is_empty(self):
		return len(self.elements) == 0
	def is_full(self):
		if len(self.elements)==self.size:
			print("stack full")
	def push(self, item):
		if not self.is_full():
			self.elements.append(item)
		else:
			print("stack is full")
	def pop(self):
		if not self.is_empty():
			self.elements.pop()
		else:
			print("stack is empty")
	def top(self):
		if not self.is_empty():
			print(self.elements[-1])
		else:
			print("stack is empty")
	def get_size(self):
		return len(self.elements)
	def print_ele(self):
		return (self.elements)
stack =Stack(10)
stack.push(10)
stack.push(25)
stack.push(5)
print(stack.print_ele())
print("Size: ", stack.get_size())
print("Top: ", stack.top())

stack.push(30)
stack.push(15)
stack.push(20)
print("Top: ", stack.top())
print("Size: ", stack.get_size())
stack.push(40)