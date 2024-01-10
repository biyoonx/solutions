class LinkedList:
		class Node:
				def __init__(self, data):
						self.data = data
						self.next = None
    
		def __init__(self):
				self.head = None
				self.tail = None
    
		def is_empty(self):
				return self.head is None
    
		def push(self, data):
				data_in = self.Node(data)
    
				if (self.tail is not None):
						self.tail.next = data_in
				self.tail = data_in
    
				if (self.is_empty()):
						self.head = None
    
		def pop(self):
				data_out = self.head.data
				self.head = self.head.next
				return data_out
    
    # 여기서부터
		def insert(self, data, index):
				data_in = self.Node(data)
				range(index)
  
		def remove(self, index):
				range(index)