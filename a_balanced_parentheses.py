parentheses_set = [ ['{', '}' ], [ '[', ']' ], [ '(', ')' ], [ '<', '>' ] ]

def is_open(open_char):
		for paren in parentheses_set:
				if (open_char == paren[0]):
						return True
		return False

def is_paired(open_char, closed_char):
		for paren in parentheses_set:
				if ((open_char == paren[0]) and (closed_char == paren[1])):
						return True
		return False

def is_balanced(input_paren):
		paren_stack = []
		for paren in input_paren:
				if (is_open(paren)):
						paren_stack.append(paren)
				else:
						is_paired(paren_stack.pop(), paren)
		return not paren_stack

# test
input_arr = list(input('input > '))
result = is_balanced(input_arr)
print('result >', result)