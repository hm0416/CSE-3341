from Decl import Decl
from Core import Core
from FuncDecl import FuncDecl
import globals

class DeclSeq:
	
	def parse(self, parser):
		if parser.scanner.currentToken() != Core.ID:
			self.decl = Decl()
			self.decl.parse(parser)
		else:
			self.fd = FuncDecl()
			self.fd.parse(parser)
		if not parser.scanner.currentToken() == Core.BEGIN:
			self.ds = DeclSeq()
			self.ds.parse(parser)
	
	# def print(self, indent):
	# 	self.decl.print(indent)
	# 	if hasattr(self, 'ds'):
	# 		self.ds.print(indent)

	def execute(self, executor):
		#checks to see if function declared or not
		if hasattr(self, 'fd'):
			# globals.isFunc = True
			self.fd.execute(executor)
			# globals.isFunc = False
		else:
			self.decl.execute(executor)
		if hasattr(self, 'ds'):
			self.ds.execute(executor)