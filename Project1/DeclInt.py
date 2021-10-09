from IdList import IdList
from Core import Core
import globals

class DeclInt:
	
	def parse(self, parser):
		parser.expectedToken(Core.INT)
		parser.scanner.nextToken()
		globals.addInt = True
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
		globals.isInt.append(parser.scanner.getID())
		if globals.goInStmt == True:
			parser.ids.append({})
			globals.needToPop = True
		else:
			pass

		# if hasattr(self, 'list'):
		# 	self.list.semanticIntVars(parser)
		# # self.list.executeInt(parser, inputData, inputID, outputID)