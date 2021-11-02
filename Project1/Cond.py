from Core import Core
from Cmpr import Cmpr

class Cond:
	
	def parse(self, parser):
		if parser.scanner.currentToken() == Core.NEGATION:
			parser.scanner.nextToken()
			parser.expectedToken(Core.LPAREN)
			parser.scanner.nextToken()
			self.cond = Cond()
			self.cond.parse(parser)
			parser.expectedToken(Core.RPAREN)
			parser.scanner.nextToken()
		else:
			self.cmpr = Cmpr()
			self.cmpr.parse(parser)
			if parser.scanner.currentToken() == Core.OR:
				parser.scanner.nextToken()
				self.cond = Cond()
				self.cond.parse(parser)
	
	def print(self):
		if not hasattr(self, 'cmpr'):
			print("!(", end='')
			self.cond.print()
			print(")", end='')
		else:
			self.cmpr.print()
			if hasattr(self, 'cond'):
				print(" or ", end='')
				self.cond.print()

	def execute(self, executor):
		result = False
		if not hasattr(self, 'cmpr'):
			result = not self.cond.execute(executor)
		else:
			result = self.cmpr.execute(executor)
			if hasattr(self, 'cond'):
				result = result or self.cond.execute(executor)
		return result