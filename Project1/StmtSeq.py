from Assign import Assign
from Input import Input
from Output import Output
from If import If
from Loop import Loop
from Decl import Decl
from Core import Core
import sys

class StmtSeq:

	def parse(self, parser):
		if parser.scanner.currentToken() == Core.ID:
			self.stmt = Assign()
		elif parser.scanner.currentToken() == Core.INPUT:
			self.stmt = Input()
		elif parser.scanner.currentToken() == Core.OUTPUT:
			self.stmt = Output()
		elif parser.scanner.currentToken() == Core.IF:
			self.stmt = If()
		elif parser.scanner.currentToken() == Core.WHILE:
			self.stmt = Loop()
		elif parser.scanner.currentToken() == Core.INT or parser.scanner.currentToken() == Core.REF:
			self.stmt = Decl()
		else:
			print("ERROR: Bad start to statement: " + parser.scanner.currentToken().name + "\n", end='')
			sys.exit()
		self.stmt.parse(parser)
		if (not parser.scanner.currentToken() == Core.END
			and not parser.scanner.currentToken() == Core.ENDIF
			and not parser.scanner.currentToken() == Core.ENDWHILE
			and not parser.scanner.currentToken() == Core.ELSE):
			self.ss = StmtSeq()
			self.ss.parse(parser)
	
	def semantic(self, parser):
		self.stmt.semantic(parser)
		if hasattr(self, 'ss'):
			self.ss.semantic(parser)
	
	def print(self, indent):
		self.stmt.print(indent)
		if hasattr(self, 'ss'):
			self.ss.print(indent)

	#recursively calls stmt and ss
	def execute(self, parser, inputData):
		self.stmt.execute(parser, inputData)
		if hasattr(self, 'ss'):
			self.ss.execute(parser, inputData)