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

	def execute(self, parser, inputData, inputID, outputID):
		if inputID == outputID:
			print(inputData.pop(0))
		else:
			print(self.expr.execute(parser, inputData, inputID, outputID))