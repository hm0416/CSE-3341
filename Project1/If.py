from Core import Core
from Cond import Cond
import StmtSeq
import globals

class If:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.cond = Cond()
		self.cond.parse(parser)
		parser.expectedToken(Core.THEN)
		parser.scanner.nextToken()
		self.ss1 = StmtSeq.StmtSeq()
		self.ss1.parse(parser)
		if parser.scanner.currentToken() == Core.ELSE:
			parser.scanner.nextToken()
			self.ss2 = StmtSeq.StmtSeq()
			self.ss2.parse(parser)
		parser.expectedToken(Core.ENDIF)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.cond.semantic(parser)
		parser.scopes.append({})
		self.ss1.semantic(parser)
		parser.scopes.pop()
		if hasattr(self, 'ss2'):
			parser.scopes.append({})
			self.ss2.semantic(parser)
			parser.scopes.pop()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("if ", end='')
		self.cond.print()
		print(" then\n", end='')
		self.ss1.print(indent+1)
		if hasattr(self, 'ss2'):
			for x in range(indent):
				print("  ", end='')
			print("else\n", end='')
			self.ss2.print(indent+1)
		for x in range(indent):
			print("  ", end='')
		print("endif\n", end='')

	def execute(self, parser, inputData):
		if not hasattr(self, 'ss2'):  #if there is no else statement
			if self.cond.execute(parser, inputData):
				globals.goInStmt = True #have gone into new scope/if stmt
				self.ss1.execute(parser, inputData)
				if globals.needToPop == True: #checks to see if need to pop dict
					parser.ids.pop()
		else:  # if there is an else stmt
			if self.cond.execute(parser, inputData):
				globals.goInStmt = True
				self.ss1.execute(parser, inputData)
				if globals.needToPop == True:
					parser.ids.pop()
			else:
				globals.goInStmt = True
				self.ss2.execute(parser, inputData)
				if globals.needToPop == True:
					parser.ids.pop()