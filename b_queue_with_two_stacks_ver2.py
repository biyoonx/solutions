class Stack:
		class Node:
				def __init__(self, data):
						self.data = data
						self.next = None
    
		def __init__(self):
				self.top = None
  
		def is_empty(self):
				return self.top is None
  
		def peek(self):
				return self.top if self.is_empty() else self.top.data
    
		def push(self, data):
				data_in = self.Node(data)
    
				if (self.top is not None):
						data_in.next = self.top
      
				self.top = data_in
    
		def pop(self):
				if (self.is_empty()):
						return None
    
				data_out = self.top.data
				self.top = self.top.next
				return data_out

# Stack test
stack = Stack()
print(stack.top) # None
stack.push('first')
print(stack.peek(), stack.top.data, stack.top.next) # first first None
stack.push('second')
print(stack.peek(), stack.top.data, stack.top.next.data) # second second first
print(stack.pop(), stack.top.data, stack.top.next) # second first None
print(stack.pop(), stack.top) # first None

class Queue:
		class Node:
				def __init__(self, data):
						self.data = data
						self.next = None
    
		def __init__(self):
				self.front = None # 출력될 데이터, head
				self.rear = None	# 입력된 데이터, tail
    
		def is_empty(self):
				return self.front is None
  
		def peek(self):
				return self.front if self.is_empty() else self.front.data
  
		def add(self, data):
				data_in = self.Node(data)
    
				if (self.rear is not None):
						self.rear.next = data_in
				self.rear = data_in
    
				if (self.front is None):
						self.front = data_in
    
		def remove(self):
				if (self.is_empty()):
						return None
    
				data_out = self.front.data
				self.front = self.front.next
    
				if (self.front is None):
						self.rear = None
      
				return data_out

# Queue test
queue = Queue()
print(queue.front, queue.rear) # None None
queue.add('first')
print(queue.peek(), queue.front.data, queue.rear.data) # first first first
queue.add('second')
print(queue.peek(), queue.front.data, queue.rear.data) # first first second
print(queue.remove(), queue.front.data, queue.rear.data) # first second second
print(queue.remove(), queue.front, queue.rear) # second None None

class QueueWithTwoStacks:
		def __init__(self):
				self.stack_in = Stack()
				self.stack_out = Stack()
    
		def is_empty(self):
				return self.stack_in is self.stack_out is None
  
		def move_if_empty(self):
				if (self.stack_out.is_empty()):
						while not self.stack_in.is_empty():
								self.stack_out.push(self.stack_in.pop())
    
		def peek(self):
				self.move_if_empty()
    
				return self.stack_out.peek()

		def add(self, data):
				self.stack_in.push(data)
    
		def remove(self):
				self.move_if_empty()
    
				return self.stack_out.pop()

# Queue with two stack test
queue_with_two_stacks = QueueWithTwoStacks()
print(queue_with_two_stacks.stack_out.top, queue_with_two_stacks.stack_in.top) # None None
queue_with_two_stacks.add('first')
print(queue_with_two_stacks.stack_out.top, queue_with_two_stacks.stack_in.top.data) # None first
print(queue_with_two_stacks.peek(), queue_with_two_stacks.stack_out.top.data, queue_with_two_stacks.stack_in.top) # first first None
queue_with_two_stacks.add('second')
queue_with_two_stacks.add('third')
print(queue_with_two_stacks.stack_out.top.data, queue_with_two_stacks.stack_in.top.data) # first third
print(queue_with_two_stacks.remove(), queue_with_two_stacks.stack_out.top, queue_with_two_stacks.stack_in.top.data) # first None third
print(queue_with_two_stacks.remove(), queue_with_two_stacks.stack_out.top.data, queue_with_two_stacks.stack_in.top) # second third None
print(queue_with_two_stacks.remove(), queue_with_two_stacks.stack_out.top, queue_with_two_stacks.stack_in.top) # third None None