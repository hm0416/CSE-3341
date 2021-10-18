from Scanner import Scanner
from Core import Core
import sys

# Parser class contains all the persistent data structures we will need, and some helper functions
class Parser:
	
	#Constructor for Parser.
	#scanner is stored here so it is avaiable to the parse method of all contained classes
	#scopes is a data structure for the semantic checks, to verify variables being used are declared
	def __init__(self, s):
		self.scanner = Scanner(s)
		self.scopes = [{}]
		self.ids = [{}] #list of dictionaries to handle variables in the program
	
	#helper method for the semantic checks
	#returns Core.INT or Core.REF if the string x is the name of a variable that is in scope, Core.ERROR otherwise
	def nestedScopeCheck(self, x):
		match = Core.ERROR
		if not len(self.scopes) == 0:
			temp = self.scopes.pop() #check every dict
			if x in temp:
				match = temp[x]
			else:
				match = self.nestedScopeCheck(x) #recurse and keep checking each dict
			self.scopes.append(temp)
		return match
	
	#helper method for the semantic checks
	#returns Core.INT or Core.REF if the string x is the name of a variable that was declared in the current scope, Core.ERROR otherwise
	def currentScopeCheck(self, x):
		match = Core.ERROR
		if not len(self.scopes) == 0:
			if x in self.scopes[-1]:
				match = self.scopes[-1][x]
		return match
	
	#helper method for handling error messages, used by the parse methods
	def expectedToken(self, expected):
		if self.scanner.currentToken() != expected:
			print("ERROR: Expected " + expected.name + ", recieved " + self.scanner.currentToken().name + "\n", end='')
			sys.exit()
