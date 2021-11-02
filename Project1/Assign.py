from Id import Id
from Expr import Expr
from Core import Core
import sys

class Assign:
	
	def parse(self, parser):
		self.assignTo = Id()
		self.assignTo.parse(parser)
		parser.expectedToken(Core.ASSIGN)
		parser.scanner.nextToken()
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
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		self.assignTo.print()
		print("=", end='')
		if self.type == 1:
			print("new")
		elif self.type == 2:
			print("ref ")
			self.assignFrom.print()
		else:
			self.expr.print()
		print(";\n", end='')

	def execute(self, executor):
		if self.type == 1:
			# Doing a "new"-assign
			self.assignTo.heapAllocate(executor)
		elif self.type == 2:
			# Doing a "ref"-assign
			self.assignTo.referenceCopy(executor, self.assignFrom)
		else:
			# Doing a regular assign
			self.assignTo.storeValue(executor, self.expr.execute(executor))