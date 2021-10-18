from Expr import Expr
from Core import Core

class Output:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.expr = Expr()
		self.expr.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.expr.semantic(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("output ", end='')
		self.expr.print()
		print(";\n", end='')

	#prints out the value of the variable the program wants to output
	def execute(self, parser, inputData):
		print(self.expr.execute(parser, inputData))