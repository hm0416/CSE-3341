from DeclInt import DeclInt
from DeclClass import DeclClass
from Core import Core

class Decl:
	
	def parse(self, parser):
		if parser.scanner.currentToken() == Core.INT:
			self.declInt = DeclInt()
			self.declInt.parse(parser)
		else:
			self.declClass = DeclClass()
			self.declClass.parse(parser)
	
	def print(self, indent):
		if hasattr(self, 'declInt'):
			self.declInt.print(indent)
		elif hasattr(self, 'declClass'):
			self.declClass.print(indent)

	def execute(self, executor):
		if hasattr(self, 'declInt'):
			self.declInt.execute(executor)
		elif hasattr(self, 'declClass'):
			self.declClass.execute(executor)