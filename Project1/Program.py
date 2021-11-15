from Core import Core
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq
from Executor import Executor

class Program:
	
	def parse(self, parser):
		parser.expectedToken(Core.PROGRAM)
		parser.scanner.nextToken()
		if parser.scanner.currentToken() != Core.BEGIN:
			self.ds = DeclSeq()
			self.ds.parse(parser)
		parser.expectedToken(Core.BEGIN)
		parser.scanner.nextToken()
		self.ss = StmtSeq()
		self.ss.parse(parser)
		parser.expectedToken(Core.END)
		parser.scanner.nextToken()
		parser.expectedToken(Core.EOF)
	
	def print(self):
		print("program\n", end='')
		if hasattr(self, 'ds'):
			self.ds.print(1)
		print("begin\n", end='')
		self.ss.print(1)
		print("end\n", end='')

	def execute(self, dataFileString):
		executor = Executor(dataFileString)
		if hasattr(self, 'ds'):
			self.ds.execute(executor)
		executor.pushMainFrame()
		self.ss.execute(executor)
		executor.popFrame()
		# if executor.counter >= 0:
		# 	executor.counter = executor.counter - 1  # decrement number of references because function popped off and variables have gone out of scope
		# # if executor.counter >= 0:
		print("gc:" + str(executor.counter))
		# if executor.counter != 0:
		# 	print("gc:0")