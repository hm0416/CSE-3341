from Id import Id
from Expr import Expr
from Core import Core
import sys

class Assign:

	# def __init__(self):
	# 	self.refID = ""

	def parse(self, parser):
		# self.assignTo will store the id on the LHS of the assignment
		# global self.assignFrom
		self.refID = ""
		# global ref2
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
			# ref = True
			parser.scanner.nextToken()
			self.refID = parser.scanner.getID()
			self.assignFrom = Id()
			self.assignFrom.parse(parser)
		else:
			self.type = 3
			# ref2 = True
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
			self.assignTo.setValOfID(0, parser, inputData)
		elif self.type == 2:
			valForX = parser.ids.get(self.assignFrom.identifier) # gets 4
			parser.ids[self.assignTo.identifier] = valForX # y = 4
		elif self.type == 3:
			value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
			self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS

		# parser.ids["x"] = parser.ids.get(self.assignTo.identifier)

		# if self.ref == True and hasattr(self, 'expr'):
		# 	value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
		# 	# self.id.setValOfID(value, self.assignTo) #set the LHS to the RHS
		# 	self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
		# 	self.assignFrom.setValOfID(value, parser, inputData)  # set the LHS to the RHS
		# 	self.ref = False
		# elif self.ref == False and hasattr(self, 'expr'):
		# 	value = self.expr.execute(parser, inputData, inputID, outputID) #gets the value on the RHS
		# 	# self.id.setValOfID(value, self.assignTo) #set the LHS to the RHS
		# 	self.assignTo.setValOfID(value, parser, inputData) #set the LHS to the RHS
		# elif self.type == 2:
		# 	valForX = parser.ids.get(self.assignFrom.identifier) # gets 4
		# 	parser.ids[self.assignTo.identifier] = valForX # y = 4
		# 	self.ref = True


			# if hasattr(self, 'expr'):
			# 	value = self.expr.execute(parser, inputData, inputID, outputID)  # gets the value on the RHS
			# 	# self.id.setValOfID(value, self.assignTo) #set the LHS to the RHS
			# 	self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			# 	self.assignFrom.setValOfID(value, parser, inputData)  # set the LHS to the RHS



# self.assignFrom.identifier = self.assignTo.identifier

			#where x shows up, replace with y?
			# self.assignFrom.identifier = self.assignTo.identifier
			# parser.ids[self.assignTo.identifier] = parser.ids[self.assignFrom.identifier]
			# del parser.ids[self.assignFrom.identifier]

		# self.assignFrom.setValOfID(value, parser, inputData)  # set the LHS to the RHS


	# valForY = parser.ids.get(self.assignTo.identifier)
			# parser.ids[self.assignFrom.identifier] = valForY

			# rhs = parser.ids[self.assignFrom.identifier]
			# parser.ids[self.assignTo.identifier] = rhs
			# self.assignTo.replaceValOfID(self.assignFrom.identifier, self.assignTo.identifier, parser)