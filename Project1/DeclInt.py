from IdList import IdList
from Core import Core
import globals

class DeclInt:
	
	def parse(self, parser):
		parser.expectedToken(Core.INT)
		parser.scanner.nextToken()
		globals.addInt = True #helper variable for idList class to see if there is an additional int that is declared/if there is a list of id's
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

	def execute(self, parser, inputData):
		# globals.isInt.append(parser.scanner.getID()) #appends the id of the int that's been declared - isInt is an array of ints that's been declared
		# if globals.goInStmt == True: #if code is inside if/loop stmt then want to append another dict
		# 	parser.ids.append({})
		# 	globals.needToPop = True #sets needToPop to true to determine if a dict needs to be popped
		# else:
		pass