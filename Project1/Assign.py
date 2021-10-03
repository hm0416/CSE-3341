from Id import Id
from Expr import Expr
from Core import Core
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
		# self.id = Id()
		if hasattr(self, 'expr'):
			value = self.expr.execute(parser, inputData, inputID, outputID) #gets the value on the RHS
			# self.id.setValOfID(value, self.assignTo) #set the LHS to the RHS
			self.assignTo.setValOfID(value, parser, inputData) #set the LHS to the RHS
		elif self.type == 2:
			valForLHS = parser.ids.get(self.assignTo.identifier)
			parser.ids[self.assignFrom.identifier] = valForLHS
			# rhs = parser.ids[self.assignFrom.identifier]
			# parser.ids[self.assignTo.identifier] = rhs
			# self.assignTo.replaceValOfID(self.assignFrom.identifier, self.assignTo.identifier, parser)