from Id import Id
from Core import Core

class IdList:
	
	def parse(self, parser):
		self.id = Id()
		self.id.parse(parser)
		if parser.scanner.currentToken() == Core.COMMA:
			parser.scanner.nextToken()
			self.list = IdList()
			self.list.parse(parser)
	
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

	def execute(self, parser, inputData, inputID, outputID):
		pass

	def executeInt(self, parser, inputData, inputID, outputID):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.INT)
		if hasattr(self, 'list'):
			self.list.semanticIntVars(parser)

	def executeRef(self, parser, inputData, inputID, outputID):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.REF)
		if hasattr(self, 'list'):
			self.list.semanticRefVars(parser)