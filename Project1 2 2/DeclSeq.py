from Decl import Decl
from Core import Core
from FuncDecl import FuncDecl

class DeclSeq:
	
	def parse(self, parser):
		#checks to see if current token starts with ID or not, if it does then that means there is a function declaration
		if parser.scanner.currentToken() != Core.ID:
			self.decl = Decl()
			self.decl.parse(parser)
		else:
			self.fd = FuncDecl()
			self.fd.parse(parser)
		if not parser.scanner.currentToken() == Core.BEGIN:
			self.ds = DeclSeq()
			self.ds.parse(parser)

	def execute(self, executor):
		#checks to see if function declared or not
		if hasattr(self, 'fd'):
			self.fd.execute(executor)
		else:
			self.decl.execute(executor)
		if hasattr(self, 'ds'):
			self.ds.execute(executor)