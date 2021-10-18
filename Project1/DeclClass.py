from IdList import IdList
from Core import Core
import globals

class DeclClass:
	
	def parse(self, parser):
		parser.expectedToken(Core.REF)
		parser.scanner.nextToken()
		# globals.varAfterRef = parser.scanner.getID() #gets the variable after ref declaration
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

	#nothing to do here
	def execute(self, parser, inputData):
		pass
		# globals.varAfterRef = parser.scanner.getID()