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
	
	def semantic(self, parser):
		if hasattr(self, 'id'):
			self.id.semantic(parser)
		elif hasattr(self, 'expr'):
			self.expr.semantic(parser)
	
	def print(self):
		if hasattr(self, 'id'):
			self.id.print()
		elif hasattr(self, 'expr'):
			print("(", end='')
			self.expr.print()
			print(")", end='')
		else:
			print(self.constant, end='')

	def execute(self, parser, inputData, inputID, outputID):
		if hasattr(self, 'id'):
			# scope = parser.scopeCheckForID(self.id.identifier) #gets scope index that id is in
			scope = 1
			return self.id.execute(parser, inputData, inputID, outputID, scope)
		elif hasattr(self, 'expr'):
			return self.expr.execute(parser, inputData, inputID, outputID)
		else:
			return self.constant
