from Term import Term
from Core import Core

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
	
	def semantic(self, parser):
		self.term.semantic(parser)
		if hasattr(self, 'expr'):
			self.expr.semantic(parser)
	
	def print(self):
		self.term.print()
		if self.option == 1:
			print("+", end='')
			self.expr.print()
		elif self.option == 2:
			print("-", end='')
			self.expr.print()

	def execute(self, parser, inputData):
		value = self.term.execute(parser, inputData) #gets the first value
		if self.option == 1:
			value = value + self.expr.execute(parser, inputData) #if expr is addition, get the second value and adds to the first
		elif self.option == 2:
			value = value - self.expr.execute(parser, inputData) #if expr is subtraction, get the second value and subtracts from the first
		return value