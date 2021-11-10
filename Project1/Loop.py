from Core import Core
from Cond import Cond
import StmtSeq

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

	def execute(self, executor):
		while self.cond.execute(executor):
			executor.pushLocalScope()
			self.ss.execute(executor)
			executor.popLocalScope()
			executor.counter = executor.counter - 1  # decrement number of references because function popped off and variables have gone out of scope
			print("gc:" + str(executor.counter))