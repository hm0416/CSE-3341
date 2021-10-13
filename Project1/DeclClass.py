from IdList import IdList
from Core import Core
import globals

class DeclClass:
	
	def parse(self, parser):
		parser.expectedToken(Core.REF)
		parser.scanner.nextToken()
		globals.varAfterRef = parser.scanner.getID() #gets the variable after ref declaration
		self.list = IdList()
		self.list.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.list.semanticRefVars(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("ref ", end='')
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
				parser.static[-1][self.list.id.identifier] = [None, "ref"]
		else:
			for ele in parser.static:
				if globals.varAfterRef in ele:
					parser.scope = 0
					parser.static[-1][self.list.id.identifier] = [None, "ref"]
				elif parser.scope == 0:
					parser.static[-1][self.list.id.identifier] = [None, "ref"]

		if all(len(ele) == 0 for ele in parser.stack):
			if parser.scope == 1:
				parser.stack[-1][self.list.id.identifier] = [None, "ref"]
		else:
			for ele in parser.stack:
				if globals.varAfterRef in ele:
					parser.scope = 1
					parser.stack[-1][self.list.id.identifier] = [None, "ref"]
				elif parser.scope == 1:
					parser.stack[-1][self.list.id.identifier] = [None, "ref"]

		# self.list.executeRef(parser, inputData, inputID, outputID)
		globals.varAfterRef = parser.scanner.getID()