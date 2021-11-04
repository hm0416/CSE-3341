from Core import Core
import sys

class Id:
	
	def parse(self, parser):
		parser.expectedToken(Core.ID)
		self.identifier = parser.scanner.getID()
		parser.scanner.nextToken()
	
	def print(self):
		print(self.identifier, end='')

	# Returns the string value of the Id
	def getString(self):
		return self.identifier
	
	# Finds the stored value of the variable
	def getValue(self, executor):
		return executor.getValue(self.identifier)
	
	# Stores the passed value to the variable, used to handle regular assign
	def storeValue(self, executor, value):
		executor.storeValue(self.identifier, value)
	
	# Called by assign to handle "ref"-assign
	def referenceCopy(self, executor, copyFrom):
		executor.referenceCopy(self.identifier, copyFrom.getString())
	
	# Called by assign to handle "new"-assign
	def heapAllocate(self, executor):
		executor.heapAllocate(self.identifier)
	
	# Called when declaring an int variable
	def executeIntAllocate(self, executor):
		executor.allocate(self.identifier, Core.INT)
	
	# Called when declaring a ref variable
	def executeRefAllocate(self, executor):
		executor.allocate(self.identifier, Core.REF)
