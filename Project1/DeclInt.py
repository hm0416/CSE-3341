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
		for ele in parser.static:
			if globals.varAfterRef in ele:
				parser.scope = 0
			elif all(len(ele) == 0 for ele in parser.static):
				parser.scope = 0
			else:
				parser.scope = 1

		# for ele in parser.stack:
		# 	if globals.varAfterRef in ele:
		# 		parser.scope = 1
		# 	else:
		# 		parser.scope = 0


		if all(len(ele) == 0 for ele in parser.static):
			if parser.scope == 0:
				parser.static[-1][self.list.id.identifier] = [0, "int"]
		else:
			for ele in parser.static:
				if globals.varAfterRef in ele:
					parser.scope = 0
					parser.static[-1][self.list.id.identifier] = [0, "int"]
				elif parser.scope == 0:
					parser.static[-1][self.list.id.identifier] = [0, "int"]

		if all(len(ele) == 0 for ele in parser.stack):
			if parser.scope == 1:
				parser.stack[-1][self.list.id.identifier] = [0, "int"]
		else:
			for ele in parser.stack:
				if globals.varAfterRef in ele:
					parser.scope = 1
					parser.stack[-1][self.list.id.identifier] = [0, "int"]
				elif parser.scope == 1:
					parser.stack[-1][self.list.id.identifier] = [0, "int"]

		globals.isInt.append(parser.scanner.getID())
		if globals.goInStmt == True:
			parser.ids.append({})
			globals.needToPop = True
		else:
			pass

		# if hasattr(self, 'list'):
		# 	self.list.semanticIntVars(parser)
		# # self.list.executeInt(parser, inputData, inputID, outputID)