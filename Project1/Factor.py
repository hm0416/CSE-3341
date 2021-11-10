from Id import Id
import Expr
from Core import Core
import sys

class Factor:

	def parse(self, parser):
		if parser.scanner.currentToken() == Core.ID:
			self.id = Id()
			self.id.parse(parser)
		elif parser.scanner.currentToken() == Core.CONST:
			self.constant = parser.scanner.getCONST()
			parser.scanner.nextToken()
		elif parser.scanner.currentToken() == Core.LPAREN:
			parser.scanner.nextToken()
			self.expr = Expr.Expr()
			self.expr.parse(parser)
			parser.expectedToken(Core.RPAREN)
			parser.scanner.nextToken()
		else:
			print("ERROR: Expected ID, CONST, or LPAREN, recieved " + parser.scanner.currentToken().name + "\n", end='')
			sys.exit()
	
	def print(self):
		if hasattr(self, 'id'):
			self.id.print()
		elif hasattr(self, 'expr'):
			print("(", end='')
			self.expr.print()
			print(")", end='')
		else:
			print(self.constant, end='')

	def execute(self, executor):
		result = 0
		if hasattr(self, 'id'):
			try:
				result = int(self.id.getValue(executor))
			except ValueError:
				print("ERROR: " + self.id.getString() + " is null\n", end='')
				sys.exit()
		elif hasattr(self, 'expr'):
			result = self.expr.execute(executor)
		else:
			result = self.constant
		return result