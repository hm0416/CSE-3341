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

	#checks to see if there's a comparision or condition
	def execute(self, parser, inputData):
		value = False
		if not hasattr(self, 'cmpr'):
			value = not(self.cond.execute(parser, inputData)) #whatever condition is here, negates it
		else:
			value = self.cmpr.execute(parser, inputData)
			if hasattr(self, 'cond'): #if there is a condition as well, do the 3rd production in the cond grammar
				value = self.cmpr.execute(parser, inputData) or self.cond.execute(parser, inputData)
		return value