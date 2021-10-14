from Id import Id
from Core import Core
import globals

class IdList:
	
	def parse(self, parser):
		self.id = Id()
		self.id.parse(parser)
		if globals.addInt == True or globals.addRef == True:
			globals.isInt.append(parser.scanner.getID())
			globals.isRefArr.append(parser.scanner.getID())
		if parser.scanner.currentToken() == Core.COMMA:
			parser.scanner.nextToken()
			self.list = IdList()
			self.list.parse(parser)
			if globals.addInt == True or globals.addRef == True:
				globals.isInt.append(parser.scanner.getID())
				globals.isRefArr.append(parser.scanner.getID())

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
		if parser.scope == 0:
			if hasattr(self, 'list'):
				parser.static[-1][self.list.id.identifier] = [0, "int"]
		elif parser.scope == 1:
			if hasattr(self, 'list'):
				parser.stack[-1][self.list.id.identifier] = [0, "int"]

		if hasattr(self, 'list'):
			self.list.executeInt(parser, inputData, inputID, outputID)

	def executeRef(self, parser, inputData, inputID, outputID):
		if parser.scope == 0:
			if hasattr(self, 'list'):
				parser.static[-1][self.list.id.identifier] = [None, "ref"]
		elif parser.scope == 1:
			if hasattr(self, 'list'):
				parser.stack[-1][self.list.id.identifier] = [None, "ref"]

		if hasattr(self, 'list'):
			self.list.executeRef(parser, inputData, inputID, outputID)