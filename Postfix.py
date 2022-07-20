# l = []
# def Postfix(p):
#     d = p.split(",")
#     for i in range(len(d)):
#         if d[i] not in ['+', '-', '*', '/']:
#             l.append(int(d[i]))
#             # print(l)
#         else:
#             a = l.pop(l.index(l[-1]))
#             b = l.pop(l.index(l[-1]))

#             if d[i] == "+":
#                 sum = b + a
#                 l.append(sum)
#                 # print(l)
                
#             elif d[i] == "-":
#                 sum = b - a
#                 l.append(sum)
#                 # print(l)
#             elif d[i] == "*":
#                 sum = b * a
#                 l.append(sum)
#                 # print(l)
#             elif d[i] == "/":
#                 sum = b / a
#                 l.append(sum)
#                 # print(l)
#     print("Postfix is: ",int(l[0]))

# p = '5,6,2,+,*,12,4,/,-'
# Postfix(p)




def is_operand(c):
	return c.isdigit()

def evaluate(expression):
	stack = []

	for c in expression[::-1]:

		if is_operand(c):
			stack.append(int(c))

		else:
			o1 = stack.pop()
			o2 = stack.pop()

			if c == '+':
				stack.append(o1 + o2)

			elif c == '-':
				stack.append(o1 - o2)

			elif c == '*':
				stack.append(o1 * o2)

			elif c == '/':
				stack.append(o1 / o2)

	return stack.pop()

if __name__ == "__main__":
	test_expression = "+9*26"
	print(evaluate(test_expression))