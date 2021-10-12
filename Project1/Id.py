from Core import Core
import sys
import globals

class Id:
	
	def parse(self, parser):
		parser.expectedToken(Core.ID)
		self.identifier = parser.scanner.getID()
		parser.scanner.nextToken()
	
	# Called to check if the identifier has been declared
	def semantic(self, parser):
		if parser.nestedScopeCheck(self.identifier)==Core.ERROR:
			print("ERROR: No matching declaration found: " + self.identifier + "\n", end='')
			sys.exit()
	
	# Called by IdList semantic functions to check for doubly declared variables
	def doublyDeclared(self, parser):
		if not parser.currentScopeCheck(self.identifier)==Core.ERROR:
			print("ERROR: Doubly declared variable detected: " + self.identifier + "\n", end='')
			sys.exit()

	# Called by IdList semantic functions to add the variable to the scopes data structure in Parser
	def addToScopes(self, parser, declaredType):
		parser.scopes[-1][self.identifier] = declaredType

	def addToIds(self, parser, declaredType):
		parser.scopes[-1][self.identifier] = declaredType

	# Called by Assign semantic function to check the declared type of the variable
	def checkType(self, parser):
		return parser.nestedScopeCheck(self.identifier)
	
	def print(self):
		print(self.identifier, end='')

	def setValOfID(self, val, parser, inputData):
		parser.ids[-1][self.identifier] = val #ids needs to be unique
		if globals.isRef == True: #changing x to be z, needs to be other way around
			# 	parser.ids[-1][self.identifier] = parser.ids[-1][globals.refID]

			parser.ids[-1][globals.refID] = parser.ids[-1][self.identifier]
		# else:
		# 	parser.ids[-1][self.identifier] = parser.ids[-1][globals.refID]


	# def replaceValOfID(self, idToReplace, id, parser):
	# 	rhsValue = parser.ids[idToReplace]
	# 	parser.ids[id] = rhsValue #ids needs to be unique

	def execute(self, parser, inputData, inputID, outputID, scope):
		# if len(parser.ids) > 3:
		# 	parser.ids.pop()
		return parser.ids[-1].get(self.identifier)


