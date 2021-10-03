from Id import Id
from Core import Core

class Input:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.id = Id()
		self.id.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.id.semantic(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("input ", end='')
		self.id.print()
		print(";\n", end='')

	def execute(self, parser, inputData, inputID, outputID):
		# self.tokAfterInput = parser.scanner.getID() #gets the id after input keyword
		self.id.setValOfID(self.id, parser, inputData)
