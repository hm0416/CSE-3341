from IdList import IdList
from Core import Core

class DeclClass:
	
	def parse(self, parser):
		parser.expectedToken(Core.REF)
		parser.scanner.nextToken()
		self.list = IdList()
		self.list.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("ref ", end='')
		self.list.print()
		print(";\n", end='')

	def execute(self, executor):
		# Id list has two execute functions, call the one for ref variables
		self.list.executeRefIdList(executor)