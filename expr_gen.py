import sys 
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Expression generator')
parser.add_argument('--depth', type=int, default=5, help="Depth of exprs to generate")
parser.add_argument('--in_min', type=int, default=0, help="Minimum input val (inclusive)")
parser.add_argument('--in_max', type=int, default=5, help="Maximum input val (exclusive)")

parser.add_argument('--out_min', type=int, default=-10, help="Minimum output val (inclusive)")
parser.add_argument('--out_max', type=int, default=10, help="Maximum output val (exclusive)")


class Expression:
	def __init__(self):
		pass 

	def __str__(self):
		pass 

	def eval(self):
		pass

class Parenthesis:
	def __init__(self, expr):
		self.expr = expr

	def __str__(self):
		return "(" + str(self.expr) + ")"

	def eval(self):
		return self.expr.eval()

class Addition:
	def __init__(self, left, right):
		self.left = left 
		self.right = right

	def __str__(self):
		return "(" + str(self.left) + "+" + str(self.right) + ")"

	def eval(self):
		return self.left.eval() + self.right.eval()

class Subtraction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + str(self.left) + "-" + str(self.right) + ")"

	def eval(self):
		return self.left.eval() - self.right.eval()
 
class Multiplication:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + str(self.left) + "*" + str(self.right) + ")"

	def eval(self):
		return self.left.eval() * self.right.eval()

class Constant:
	def __init__(self, val):
		self.val = val

	def __str__(self):
		return str(self.val)

	def eval(self):
		return self.val

'''
	E : c | E + E | E - E | E * E | (E)
'''
def expression_generator(depth=5, low=0, high=5):
	if depth == 1:
		val = np.random.randint(low, high)
		return Constant(val)

	else:
		choice = np.random.randint(0, 4)
		if choice == 0:
			val = np.random.randint(low, high)
			return Constant(val)

		else:
			left = expression_generator(depth = depth-1)
			right = expression_generator(depth = depth-1)
			
			if choice ==1:
				return Addition(left, right)
			elif choice ==2:
				return Subtraction(left, right)
			else:
				return Multiplication(left, right)
			

def expr_parser(s):
	stack = []
	for c in s:
		if c == "+" or c == "-" or c == "*":
			stack.append(c)

		if c.isdigit():
			stack.append(int(c))

		if c == ")":
			assert(isinstance(stack[-1], int))
			rhs = stack.pop()
			op = stack.pop()
			lhs = stack.pop()
			val = eval("%i%s%i"%(lhs, op, rhs))
			stack.append(val)

	return stack[-1]





if __name__ == "__main__":
	args = parser.parse_args()

	for i in range(100):
		expr = expression_generator(depth=args.depth, low=args.in_min, high=args.in_max)
		val = expr.eval()
		if val >= args.out_min and val < args.out_max:
			print(str(expr) + " = " + str(val) + " = " + str(expr_parser(str(expr))))


