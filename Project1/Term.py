from Factor import Factor
from Core import Core

class Term:
	
	def parse(self, parser):
		self.factor = Factor()
		self.factor.parse(parser)
		if parser.scanner.currentToken() == Core.MULT:
			parser.scanner.nextToken()
			self.term = Term()
			self.term.parse(parser)
	
	def semantic(self, parser):
		self.factor.semantic(parser)
		if hasattr(self, 'term'):
			self.term.semantic(parser)
	
	def print(self):
		self.factor.print()
		if hasattr(self, 'term'):
			print("*", end='')
			self.term.print()

	def execute(self, parser, inputData):
		value = self.factor.execute(parser, inputData) #Gets value
		if hasattr(self, 'term'):
			value = value * self.term.execute(parser, inputData) #if value multiplied by another value, then gets the other value
		return value