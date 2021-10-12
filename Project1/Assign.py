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
			if self.assignFrom.checkType(parser) != Core.REF:
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
			globals.arrOfDeclared[self.assignTo.identifier] = "new"
			globals.isRefThen = True
			v = globals.arrOfDeclared
			self.assignTo.setValOfID(0, parser, inputData)
		elif self.type == 2: #y = ref x, need a case for when ref x; then y = x;
			# valForX = parser.ids[-1].get(self.assignFrom.identifier) # gets 4
			# parser.ids[-1][self.assignTo.identifier] = valForX # y = 4
			parser.ids[-1][self.assignTo.identifier] = parser.ids[-1][self.assignFrom.identifier]
			globals.arrOfDeclared[self.assignTo.identifier] = "ref"
			globals.isRef = True
		elif self.type == 3:
			#need to check if assigned new to this variable that's trying to get set
			# if globals.isRefThen == False:
			# 	value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
			# 	self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			i = globals.isInt
			p = globals.arrOfDeclared
			valueForRef = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
			r = globals.refID
			if globals.refID == valueForRef:
				globals.onlyChar = True
			# if globals.refID in globals.arrOfDeclared and globals.refID == valueForRef:
			# 	parser.ids[-1][self.assignTo.identifier] = parser.ids[-1][globals.refID]
			if self.assignTo.identifier in globals.arrOfDeclared: #if ref var thats been assigned new
				value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			elif self.assignTo.identifier in globals.isInt: #if int
				value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			else:
				print("ERROR: Error is assignment to null ref variable")
				quit()
