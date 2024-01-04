parentheses_set = [ ['{', '}' ], [ '[', ']' ], [ '(', ')' ], [ '<', '>' ] ]

def isOpen(open_char):
		for paren in parentheses_set:
				if (open_char == paren[0]):
						return True
		return False

def isPaired(open_char, closed_char):
		for paren in parentheses_set:
				if ((open_char == paren[0]) and (closed_char == paren[1])):
						return True
		return False

def isBalanced(input_paren):
		paren_stack = []
		for paren in input_paren:
				if (isOpen(paren)):
						paren_stack.append(paren)
				else:
						isPaired(paren_stack.pop(), paren)
		return not paren_stack

# test
input_arr = list(input('input > '))
result = isBalanced(input_arr)
print('result >', result)