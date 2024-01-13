class LinkedList:
		class Node:
				def __init__(self, data):
						self.data = data
						self.next = None
    
		def __init__(self):
				self.head = None
				self.tail = None
				self.size = 0
    
		def is_empty(self):
				return self.head is None
				# return self.size == 0
    
		def push(self, data):
				data_in = self.Node(data)
    
				if (self.tail is not None):
						self.tail.next = data_in
				self.tail = data_in
    
				if (self.is_empty()):
						self.head = data_in

				self.size += 1
    
		def pop(self):
				data_out = self.head.data
				self.head = self.head.next
				self.size -= 1
				return data_out
    
    # 여기서부터, 어떻게 해야 index번째에 있는 데이터를 찾아서 삽입/삭제할 수 있을까?
		def insert(self, data, index):
				if (self.size < index or index < 0):
						raise IndexError

				data_in = self.Node(data)
				self.size += 1
    
				pre_index_data = self.head
				if (index == 0):
						self.head = data_in
						data_in.next = pre_index_data
						return
    
				for i in range(index - 1):
						pre_index_data = pre_index_data.next
      
				data_in.next = pre_index_data.next
				pre_index_data.next = data_in
  
		def remove(self, index):
				if (self.size < index or index < 0):
						raise IndexError

				self.size -= 1
				pre_index_data = self.head
				if (index == 0):
						self.head = self.head.next
						# pre_index_data.next = None
						return
      
				for i in range(index - 1):
						pre_index_data = pre_index_data.next
      
				# index_data = pre_index_data.next
				pre_index_data.next = pre_index_data.next.next
				# index_data.next = None

		def indexOf(self, index):
				if (self.size <= index or index < 0 or self.is_empty()):
						raise IndexError
    
				index_data = self.head
				for i in range(index):
						index_data = index_data.next
				return index_data.data

# test
linkedList = LinkedList()

# 조회
print(linkedList.head, linkedList.tail) # None None
print(linkedList.is_empty(), linkedList.size) # True 0
# print(linkedList.indexOf(0)) ← IndexError

# 데이터 추가(tail 추가)
linkedList.push('first')
print(linkedList.head.data, linkedList.tail.data) # first first
linkedList.push('second')
print(linkedList.head.data, linkedList.tail.data) # first second
linkedList.push('third')
print(linkedList.head.data, linkedList.tail.data) # first third
linkedList.push('fourth')
print(linkedList.head.data, linkedList.tail.data) # first fourth
linkedList.push('fifth')

# 조회
print(linkedList.is_empty(), linkedList.size) # False 5
print(linkedList.head.data, linkedList.tail.data) # first fifth
print(linkedList.indexOf(1), linkedList.indexOf(2), linkedList.indexOf(3)) # second third fourth

# 데이터 삭제(head 삭제)
print(linkedList.pop(), linkedList.head.data, linkedList.tail.data) # first second fifth

# 데이터 삽입(index에 추가)
linkedList.insert('first', 0)
print(linkedList.head.data, linkedList.tail.data) # first fifth
linkedList.insert('index_2', 2)
print(linkedList.indexOf(0), linkedList.indexOf(1), linkedList.indexOf(2), linkedList.indexOf(3), linkedList.indexOf(4), linkedList.indexOf(5)) # first second index_2 third fourth fifth
print(linkedList.indexOf(2)) # index_2

# 데이터 삭제(index 삭제)
linkedList.remove(0)
print(linkedList.indexOf(0), linkedList.indexOf(1), linkedList.indexOf(2), linkedList.indexOf(3), linkedList.indexOf(4)) # second index_2 third fourth fifth
print(linkedList.head.data, linkedList.tail.data, linkedList.size) # second fifth 5
linkedList.remove(1)
print(linkedList.indexOf(0), linkedList.indexOf(1), linkedList.indexOf(2), linkedList.indexOf(3)) # second third fourth fifth
print(linkedList.head.data, linkedList.tail.data, linkedList.size) # second fifth 4