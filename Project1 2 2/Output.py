from Expr import Expr
from Core import Core

class Output:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.expr = Expr()
		self.expr.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("output ", end='')
		self.expr.print()
		print(";\n", end='')

	def execute(self, executor):
		print(str(self.expr.execute(executor)) + "\n", end='')