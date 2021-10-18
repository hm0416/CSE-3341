from Core import Core
from Cond import Cond
import StmtSeq
import globals

class Loop:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.cond = Cond()
		self.cond.parse(parser)
		parser.expectedToken(Core.BEGIN)
		parser.scanner.nextToken()
		self.ss = StmtSeq.StmtSeq()
		self.ss.parse(parser)
		parser.expectedToken(Core.ENDWHILE)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.cond.semantic(parser)
		parser.scopes.append({})
		self.ss.semantic(parser)
		parser.scopes.pop()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("while ", end='')
		self.cond.print()
		print(" begin\n", end='')
		self.ss.print(indent+1)
		for x in range(indent):
			print("  ", end='')
		print("endwhile\n", end='')

	def execute(self, parser, inputData):
		while self.cond.execute(parser, inputData):
			globals.goInStmt = True #have gone into new scope/if stmt
			self.ss.execute(parser, inputData)
			if globals.needToPop == True: #checks to see if need to pop dict
				parser.ids.pop()