class Stack:
		top = -1
		stack = []

		def __init__(self) -> None:
				self.top = -1
				self.stack = []

		def push(self, new_data):
				self.top += 1
				try:
						self.stack[self.top] = new_data
				except IndexError:
						self.stack.insert(self.top, new_data)

		def pop(self):
				if (self.top == -1):
						return None
				
				# 반환할 데이터를 먼저 로컬변수에 저장했다가 top을 감소시킨 후 저장한 값을 반환하도록 하는 것이 더 적절할까?
				# self.top -= 1
				# return self.stack[self.top + 1]
				top_data = self.stack[self.top]
				self.top -= 1
				return top_data # 큐와는 다르게 top이 범위 외의 값을 호출하게 되는 시스템 같아서 저장하고 top을 감소시킨 후 꺼낸 값을 반환하도록 함

		def peek(self):
				if (self.top == -1):
						return None

				return self.stack[self.top]

# Stack test
stack = Stack()
print(stack.top) # -1
stack.push('first')
print(stack.peek(), stack.top) # first 0
stack.push('second')
print(stack.peek(), stack.top) # second 1
print(stack.pop(), stack.top) # second 0
print(stack.pop(), stack.top) # first -1

class Queue:
		front = -1
		rear = -1
		queue = []
		# capacity는 여기서는 생략
  
		def __init__(self) -> None:
				self.front = -1
				self.rear = -1
				self.queue = []
    
		def enqueue(self, new_data):
				self.rear += 1
				try:
						self.queue[self.rear] = new_data
				except IndexError:
						self.queue.insert(self.rear, new_data)
    
		def dequeue(self):
				if (self.front == self. rear):
						return None
    
				self.front += 1
				return self.queue[self.front]
    
		def peek(self):
				if (self.front == self.rear):
						return None
	
				return self.queue[self.front + 1] # 여기서도 마찬가지로 front 값을 증가시키고 값을 저장했다가 다시 감소시키고 저장한 값을 반환하는 것이 더 적절할까? -> 스택과 큐의 출력할 데이터의 포인터가 바뀌는 시스템이 상이하므로 큐는 프로세스상 괜찮을 것이라 생각함 + 데이터의 포인터가 범위 외의 값을 가리키지 않으므로 수정하지 않음.

# Queue test
queue = Queue()
print(queue.front, queue.rear) # -1 -1
queue.enqueue('first')
print(queue.peek(), queue.front, queue.rear) # first -1 0
queue.enqueue('second')
print(queue.peek(), queue.front, queue.rear) # first -1 1
print(queue.dequeue(), queue.front, queue.rear) # first 0 1
print(queue.dequeue(), queue.front, queue.rear) # second 1 1

class QueueWithTwoStacks:
		front = -1 # front는 두번째로 삽입하는 스택(데이터를 출력할)의 top
		rear = -1 # rear는 (이동 전) 첫번째로 삽입하는 스택(데이터를 입력할)의 top, 이동 후에는 다시 -1로 초기화(마지막으로 삽입한 데이터가 출력용 스택으로 옮겨지지만 top이 아니므로 좀 애매하고 또, 데이터가 입력될 위치를 표시하는게 더 적절하다고 생각하여 -1로 초기화함)

		def __init__(self) -> None:
				self.front = -1
				self.rear = -1
				self.stack_first_in = Stack()
				self.stack_last_out = Stack()

		def enqueue(self, new_data):
				self.stack_first_in.push(new_data)
				self.rear = self.stack_first_in.top
    
		def move_if_empty(self):
				if (self.stack_last_out.top == -1 or not self.stack_last_out.stack[self.stack_last_out.top:]) and (self.stack_first_in.top != -1 and self.stack_first_in.stack[self.stack_first_in.top:]):
						while self.stack_first_in.top != -1 and self.stack_first_in.stack[self.stack_first_in.top:]:
								self.stack_last_out.push(self.stack_first_in.pop())
						self.front = self.stack_last_out.top
						self.rear = self.stack_first_in.top

		def dequeue(self):
				if (self.front == self.rear == -1):
						return None
    
				self.move_if_empty()

				self.front = self.stack_last_out.top - 1
				return self.stack_last_out.pop() # top_data = self.stack_last_out.stack[self.stack_last_out.top];self.stack_last_out.top -= 1;return top_data;

		def peek(self):
				self.move_if_empty()
    
				if (self.front == self.rear == -1):
						return None

				return self.stack_last_out.peek() # self.stack_last_out.stack[self.stack_last_out.top]

# Queue with two stack test
queue_with_two_stacks = QueueWithTwoStacks()
print(queue_with_two_stacks.front, queue_with_two_stacks.rear) # -1 -1
queue_with_two_stacks.enqueue('first')
print(queue_with_two_stacks.front, queue_with_two_stacks.rear) # -1 0
print(queue_with_two_stacks.peek(), queue_with_two_stacks.front, queue_with_two_stacks.rear) # first 0 -1
queue_with_two_stacks.enqueue('second')
queue_with_two_stacks.enqueue('third')
print(queue_with_two_stacks.front, queue_with_two_stacks.rear) # 0 1
print(queue_with_two_stacks.dequeue(), queue_with_two_stacks.front, queue_with_two_stacks.rear) # first -1 1
print(queue_with_two_stacks.dequeue(), queue_with_two_stacks.front, queue_with_two_stacks.rear) # second 0 -1
print(queue_with_two_stacks.dequeue(), queue_with_two_stacks.front, queue_with_two_stacks.rear) # third -1 -1