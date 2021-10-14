from Id import Id
from Expr import Expr
from Core import Core
import globals
import sys

class Assign:

	def parse(self, parser):
		# self.assignTo will store the id on the LHS of the assignment
		self.assignTo = Id()
		self.assignTo.parse(parser)
		parser.expectedToken(Core.ASSIGN)
		parser.scanner.nextToken()

		# self.type will store 1 if "new" assignment, 2 if "ref" assignment, 3 if "<expr>" assignment
		if parser.scanner.currentToken() == Core.NEW:
			self.type = 1
			parser.scanner.nextToken()
		elif parser.scanner.currentToken() == Core.REF:
			self.type = 2
			parser.scanner.nextToken()
			globals.refID = parser.scanner.getID()
			self.assignFrom = Id()
			self.assignFrom.parse(parser)
		else:
			self.type = 3
			self.expr = Expr()
			self.expr.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()

	def semantic(self, parser):
		self.assignTo.semantic(parser)
		if self.type == 1:
			if self.assignTo.checkType(parser) != Core.REF:
				print("ERROR: int variable used in new assignment\n", end='')
				sys.exit()
		elif self.type == 2:
			if self.assignTo.checkType(parser) != Core.REF:
				print("ERROR: int variable used in class assignment\n", end='')
				sys.exit()
			if globals.assignFrom.checkType(parser) != Core.REF:
				print("ERROR: int variable used in class assignment\n", end='')
				sys.exit()
		else:
			self.expr.semantic(parser)

	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		self.assignTo.print()
		print("=", end='')
		if self.type == 1:
			print("new", end='')
		elif self.type == 2:
			print("ref ", end='')
			self.assignFrom.print()
		else:
			self.expr.print()
		print(";\n", end='')

	def execute(self, parser, inputData, inputID, outputID):
		if self.type == 1:
			parser.heap[self.assignTo.identifier] = 0
			globals.arrOfDeclared[self.assignTo.identifier] = "new"
			globals.isRefThen = True
			v = globals.arrOfDeclared
			self.assignTo.setValOfID(0, parser, inputData)
		elif self.type == 2: #y = ref x, need a case for when ref x; then y = x;
			if self.assignFrom.identifier in parser.heap:
				indxKeyAssignFrom = list(parser.heap).index(self.assignFrom.identifier)
				assignFromVal = parser.heap.get(self.assignFrom.identifier)

			# for ele in parser.heap:
			# 	if self.assignFrom.identifier in ele:
			# 		indxKeyAssignFrom = parser.heap.index(ele)  # gets index of ref var in the heap
				indxKey = 0
				if parser.scope == 0:
					for ele in parser.static:
						if self.assignTo.identifier in ele:
							indxKey = parser.static.index(ele)  # gets index of pair
					dict = parser.static[indxKey]  # gets the dict at the index
					valsForKey = dict[self.assignTo.identifier] #array
					valsForKey[0] = indxKeyAssignFrom #sets to the index of ref var in the heap
				elif parser.scope == 1:
					for ele in parser.stack:
						if self.assignTo.identifier in ele:
							indxKey = parser.stack.index(ele)  # gets index of pair
					dict = parser.stack[indxKey]  # gets the dict at the index
					valsForKey = dict[self.assignTo.identifier]
					valsForKey[0] = indxKeyAssignFrom #sets to the index of ref var in the heap

			#need to find y in the stack space
			#get it's first ele in its list
			#set it to be whatever is in the heap - find assignFrom in heap and get that value

			# if parser.scope == 0:
			# 	for ele in parser.static:
			# 		if self.assignTo.identifier in ele:
			# 			indxKey = parser.static.index(ele)  # gets index of pair
			# 	dict = parser.static[indxKey]  # gets the dict at the index
			# 	valsForKey = dict[self.assignTo.identifier] #array
			#
			# 	for ele in parser.heap:
			# 		if self.assignFrom.identifier in ele:
			# 			indxKeyAssignFrom = parser.heap.index(ele)  # gets index of pair
			# 	dictAssignFrom = parser.heap[indxKeyAssignFrom]  # gets the dict at the index
			# 	valForAssignFrom = dictAssignFrom[self.assignFrom.identifier] #array
			# 	valsForKey[0] = valForAssignFrom
			# elif parser.scope == 1:
			# 	for ele in parser.stack:
			# 		if self.assignTo.identifier in ele:
			# 			indxKey = parser.stack.index(ele)  # gets index of pair
			# 	# dict = parser.stack[indxKey]  # gets the dict at the index
			# 	# valsForKey = dict[self.assignTo.identifier]
			# 	# parser.stack[indxKey][self.assignTo.identifier]
			#
			# 	for ele in parser.heap:
			# 		if self.assignFrom.identifier in ele:
			# 			indxKeyAssignFrom = parser.heap.index(ele)  # gets index of pair
			# 	dictAssignFrom = parser.heap[indxKeyAssignFrom]  # gets the dict at the index
			# 	valForAssignFrom = dictAssignFrom[self.assignFrom.identifier] #array
			# 	parser.stack[indxKey][self.assignTo.identifier][0] = valForAssignFrom


			# valForX = parser.ids[-1].get(self.assignFrom.identifier) # gets 4
			# parser.ids[-1][self.assignTo.identifier] = valForX # y = 4
			# parser.ids[-1][self.assignTo.identifier] = parser.ids[-1][self.assignFrom.identifier]
			# globals.arrOfDeclared[self.assignTo.identifier] = "ref"
			# globals.isRef = True
		elif self.type == 3:
			# if globals.refID in parser.heap:
			# 	assignFromVal2 = parser.heap.get(globals.refID)
			# 	indxKey2 = 0
			# 	if parser.scope == 0:
			# 		for ele in parser.static:
			# 			if self.assignTo.identifier in ele:
			# 				indxKey2 = parser.static.index(ele)  # gets index of pair
			# 		dict2 = parser.static[indxKey2]  # gets the dict at the index
			# 		valsForKey2 = dict2[self.assignTo.identifier] #array
			# 		valsForKey2[0] = assignFromVal2 #sets to the index of ref var in the heap
			# 	elif parser.scope == 1:
			# 		for ele in parser.stack:
			# 			if self.assignTo.identifier in ele:
			# 				indxKey2 = parser.stack.index(ele)  # gets index of pair
			# 		dict2 = parser.stack[indxKey2]  # gets the dict at the index
			# 		valsForKey2 = dict2[self.assignTo.identifier]
			# 		valsForKey2[0] = assignFromVal2 #sets to the index of ref var in the heap
			# for ele in parser.heap:
			# 	if globals.refID in ele:
			# 		indxKeyAssignFrom = parser.heap.index(ele)  # gets index of ref var in the heap
			# 		if parser.scope == 0:
			# 			for ele in parser.static:
			# 				if self.assignTo.identifier in ele:
			# 					indxKey = parser.static.index(ele)  # gets index of pair
			# 			dict = parser.static[indxKey]  # gets the dict at the index
			# 			valsForKey = dict[self.assignTo.identifier]  # array
			# 			valsForKey[0] = indxKeyAssignFrom  # sets to the index of ref var in the heap

			temp = None
			for ele in parser.static:
				if self.assignTo.identifier in ele:
					parser.scope = 0
					temp = parser.static.copy()
			for ele in parser.stack:
				if self.assignTo.identifier in ele:
					parser.scope = 1
					temp = parser.stack.copy()

			while temp != None and len(temp) != 0:
				pair = temp.pop(len(temp)-1) #the last item in stack -- most recent decl
				indxKey = 0
				if parser.scope == 0:
					if self.assignTo.identifier in pair:
						#find the vars index in the static list of dicts
						for ele in parser.static:
							if self.assignTo.identifier in ele:
								indxKey = parser.static.index(ele) #gets index of pair
						dict = parser.static[indxKey] #gets the dict at the index
						valsForKey = dict[self.assignTo.identifier]
						valsForKey[0] = self.expr.execute(parser, inputData, inputID, outputID)
						for heapEle in parser.heap:
							if self.assignTo.identifier in heapEle:
								parser.heap[self.assignTo.identifier] = self.expr.execute(parser, inputData, inputID, outputID)
				elif parser.scope == 1:
					if self.assignTo.identifier in pair:
						#find the vars index in the static list of dicts
						for ele in parser.stack:
							if self.assignTo.identifier in ele:
								indxKey = parser.stack.index(ele) #gets index of pair
						dict = parser.stack[indxKey] #gets the dict at the index
						valsForKey = dict[self.assignTo.identifier]
						valsForKey[0] = self.expr.execute(parser, inputData, inputID, outputID)
						for heapEle in parser.heap:
							if self.assignTo.identifier in heapEle:
								parser.heap[self.assignTo.identifier] = self.expr.execute(parser, inputData, inputID, outputID)


			if self.assignTo.identifier in globals.arrOfDeclared: #if ref var thats been assigned new
				value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			elif self.assignTo.identifier in globals.isInt: #if int
				value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			else:
				print("ERROR: Error is assignment to null ref variable")
				quit()
