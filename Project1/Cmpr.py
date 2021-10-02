from Core import Core
from Expr import Expr
import sys

class Cmpr:
	
	def parse(self, parser):
		self.expr1 = Expr()
		self.expr1.parse(parser)
		if parser.scanner.currentToken() == Core.EQUAL:
			self.option = 0
		elif parser.scanner.currentToken() == Core.LESS:
			self.option = 1
		elif parser.scanner.currentToken() == Core.LESSEQUAL:
			self.option = 2
		else:
			print("ERROR: Expected EQUAL, LESS, or LESSEQUAL, recieved " + parser.scanner.currentToken().name + "\n", end='')
			sys.exit()
		parser.scanner.nextToken()
		self.expr2 = Expr()
		self.expr2.parse(parser)
	
	def semantic(self, parser):
		self.expr1.semantic(parser)
		self.expr2.semantic(parser)
	
	def print(self):
		self.expr1.print()
		if self.option == 0:
			print("==", end='')
		elif self.option == 1:
			print("<", end='')
		elif self.option == 2:
			print("<=", end='')
		self.expr2.print()

	def execute(self, parser):
		value = self.expr1.execute(parser)
		if self.option == 0:
			if value == self.expr2.execute(parser):
				value = True
			else:
				value = False
		elif self.option == 1:
			if value < self.expr2.execute(parser):
				value = True
			else:
				value = False
		elif self.option == 2:
			if value <= self.expr2.execute(parser):
				value = True
			else:
				value = False

		return value