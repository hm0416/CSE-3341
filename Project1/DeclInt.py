from IdList import IdList
from Core import Core
import globals

class DeclInt:
	
	def parse(self, parser):
		parser.expectedToken(Core.INT)
		parser.scanner.nextToken()
		self.list = IdList()
		self.list.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.list.semanticIntVars(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("int ", end='')
		self.list.print()
		print(";\n", end='')

	def execute(self, parser, inputData, inputID, outputID):
		if globals.goInStmt == True:
			parser.ids.append({})
			globals.needToPop = True
		else:
			pass
		# self.list.executeInt(parser, inputData, inputID, outputID)