from Decl import Decl
from FuncDecl import FuncDecl
from Core import Core

class DeclSeq:
	
	def parse(self, parser):
		if parser.scanner.currentToken() == Core.ID:
			self.fdecl = FuncDecl()
			self.fdecl.parse(parser)
		else:
			self.decl = Decl()
			self.decl.parse(parser)
		if not parser.scanner.currentToken() == Core.BEGIN:
			self.ds = DeclSeq()
			self.ds.parse(parser)
	
	def print(self, indent):
		if hasattr(self, 'fdecl'):
			self.fdecl.print(indent)
		else:
			self.decl.print(indent)
		if hasattr(self, 'ds'):
			self.ds.print(indent)

	def execute(self, executor):
		if hasattr(self, 'fdecl'):
			self.fdecl.execute(executor)
		else:
			self.decl.execute(executor)
		if hasattr(self, 'ds'):
			self.ds.execute(executor)