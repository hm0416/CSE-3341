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

		#if func body present, then replaces the existing heap values (for the actual parameters) with their new values that they get set to within the function
		if globals.isFunc == True: #checks if there is a function declaration
			for item in executor.heapSpace:
				# gets index of each heap value (for the actual params that gets passed)
				indexOfParam = executor.heapSpace.index(item)
				#sets the value at the specified index to the new value
				executor.heapSpace[indexOfParam] = result
		return result