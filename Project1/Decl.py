from DeclInt import DeclInt
from DeclClass import DeclClass
from Core import Core
import globals

class Decl:
	
	def parse(self, parser):
		if parser.scanner.currentToken() == Core.INT:
			self.declInt = DeclInt()
			self.declInt.parse(parser)
		else:
			self.declRef = DeclClass()
			self.declRef.parse(parser)

	
	def semantic(self, parser):
		if hasattr(self, 'declInt'):
			self.declInt.semantic(parser)
		elif hasattr(self, 'declRef'):
			self.declRef.semantic(parser)
	
	def print(self, indent):
		if hasattr(self, 'declInt'):
			self.declInt.print(indent)
		elif hasattr(self, 'declRef'):
			self.declRef.print(indent)

	#chcks to see which declaration is made - an int or ref
	def execute(self, parser, inputData):
		if hasattr(self, 'declInt'):
			self.declInt.execute(parser, inputData)
		elif hasattr(self, 'declRef'):
			self.declRef.execute(parser, inputData)