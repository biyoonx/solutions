# 연결 리스트 안에 있는 사이클(루프)을 탐지하라. 만약 리스트가 비어있다면 head는 null일 것이다. 정의된 Node는 다음과 같다.
class Node:
		def __init__(self):
				self.data = ''
				self.next = None
   
		def __init__(self, data):
				self.data = data
				self.next = None

def has_cycle(head: Node):
		if (head is None):
				return False
  
		fast_node = head.next
		slow_node = head
  
		while (fast_node is not None) and (fast_node.next is not None) and (slow_node is not None):
				if (fast_node is slow_node):
						return True

				fast_node = fast_node.next.next
				slow_node = slow_node.next
    
		return False

# test
node_list_head = Node('first')
node_list_head.next = Node('second')
node_list_head.next.next = Node('third')
node_list_head.next.next.next = Node('fourth')
node_list_head.next.next.next.next = Node('fifth')

result1 = has_cycle(node_list_head)
print(result1) # False

node_list_head.next.next.next.next.next = node_list_head

result2 = has_cycle(node_list_head)
print(result2) # True

# 루프가 반복적으로 돌지 않고 빠져나올수 있다면 상관없는 걸까?
node_list_head.next.next.next.next.next.next = Node('sixth')

result3 = has_cycle(node_list_head)
print(result3) # False