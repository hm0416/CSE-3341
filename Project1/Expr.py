from Term import Term
from Core import Core
import globals

class Expr:
	
	def parse(self, parser):
		self.option = 0
		self.term = Term()
		self.term.parse(parser)
		if parser.scanner.currentToken() == Core.ADD:
			self.option = 1
		elif parser.scanner.currentToken() == Core.SUB:
			self.option = 2
		if not self.option == 0:
			parser.scanner.nextToken()
			self.expr = Expr()
			self.expr.parse(parser)
	
	def print(self):
		self.term.print()
		if self.option == 1:
			print("+", end='')
			self.expr.print()
		elif self.option == 2:
			print("-", end='')
			self.expr.print()

	def execute(self, executor):
		result = self.term.execute(executor)
		if self.option == 1:
			result += self.expr.execute(executor)
		elif self.option == 2:
			result -= self.expr.execute(executor)

		#if func body present, then replaces existing heap values for the actual paramters
		# with their new values that they get set to within the function
		if globals.isFunc == True:
			for i in range(len(executor.heapSpace)):
				executor.heapSpace[i] = result
		return result