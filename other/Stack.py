class Stack:
	def __init__ (self):
		self.items = list()

	def push (self, item):
		self.items.append (item)

	def pop (self):
		if len(self.items) > 0:
			return self.items.pop()
		return ('Stack is empty')

	def isEmpty (self):
		return self.items == list()

	def size (self):
		return len(self.items)

	def peek (self):
		return self.items[0]

	def printStack (self):
		print(self.items)

if __name__ == '__main__':
	my_stack = Stack()

	my_stack.push(1)
	my_stack.printStack()

	my_stack.push(5)
	my_stack.push(3)
	my_stack.printStack()

	print('Pop {} from stack'.format(my_stack.pop()))
	my_stack.printStack()
	print('Now stack size is {}'.format(my_stack.size()))

	print('First element in stack is {}'.format(my_stack.peek()))
	print('Pop {} from stack'.format(my_stack.pop()))
	my_stack.printStack()
	print('Pop {} from stack'.format(my_stack.pop()))
	my_stack.printStack()
	print('Now stack size is {}'.format(my_stack.size()))
	print(my_stack.pop())

