from Id import Id
from Core import Core
import globals

class IdList:
	
	def parse(self, parser):
		self.id = Id()
		self.id.parse(parser)
		# if globals.addInt == True: #if additional int is present after first int, append
		globals.isInt.append(parser.scanner.getID()) #append the first int that's been declared
		if parser.scanner.currentToken() == Core.COMMA:
			parser.scanner.nextToken()
			self.list = IdList()
			self.list.parse(parser)
			if globals.addInt == True: #if additional int is present after first int, append
				globals.isInt.append(parser.scanner.getID())

	# called by DeclInt.semantic
	def semanticIntVars(self, parser):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.INT)
		if hasattr(self, 'list'):
			self.list.semanticIntVars(parser)

	# called by DeclClass.semantic
	def semanticRefVars(self, parser):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.REF)
		if hasattr(self, 'list'):
			self.list.semanticRefVars(parser)
	
	def print(self):
		self.id.print()
		if hasattr(self, 'list'):
			print(",", end='')
			self.list.print()

	#Nothing to do here
	def execute(self, parser, inputData):
		pass
