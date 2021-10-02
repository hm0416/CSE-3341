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
	
	def semantic(self, parser):
		if not hasattr(self, 'cmpr'):
			self.cond.semantic(parser)
		else:
			self.cmpr.semantic(parser)
			if hasattr(self, 'cond'):
				self.cond.semantic(parser)
	
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

	def execute(self, parser):
		value = False
		if not hasattr(self, 'cmpr'):
			value = not (self.cond.execute(parser))
		else:
			value = self.cmpr.execute(parser)
			if hasattr(self, 'cond'):
				value = self.cmpr.execute(parser) or self.cond.execute(parser)

		return value