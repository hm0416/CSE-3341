from Decl import Decl
from Core import Core

class DeclSeq:
	
	def parse(self, parser):
		self.decl = Decl()
		self.decl.parse(parser)
		if not parser.scanner.currentToken() == Core.BEGIN:
			self.ds = DeclSeq()
			self.ds.parse(parser)
	
	def semantic(self, parser):
		self.decl.semantic(parser)
		if hasattr(self, 'ds'):
			self.ds.semantic(parser)
	
	def print(self, indent):
		self.decl.print(indent)
		if hasattr(self, 'ds'):
			self.ds.print(indent)

	def execute(self, parser):
		self.decl.execute(parser)
		if hasattr(self, 'ds'):
			self.ds.execute(parser)