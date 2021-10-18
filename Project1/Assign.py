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
			globals.refID = parser.scanner.getID() #gets ID of the variable to be referenced
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

	def execute(self, parser, inputData):
		if self.type == 1:
			globals.arrOfDeclaredWithNew[self.assignTo.identifier] = "new" #array to help determine which if-stmt to go into when self.type is == 3
			self.assignTo.setValOfID(0, parser, inputData) #initializes the variable that's being set to new to zero
		elif self.type == 2:
			#LHS of the expression is now pointing to the value that's getting referenced on the RHS
			parser.ids[-1][self.assignTo.identifier] = parser.ids[-1][self.assignFrom.identifier]
			globals.arrOfDeclaredWithNew[self.assignTo.identifier] = "ref" #array to help determine which if-stmt to go into when self.type is == 3
			globals.isRef = True #knows to copy the value of the referenced variable to the variable onto the LHS when setValOfID is called
		elif self.type == 3:
			if self.assignTo.identifier in globals.arrOfDeclaredWithNew: #if ref variable has been assigned new
				value = self.expr.execute(parser, inputData)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			elif self.assignTo.identifier in globals.arrOfDeclared: #if int var has been assigned ref
				value = self.expr.execute(parser, inputData)  # gets the value on the RHS
				self.assignTo.setValOfID(value, parser, inputData)  # set the LHS to the RHS
			else:
				print("ERROR: Error is assignment to null ref variable")
				quit()
