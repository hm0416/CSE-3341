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


	# def replaceValOfID(self, idToReplace, id, parser):
	# 	rhsValue = parser.ids[idToReplace]
	# 	parser.ids[id] = rhsValue #ids needs to be unique

	def execute(self, parser, inputData, inputID, outputID, scope):
		# if len(parser.ids) > 3:
		# 	parser.ids.pop()
		# return parser.ids[-1].get(self.identifier)
		#index of id then get value
		indxKey = 0
		# if parser.scope == 0:
		if parser.scope == 0:
			for ele in parser.static:
				if self.identifier in ele:
					indxKey = parser.static.index(ele)  # gets index of pair

			if self.identifier in parser.heap:
				assignFromVal = parser.heap.get(self.identifier) #gets val of x
				return assignFromVal
			else:
				dict = parser.static[indxKey]  # gets the dict at the index
				valsForKey = dict[self.identifier]  # array looking for 0th key

				if len(parser.heap) != 0:
					vals = parser.heap.values() #gets all values in heap, want 0th
					vals_list = list(vals)
					return vals_list[valsForKey[0]]
				else:
					return valsForKey[0]
		elif parser.scope == 1:
			for ele in parser.stack:
				if self.identifier in ele:
					indxKey = parser.stack.index(ele)  # gets index of pair

			if self.identifier in parser.heap:
				assignFromVal = parser.heap.get(self.identifier) #gets val of x
				return assignFromVal
			else:
				dict = parser.stack[indxKey]  # gets the dict at the index
				valsForKey = dict[self.identifier]  # array looking for 0th key
				if len(parser.heap) != 0:
					vals = parser.heap.values() #gets all values in heap, want 0th
					vals_list = list(vals)
					return vals_list[valsForKey[0]]
				else:
					return valsForKey[0]





		# 	if self.identifier in parser.heap:
		# 		assignFromVal = parser.heap.get(self.identifier) #gets val of x
		# 		return assignFromVal
		#
		# 	# for ele in parser.static:
		# 	# 	if self.identifier in ele:
		# 	# 		indxKey = parser.static.index(ele)  # gets index of pair
		# 	# dict = parser.static[indxKey]  # gets the dict at the index
		# 	# valForKey = dict.get(self.identifier)
		# 	# return valForKey
		# elif parser.scope == 1:
		# 	if self.identifier in parser.heap:
		# 		assignFromVal = parser.heap.get(self.identifier) #gets val of x
		# 		return assignFromVal

			# for ele in parser.stack:
			# 	if self.identifier in ele:
			# 		indxKey = parser.stack.index(ele)  # gets index of pair
			# dict = parser.stack[indxKey]  # gets the dict at the index
			# valForKey = dict.get(self.identifier)

