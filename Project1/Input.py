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

	def execute(self, parser, inputData):
		# if there are still ints in the inputData file, pop each off otherwise print an error
		if len(inputData) != 0:
			val = inputData.pop(0)
		else:
			print("ERROR: Error is .data file not having enough values")
			quit()
		self.id.setValOfID(val, parser, inputData) #sets the value of the input variable to the values in the input file
